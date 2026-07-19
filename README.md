# ⚡ Bilan Énergétique

Application Python permettant de suivre la consommation énergétique d'un établissement : l'utilisateur sélectionne son type de lieu, ajuste la liste des appareils utilisés et leur durée d'utilisation, puis obtient un bilan détaillé par appareil ainsi qu'un bilan global (énergie et coût).

## Fonctionnalités

- Sélection du type d'établissement parmi 8 catégories : Maison, Appartement, Bureau, Pharmacie, Bar, Restaurant, Café, Boutique
- Liste pré-remplie des appareils typiques de chaque établissement (avec puissance moyenne en W)
- Tableau entièrement modifiable : activer/désactiver un appareil, changer sa puissance ou sa durée d'utilisation
- Ajout d'appareils personnalisés non présents dans la liste par défaut
- Calcul automatique :
  - Énergie consommée par appareil (kWh)
  - Coût par appareil (basé sur un tarif au kWh modifiable)
  - Bilan global (énergie totale + coût total)
  - Graphique de répartition de la consommation par appareil

## Aperçu technique

| Élément | Détail |
|---|---|
| Langage | Python 3 |
| Framework | [Streamlit](https://streamlit.io) |
| Dépendances | `streamlit`, `pandas` |

## Installation

```bash
git clone https://github.com/<ton-user>/<ton-repo>.git
cd <ton-repo>
pip install -r requirements.txt
```

## Utilisation en local

```bash
streamlit run energy_app.py
```

L'application s'ouvre automatiquement dans le navigateur à l'adresse `http://localhost:8501`.

## Déploiement gratuit (Streamlit Community Cloud)

1. Pousser ce repo sur GitHub (avec `energy_app.py` et `requirements.txt`)
2. Aller sur [share.streamlit.io](https://share.streamlit.io)
3. Se connecter avec GitHub et sélectionner le repo
4. Indiquer `energy_app.py` comme fichier principal
5. Déployer — l'app est en ligne en HTTPS, gratuitement

## Structure du projet

```
.
├── energy_app.py       # Application Streamlit (page de sélection + calcul du bilan)
├── requirements.txt    # Dépendances Python
└── README.md
```

## Prochaines étapes (roadmap)

- [ ] Page d'historique des bilans passés (sauvegarde)
- [ ] Tarification par tranches / distinction jour-nuit
- [ ] Export du bilan en PDF ou CSV
- [ ] Suivi multi-établissements

## Licence

Projet personnel — usage libre.
