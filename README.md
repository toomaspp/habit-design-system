# Habit Tracker — Design System

Source of truth for the habit-tracker app's design tokens and screens.
Developers consume this repo directly. The Pencil (pen.dev) design file is
kept as a **consumer** of this repo, not the other way around.

## Files

- `tokens.css` — the canonical design tokens (`:root{}` custom properties).
  Edit values here.
- `components.css` — semantic component classes built from the tokens.
- `home.html`, `stats.html`, `profile.html` — the three app screens (the
  real prototype, not documentation).
- `index.html`, `docs.css`, `nav.html`, `nav.js` — the design system
  documentation site. `index.html` covers Foundations (colors, typography,
  spacing/radius) and links into three sub-sections; `docs.css` is the
  site's shared chrome (sidebar, cards, demo containers — separate from
  the app's own `components.css`); `nav.html`/`nav.js` are the shared
  sidebar, fetched into every page rather than duplicated (see below).
- `components/` — one page per reusable component (Avatar, Stat tile,
  Habit row, Settings row, Card), each with a live preview, its variants,
  usage guidelines, and a copyable code snippet.
- `patterns/` — one page per composed pattern (Status bar, Tab bar, Habit
  list, Settings list, Progress bar) — how components combine into
  recurring UI sections.
- `screens/index.html` — links out to the three real screens at the repo
  root.
- `.design-sync-snapshot.css` — a copy of `tokens.css` as of the last
  successful push into Pencil. Don't edit this by hand; it's maintained by
  the sync process below.
- `sync-tokens.py` — computes the diff between `tokens.css` and the
  snapshot. Doesn't talk to Pencil itself (only Claude's session can call
  Pencil's tools) — its output is what gets fed into Pencil's
  `GetVariables`/`SetVariables` calls.

## Documentation site structure

Every page declares `const NAV_BASE = "";` (root) or `"../"` (one level
deep, e.g. `components/avatar.html`) before loading `nav.js`, which fetches
`nav.html`, substitutes that base into its relative links, injects it into
`<nav id="nav">`, and highlights the current page. **This means the site
must be viewed through a local server** (e.g. `preview_start` /
`python3 -m http.server`) — opening a file directly (`file://`) won't run
the fetch. `home.html`/`stats.html`/`profile.html` don't have this
requirement; they're plain standalone pages.

Adding a new component/pattern page: copy the structure of an existing one
in `components/`/`patterns/` (Preview → Variants → Guidelines → Code
sections), add it to `nav.html`, and link it from that folder's
`index.html`. Future content types (guidelines-only pages, worked
examples, etc.) should follow the same per-page section pattern.

## Sync direction

**Normal flow: this repo → Pencil.** When `tokens.css` changes, ask Claude to
sync it into Pencil. Claude runs `sync-tokens.py` to get the added/changed/
removed tokens, then applies them via `SetVariables`: a merge call
(`replace: false`) if nothing was removed, or a full-set call
(`replace: true`) if something was — Pencil has no per-key delete. Then
Claude updates `.design-sync-snapshot.css` to match `tokens.css` and commits.

**Exceptional flow: Pencil → this repo.** If a designer makes a deliberate
change directly in Pencil that should become a real system change, ask
Claude to "propose it back." Claude will read the current Pencil variables
via `GetVariables`, diff them against the snapshot, and open a branch/PR with
just that change for review — it will never push directly to `main`.

**Scope:** the sync covers tokens only. Screen and component structure
(the 8 reusable Pencil components — StatusBar, Avatar, HeroCard, HabitRow,
CheckControl, TabBar, StatTile, SettingsRow — and this documentation site)
are built/maintained by hand, not generated from a script.

**Note:** the `.pen` file's path can change if the designer moves/renames it
(it already has once). Always resolve the current path via Pencil's
`get_app_state` before targeting it — don't hardcode a path.
