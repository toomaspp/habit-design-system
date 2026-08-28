#!/bin/bash
# Double-click this file to serve the design system locally and open it
# in your browser. Needed because the sidebar nav is fetched via JS,
# which browsers block when a page is opened directly (double-clicked)
# instead of served over http://.
#
# The server runs detached, so closing this Terminal window afterwards is
# fine and won't break the site. To stop the server later, run:
#   pkill -f "http.server 8420"
cd "$(dirname "$0")"
PORT=8420

if ! lsof -i ":$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  nohup python3 -m http.server "$PORT" > /tmp/habit-design-system-preview.log 2>&1 &
  disown
  sleep 1
  echo "Started server on port $PORT (runs in the background - closing this window is fine)."
else
  echo "Server already running on port $PORT."
fi

open "http://localhost:$PORT/index.html"
echo "To stop it later: pkill -f \"http.server $PORT\""
sleep 2
