# Project memory — habit-design-system

- Tech: plain HTML + CSS custom properties, no build tools, no JS framework.
  Matches the user's default web-prototype preferences.
- This repo is the source of truth; the Paper file (paper.design) is a
  consumer. Sync direction is repo → Paper by default; Paper → repo only as
  an explicit, reviewed "propose back" (branch/diff, never a direct push
  to main).
- Bootstrapped from an existing Paper file (habit-tracker app: Home, Stats,
  Profile screens) — tokens and markup were transcribed from Paper's
  `get_tokens`/`get_jsx` exports, not hand-designed from scratch.
- Paper's MCP plugin has a weekly call quota — keep syncs batched (one
  `create_tokens` call for additions, one `set_tokens` call for
  changes/removals per sync) rather than per-token calls.
- Markup is intentionally duplicated across `home.html`/`stats.html`/
  `profile.html` rather than using JS includes — `file://` + `fetch` is
  CORS-blocked without a server, and 3 screens is small enough that
  duplication is cheaper than solving that problem.
- Icons are inline SVG (stroke/fill `currentColor`, colored via the
  `.icon`'s parent), reused verbatim from Paper's exported markup.
- GitHub push/PR auth: user is installing `gh` CLI + `gh auth login`
  themselves (one-time, interactive OAuth — not something Claude can do).
