# Analyse Spectroscopique Raman & Déconvolution Numérique

## 📝 Description
Ce projet consiste à simuler et analyser des spectres Raman en conditions expérimentales réalistes. L'objectif est de développer une méthode de traitement du signal permettant d'extraire les paramètres physiques des pics (position, largeur, amplitude) même en présence d'un bruit de fond significatif.

## 🔬 Méthodes
* **Modélisation physique :** Utilisation de fonctions lorentziennes pour décrire les modes de vibration.
* **Simulation réaliste :** Injection de bruit gaussien pour tester la robustesse de l'algorithme.
* **Optimisation :** Régression non linéaire via l'algorithme de Levenberg-Marquardt (`scipy.optimize.curve_fit`).
* **Validation statistique :** Analyse rigoureuse des résidus pour confirmer la validité du modèle.

## 🛠 Outils
* **Langage :** Python
* **Bibliothèques :** NumPy (calcul), SciPy (optimisation), Matplotlib (visualisation)

## 📊 Résultats
* Extraction précise des paramètres Raman avec une faible incertitude.
* Robustesse démontrée face au bruit expérimental.
* Capacité de déconvolution de pics superposés ($A_g$ et $B_{1g}$).

---

### Auteur
**Babacar NDIAYE** *Master 2 Physique Appliquée – Nanophysique & Optique Avancée* *Université du Mans*
