#!/usr/bin/env python3
"""Sync SCG AI subagents, install official GSAP skills and link Claude skills.

No changes to AGENTS.md, CLAUDE.md, GEMINI.md or application source.
Python 3.11+, Git for --install-gsap, optional filesystem link support.
"""
import argparse
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    tomllib = None

ROOT = Path(__file__).resolve().parents[2]
AGENT_ROOT = ROOT / '.agents'
SKILLS_ROOT = AGENT_ROOT / 'skills'
AGENTS = {
    'ARCHITECT': 'Design architecture, evaluate technical trade-offs and plan complex implementations.',
    'DESIGNER': 'Create exceptional UI/UX, visual systems, accessible and responsive interfaces.',
    'ENGINEER': 'Implement and debug full-stack features across frameworks and languages.',
    'AUDITOR': 'Independently verify correctness, security, performance and quality.',
    'DEVOPS': 'Manage secure, reliable infrastructure, CI/CD and deployments.'
}
REQUIRED_SKILLS = (
    'accessibility', 'api-design', 'application-security', 'architecture-design',
    'code-review', 'css-scss', 'database-engineering', 'devops-infrastructure',
    'git-workflows', 'multi-tenant-authorization', 'nodejs', 'php', 'react',
    'stripe-payments', 'technical-seo', 'testing-quality', 'typescript',
    'ui-ux', 'web-performance'
)
GSAP = (
    'gsap-core', 'gsap-timeline', 'gsap-scrolltrigger', 'gsap-plugins',
    'gsap-utils', 'gsap-react', 'gsap-performance', 'gsap-frameworks'
)
URL = 'https://github.com/greensock/gsap-skills.git'


class RecoveryError(RuntimeError):
    """A replacement failed and its workspace must be retained for recovery."""


def is_link(path: Path):
    """Include Windows junctions, even on Python versions without is_junction()."""
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, 'st_file_attributes', 0)
        & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0)
    )


def check_path(path: Path, *, allow_leaf_link=False):
    """Reject writes through links or outside the explicit project root."""
    root = ROOT.resolve()
    try:
        relative = path.absolute().relative_to(root)
        path.resolve().relative_to(root)
    except ValueError as exc:
        raise RuntimeError(f'Path is outside the project root: {path}') from exc
    current = root
    for index, part in enumerate(relative.parts):
        current = current / part
        if is_link(current) and not (allow_leaf_link and index == len(relative.parts) - 1):
            raise RuntimeError(f'Refusing to traverse or replace a link/junction: {current}')


def project_errors():
    errors = []
    required = [ROOT / '.codex' / 'scripts' / 'setup.py'] + [AGENT_ROOT / f'{name}.md' for name in AGENTS]
    for path in [AGENT_ROOT, SKILLS_ROOT, *required]:
        try:
            check_path(path)
        except (OSError, RuntimeError) as exc:
            errors.append(str(exc))
    for path in required:
        if not path.is_file():
            errors.append(f'Missing project source: {path}')
    if not SKILLS_ROOT.is_dir():
        errors.append(f'Missing skills directory: {SKILLS_ROOT}')
    return errors


def require_project():
    errors = project_errors()
    if errors:
        raise RuntimeError('\n'.join(errors))


def save(path: Path, value: str):
    check_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value.rstrip() + '\n', encoding='utf-8')


def expected_agent_files():
    """One rendering path for both synchronization and drift detection."""
    files = {}
    for name, description in AGENTS.items():
        content = (AGENT_ROOT / f'{name}.md').read_text(encoding='utf-8').strip()
        if not content:
            raise RuntimeError(f'Empty agent source: {name}.md')
        slug = name.lower()
        full_prompt = (
            'You are a specialized AI agent. Do not assume the authority or responsibilities '
            'of the main orchestrator. Follow company-wide rules from AGENTS.md when they '
            'are provided to you; your role is defined below. Activate relevant project skills '
            'from .agents/skills/ when available; resolve these paths from the outer workspace root. '
            'By default, every request to create, change, debug, review or document a product targets '
            'project/ under the outer workspace root, even when the chat or terminal starts at that root. '
            'Resolve that root from AGENTS.md and the kit .agents/ directory before product work. '
            'If the current directory is already project/ or a child, use the same application root; '
            'never create project/project/. Before file mutations or product commands, check the resolved '
            'target paths and working directory against that application root. '
            'Keep product source, assets, dependencies, configuration, tests, scripts, documentation '
            'and build output inside project/, and run product commands there or in its subdirectories. '
            'When delegating, pass the absolute workspace root, application root, file ownership and '
            'command working directory. Before reporting completion, review the files changed by the '
            'product work and correct any accidental placement outside project/ without touching '
            'unrelated files. The outer root and its tooling directories belong to the AI kit and '
            'repository metadata; edit them only when the user explicitly requests their maintenance '
            'or configuration.\n\n' + content
        )
        files[ROOT / '.codex' / 'agents' / f'{slug}.toml'] = (
            f'name = {json.dumps(slug)}\n'
            f'description = {json.dumps(description)}\n'
            f'developer_instructions = {json.dumps(full_prompt, ensure_ascii=False)}\n'
        )
        yaml_header = f'---\nname: {slug}\ndescription: {description}\n'
        files[ROOT / '.claude' / 'agents' / f'{slug}.md'] = yaml_header + '---\n\n' + full_prompt + '\n'
        files[ROOT / '.gemini' / 'agents' / f'{slug}.md'] = yaml_header + 'kind: local\n---\n\n' + full_prompt + '\n'
    return files


