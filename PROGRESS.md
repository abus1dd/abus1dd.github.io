# Portfolio redesign: progress

Read this first in any new session. It records what is decided, what is done and what comes next.

- **Branch:** `redesign/animated-portfolio` (work here). `main` is the live site; changes reach it through a reviewed pull request.
- **Last updated:** 2026-10-30

## Status: live

The Desk redesign was merged into `main` on 2026-10-29 and is the live site at https://abus1dd.github.io/.

## How to edit

Edit `src/desk.html` (the source), then run `python tools/build.py` from the repo root to regenerate `index.html`. Never edit `index.html` by hand: the build minifies the script and writes the CSP hash, and a hand edit to the script would make the browser block it.

## What the site is

A single-page site built from `src/desk.html` (HTML, CSS, SVG, GSAP 3.12.5 + ScrollTrigger, self-hosted in `assets/js/`). All text, English and Italian, lives inside the page's script; `content/content.json` is the old site's text, kept only as a reference.

| Object | Section | Interaction |
|---|---|---|
| Notebook | About | Cover and pages flip open |
| Laptop | Projects | Working terminal (help, whoami, projects, open 1/2, skills, status, contact…) and a ~/projects tab with both projects |
| Phone | Contact | Lifts, unlocks, three apps (Email, LinkedIn, GitHub) open in new tabs |
| Mug | Fun fact | A different fact each click (8 facts, shuffled, never twice in a row) |
| CV folder | CV | Flap opens, page rises; downloads `assets/Abu-Bakar-Siddiq-CV.pdf` |
| Lamp | Day / night | Head nods, theme switches |
| Radio | EN / IT | Knob spins, static, language switches |
| Desk companion | AI assistant | Live AI via the Cloudflare Worker in `worker/` (abu-assistant.abus1dd.workers.dev); scripted answers as fallback |
| Plant (scroll) | Skills | Skill tags pop out |
| Calendar (scroll) | Journey | Month pages flip, timeline lights up |
| Keyboard (scroll) | Certifications | Key wave, dragon hologram, four Cisco badges with Credly links |
| Sticky note (wall) | Currently looking for | Pin pops, note flutters |

Mobile shows the objects as a stacked list; reduced-motion users get fades instead of zooms; a plain-text version of every section sits below the desk; a `<noscript>` block covers browsers without JavaScript.

## Security

- Content Security Policy (meta tag): scripts only from the site itself (inline script allowed by hash) and GoatCounter; connections only to the assistant Worker and GoatCounter; images from the site, Credly and GoatCounter; no plugins, no forms posting anywhere.
- GSAP 3.12.5 and ScrollTrigger are self-hosted in `assets/js/` (no third-party CDN).
- The inline script hash in the CSP must change whenever the script changes: the build step computes it.

## Assets

`assets/Abu-Bakar-Siddiq-CV.pdf`, `assets/dragon-hologram.webp` (lazy-loaded), `assets/js/` (GSAP), `404.html` (themed not-found page), `assets/ai-issue-resolution-workflow.mp4` + `-poster.jpg`, `assets/portfolio-desk.webp` (projects thumbnail), `assets/og-image.png` (link preview), `favicon.svg`.

## Contact links

Defined once in the `LINKS` object near the top of the script in `index.html`.

## Analytics

GoatCounter (`https://abus1dd.goatcounter.com/count`), registered and counting. No cookies.

## Performance

- 2026-10-29: fewer constant repaints (rain and circuit lines are compositor-only, no live backdrop blur), camera moves reuse layers while moving.
- 2026-10-29: light mode. Browsers drawing without a graphics card (software WebGL) or running the opening below 15 fps get the card layout, with a "Show the 3D desk anyway" button. `?desk=full` / `?desk=lite` in the URL forces a mode (remembered in localStorage).

- 2026-10-29: Lighthouse (lab, local server): desktop 99 performance / 100 accessibility / 100 SEO; mobile 83 / 100 / 100. Inline script minified, dragon image lazy-loaded, desk maths skipped while the desk is hidden.

## Case studies

- 2026-10-30: both projects have an expandable bilingual case study (problem, role, how it works, security, results, limits, stack), from the Nabla2 internship report and the ITS presentation. Client names and internal details are left out on purpose. The private project also says "More details are available on request". Laptop: results tiles on project 2 and `cat case-study` in the terminal. The assistant's facts include the results (needs `npx wrangler deploy` from `worker/`).

## Open items

- [x] Register `abus1dd` on GoatCounter (done 2026-10-29; stats at https://abus1dd.goatcounter.com).
- [x] LinkedIn preview checked with Post Inspector (2026-10-29): title, image and URL show correctly.
- [x] Live AI assistant (2026-10-29): Worker `abu-assistant` deployed at https://abu-assistant.abus1dd.workers.dev (model `@cf/qwen/qwen3-30b-a3b-fp8`, rate limit 6/min). Site connected via `LINKS.assistant`. After editing `worker/src/index.js`, run `npx wrangler deploy` from `worker/`.
- [ ] Proofread the English and Italian text (Abu).
- [ ] Test on a real iPhone (Safari) and Android phone, and on Firefox (Abu).
- [ ] Redeploy the assistant after facts changes: `cd worker` then `npx wrangler deploy` (Abu).
