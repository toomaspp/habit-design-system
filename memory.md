# Project memory — habit-design-system

- Tech: plain HTML + CSS custom properties, no build tools, no JS framework
  beyond the tiny shared-nav fetch script. Matches the user's default
  web-prototype preferences.
- This repo is the source of truth; Pencil (pen.dev) is the design tool and
  a consumer of it. Sync direction is repo → Pencil by default; Pencil →
  repo only as an explicit, reviewed "propose back" (branch/diff, never a
  direct push to main). See README.md for the full sync procedure.
- The Pencil file lives at `/Users/toomas.pippar/Documents/habit-app.pen`
  as of this writing, but its path has already moved once — always confirm
  via `get_app_state` rather than trusting a hardcoded path.
- 8 reusable Pencil components exist: StatusBar, Avatar, HeroCard, HabitRow,
  CheckControl, TabBar, StatTile, SettingsRow. Plus two reference-only
  top-level pages: "Styleguide" (tokens/type/radius reference) and a nav
  design mockup (`bPI5p`) — kept intentionally, not a real screen, used as
  the source for the current sidebar nav styling in `docs.css`.

## Documentation site (components/, patterns/, screens/, index.html)

- Multi-page site: root `index.html` covers Foundations (colors, type,
  spacing/radius); `components/` and `patterns/` each have one page per
  item (Preview → Variants → Guidelines → Code); `screens/index.html`
  links out to the real `home.html`/`stats.html`/`profile.html` at the
  repo root (those are the actual app prototype, never moved).
- Sidebar nav is one shared `nav.html` partial fetched by `nav.js` into
  every page (not duplicated) — **this means the site must be viewed
  through a local server**, not opened via `file://`. Adding a page: copy
  an existing one's structure, add it to `nav.html`, link it from that
  folder's `index.html`.
- Recurring bug worth remembering: several component classes
  (`.tab-bar`, `.progress-track`, etc.) get their width for free by
  stretching inside `.screen` (a column flexbox). The docs `.demo`
  container is a row flexbox, so that stretch doesn't happen there — any
  new pattern/component demo needs an explicit `width` (not `max-width`)
  on its wrapper, or it collapses to fit-content and looks broken. Hit
  this twice (Tab bar, Progress bar) before catching the pattern.
- Verification gotcha: the browser aggressively caches linked stylesheets
  independently of the HTML page's own cache-busting — navigating to
  `page.html?v=2` does NOT guarantee `docs.css` re-fetches. Force it with
  a small JS snippet that rewrites each `<link>`'s href with a fresh query
  param before screenshotting, or you'll "verify" a stale render.

## Design tokens

- Colors, type, radius as before. Added a real spacing scale: `--space-xs`
  (4px) through `--space-3xl` (28px), every step divisible by 4 — replaced
  the ad-hoc values that used to live directly in `components.css`.
- `sync-tokens.py` categorizes token types by name prefix
  (`--color-`/`--space-`/etc.) for Pencil's `SetVariables` call — if a new
  token prefix is ever added, it needs a matching entry in that script's
  `TYPE_PREFIXES` list or it falls back to "unknown".

## Pencil-specific gotchas

- The `execute` tool had a real, reproducible bug during this build: new
  `ref`/`Copy` instances as the first items in certain vertical-layout
  containers intermittently collapsed to zero height / rendered blank.
  Workaround that consistently fixed it: use `Copy()` rather than manual
  `Insert({type:"ref",...})` for instancing, and rebuild the container
  fresh (`Replace` or delete+recreate) rather than patching in place if it
  recurs.
- Lucide icon names aren't 1:1 with the library's real names in this
  Pencil build — e.g. `"clock"` silently falls back to a placeholder
  glyph; `"alarm-clock"` works. A generic question-mark/placeholder glyph
  is the tell — try an alternate name or reuse an existing hand-drawn
  icon's path geometry instead.

## Other

- Markup is intentionally duplicated across `home.html`/`stats.html`/
  `profile.html` rather than using JS includes for the app screens
  themselves — `file://` + `fetch` is CORS-blocked without a server, and
  3 screens is small enough that duplication is cheaper than solving that
  (the documentation site's shared nav is the one place that tradeoff was
  made differently, since it's expected to grow much larger).
- Icons are inline SVG (stroke/fill `currentColor`, colored via the
  `.icon`'s parent).
- GitHub push/PR auth: user installed `gh` CLI + ran `gh auth login`
  themselves (one-time, interactive OAuth — not something Claude can do).