def sync_agents():
    require_project()
    files = expected_agent_files()
    for path in files:
        check_path(path)
    for path, content in files.items():
        save(path, content)
    print(f'Synced {len(AGENTS)} agents to Codex, Claude Code and Gemini CLI.')


def skill_errors(path: Path):
    if not path.is_file():
        return [f'{path}: missing SKILL.md']
    raw = path.read_text(encoding='utf-8')
    if not raw.startswith('---\n') or '\n---\n' not in raw[4:]:
        return [f'{path}: missing frontmatter']
    header = raw.split('\n---\n', 1)[0]
    values = {}
    for key in ('name', 'description'):
        match = re.search(rf'^{key}:[ \t]*(.*)$', header, re.M)
        value = match.group(1).strip() if match else ''
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except ValueError:
                return [f'{path}: invalid quoted {key}']
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        values[key] = value
    errors = []
    name, desc = values['name'], values['description']
    if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name != path.parent.name:
        errors.append(f'{path}: invalid or missing skill name {name!r}')
    if not isinstance(desc, str) or not desc.strip() or desc in ('|', '>', '|-', '>-') or len(desc) > 1024:
        errors.append(f'{path}: invalid description (expected a nonempty single-line string, at most 1024 characters)')
    return errors


def replace_gsap(staged_files, workspace: Path):
    """Replace prepared files; restore every previous destination on failure."""
    backup_root = workspace / 'backups'
    backup_root.mkdir()
    changed = []
    try:
        for index, (source, destination) in enumerate(staged_files):
            check_path(destination)
            destination.parent.mkdir(parents=True, exist_ok=True)
            backup = backup_root / str(index)
            had_previous = destination.exists()
            if had_previous:
                destination.rename(backup)
            changed.append((destination, backup if had_previous else None))
            source.rename(destination)
    except (OSError, RuntimeError) as exc:
        rollback_errors = []
        for index, (destination, backup) in reversed(list(enumerate(changed))):
            try:
                check_path(destination)
                if destination.exists():
                    destination.rename(workspace / f'failed-{index}')
                if backup is not None:
                    backup.rename(destination)
            except (OSError, RuntimeError) as rollback_exc:
                rollback_errors.append(f'{destination}: {rollback_exc}')
        if rollback_errors:
            raise RecoveryError(
                f'GSAP replacement failed ({exc}); recovery incomplete. '
                f'Backups retained in {workspace}.\n' + '\n'.join(rollback_errors)
            ) from exc
        raise


def remove_workspace(workspace: Path):
    """Clean only the verified staging tree, including read-only Git objects."""
    check_path(workspace)

    def retry_readonly(function, filename, error):
        path = Path(filename)
        check_path(path)
        try:
            path.resolve().relative_to(workspace.resolve())
        except ValueError as exc:
            raise RuntimeError(f'Refusing cleanup outside staging: {path}') from exc
        if not isinstance(error[1], PermissionError) or function not in (os.unlink, os.remove, os.rmdir):
            raise error[1]
        os.chmod(path, path.stat().st_mode | stat.S_IWRITE)
        function(filename)

    shutil.rmtree(workspace, onerror=retry_readonly)


