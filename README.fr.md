<p align="center">
  <img src="logo.svg" alt="Marketplace" width="128" height="128">
</p>

# Marketplace Shortcut pour Home Assistant

🇬🇧 [English](README.md) · 🇫🇷 Français

Ajoute une entrée **Marketplace** dans la barre latérale de Home Assistant. Un chemin interne (ex. `/marketplace/browse`) ouvre directement la page dans Home Assistant.

## Prérequis

Home Assistant **2026.11** ou plus récent (la version qui introduit la Marketplace native).

## Installation

### Via la Marketplace (recommandé)

La Marketplace intégrée remplace HACS. Cette intégration s'ajoute comme dépôt personnalisé, ce qui nécessite de [connecter GitHub](https://www.home-assistant.io/integrations/marketplace/#connecting-github) à la Marketplace.

[![Ouvrir dans la Marketplace](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=aubierr&repository=ha-marketplace-shortcut&category=integration)

1. Cliquer sur le bouton ci-dessus. Ou aller dans **Paramètres → Marketplace → Ajouter depuis un lien** (*Add from link*), saisir `https://github.com/aubierr/ha-marketplace-shortcut` et valider avec **Ajouter** (*Add*).
2. Installer **Marketplace Shortcut**, puis redémarrer Home Assistant.
3. Ajouter l'intégration :

   [![Ajouter l'intégration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=marketplace_shortcut)

### Manuellement

1. Copier `custom_components/marketplace_shortcut` dans le dossier `config/custom_components/`.
2. Redémarrer Home Assistant.
3. **Paramètres → Appareils et services → Ajouter une intégration → Marketplace Shortcut**.

## Options

- **Titre** et **icône** (`mdi:store` par défaut) de l'entrée dans la barre latérale.
- **URL** de la marketplace.
- **Mode d'ouverture** :
  - *iframe* : affiché dans Home Assistant (ne fonctionne que si le site autorise l'intégration en iframe ; un site en `http://` est bloqué si HA est en HTTPS).
  - *nouvel onglet* : ouvre l'URL dans un nouvel onglet (à utiliser si le site refuse l'iframe).
- **Réservé aux administrateurs**.

Tout est modifiable ensuite via le bouton **Configurer** de l'intégration. L'entrée de la barre latérale peut aussi être masquée par utilisateur dans le profil.
