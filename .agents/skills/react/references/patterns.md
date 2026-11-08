# React Patterns and Anti-patterns

## Correct derived state
```tsx
function OrderSummary({ items }: { items: Array<{price: number; qty: number}> }) {
  const total = items.reduce((sum, item) => sum + item.price * item.qty, 0);
  return <output aria-label="Order total">{total.toFixed(2)}</output>;
}
```
Do not store `total` in local state and then maintain it using an Effect. Derive from source data.

## External effects with cleanup
```tsx
import { useEffect, useState } from 'react';

function useOnlineStatus() {
  const [online, setOnline] = useState(() =>
    typeof navigator === 'undefined' ? true : navigator.onLine
  );
  useEffect(() => {
    const update = () => setOnline(navigator.onLine);
    window.addEventListener('online', update);
    window.addEventListener('offline', update);
    return () => {
      window.removeEventListener('online', update);
      window.removeEventListener('offline', update);
    };
  }, []);
  return online;
}
```
For server-rendered code, ensure initial server and client markup are consistent; `useSyncExternalStore` is often preferable for external subscriptions.

## Async effects
- Prefer router/framework loaders or existing server-state library.
- If fetching in an Effect, handle abort and stale responses with AbortController. Avoid setting state for a request that no longer represents current input.
- Include loading, error, empty and success states; test rapid transitions and interrupted navigation.

## Avoid
- Unstable list keys on reorderable elements.
- Changing refs during render or manipulating the DOM behind React's back.
- Subscribing to browser events without cleanup.
- Using `useMemo`/`useCallback` indiscriminately when React Compiler or simpler code suffices.
- Adding an application-wide state management library for a local UI problem.
