---
name: technical-seo
description: "Technical SEO for websites and React apps: crawlability, indexation, metadata, canonicals, sitemaps, structured data, hreflang, redirects, CWV, semantic HTML and search validation. Use when improving organic search discoverability."
---

# Technical SEO

## Workflow
- Identify site purpose, indexable pages, staging/production, canonical domain, languages and rendering strategy (SPA/SSR/SSG).
- Check crawlability and site health: HTTP status, robots.txt, XML sitemaps, canonical tags, redirects, noindex, routing and server-rendered or discoverable content.
- Audit unique page titles, descriptions, headings, semantic navigation, internal links and image descriptions; preserve meaningful content.
- Validate structured data with the applicable schema types; do not fabricate reviews, prices, offers or eligibility.
- For bilingual FR/EN pages, map equivalent translations with correct `hreflang`, canonicals and URL structure.
- Review Core Web Vitals and mobile usability; performance improvements require measurement.
- For React SPA, verify whether critical route content is indexable in target crawlers; consider SSR/SSG where necessary instead of assuming JS rendering suffices.
- Test important URLs and route changes without accidentally indexing staging.

## Verification
Report concrete URL examples, metadata and structured-data checks, indexing limitations, and items that require Search Console access rather than guessing.

Reference: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
