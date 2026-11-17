# Marketplace shortcut for Home Assistant

Ajoute une entrée **Marketplace** dans la barre latérale de Home Assistant, à la manière de HACS.

## Installation

1. Copier `custom_components/marketplace` dans le dossier `config/custom_components/` (ou ajouter ce dépôt comme dépôt personnalisé HACS).
2. Redémarrer Home Assistant.
3. **Paramètres → Appareils et services → Ajouter une intégration → Marketplace**.

## Options

- **Titre** et **icône** (`mdi:store` par défaut) de l'entrée dans la barre latérale.
- **URL** de la marketplace.
- **Mode d'ouverture** :
  - *iframe* : affiché dans Home Assistant (ne fonctionne que si le site autorise l'intégration en iframe ; un site en `http://` est bloqué si HA est en HTTPS).
  - *nouvel onglet* : ouvre l'URL dans un nouvel onglet (à utiliser si le site refuse l'iframe).
- **Réservé aux administrateurs**.

Tout est modifiable ensuite via le bouton **Configurer** de l'intégration. L'entrée de la barre latérale peut aussi être masquée par utilisateur dans le profil.
