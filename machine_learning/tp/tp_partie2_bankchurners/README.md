# TP Partie 2 — Prédiction du Churn Bancaire

**Notions abordées :** classification, PCA, validation croisée, GridSearch, XGBoost, pipeline  
**Difficulté :** Intermédiaire

---

## Ce que fait ce notebook

Prédit le départ (churn) des clients d'une banque à partir de leurs données comportementales.

Le TP se déroule en deux étapes :
1. Exploration des données + modèle de base avec validation croisée
2. Optimisation avec PCA + Grid Search + modèle fort (XGBoost)

---

## Dataset

`BankChurners.csv` — 10 127 clients, 23 variables (données comportementales et démographiques).

---

## Modèles utilisés

- Régression Logistique, SVM, Arbre de Décision
- Random Forest, Gradient Boosting, **XGBoost**

---

## Fichiers

```
tp_partie2_bankchurners/
├── tp_partie2_bankchurners.ipynb
└── data/
    ├── BankChurners.csv
    └── dictionnaire.txt
```
