"""Marketplace: adds a sidebar entry (like HACS) pointing to a configurable URL."""

from __future__ import annotations

from pathlib import Path

from homeassistant.components import frontend, panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import (
    CONF_ICON,
    CONF_MODE,
    CONF_REQUIRE_ADMIN,
    CONF_TITLE,
    CONF_URL,
    DEFAULT_ICON,
    DEFAULT_MODE,
    DEFAULT_TITLE,
    DOMAIN,
    MODE_NEW_TAB,
    PANEL_URL_PATH,
    STATIC_URL,
)

_STATIC_KEY = f"{DOMAIN}_static_registered"


def _conf(entry: ConfigEntry) -> dict:
    """Merge data and options (options win)."""
    return {**entry.data, **entry.options}


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Register the sidebar panel."""
    conf = _conf(entry)
    title = conf.get(CONF_TITLE, DEFAULT_TITLE)
    icon = conf.get(CONF_ICON, DEFAULT_ICON)
    url = conf[CONF_URL]
    mode = conf.get(CONF_MODE, DEFAULT_MODE)
    require_admin = conf.get(CONF_REQUIRE_ADMIN, False)

    # A path inside Home Assistant (e.g. /marketplace/browse) can't be put in an
    # iframe (it would nest the whole frontend), so navigate to it instead.
    if mode == MODE_NEW_TAB or url.startswith("/"):
        if not hass.data.get(_STATIC_KEY):
            await hass.http.async_register_static_paths(
                [
                    StaticPathConfig(
                        STATIC_URL,
                        str(Path(__file__).parent / "frontend"),
                        cache_headers=False,
                    )
                ]
            )
            hass.data[_STATIC_KEY] = True

        await panel_custom.async_register_panel(
            hass,
            webcomponent_name="marketplace-redirect",
            frontend_url_path=PANEL_URL_PATH,
            sidebar_title=title,
            sidebar_icon=icon,
            module_url=f"{STATIC_URL}/marketplace-redirect.js",
            config={"url": url, "title": title},
            require_admin=require_admin,
            embed_iframe=False,
        )
    else:
        frontend.async_register_built_in_panel(
            hass,
            component_name="iframe",
            sidebar_title=title,
            sidebar_icon=icon,
            frontend_url_path=PANEL_URL_PATH,
            config={"url": url},
            require_admin=require_admin,
        )

    entry.async_on_unload(entry.add_update_listener(_async_reload))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Remove the sidebar panel."""
    frontend.async_remove_panel(hass, PANEL_URL_PATH)
    return True


async def _async_reload(hass: HomeAssistant, entry: ConfigEntry) -> None:
    await hass.config_entries.async_reload(entry.entry_id)
