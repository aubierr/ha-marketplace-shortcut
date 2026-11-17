// Custom panel: redirects to the configured URL.
// - Path inside Home Assistant ("/...") -> in-app navigation (no iframe, no nested sidebar)
// - External URL -> opens a new browser tab
class MarketplaceRedirect extends HTMLElement {
  set panel(panel) {
    this._url = panel.config.url;
    this._title = panel.config.title || "Marketplace";
    this._render();
    this._go();
  }

  _go() {
    if (this._done || !this._url) return;
    this._done = true;
    if (this._url.startsWith("/")) {
      // replaceState so the browser "back" button doesn't bounce back here.
      history.replaceState(history.state, "", this._url);
      window.dispatchEvent(new CustomEvent("location-changed", { detail: { replace: true } }));
    } else {
      window.open(this._url, "_blank", "noopener");
      if (history.length > 1) history.back();
    }
  }

  _render() {
    const a = document.createElement("a");
    a.href = this._url;
    a.textContent = this._url;
    if (!this._url.startsWith("/")) {
      a.target = "_blank";
      a.rel = "noopener";
    }
    a.style.color = "var(--primary-color)";
    const wrap = document.createElement("div");
    wrap.style.cssText =
      "display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;gap:16px;color:var(--primary-text-color)";
    const t = document.createElement("div");
    t.textContent = this._title;
    wrap.append(t, a);
    this.replaceChildren(wrap);
  }
}
customElements.define("marketplace-redirect", MarketplaceRedirect);