def install_gsap(update: bool):
    require_project()
    destinations = [SKILLS_ROOT / name for name in GSAP]
    license_dest = AGENT_ROOT / 'licenses' / 'gsap-skills-LICENSE'
    manifest_dest = ROOT / '.codex' / 'docs' / 'GSAP_UPSTREAM.md'
    for path in [*destinations, license_dest, manifest_dest]:
        check_path(path)
    for path in destinations:
        if path.exists() and not path.is_dir():
            raise RuntimeError(f'Refusing to replace a file with a skill directory: {path}')
    for path in (license_dest, manifest_dest):
        if path.exists() and not path.is_file():
            raise RuntimeError(f'Refusing to replace a directory with a metadata file: {path}')
    present = [path for path in destinations if path.exists()]
    if present and not update:
        if len(present) != len(GSAP):
            raise RuntimeError('GSAP installation is incomplete; use --install-gsap --update-gsap to replace the complete set.')
        print('Preserving all existing GSAP skills and provenance; use --update-gsap to replace them.')
        return
    if shutil.which('git') is None:
        raise RuntimeError('Git is required to download the official GSAP skills.')

    workspace = Path(tempfile.mkdtemp(prefix='.setup-gsap-', dir=ROOT))
    committed = False
    preserve_workspace = False
    try:
        repo = workspace / 'repo'
        subprocess.run(['git', 'clone', '--quiet', '--depth', '1', URL, str(repo)], check=True)
        sha = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
        if not re.fullmatch(r'[0-9a-fA-F]{40,64}', sha):
            raise RuntimeError('Git returned an invalid source commit.')
        staging = workspace / 'prepared'
        staging.mkdir()
        staged_files = []
        for name, destination in zip(GSAP, destinations):
            source = repo / 'skills' / name
            if not source.is_dir() or is_link(source):
                raise RuntimeError(f'GSAP repo is missing a regular skill directory: {name}')
            if any(is_link(item) for item in source.rglob('*')):
                raise RuntimeError(f'Refusing upstream links inside GSAP skill: {name}')
            staged = staging / name
            shutil.copytree(source, staged)
            errors = skill_errors(staged / 'SKILL.md')
            if errors:
                raise RuntimeError('\n'.join(errors))
            staged_files.append((staged, destination))
        license_src = repo / 'LICENSE'
        if not license_src.is_file() or is_link(license_src):
            raise RuntimeError('GSAP repo is missing a regular LICENSE file.')
        if not license_src.read_text(encoding='utf-8').strip():
            raise RuntimeError('GSAP repo contains an empty LICENSE file.')
        license_staged = staging / 'LICENSE'
        shutil.copy2(license_src, license_staged)
        staged_files.append((license_staged, license_dest))
        manifest_staged = staging / 'GSAP_UPSTREAM.md'
        save(manifest_staged,
             f'# Official GSAP Skills\n\nSource: {URL}\nCommit: `{sha}`\n'
             'Installed from the official GreenSock repository. Preserve source and license.\n'
             'Run `python .codex/scripts/setup.py --install-gsap --update-gsap --link-claude --validate` to update.\n')
        staged_files.append((manifest_staged, manifest_dest))
        replace_gsap(staged_files, workspace)
        committed = True
        print(f'Installed {len(GSAP)} official GSAP skills; source commit: {sha}')
    except RecoveryError:
        preserve_workspace = True
        raise
    finally:
        backups = workspace / 'backups'
        needs_recovery = preserve_workspace or (not committed and backups.exists() and any(backups.iterdir()))
        if not needs_recovery:
            try:
                remove_workspace(workspace)
            except OSError as exc:
                print(f'Warning: could not remove temporary workspace {workspace}: {exc}', file=sys.stderr)


def link_claude():
    require_project()
    dest_root = ROOT / '.claude' / 'skills'
    check_path(dest_root)
    sources = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir() or is_link(path))
    for source in sources:
        check_path(source)
        destination = dest_root / source.name
        check_path(destination, allow_leaf_link=True)
        if os.path.lexists(destination) and (not is_link(destination) or destination.resolve() != source.resolve()):
            raise RuntimeError(f'Conflicting Claude skill preserved: {destination}; expected a link to {source}.')
    dest_root.mkdir(parents=True, exist_ok=True)
    for source in sources:
        destination = dest_root / source.name
        if os.path.lexists(destination):
            print(f'Linked correctly: {destination.relative_to(ROOT)}; preserving')
            continue
        try:
            destination.symlink_to(source.resolve(), target_is_directory=True)
        except OSError:
            if os.name != 'nt':
                raise
            subprocess.run(['cmd', '/c', 'mklink', '/J', str(destination), str(source.resolve())],
                           check=True, stdout=subprocess.DEVNULL)
        if not destination.is_dir() or destination.resolve() != source.resolve():
            raise RuntimeError(f'Could not verify Claude skill link: {destination}')
        print(f'Linked: {destination.relative_to(ROOT)} -> {source.relative_to(ROOT)}')


