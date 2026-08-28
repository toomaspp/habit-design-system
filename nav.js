(function () {
  var base = typeof NAV_BASE === "string" ? NAV_BASE : "";
  var container = document.getElementById("nav");
  fetch(base + "nav.html")
    .then(function (res) {
      if (!res.ok) throw new Error("nav.html responded with " + res.status);
      return res.text();
    })
    .then(function (html) {
      if (!container) return;
      container.innerHTML = html.split("{base}").join(base);
      var links = container.querySelectorAll("a.nav-link");
      for (var i = 0; i < links.length; i++) {
        var link = links[i];
        if (link.getAttribute("href").indexOf("#") !== -1) continue;
        if (link.pathname === window.location.pathname) {
          link.classList.add("active");
        }
      }
    })
    .catch(function (err) {
      console.error("Sidebar nav failed to load:", err);
      if (!container) return;
      container.innerHTML =
        '<a class="brand" href="' + base + 'index.html">Design System</a>' +
        '<p style="font-size:13px;color:var(--color-muted);padding:0 8px;">' +
        "Nav failed to load — this site needs to be opened through the local " +
        "server (e.g. http://localhost:4173/...), not by double-clicking the " +
        "file directly." +
        "</p>";
    });
})();
