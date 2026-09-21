# Agenda de Yassine

Planning de la semaine façon Google Calendar : services chez Madeleine, cours, et Kilua, l'assistant vocal.

En ligne : https://yassinelabiedh1-pixel.github.io/agenda-yassine/

## L'installer sur l'iPhone

1. Ouvre le lien dans **Safari**.
2. Touche **Partager** (le carré avec la flèche), puis **Sur l'écran d'accueil**.
3. Laisse « Ouvrir comme app web » activé, puis **Ajouter**.

## Raccourci Siri

Dans l'app **Raccourcis** : nouveau raccourci, action **Ouvrir les URL**, avec
`https://yassinelabiedh1-pixel.github.io/agenda-yassine/#kilua`, nommé par exemple « Kilua ».
« Dis Siri, Kilua » ouvre alors l'agenda directement sur Kilua.

## Fichiers

- `src/page.html` : la page (source).
- `build.py` : fabrique `index.html` à partir de `src/page.html` (`python build.py`).
- `manifest.webmanifest`, `icons/`, `sw.js` : ce qui en fait une app sur l'écran d'accueil et la garde utilisable hors ligne.
