# Portfolio assistant (Cloudflare Worker)

A small Cloudflare Worker that answers visitors' questions about Abu with Workers AI. The site calls it from the chat on the desk. If the Worker is unreachable, rate-limited or out of its free daily allowance, the site falls back to its scripted answers, so the chat never breaks.

## What it protects against

| Risk | Protection |
|---|---|
| Other websites using it | Only `ALLOWED_ORIGINS` (https://abus1dd.github.io) get a CORS answer |
| Spamming | 6 questions per minute per visitor (rate-limit binding), plus an 8/minute in-memory limit |
| Huge requests | Body ≤ 8 KB, last 8 messages, 500 characters each, answers ≤ 220 tokens |
| Prompt injection | System prompt and facts live only in the Worker; visitor "system" messages are dropped; the prompt refuses to change rules or talk about anything but Abu |
| Cost | On the Workers Free plan, Workers AI stops at 10,000 neurons/day (resets 00:00 UTC) instead of charging. One question costs roughly 8 neurons with the default model |

The Origin check stops browsers on other sites, not scripts that fake the header. The rate limits and the free daily allowance cap what such scripts can do.

## Deploy (about 10 minutes)

You need a free Cloudflare account and Node.js 18 or newer.

```bash
cd worker
npx wrangler login          # opens the browser: log in to Cloudflare and click Allow
npx wrangler deploy         # prints the URL, e.g. https://abu-assistant.<your-subdomain>.workers.dev
```

Then put that URL in `index.html`, in the `LINKS` object: `assistant: 'https://abu-assistant.<your-subdomain>.workers.dev',`.

If `deploy` rejects the `ratelimits` block, delete it from `wrangler.jsonc` and deploy again: the built-in limit still applies.

## Test it

```bash
curl -s https://abu-assistant.<your-subdomain>.workers.dev/      # {"ok":true,"service":"abu-assistant"}
curl -s -X POST https://abu-assistant.<your-subdomain>.workers.dev/ \
  -H "Origin: https://abus1dd.github.io" -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"What did Abu do at Nabla2?"}]}'
```

## Updating facts

The facts are in `FACTS` at the top of `src/index.js`. After changing them, run `npx wrangler deploy` again. Keep them in step with the site.

## Settings (`wrangler.jsonc` → `vars`)

- `ALLOWED_ORIGINS`: comma-separated sites allowed to call the Worker.
- `MODEL`: Workers AI model id. Default `@cf/qwen/qwen3-30b-a3b-fp8`; if it fails, the Worker tries `@cf/meta/llama-3.1-8b-instruct`.
