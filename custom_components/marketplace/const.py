"""Constants for the Marketplace integration."""

DOMAIN = "marketplace"

CONF_TITLE = "title"
CONF_URL = "url"
CONF_ICON = "icon"
CONF_MODE = "mode"
CONF_REQUIRE_ADMIN = "require_admin"

MODE_IFRAME = "iframe"
MODE_NEW_TAB = "new_tab"

DEFAULT_TITLE = "Marketplace"
DEFAULT_ICON = "mdi:store"
DEFAULT_MODE = MODE_IFRAME

DEFAULT_URL = "/marketplace/browse?sort=last_updated&direction=desc&group=status"

# Must differ from "/marketplace": HA serves every sub-path of a panel URL with the frontend.
PANEL_URL_PATH = "marketplace-shortcut"
STATIC_URL = "/marketplace_static"
