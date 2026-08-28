# Habit Tracker — Design System

Source of truth for the habit-tracker app's design tokens and screens.
Developers consume this repo directly. The Paper file (visual design tool)
is kept as a **consumer** of this repo, not the other way around.

## Files

- `tokens.css` — the canonical design tokens (`:root{}` custom properties).
  Edit values here.
- `components.css` — semantic component classes built from the tokens.
- `home.html`, `stats.html`, `profile.html` — the three app screens.
- `index.html` — links to all three, for a quick visual check in a browser.
- `.paper-sync-snapshot.css` — a copy of `tokens.css` as of the last
  successful push into Paper. Don't edit this by hand; it's maintained by
  the sync process below.
- `sync-tokens.py` — computes the diff between `tokens.css` and the
  snapshot. Doesn't talk to Paper itself (only Claude's session can call
  Paper's MCP tools) — its output is what gets fed into Paper's
  `create_tokens`/`set_tokens` calls.

## Sync direction

**Normal flow: this repo → Paper.** When `tokens.css` changes, ask Claude to
sync it into Paper. Claude runs `sync-tokens.py`, then applies the
added/changed/removed tokens to the Paper file, then updates
`.paper-sync-snapshot.css` to match.

**Exceptional flow: Paper → this repo.** If a designer makes a deliberate
change directly in Paper that should become a real system change, ask
Claude to "propose it back." Claude will pull the current Paper tokens,
diff them against the snapshot, and open a branch/PR with just that change
for review — it will never push directly to `main`.

## Screens

Open `index.html` directly in a browser — no build step, no server needed.
