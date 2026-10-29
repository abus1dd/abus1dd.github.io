# Portfolio redesign: progress

Read this first in any new session. It records what is decided, what is done and what comes next.

- **Branch:** `redesign/animated-portfolio` (work here). `main` is the live site; changes reach it through a reviewed pull request.
- **Last updated:** 2026-10-29

## Status: live

The Desk redesign was merged into `main` on 2026-10-29 and is the live site at https://abus1dd.github.io/.

## What the site is

A single self-contained `index.html` (HTML, CSS, SVG, GSAP 3.12.5 + ScrollTrigger from cdnjs). All text, English and Italian, lives inside the page's script; `content/content.json` is the old site's text, kept only as a reference.

| Object | Section | Interaction |
|---|---|---|
| Notebook | About | Cover and pages flip open |
| Laptop | Projects | Working terminal (help, whoami, projects, open 1/2, skills, status, contact…) and a ~/projects tab with both projects |
| Phone | Contact | Lifts, unlocks, three apps (Email, LinkedIn, GitHub) open in new tabs |
| Mug | Fun fact | A different fact each click (8 facts, shuffled, never twice in a row) |
| CV folder | CV | Flap opens, page rises; downloads `assets/Abu-Bakar-Siddiq-CV.pdf` |
| Lamp | Day / night | Head nods, theme switches |
| Radio | EN / IT | Knob spins, static, language switches |
| Desk companion | AI assistant | Scripted answers on GitHub Pages; live answers only inside the Claude preview |
| Plant (scroll) | Skills | Skill tags pop out |
| Calendar (scroll) | Journey | Month pages flip, timeline lights up |
| Keyboard (scroll) | Certifications | Key wave, dragon hologram, four Cisco badges with Credly links |
| Sticky note (wall) | Currently looking for | Pin pops, note flutters |

Mobile shows the objects as a stacked list; reduced-motion users get fades instead of zooms; a plain-text version of every section sits below the desk; a `<noscript>` block covers browsers without JavaScript.

## Assets

`assets/Abu-Bakar-Siddiq-CV.pdf`, `assets/ai-issue-resolution-workflow.mp4` + `-poster.jpg`, `assets/portfolio-desk.webp` (projects thumbnail), `assets/og-image.png` (link preview), `favicon.svg`.

## Contact links

Defined once in the `LINKS` object near the top of the script in `index.html`.

## Analytics

GoatCounter (`https://abus1dd.goatcounter.com/count`), registered and counting. No cookies.

## Performance

- 2026-10-29: fewer constant repaints (rain and circuit lines are compositor-only, no live backdrop blur), camera moves reuse layers while moving.
- 2026-10-29: light mode. Browsers drawing without a graphics card (software WebGL) or running the opening below 15 fps get the card layout, with a "Show the 3D desk anyway" button. `?desk=full` / `?desk=lite` in the URL forces a mode (remembered in localStorage).

## Open items

- [x] Register `abus1dd` on GoatCounter (done 2026-10-29; stats at https://abus1dd.goatcounter.com).
- [x] LinkedIn preview checked with Post Inspector (2026-10-29): title, image and URL show correctly.
- [ ] Later: live AI assistant via a small backend (e.g. a Cloudflare Worker with daily caps).
