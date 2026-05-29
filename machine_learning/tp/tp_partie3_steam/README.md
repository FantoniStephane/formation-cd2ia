# TP Partie 3 — Classification de Reviews Steam avec LSTM

**Notions abordées :** NLP, LSTM, TensorFlow/Keras, tokenisation, embedding, deep learning  
**Difficulté :** Avancé

---

## Ce que fait ce notebook

Prédit si un utilisateur **recommande ou non** un jeu vidéo à partir de son commentaire textuel.

Pipeline complet :
1. Exploration des données (EDA)
2. Nettoyage et normalisation du texte
3. Vectorisation (Tokenizer + Padding)
4. Modèle LSTM avec couche Embedding (TensorFlow/Keras)
5. Entraînement + courbes de convergence
6. Évaluation des performances
7. Sauvegarde et rechargement du modèle
8. Prédiction sur nouvelles phrases

---

## Dataset

`steam_reviews.csv` — 20 000 reviews de jeux vidéo Steam (fourni par le formateur).  
⚠️ Fichier non inclus dans le repo — à placer dans `data/` avant d'exécuter le notebook.

---

## Fichiers

```
tp_partie3_steam/
├── tp_partie3_steam.ipynb
├── data/
│   ├── steam_reviews.csv     ← à fournir manuellement
│   └── README.md
└── models/
    ├── model_steam_lstm.keras
    └── tokenizer_steam.json
```
