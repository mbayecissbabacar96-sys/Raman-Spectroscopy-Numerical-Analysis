# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:18:39 2026

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ============================================================
# 1. MODÈLE PHYSIQUE
# ============================================================

def lorentz(x, x0, gamma, A):
    return A * gamma**2 / ((x - x0)**2 + gamma**2)

def multi_lorentz(x, *params):
    y = np.zeros_like(x)
    for i in range(0, len(params), 3):
        y += lorentz(x, params[i], params[i+1], params[i+2])
    return y

# ============================================================
# 2. GÉNÉRATION DES DONNÉES
# ============================================================

x = np.linspace(100, 800, 1000)
real_params = [300, 15, 100, 500, 25, 80] 

y_clean = multi_lorentz(x, *real_params)

np.random.seed(42) 
noise = np.random.normal(0, 5, len(x))
y_noisy = y_clean + noise

# ============================================================
# 3. CALCUL DES INCERTITUDES (FIT)
# ============================================================

p0 = [290, 10, 90, 510, 20, 70]
popt, pcov = curve_fit(multi_lorentz, x, y_noisy, p0=p0)
perr = np.sqrt(np.diag(pcov))

print("\n" + "="*45)
print("     RESULTATS AVEC CALCUL INCERTITUDE      ")
print("="*45)
for i in range(0, len(popt), 3):
    n = i//3 + 1
    print(f"Pic {n} :")
    print(f"  -> Position  = {popt[i]:.3f} +/- {perr[i]:.3f} cm-1")
    print(f"  -> Largeur   = {popt[i+1]:.3f} +/- {perr[i+1]:.3f} cm-1")
    print(f"  -> Amplitude = {popt[i+2]:.3f} +/- {perr[i+2]:.3f} u.a.")
    print("-" * 45)

# ============================================================
# 4. GÉNÉRATION DES 5 FIGURES (S'AFFICHENT TOUTES)
# ============================================================

plt.rcParams.update({'font.size': 10})

# --- FIGURE 1 ---
plt.figure(1, figsize=(8, 5))
plt.plot(x, y_clean, color='tab:blue', lw=2)
plt.title("Figure 1 : Spectre Raman theorique")
plt.xlabel("Nombre d'ondes (cm-1)")
plt.ylabel("Intensite (u.a.)")
plt.grid(alpha=0.3)
plt.savefig("Figure_1.png", dpi=300)

# --- FIGURE 2 ---
plt.figure(2, figsize=(8, 5))
plt.plot(x, y_noisy, color='black', lw=0.8)
plt.title("Figure 2 : Signal avec bruit de mesure")
plt.xlabel("Nombre d'ondes (cm-1)")
plt.ylabel("Intensite (u.a.)")
plt.savefig("Figure_2.png", dpi=300)

# --- FIGURE 3 ---
plt.figure(3, figsize=(8, 5))
plt.plot(x, y_clean, 'r--', label="Ideal")
plt.plot(x, y_noisy, 'k-', alpha=0.3, label="Bruite")
plt.legend()
plt.title("Figure 3 : Comparaison Signal/Bruit")
plt.savefig("Figure_3.png", dpi=300)

# --- FIGURE 4 ---
plt.figure(4, figsize=(8, 5))
plt.scatter(x[::10], y_noisy[::10], s=10, color='gray', label="Mesures")
plt.plot(x, multi_lorentz(x, *popt), 'r-', lw=2, label="Fit")
plt.title("Figure 4 : Ajustement des parametres")
plt.savefig("Figure_4.png", dpi=300)

# --- FIGURE 5 (COMPOSITE) ---
fig5, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, 
                                 gridspec_kw={'height_ratios': [3, 1]})
plt.figure(5)

ax1.scatter(x[::5], y_noisy[::5], s=12, color='gray', alpha=0.5, label="Donnees")
ax1.plot(x, multi_lorentz(x, *popt), color='red', lw=2, label="Fit Global")

colors = ['skyblue', 'orange']
for i in range(0, len(popt), 3):
    ax1.fill_between(x, lorentz(x, *popt[i:i+3]), alpha=0.4, 
                    color=colors[i//3], label=f"Mode Raman {i//3 + 1}")
ax1.set_ylabel("Intensite (u.a.)")
ax1.set_title("Figure 5 : Deconvolution et Analyse des Residus")
ax1.legend(loc='upper right')

residuals = y_noisy - multi_lorentz(x, *popt)
ax2.plot(x, residuals, color='purple', lw=0.8) 
ax2.axhline(0, color='black', lw=1, ls='--')
ax2.set_ylabel("Residus")
ax2.set_xlabel("Nombre d'ondes (cm-1)")

plt.tight_layout()
plt.subplots_adjust(hspace=0.05)
plt.savefig("Figure_5.png", dpi=300)

# Affiche tout à la fin
plt.show()

# print("\nSucces : Les 5 fenetres doivent etre ouvertes et les fichiers enregistres.")