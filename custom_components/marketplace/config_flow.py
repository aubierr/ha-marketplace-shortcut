"""Config flow for Marketplace."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry, ConfigFlow, ConfigFlowResult, OptionsFlow
from homeassistant.core import callback
from homeassistant.helpers import selector

from .const import (
    CONF_ICON,
    CONF_MODE,
    CONF_REQUIRE_ADMIN,
    CONF_TITLE,
    CONF_URL,
    DEFAULT_ICON,
    DEFAULT_MODE,
    DEFAULT_TITLE,
    DEFAULT_URL,
    DOMAIN,
    MODE_IFRAME,
    MODE_NEW_TAB,
)


def _schema(defaults: dict[str, Any]) -> vol.Schema:
    return vol.Schema(
        {
            vol.Required(CONF_TITLE, default=defaults.get(CONF_TITLE, DEFAULT_TITLE)): str,
            vol.Required(CONF_URL, default=defaults.get(CONF_URL, DEFAULT_URL)): selector.TextSelector(
                selector.TextSelectorConfig(type=selector.TextSelectorType.URL)
            ),
            vol.Required(CONF_ICON, default=defaults.get(CONF_ICON, DEFAULT_ICON)): selector.IconSelector(),
            vol.Required(CONF_MODE, default=defaults.get(CONF_MODE, DEFAULT_MODE)): selector.SelectSelector(
                selector.SelectSelectorConfig(
                    options=[MODE_IFRAME, MODE_NEW_TAB],
                    translation_key=CONF_MODE,
                    mode=selector.SelectSelectorMode.DROPDOWN,
                )
            ),
            vol.Required(
                CONF_REQUIRE_ADMIN, default=defaults.get(CONF_REQUIRE_ADMIN, False)
            ): bool,
        }
    )


def _validate(user_input: dict[str, Any]) -> dict[str, str]:
    errors: dict[str, str] = {}
    if not user_input[CONF_URL].startswith(("http://", "https://", "/")):
        errors[CONF_URL] = "invalid_url"
    return errors


class MarketplaceConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        errors: dict[str, str] = {}
        if user_input is not None:
            errors = _validate(user_input)
            if not errors:
                return self.async_create_entry(title=user_input[CONF_TITLE], data=user_input)
        return self.async_show_form(
            step_id="user", data_schema=_schema(user_input or {}), errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        return MarketplaceOptionsFlow()


class MarketplaceOptionsFlow(OptionsFlow):
    """Edit the shortcut after setup."""

    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        errors: dict[str, str] = {}
        if user_input is not None:
            errors = _validate(user_input)
            if not errors:
                return self.async_create_entry(data=user_input)
        current = user_input or {**self.config_entry.data, **self.config_entry.options}
        return self.async_show_form(step_id="init", data_schema=_schema(current), errors=errors)
