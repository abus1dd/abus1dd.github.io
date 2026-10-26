# Portfolio redesign: progress

Read this first in any new session. It records what is decided, what is done and what comes next.

- **Branch:** `redesign/animated-portfolio` (work here). `main` is the live site and stays untouched until a reviewed pull request.
- **Full plan:** the Claude Doc "Portfolio redesign: piano completo".
- **Last updated:** 2026-10-26

## Decisions

| Item | Decision |
|---|---|
| Concept | **The Desk**: interactive top-down desk; each object is a section |
| Tone | Professional writing. Personality comes from motion and interaction |
| Languages | English + Italian, from `content/content.json` |
| Stack | Plain HTML/CSS/JS, GSAP + ScrollTrigger, Lenis, optional Three.js; Vite optional |
| Visual design | Abu designs it in Claude Design and brings it back |
| AI assistant | Scripted first, then Cloudflare Worker + Workers AI free tier with daily caps |
| Private project | `gitlab_ai_workflow` (shown as "AI Issue-Resolution Workflow"): description + video only, no code or internal details |

### Desk object map

| Object | Section |
|---|---|
| Notebook | About |
| Laptop | Projects |
| Phone | Contact |
| Mug | Fun fact |
| Folder | CV (EN + IT) |
| Lamp | Day/night theme |
| Radio | EN/IT switch |
| Desk companion | AI assistant |
| Scroll extras (plant, calendar, keyboard) | Skills, journey, "currently looking for" |

## Status

| Phase | Status |
|---|---|
| 0. Foundations | **In progress**: content extracted; tokens and EN/IT switch next |
| 1. Motion engine | Not started |
| Pause: design in Claude Design | Waiting on Abu |
| 2. Build the Desk | Blocked on design |
| 3. Private project card + video | Blocked on video file |
| 4. AI assistant | Not started |
| 5. Content safety and polish | Not started |
| 6. Quality gates and launch (PR to `main`) | Not started |

## Done

- 2026-10-25: created branch `redesign/animated-portfolio` from `main` (72b0581).
- 2026-10-26: extracted every visible and tabbed string from the old `index.html` into `content/content.json` (EN verbatim, IT first translation). Checked line by line against the original.

## Notes about the old site

- `index.html` is a bundled export (content lives in a JSON-escaped template inside a `<script type="__bundler/template">`). It is kept unchanged on this branch as a reference until the new site replaces it.
- Assets: `assets/Abu-Bakar-Siddiq-CV.pdf`, `assets/og-image.png`, `favicon.svg`.

## Open items for Abu

- [ ] Proofread the Italian text in `content/content.json`.
- [ ] Supply the conceptual animation video for the private project.
- [ ] Supply one short fun fact for the mug.
- [ ] Provide an Italian CV PDF (only the English-language file exists).
- [ ] Bring back the Claude Design output.
- [ ] Confirm nothing in the project descriptions must stay private.

## Next steps

1. Design tokens in CSS variables (placeholder values until the design arrives).
2. EN/IT switch reading `content/content.json` (remember choice, default from browser language).
3. Phase 1 motion engine: Lenis, GSAP/ScrollTrigger, reveal/zoom helpers, reduced-motion support.
