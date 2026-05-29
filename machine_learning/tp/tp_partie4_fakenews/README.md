# TP Partie 4 — Détection de Fake News

**Notions abordées :** NLP, TF-IDF, classification binaire, LSTM, courbe ROC, feature engineering  
**Difficulté :** Avancé

---

## Ce que fait ce notebook

Analyse des articles de presse pour prédire s'ils sont **FAUX** ou **VRAIS**.  
Problème de classification binaire avec pipeline NLP complet.

Étapes du projet :
1. Exploration et visualisation des données
2. Nettoyage NLP (stopwords, lemmatisation)
3. Feature Engineering + TF-IDF
4. Entraînement et comparaison de plusieurs modèles
5. Courbe ROC et matrices de confusion
6. Sauvegarde du meilleur modèle
7. Prédiction sur de nouveaux articles

---

## Dataset

Fourni par le formateur — fichiers `train.csv`, `test.csv` et `labels.txt` à placer dans `data/`.

---

## Fichiers

```
tp_partie4_fakenews/
├── tp_partie4_fakenews.ipynb
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── labels.txt
└── models/
    ├── fake_news_best_model.pkl
    └── fake_news_tfidf.pkl
```
