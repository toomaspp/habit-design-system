#!/bin/bash
# Double-click this file to serve the design system locally and open it
# in your browser. Needed because the sidebar nav is fetched via JS,
# which browsers block when a page is opened directly (double-clicked)
# instead of served over http://.
cd "$(dirname "$0")"
PORT=8420
python3 -m http.server "$PORT" &
SERVER_PID=$!
sleep 1
open "http://localhost:$PORT/index.html"
echo "Serving at http://localhost:$PORT — close this window to stop."
wait $SERVER_PID
