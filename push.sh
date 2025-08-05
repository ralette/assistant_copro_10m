#!/bin/bash

# Vérifie qu'on est bien dans un repo git
if [ ! -d .git ]; then
  echo "Pas un dépôt Git"
  exit 1
fi

# Ajoute tous les fichiers
git add .

# Utilise le message fourni ou un message par défaut
message=${1:-"Mise à jour automatique"}
git commit -m "$message"

# Pousse les modifications
git push
