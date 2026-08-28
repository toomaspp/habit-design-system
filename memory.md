# Project memory — habit-design-system

- Tech: plain HTML + CSS custom properties, no build tools, no JS framework.
  Matches the user's default web-prototype preferences.
- This repo is the source of truth; the design tool is a consumer. Sync
  direction is repo → design tool by default; design tool → repo only as
  an explicit, reviewed "propose back" (branch/diff, never a direct push
  to main).
- Bootstrapped from an existing Paper file (habit-tracker app: Home, Stats,
  Profile screens) — tokens and markup were transcribed from Paper's
  `get_tokens`/`get_jsx` exports, not hand-designed from scratch.
- **Design tool switched from Paper to Pencil (pen.dev) mid-project.**
  Reason: Paper has no real component/instance model (only copy/duplicate);
  Pencil does (`reusable: true` + `ref` instances with descendant
  overrides), which is what the design system actually needed. The repo's
  tokens/screens are unaffected by this switch — only the sync mechanics
  (which tool's API `sync-tokens.py`'s output feeds into) changed. See
  README.md for the current Pencil-based sync procedure.
- The Pencil file lives at `/Users/toomas.pippar/Documents/habit-app.pen`
  as of this writing, but its path has already moved once — always confirm
  via `get_app_state` rather than trusting a hardcoded path.
- 8 reusable Pencil components exist: StatusBar, Avatar, HeroCard, HabitRow,
  CheckControl, TabBar, StatTile, SettingsRow. Plus a 4th top-level page,
  "Styleguide," mirroring the tokens/type/radius reference (no code
  equivalent needed — it's documentation, not a screen).
- Pencil's `execute` tool had a real, reproducible bug during this build:
  new `ref`/`Copy` instances as the first items in certain vertical-layout
  containers intermittently collapsed to zero height / rendered blank.
  Workaround that consistently fixed it: use `Copy()` rather than manual
  `Insert({type:"ref",...})` for instancing, and rebuild the container fresh
  (`Replace` or delete+recreate) rather than patching in place if it recurs.
- Lucide icon names aren't 1:1 with the library's real names in this Pencil
  build — e.g. `"clock"` silently falls back to a placeholder glyph;
  `"alarm-clock"` works. When an icon renders as a generic
  question-mark/placeholder shape, that's the tell — try an alternate name
  or reuse an existing hand-drawn icon's path geometry instead.
- Markup is intentionally duplicated across `home.html`/`stats.html`/
  `profile.html` rather than using JS includes — `file://` + `fetch` is
  CORS-blocked without a server, and 3 screens is small enough that
  duplication is cheaper than solving that problem.
- Icons are inline SVG (stroke/fill `currentColor`, colored via the
  `.icon`'s parent), reused verbatim from Paper's exported markup.
- GitHub push/PR auth: user installed `gh` CLI + ran `gh auth login`
  themselves (one-time, interactive OAuth — not something Claude can do).
