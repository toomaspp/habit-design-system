# Habit Tracker — Design System

Source of truth for the habit-tracker app's design tokens and screens.
Developers consume this repo directly. The Pencil (pen.dev) design file is
kept as a **consumer** of this repo, not the other way around.

## Files

- `tokens.css` — the canonical design tokens (`:root{}` custom properties).
  Edit values here.
- `components.css` — semantic component classes built from the tokens.
- `home.html`, `stats.html`, `profile.html` — the three app screens.
- `index.html` — links to all three, for a quick visual check in a browser.
- `.design-sync-snapshot.css` — a copy of `tokens.css` as of the last
  successful push into Pencil. Don't edit this by hand; it's maintained by
  the sync process below.
- `sync-tokens.py` — computes the diff between `tokens.css` and the
  snapshot. Doesn't talk to Pencil itself (only Claude's session can call
  Pencil's tools) — its output is what gets fed into Pencil's
  `GetVariables`/`SetVariables` calls.

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
(the 8 reusable components — StatusBar, Avatar, HeroCard, HabitRow,
CheckControl, TabBar, StatTile, SettingsRow — and the Styleguide reference
page) are built by hand in Pencil, not generated from this repo.

**Note:** the `.pen` file's path can change if the designer moves/renames it
(it already has once). Always resolve the current path via Pencil's
`get_app_state` before targeting it — don't hardcode a path.

## Screens

Open `index.html` directly in a browser — no build step, no server needed.
