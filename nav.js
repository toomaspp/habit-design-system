(function () {
  var base = typeof NAV_BASE === "string" ? NAV_BASE : "";
  fetch(base + "nav.html")
    .then(function (res) { return res.text(); })
    .then(function (html) {
      var container = document.getElementById("nav");
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
    });
})();
