TP - K-Means : Segmentation Client

Structure du projet


K-means/
├── data/                    # Dossier pour les données
│   └── Mall_Customers.csv   # Dataset à télécharger depuis Kaggle
├── notebooks/               # Notebooks Jupyter
│   └── kmeans_analysis.ipynb
├── src/                     # Scripts Python
│   ├── data_preparation.py
│   ├── kmeans_clustering.py
│   └── visualization.py
├── reports/                 # Rapports et visualisations
│   └── rapport.pdf
├── requirements.txt        
├── .gitignore             
└── README.md              

Description détaillée des fichiers


`requirements.txt`
- Liste des dépendances Python nécessaires au projet
- Contient les versions spécifiques des bibliothèques (numpy, pandas, matplotlib, seaborn, scikit-learn, jupyter, scipy, plotly)
- Utilisé pour installer toutes les dépendances avec `pip install -r requirements.txt`

`execute_notebook.py`
- Script pour exécuter le notebook Jupyter de manière programmatique
- Utilise `jupyter nbconvert` pour exécuter toutes les cellules du notebook
- Alternative si l'exécution directe échoue, tente d'exécuter le code Python directement

`execute_notebook_with_outputs.py`**
- Version avancée du script d'exécution qui capture toutes les sorties
- Capture les graphiques matplotlib et les convertit en images base64
- Sauvegarde le notebook avec toutes les sorties (texte, graphiques, erreurs) intégrées
- Utile pour générer un notebook complet avec tous les résultats visibles

`run_notebook.py`
- Script simplifié pour exécuter le notebook
- Lit le notebook JSON et exécute toutes les cellules de code séquentiellement
- Affiche un résumé du nombre de cellules exécutées et des erreurs éventuelles
- Ne sauvegarde pas les sorties dans le notebook (exécution en mémoire uniquement)

Dossier `data/`

`Mall_Customers.csv`
- Dataset principal contenant les données clients du centre commercial
- Colonnes : CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100)
- À télécharger depuis Kaggle (lien dans `data/README.md`)

`Mall_Customers_Clustered.csv`
- Version du dataset avec la colonne "Cluster" ajoutée après l'application de K-Means
- Contient les labels de cluster assignés à chaque client

`data/README.md`
- Contient le lien Kaggle pour télécharger les données

Dossier `notebooks/`

`kmeans_analysis.ipynb`**
- Notebook Jupyter principal contenant toute l'analyse
- Réalise les 5 parties du TP : préparation des données, analyse exploratoire, application K-Means, interprétation, et 1 extension
- Utilise les fonctions définies dans les modules `src/` pour organiser le code
- Contient les visualisations, les résultats et les interprétations

Dossier `src/`

`src/__init__.py`
- Fichier Python qui transforme le dossier `src/` en module Python
- Permet d'importer les fonctions depuis les autres scripts avec `from src import ...`

`src/data_preparation.py`
- Module contenant les fonctions de préparation des données
- Fonctions principales :
  - `load_data()` : charge le dataset depuis un fichier CSV
  - `check_missing_values()` : vérifie les valeurs manquantes
  - `select_features()` : sélectionne les variables pertinentes (Age, Annual Income, Spending Score)
  - `normalize_features()` : standardise les variables avec StandardScaler

`src/kmeans_clustering.py`
- Module contenant les fonctions pour l'application de K-Means
- Fonctions principales :
  - `calculate_inertia()` : calcule l'inertie (WCSS) pour différents k (méthode du coude)
  - `calculate_silhouette_scores()` : calcule les scores de silhouette pour valider le choix de k
  - `plot_elbow_method()` : visualise la courbe du coude
  - `plot_silhouette_scores()` : visualise les scores de silhouette
  - `fit_kmeans()` : entraîne le modèle K-Means final et retourne les labels

`src/visualization.py`
- Module contenant toutes les fonctions de visualisation
- Fonctions principales :
  - `plot_distributions()` : histogrammes de distribution des variables
  - `plot_correlation_heatmap()` : matrice de corrélation
  - `plot_pairplot()` : graphiques de paires de variables
  - `plot_clusters_2d()` : visualisation 2D des clusters
  - `plot_clusters_3d()` : visualisation 3D des clusters
  - `plot_cluster_profiles()` : profils moyens de chaque cluster (graphiques en barres)

Dossier `reports/`

**`reports/`**
- Dossier destiné à contenir les rapports générés (PDF, images, etc.)
- Peut contenir le rapport final du TP au format PDF

