# Plan de Présentation PowerPoint - Segmentation Client avec K-Means

## Structure de la présentation (environ 15-20 slides)

---

## SLIDE 1 : Page de titre
**Titre :** Segmentation Client avec K-Means  
**Sous-titre :** Analyse de comportement client pour un centre commercial  
**Auteur :** [Votre nom]  
**Date :** [Date]

**🎨 Couleurs suggérées :**
- Fond : Blanc ou dégradé bleu clair (#E8F4F8)
- Titre : Bleu foncé (#1E3A5F ou #2C5282)
- Sous-titre : Gris foncé (#4A5568)

**📸 Screenshot/Graphique :** Aucun (slide de titre)

---

## SLIDE 2 : Objectif du projet
**Titre :** Objectif  
**Contenu :**
- Réaliser une segmentation client à l'aide de l'algorithme K-Means
- Identifier des groupes de clients ayant des comportements similaires
- Analyser les caractéristiques socio-économiques et comportementales
- Fournir des insights actionnables pour le marketing

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Puces : Bleu moyen (#3182CE) ou Orange (#ED8936)

**📸 Screenshot/Graphique :** Aucun (slide texte avec icônes)

---

## SLIDE 3 : Plan de présentation
**Titre :** Structure de l'analyse  
**Contenu :**
1. Préparation des données
2. Analyse exploratoire
3. Application de K-Means
4. Interprétation des résultats

**🎨 Couleurs suggérées :**
- Fond : Blanc ou dégradé bleu très clair (#F0F9FF)
- Titre : Bleu foncé (#1E3A5F)
- Numéros : Bleu moyen (#3182CE) ou Orange (#ED8936)
- Texte : Gris foncé (#4A5568)

**📸 Screenshot/Graphique :** Aucun (slide texte avec numérotation)

---

# PARTIE 1 : PRÉPARATION DES DONNÉES

## SLIDE 4 : Présentation du dataset
**Titre :** Dataset - Mall Customers  
**Contenu :**
- **Source :** Kaggle
- **Taille :** 200 clients
- **Variables :**
  - CustomerID (identifiant unique)
  - Gender (Genre)
  - Age (Âge)
  - Annual Income (k$) (Revenu annuel en milliers de dollars)
  - Spending Score (1-100) (Score de dépense)

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Tableau : Alternance bleu clair (#EBF8FF) et blanc pour les lignes

**📸 Screenshot/Graphique :** 
- **Cellule 3 du notebook** : Capture d'écran de `df.head()` (les 5 premières lignes)
- Format : Tableau avec bordures, police lisible (Arial 10-12pt)

---

## SLIDE 5 : Qualité des données
**Titre :** Vérification de la qualité  
**Contenu :**
- ✅ **Aucune valeur manquante** détectée
- ✅ Dataset complet et prêt pour l'analyse
- **Statistiques descriptives :**
  - Âge moyen : 38.9 ans (18-70 ans)
  - Revenu moyen : 60.6 k$ (15-137 k$)
  - Score de dépense moyen : 50.2/100 (1-99)

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Cases à cocher : Vert (#48BB78)
- Tableau : En-tête bleu (#3182CE), lignes alternées gris clair (#F7FAFC)

**📸 Screenshot/Graphique :** 
- **Cellule 5 du notebook** : Capture de la sortie "Valeurs manquantes par colonne" (tous à 0)
- **Cellule 7 du notebook** : Capture du tableau `df.describe()` (statistiques descriptives)
- Format : Tableau formaté avec bordures claires

---

## SLIDE 6 : Distribution des variables
**Titre :** Distribution des variables numériques  
**Contenu :**
- Visualisation de la distribution de chaque variable
- Identification des patterns et outliers potentiels

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Histogramme Âge : Bleu acier (#4682B4)
- Histogramme Revenu : Corail (#FF7F50)
- Histogramme Dépense : Vert moyen (#3CB371)
- Barres Genre : Bleu ciel (#87CEEB) et Rose (#FFB6C1)

**📸 Screenshot/Graphique :** 
- **Cellule 7 du notebook** : Capture complète de la figure avec les 4 graphiques (grille 2x2)
- Format : Image PNG haute résolution (au moins 1920x1080px)
- Prendre la capture après `plt.show()` pour avoir le graphique final

---

## SLIDE 7 : Sélection des variables
**Titre :** Variables sélectionnées pour le clustering  
**Contenu :**
- **Variables retenues :**
  - Age
  - Annual Income (k$)
  - Spending Score (1-100)
- **Variables exclues :**
  - CustomerID (identifiant, non pertinent)
  - Gender (variable catégorielle, peut être intégrée plus tard)

**Justification :** Variables numériques pertinentes pour la segmentation

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Variables retenues : Fond vert clair (#C6F6D5) ou icône ✓ verte
- Variables exclues : Fond gris clair (#F7FAFC) ou icône ✗ grise

**📸 Screenshot/Graphique :** Aucun (slide texte avec liste)

---

## SLIDE 8 : Normalisation des données
**Titre :** Standardisation des variables  
**Contenu :**
- **Pourquoi normaliser ?**
  - K-Means utilise les distances euclidiennes
  - Les variables ont des échelles différentes
  - Le revenu (15-137 k$) dominerait l'âge (18-70) sans normalisation
- **Méthode :** StandardScaler (moyenne = 0, écart-type = 1)
- **Résultat :** Toutes les variables sur la même échelle

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Tableau "Avant" : Fond orange clair (#FED7AA)
- Tableau "Après" : Fond vert clair (#C6F6D5)
- Bordures : Gris (#CBD5E0)

**📸 Screenshot/Graphique :** 
- **Cellule 11 du notebook** : Capture de la sortie montrant :
  1. `features_scaled.head()` (5 premières lignes normalisées)
  2. `features_scaled.describe()` (moyennes ≈ 0, écarts-types ≈ 1)
- Format : Tableau côte à côte "Avant" vs "Après" normalisation

---

# PARTIE 2 : ANALYSE EXPLORATOIRE

## SLIDE 9 : Matrice de corrélation
**Titre :** Relations entre variables  
**Contenu :**
- Analyse des corrélations entre les variables
- **Observations :**
  - Corrélation faible entre les variables (-0.33 à 0.01)
  - Pas de multicolinéarité
  - Variables relativement indépendantes

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Heatmap : Palette "coolwarm" (bleu = corrélation négative, rouge = positive)
- Valeurs : Texte noir ou blanc selon le fond

**📸 Screenshot/Graphique :** 
- **Cellule 13 du notebook** : Capture complète de la heatmap de corrélation
- Format : Image PNG haute résolution
- S'assurer que les valeurs sont lisibles (fmt='.2f' dans le code)

---

## SLIDE 10 : Visualisation des relations (Pairplot)
**Titre :** Analyse multivariée  
**Contenu :**
- Visualisation de toutes les combinaisons de variables
- Identification visuelle de patterns et regroupements potentiels

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Points scatter : Bleu avec transparence (alpha=0.6)
- Histogrammes : Bleu (#3182CE) avec bordures noires

**📸 Screenshot/Graphique :** 
- **Cellule 14 du notebook** : Capture complète du pairplot (matrice 3x3)
- Format : Image PNG haute résolution (au moins 1920x1080px)
- S'assurer que tous les graphiques sont visibles et lisibles

---

## SLIDE 11 : Observations préliminaires
**Titre :** Hypothèses initiales  
**Contenu :**
- **Observation clé :** Le graphique "Revenu Annuel vs Score de Dépense" montre des regroupements naturels
- **Hypothèse :** 5 groupes potentiels identifiés visuellement
- **Conclusion :** k = 5 clusters semble approprié (à valider)

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Points Female : Rose (#FF69B4) ou Violet (#9F7AEA)
- Points Male : Bleu (#4299E1) ou Cyan (#38B2AC)
- Grille : Gris clair (#E2E8F0)

**📸 Screenshot/Graphique :** 
- **Cellule 15 du notebook** : Capture du 3ème scatter plot (Annual Income vs Spending Score)
- **OU** : Capture du graphique complet avec les 3 scatter plots, mais zoomer sur le 3ème
- Format : Image PNG haute résolution
- Ajouter des annotations/cercles pour montrer les 5 groupes potentiels

---

# PARTIE 3 : APPLICATION DE K-MEANS

## SLIDE 12 : Test de différentes valeurs de k
**Titre :** Détermination du nombre optimal de clusters  
**Contenu :**
- Test de k = 2 à k = 10
- Calcul de deux métriques pour chaque k :
  - **Inertie (WCSS)** : Mesure de compacité
  - **Score de silhouette** : Mesure de qualité (-1 à 1)

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Tableau : En-tête bleu (#3182CE)
- Ligne k=6 (optimal) : Fond vert clair (#C6F6D5) ou jaune clair (#FEFCBF)
- Autres lignes : Alternance blanc/gris très clair (#F7FAFC)

**📸 Screenshot/Graphique :** 
- **Cellule 18 du notebook** : Capture de la sortie complète avec tous les résultats
- Format : Tableau formaté avec mise en évidence de k=6
- Exemple de sortie :
  ```
  k=2: Inertie=389.39, Silhouette=0.335
  k=3: Inertie=295.21, Silhouette=0.358
  ...
  k=6: Inertie=133.87, Silhouette=0.428  ← OPTIMAL
  ```

---

## SLIDE 13 : Méthode du coude
**Titre :** Choix du k optimal  
**Contenu :**
- **Méthode du coude :** Visualisation de l'inertie
- **Score de silhouette :** Maximisation du score
- **Résultat :** k = 6 clusters optimal
  - Score de silhouette maximum : 0.428
  - Bon équilibre entre compacité et séparation

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Graphique Inertie : Ligne bleue (#3182CE), points bleus cerclés
- Graphique Silhouette : Ligne rouge (#E53E3E), points rouges cerclés
- Point k=6 : Mise en évidence avec cercle rouge ou étoile
- Grille : Gris clair (#E2E8F0)

**📸 Screenshot/Graphique :** 
- **Cellule 20 du notebook** : Capture complète de la figure avec les 2 graphiques côte à côte
- Format : Image PNG haute résolution
- S'assurer que :
  - Le "coude" est visible sur le graphique de gauche
  - Le maximum de silhouette (k=6) est marqué sur le graphique de droite

---

## SLIDE 14 : Analyse détaillée de la silhouette
**Titre :** Qualité du clustering  
**Contenu :**
- Analyse du score de silhouette pour chaque point
- **Interprétation :**
  - Score proche de 1 : Clusters bien séparés
  - Score proche de 0 : Clusters qui se chevauchent
  - Score négatif : Points mal assignés
- **Score moyen : 0.428** → Qualité acceptable

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Barres : Palette spectrale (nipy_spectral) - chaque cluster a une couleur différente
- Ligne moyenne : Rouge (#E53E3E) en pointillés
- Axe : Gris (#718096)

**📸 Screenshot/Graphique :** 
- **Cellule 22 du notebook** : Capture complète du graphique de silhouette
- Format : Image PNG haute résolution
- Le graphique montre des barres horizontales colorées pour chaque cluster
- La ligne rouge pointillée indique le score moyen (0.428)

---

## SLIDE 15 : Modèle final
**Titre :** Modèle K-Means final  
**Contenu :**
- **k optimal :** 6 clusters
- **Distribution des clusters :**
  - Cluster 0 : 45 clients (22.5%)
  - Cluster 1 : 39 clients (19.5%)
  - Cluster 2 : 33 clients (16.5%)
  - Cluster 3 : 39 clients (19.5%)
  - Cluster 4 : 23 clients (11.5%)
  - Cluster 5 : 21 clients (10.5%)
- **Équilibre :** Clusters de tailles relativement équilibrées

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Barres : Palette viridis (vert-jaune) ou palette personnalisée avec 6 couleurs distinctes
- Bordures : Noir ou gris foncé
- Grille : Gris clair (#E2E8F0)

**📸 Screenshot/Graphique :** 
- **Cellule 24 du notebook** : Capture de la sortie "Nombre de points par cluster"
- **OU** : Créer un diagramme en barres avec les valeurs
- Format : Graphique en barres verticales avec labels sur chaque barre

---

# PARTIE 4 : INTERPRÉTATION

## SLIDE 16 : Statistiques par cluster
**Titre :** Caractéristiques moyennes par segment  
**Contenu :**
- Analyse des moyennes pour chaque variable par cluster
- Identification des profils distincts

**Tableau :** Moyennes par cluster
| Cluster | Taille | Âge moyen | Revenu (k$) | Score dépense |
|---------|--------|-----------|-------------|---------------|
| 0 | 45 | 56.3 | 54.3 | 49.1 |
| 1 | 39 | 26.8 | 57.1 | 48.1 |
| 2 | 33 | 41.9 | 88.9 | 16.9 |
| 3 | 39 | 32.7 | 86.5 | 82.1 |
| 4 | 23 | 25.0 | 25.3 | 77.6 |
| 5 | 21 | 45.5 | 26.3 | 19.4 |

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- En-tête tableau : Bleu moyen (#3182CE) avec texte blanc
- Lignes : Alternance blanc/gris très clair (#F7FAFC)
- Valeurs importantes : Mise en évidence avec fond coloré (ex: Cluster 3 en vert clair)

**📸 Screenshot/Graphique :** 
- **Cellule 26 du notebook** : Capture du tableau "Moyennes par cluster"
- Format : Tableau formaté avec bordures, police lisible

---

## SLIDE 17 : Profils des segments
**Titre :** Description des 6 segments  
**Contenu :**

**Cluster 0 - Seniors économes (22.5%)**
- Âge : 56.3 ans | Revenu : 54.3 k$ | Dépense : 49.1/100

**Cluster 1 - Profil mixte (19.5%)**
- Âge : 26.8 ans | Revenu : 57.1 k$ | Dépense : 48.1/100

**Cluster 2 - Clients prudents à haut revenu (16.5%)**
- Âge : 41.9 ans | Revenu : 88.9 k$ | Dépense : 16.9/100

**Cluster 3 - Jeunes dépensiers (19.5%)**
- Âge : 32.7 ans | Revenu : 86.5 k$ | Dépense : 82.1/100

**Cluster 4 - Jeunes dépensiers (11.5%)**
- Âge : 25.0 ans | Revenu : 25.3 k$ | Dépense : 77.6/100

**Cluster 5 - Clients économes (10.5%)**
- Âge : 45.5 ans | Revenu : 26.3 k$ | Dépense : 19.4/100

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Chaque cluster : Fond coloré léger correspondant à sa couleur dans les graphiques
- Cluster 0 : Violet clair (#E9D5FF)
- Cluster 1 : Bleu clair (#DBEAFE)
- Cluster 2 : Cyan clair (#CCFBF1)
- Cluster 3 : Vert clair (#D1FAE5)
- Cluster 4 : Jaune clair (#FEF3C7)
- Cluster 5 : Orange clair (#FED7AA)

**📸 Screenshot/Graphique :** 
- **Cellule 28 du notebook** : Capture de la sortie "PROFILS DES CLUSTERS"
- Format : Texte formaté avec mise en évidence par cluster

---

## SLIDE 18 : Visualisation des profils
**Titre :** Comparaison des segments  
**Contenu :**
- Comparaison visuelle des caractéristiques moyennes
- Identification des différences clés entre segments

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Graphique Âge : Barres bleu acier (#4682B4)
- Graphique Revenu : Barres corail (#FF7F50)
- Graphique Dépense : Barres vert moyen (#3CB371)
- Bordures : Noir (#000000)
- Grille : Gris clair (#E2E8F0)

**📸 Screenshot/Graphique :** 
- **Cellule 30 du notebook** : Capture complète de la figure avec les 3 graphiques en barres côte à côte
- Format : Image PNG haute résolution
- Les 3 graphiques montrent les moyennes par cluster pour chaque variable

---

## SLIDE 19 : Visualisation 2D des clusters
**Titre :** Représentation spatiale des clusters  
**Contenu :**
- Visualisation des clusters dans l'espace 2D
- Identification des regroupements géographiques
- Position des centroïdes (centres des clusters)

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Points par cluster : Palette viridis (6 couleurs distinctes : violet, bleu, vert, jaune, orange)
- Centroïdes : Rouge vif (#DC2626) avec marqueur X, bordure noire
- Grille : Gris clair (#E2E8F0)
- Légende : Visible avec noms des clusters

**📸 Screenshot/Graphique :** 
- **Cellule 32 du notebook** : Capture complète de la figure avec les 3 scatter plots côte à côte
- Format : Image PNG haute résolution
- S'assurer que :
  - Les centroïdes (X rouges) sont bien visibles
  - Les clusters sont bien séparés visuellement
  - La légende/cluster est visible

---

## SLIDE 20 : Visualisation 3D
**Titre :** Vue d'ensemble en 3 dimensions  
**Contenu :**
- Visualisation complète des 3 variables simultanément
- Appréciation de la séparation des clusters dans l'espace

**🎨 Couleurs suggérées :**
- Fond : Blanc ou gris très clair (#F7FAFC)
- Titre : Bleu foncé (#1E3A5F)
- Points par cluster : Palette viridis (6 couleurs distinctes)
- Centroïdes : Rouge vif (#DC2626) avec marqueur X, bordure noire, taille plus grande
- Axes : Gris foncé (#4A5568)
- Grille : Gris clair (#E2E8F0)

**📸 Screenshot/Graphique :** 
- **Cellule 34 du notebook** : Capture de la visualisation 3D
- Format : Image PNG haute résolution
- **Important :** Prendre plusieurs angles de vue (rotation du graphique 3D) :
  1. Vue de face (angle principal)
  2. Vue de côté (si possible)
- S'assurer que les clusters sont visibles et séparés
- Les centroïdes doivent être bien marqués en rouge

---

## SLIDE 21 : Insights clés
**Titre :** Principales découvertes  
**Contenu :**
- **6 segments distincts** identifiés avec des profils clairs
- **Segment le plus prometteur :** Cluster 3 (Jeunes dépensiers à haut revenu)
  - 39 clients, revenu élevé (86.5 k$), dépense élevée (82.1/100)
- **Segment à développer :** Cluster 2 (Clients prudents à haut revenu)
  - 33 clients, revenu élevé (88.9 k$) mais dépense faible (16.9/100)
- **Segment jeune :** Cluster 4 (Jeunes dépensiers à faible revenu)
  - 23 clients, dépense élevée malgré revenu modéré

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- "Prometteur" : Fond vert clair (#D1FAE5) avec icône ✓
- "À développer" : Fond orange clair (#FED7AA) avec icône ⚠
- "Jeune" : Fond bleu clair (#DBEAFE) avec icône 👥

**📸 Screenshot/Graphique :** Aucun (slide texte avec icônes)

---

## SLIDE 22 : Recommandations business
**Titre :** Applications pratiques  
**Contenu :**
- **Marketing personnalisé :** Campagnes ciblées par segment
- **Stratégie produit :** Offres adaptées aux profils
- **Fidélisation :** Programmes différenciés
- **Optimisation :** Allocation des ressources marketing

**Exemples :**
- Cluster 3 : Programmes premium, événements VIP
- Cluster 2 : Promotions pour inciter à dépenser
- Cluster 4 : Offres accessibles, promotions jeunes

**🎨 Couleurs suggérées :**
- Fond : Blanc
- Titre : Bleu foncé (#1E3A5F)
- Catégories principales : Icônes colorées (📊 Marketing, 💼 Stratégie, 💎 Fidélisation, 📈 Optimisation)
- Exemples : Fond gris très clair (#F7FAFC) avec bordures colorées par cluster

**📸 Screenshot/Graphique :** Aucun (slide texte avec icônes)

---

## SLIDE 23 : Conclusion
**Titre :** Synthèse et résultats  
**Contenu :**
- ✅ **200 clients** analysés et segmentés
- ✅ **6 clusters** identifiés avec qualité acceptable (silhouette = 0.428)
- ✅ **Profils distincts** permettant une stratégie marketing ciblée
- ✅ **Insights actionnables** pour améliorer la performance commerciale

**Valeur ajoutée :**
- Compréhension approfondie de la base client
- Segmentation objective basée sur les données
- Base solide pour des décisions stratégiques

**🎨 Couleurs suggérées :**
- Fond : Blanc ou dégradé bleu très clair (#F0F9FF)
- Titre : Bleu foncé (#1E3A5F)
- Cases à cocher : Vert (#48BB78)
- Points principaux : Fond vert très clair (#D1FAE5)
- "Valeur ajoutée" : Fond bleu très clair (#DBEAFE)

**📸 Screenshot/Graphique :** Aucun (slide texte avec icônes)

---

## SLIDE 24 : Questions / Merci
**Titre :** Questions ?  
**Contenu :**
- Merci pour votre attention
- Questions et discussions

**🎨 Couleurs suggérées :**
- Fond : Dégradé bleu clair (#E8F4F8 vers blanc) ou image de fond discrète
- Titre : Bleu foncé (#1E3A5F) ou Orange (#ED8936)
- Texte : Gris foncé (#4A5568)
- Icône "?" : Grande, centrée, couleur bleue ou orange

**📸 Screenshot/Graphique :** Aucun (slide de fin avec design élégant)

---

## NOTES POUR LA PRÉSENTATION

### 🎨 PALETTE DE COULEURS PRINCIPALE

**Couleurs principales :**
- **Bleu foncé (titres)** : #1E3A5F ou #2C5282
- **Bleu moyen (accent)** : #3182CE ou #4299E1
- **Bleu clair (fond)** : #EBF8FF ou #E8F4F8
- **Rouge (points importants)** : #E53E3E ou #DC2626
- **Vert (succès/positif)** : #48BB78 ou #3CB371
- **Orange (attention)** : #ED8936 ou #FF7F50
- **Gris clair (grilles)** : #E2E8F0 ou #F7FAFC
- **Gris foncé (texte)** : #4A5568 ou #718096

**Palette pour les clusters (6 couleurs distinctes) :**
- Cluster 0 : Violet (#9F7AEA)
- Cluster 1 : Bleu (#4299E1)
- Cluster 2 : Cyan (#38B2AC)
- Cluster 3 : Vert (#48BB78)
- Cluster 4 : Jaune (#ECC94B)
- Cluster 5 : Orange (#ED8936)

### 📸 RÉCAPITULATIF DES SCREENSHOTS À PRENDRE

| Slide | Cellule Notebook | Screenshot à capturer | Format |
|-------|------------------|----------------------|--------|
| 4 | Cellule 3 | `df.head()` - 5 premières lignes | Tableau |
| 5 | Cellule 5 | Valeurs manquantes (tous à 0) | Texte/Tableau |
| 5 | Cellule 7 | `df.describe()` - Statistiques | Tableau |
| 6 | Cellule 7 | Figure complète 2x2 (4 graphiques) | PNG 1920x1080 |
| 8 | Cellule 11 | `features_scaled.head()` + `describe()` | Tableau |
| 9 | Cellule 13 | Heatmap de corrélation | PNG haute résolution |
| 10 | Cellule 14 | Pairplot complet (3x3) | PNG 1920x1080 |
| 11 | Cellule 15 | Scatter plot Revenu vs Dépense | PNG haute résolution |
| 12 | Cellule 18 | Sortie complète des tests k=2 à 10 | Texte/Tableau |
| 13 | Cellule 20 | 2 graphiques côte à côte (Coude + Silhouette) | PNG haute résolution |
| 14 | Cellule 22 | Graphique de silhouette détaillé | PNG haute résolution |
| 15 | Cellule 24 | Distribution des clusters | Tableau ou Graphique |
| 16 | Cellule 26 | Tableau statistiques par cluster | Tableau |
| 18 | Cellule 30 | 3 graphiques en barres côte à côte | PNG haute résolution |
| 19 | Cellule 32 | 3 scatter plots 2D côte à côte | PNG haute résolution |
| 20 | Cellule 34 | Visualisation 3D (plusieurs angles) | PNG haute résolution |

### 📋 CHECKLIST AVANT LA PRÉSENTATION

**Graphiques à exporter :**
- [ ] Slide 6 : Distribution des variables (4 graphiques)
- [ ] Slide 9 : Matrice de corrélation
- [ ] Slide 10 : Pairplot complet
- [ ] Slide 11 : Scatter plot Revenu vs Dépense
- [ ] Slide 13 : Méthode du coude + Silhouette
- [ ] Slide 14 : Graphique de silhouette détaillé
- [ ] Slide 18 : Graphiques en barres des profils
- [ ] Slide 19 : Visualisations 2D des clusters
- [ ] Slide 20 : Visualisation 3D (plusieurs angles)

**Tableaux à formater :**
- [ ] Slide 4 : Aperçu dataset
- [ ] Slide 5 : Statistiques descriptives
- [ ] Slide 8 : Avant/Après normalisation
- [ ] Slide 12 : Résultats tests k=2 à 10
- [ ] Slide 15 : Distribution clusters
- [ ] Slide 16 : Statistiques par cluster

### 💡 Conseils de design :
- Utiliser la palette de couleurs cohérente définie ci-dessus
- Limiter le texte par slide (maximum 5-7 points)
- Utiliser des graphiques clairs et lisibles (police minimum 12pt)
- Ajouter des animations discrètes pour les transitions
- Utiliser des icônes pour rendre les slides plus visuelles
- S'assurer que tous les graphiques sont en haute résolution (minimum 1920x1080px)
- Tester la lisibilité sur un écran de projection

### ⏱️ Durée estimée : 15-20 minutes
- Introduction (Slides 1-3) : 2 min
- Partie 1 - Préparation (Slides 4-8) : 3-4 min
- Partie 2 - Analyse exploratoire (Slides 9-11) : 3-4 min
- Partie 3 - K-Means (Slides 12-15) : 4-5 min
- Partie 4 - Interprétation (Slides 16-23) : 4-5 min
- Conclusion (Slides 23-24) : 1-2 min

