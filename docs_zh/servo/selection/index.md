<div class="fs-selection-shell">
  <iframe
    id="fs-selection-iframe"
    src="./servo-selection.html"
    title="舵机选型器"
    loading="lazy"
  ></iframe>
</div>

<style>
body:has(.fs-selection-shell) .md-sidebar--primary,
body:has(.fs-selection-shell) .md-sidebar--secondary {
  display: none !important;
}

body:has(.fs-selection-shell) .md-path {
  display: none !important;
}

body:has(.fs-selection-shell) .md-main__inner {
  margin: 0 !important;
}

body:has(.fs-selection-shell) .md-main .md-grid {
  max-width: 100% !important;
}

body:has(.fs-selection-shell) .md-content {
  max-width: 100% !important;
}

body:has(.fs-selection-shell) .md-content__inner {
  margin: 0 !important;
  padding: 0 !important;
}

body:has(.fs-selection-shell) .md-content__inner > h1 {
  display: none !important;
}

body:has(.fs-selection-shell) .md-content__inner::before {
  display: none !important;
}

.md-typeset .fs-selection-shell {
  width: 100%;
  margin: 0;
  border: 0;
  border-radius: 0;
  overflow: visible;
  background: transparent;
}

.md-typeset .fs-selection-shell iframe {
  display: block;
  width: 100%;
  height: calc(100dvh - 4.8rem);
  min-height: calc(100dvh - 4.8rem);
  border: 0;
}

@media (max-width: 900px) {
  .md-typeset .fs-selection-shell iframe {
    height: calc(100dvh - 4.2rem);
    min-height: calc(100dvh - 4.2rem);
  }
}
</style>

<script>
(function () {
  const iframe = document.getElementById("fs-selection-iframe");
  if (!iframe) return;

  const postTheme = () => {
    const scheme = document.body.getAttribute("data-md-color-scheme") || "default";
    if (iframe.contentWindow) {
      iframe.contentWindow.postMessage(
        { type: "fs-wiki-theme", scheme: scheme },
        "*"
      );
    }
  };

  iframe.addEventListener("load", postTheme);
  postTheme();

  const observer = new MutationObserver(postTheme);
  observer.observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"]
  });
})();
</script>
