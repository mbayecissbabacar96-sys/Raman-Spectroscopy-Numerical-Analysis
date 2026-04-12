# 🔬 Analyse Spectroscopique Raman & Déconvolution Numérique

Ce projet porte sur la simulation et le traitement avancé de signaux spectroscopiques pour l'extraction de paramètres physiques en milieux bruités.

---

## 🔗 Accès aux documents
* 📄 **Rapport complet :** [Mini_Projet_personnel.pdf](./Mini__Projet_personnel.pdf)
* 💻 **Code Source (Python) :** [Script Python projet.py](./Script%20Python%20projet.py)

---

## 📝 Description
L'objectif est de développer une méthodologie robuste de traitement du signal permettant d'extraire avec précision les caractéristiques des pics Raman (position, largeur à mi-hauteur, amplitude) au sein de spectres complexes intégrant un bruit de fond significatif.

## 🔬 Méthodes & Approches
* **Modélisation Physique :** Utilisation de fonctions lorentziennes pour la description théorique des modes de vibration.
* **Simulation Réaliste :** Injection de bruit gaussien pour évaluer la robustesse et la limite de détection de l'algorithme.
* **Optimisation Numérique :** Mise en œuvre d'une régression non linéaire via l'algorithme de **Levenberg-Marquardt** (`scipy.optimize.curve_fit`).
* **Validation Statistique :** Analyse rigoureuse des résidus pour confirmer la convergence et la validité du modèle ajusté.

## 🛠 Outils & Technologies
* **Langage :** Python
* **Bibliothèques Scientifiques :** * **NumPy :** Gestion des tableaux multidimensionnels et calculs matriciels.
  * **SciPy :** Optimisation et intégration numérique.
  * **Matplotlib :** Visualisation des données et des ajustements de courbes.

## 📊 Résultats Clés
* **Précision :** Extraction des paramètres Raman avec une incertitude résiduelle minimale.
* **Fiabilité :** Robustesse de la méthode démontrée face à un rapport signal/bruit dégradé.
* **Analyse de Structure :** Capacité confirmée de déconvolution de pics superposés (ex: modes $A_{g}$ et $B_{1g}$).

---
**Babacar NDIAYE** | *Master 2 Physique Appliquée – Nanophysique & Optique Avancée* | *Université du Mans*
