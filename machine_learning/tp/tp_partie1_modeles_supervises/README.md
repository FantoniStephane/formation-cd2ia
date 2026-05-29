# TP Partie 1 — Modèles Supervisés

**Notions abordées :** classification, régression, scikit-learn, métriques, matrices de confusion  
**Difficulté :** Intermédiaire

---

## Ce que fait ce notebook

Compare 6 modèles de classification sur le dataset Iris et évalue une régression linéaire sur le dataset Diabetes.

---

## Datasets utilisés

- **Iris** — classification de 3 espèces de fleurs (150 échantillons, 4 features)
- **Diabetes** — régression sur la progression du diabète (442 patients, 10 features)

---

## Modèles comparés

| Modèle | Type |
|--------|------|
| Régression Logistique | Classification |
| SVM | Classification |
| Naive Bayes | Classification |
| Arbre de Décision | Classification |
| Random Forest | Classification |
| LDA | Classification |
| Régression Linéaire | Régression |

---

## Résultats

| Rang | Modèle | Accuracy |
|------|--------|----------|
| 🥇 | LDA | 100% |
| 🥈 | SVM | 96.7% |
| 🥈 | Naive Bayes | 96.7% |

Régression Linéaire — R² = 0.45

---

## Fichiers

```
tp_partie1_modeles_supervises/
└── tp_partie1_modeles_supervises.ipynb
```