def validate():
    if tomllib is None:
        raise RuntimeError('Python 3.11 or newer is required (tomllib is unavailable).')
    errors = project_errors()
    if errors:
        raise RuntimeError('\n'.join(errors))
    for name in REQUIRED_SKILLS:
        if not (SKILLS_ROOT / name / 'SKILL.md').is_file():
            errors.append(f'Missing required skill: {name}')
    skills = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir() or is_link(path))
    for source in skills:
        try:
            check_path(source)
            check_path(source / 'SKILL.md')
            errors.extend(skill_errors(source / 'SKILL.md'))
            destination = ROOT / '.claude' / 'skills' / source.name
            check_path(destination, allow_leaf_link=True)
            if not is_link(destination) or not destination.is_dir() or destination.resolve() != source.resolve():
                errors.append(f'{destination}: missing or incorrect Claude skill link')
        except (OSError, RuntimeError, UnicodeError) as exc:
            errors.append(str(exc))
    present_gsap = [name for name in GSAP if os.path.lexists(SKILLS_ROOT / name)]
    if present_gsap:
        if len(present_gsap) != len(GSAP):
            errors.append('Incomplete GSAP installation: all eight skills are required when GSAP is present.')
        for path in (ROOT / '.codex' / 'docs' / 'GSAP_UPSTREAM.md', AGENT_ROOT / 'licenses' / 'gsap-skills-LICENSE'):
            if not path.is_file() or not path.read_text(encoding='utf-8').strip():
                errors.append(f'Missing or empty GSAP provenance/license: {path}')
    try:
        expected = expected_agent_files()
        for path, content in expected.items():
            check_path(path)
            if not path.is_file():
                errors.append(f'Missing generated agent: {path}')
            elif path.read_text(encoding='utf-8') != content:
                errors.append(f'{path}: differs from its canonical source; run --sync-agents')
    except (OSError, RuntimeError, UnicodeError) as exc:
        errors.append(str(exc))
    configs = sorted((ROOT / '.codex' / 'agents').glob('*.toml'))
    for config in configs:
        try:
            with config.open('rb') as file:
                data = tomllib.load(file)
            if not all(isinstance(data.get(key), str) and data[key].strip()
                       for key in ('name', 'description', 'developer_instructions')):
                errors.append(f'{config}: missing or invalid native Codex fields')
        except (OSError, ValueError, UnicodeError) as exc:
            errors.append(f'{config}: {exc}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise RuntimeError(f'{len(errors)} validation issue(s)')
    print(f'Validated {len(skills)} skills, {len(skills)} Claude links, '
          f'{len(AGENTS) * 3} synchronized agents and {len(configs)} Codex TOML configs.')


def main():
    if sys.version_info < (3, 11) or tomllib is None:
        print('Setup failed: Python 3.11 or newer is required. Run this script with a supported Python interpreter.', file=sys.stderr)
        return 1
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--install-gsap', action='store_true', help='Download 8 original GSAP skills from GitHub')
    parser.add_argument('--update-gsap', action='store_true', help='Replace all GSAP skills with the latest official versions (only with --install-gsap)')
    parser.add_argument('--sync-agents', action='store_true', help='Generate native Codex, Claude and Gemini subagent definitions')
    parser.add_argument('--link-claude', action='store_true', help='Link all skills to .claude/skills; reject existing conflicts')
    parser.add_argument('--validate', action='store_true', help='Check sources, required skills, generated agents, TOML syntax and Claude links')
    args = parser.parse_args()
    if args.update_gsap and not args.install_gsap:
        parser.error('--update-gsap requires --install-gsap')
    if not any((args.install_gsap, args.sync_agents, args.link_claude, args.validate)):
        args.sync_agents = args.link_claude = args.validate = True
    try:
        require_project()
        if args.install_gsap:
            install_gsap(args.update_gsap)
        if args.sync_agents:
            sync_agents()
        if args.link_claude:
            link_claude()
        if args.validate:
            validate()
    except (OSError, RuntimeError, ValueError, UnicodeError, subprocess.CalledProcessError) as exc:
        print(f'Setup failed: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
