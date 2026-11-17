// Custom panel used in "new tab" mode: opens the URL in a new browser tab.
class MarketplaceRedirect extends HTMLElement {
  set panel(panel) {
    this._url = panel.config.url;
    this._title = panel.config.title || "Marketplace";
    this._render();
    this._open();
  }

  _open() {
    if (this._opened || !this._url) return;
    this._opened = true;
    window.open(this._url, "_blank", "noopener");
    // Return to the previous dashboard.
    if (history.length > 1) history.back();
  }

  _render() {
    this.innerHTML = `
      <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;gap:16px;font-family:var(--paper-font-body1_-_font-family, sans-serif);color:var(--primary-text-color)">
        <div>${this._title}</div>
        <a href="${this._url}" target="_blank" rel="noopener" style="color:var(--primary-color)">${this._url}</a>
      </div>`;
  }
}
customElements.define("marketplace-redirect", MarketplaceRedirect);
