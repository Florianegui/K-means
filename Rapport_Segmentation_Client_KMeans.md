Rapport d'Analyse : Segmentation Client par K-Means

Projet : Segmentation de la clientèle d'un centre commercial  
Méthode : Clustering K-Means  
Date : 27/11/2025  
Auteur : GUILLOU Floriane, JARI Jenna, KARABAJAKIAN Fred



Objectif du tp

Réaliser une segmentation client à l'aide de l'algorithme K-Means pour identifier des groupes de clients ayant des comportements similaires à partir de leurs caractéristiques socio-économiques et comportementales.

Résultats principaux :

- Dataset analysé : 200 clients
- Nombre optimal de clusters : 6 segments identifiés
- Qualité du clustering : Score de silhouette de 0.428 (qualité acceptable)
- Segments identifiés :
  - Cluster 0 : Seniors économes (22.5% - 45 clients)
  - Cluster 1 : Profil mixte (19.5% - 39 clients)
  - Cluster 2 : Clients prudents à haut revenu (16.5% - 33 clients)
  - Cluster 3 : Jeunes dépensiers à haut revenu (19.5% - 39 clients)
  - Cluster 4 : Jeunes dépensiers à faible revenu (11.5% - 23 clients)
  - Cluster 5 : Clients économes (10.5% - 21 clients)

Insights clés
- Segment le plus prometteur : Cluster 3 (Jeunes dépensiers à haut revenu) avec un revenu élevé (86.5 k$) et un score de dépense élevé (82.1/100)
- Segment à développer : Cluster 2 (Clients prudents à haut revenu) avec un revenu élevé (88.9 k$) mais un score de dépense faible (16.9/100), indiquant un potentiel inexploité
- Segments jeunes : Clusters 1 et 4 représentent 31% de la clientèle avec des profils de dépense variés


1. Introduction

1.1 Contexte

La segmentation client est un enjeu majeur pour les entreprises souhaitant personnaliser leurs stratégies marketing et optimiser leurs campagnes. L'analyse de la clientèle d'un centre commercial permet d'identifier des groupes homogènes de clients partageant des caractéristiques similaires en termes d'âge, de revenu et de comportement d'achat.

1.2 Objectifs

- Identifier des segments de clients distincts et homogènes
- Comprendre les caractéristiques de chaque segment
- Fournir des recommandations stratégiques pour chaque segment
- Évaluer la qualité de la segmentation réalisée

2.3 Données

Le dataset utilisé provient de Kaggle et contient les informations de 200 clients d'un centre commercial :
- CustomerID : Identifiant unique du client
- Gender : Genre (Male/Female)
- Age : Âge en années
- Annual Income (k$) : Revenu annuel en milliers de dollars
- Spending Score (1-100) : Score de dépense sur une échelle de 1 à 100


2. Méthodologie

2.1 Algorithme K-Means

K-Means est un algorithme de clustering non supervisé qui partitionne les données en k clusters en minimisant la somme des carrés des distances intra-clusters (inertie). L'algorithme :

1. Initialise k centroïdes aléatoirement
2. Assigne chaque point au centroïde le plus proche
3. Recalcule les centroïdes comme centres de gravité des points assignés
4. Répète les étapes 2 et 3 jusqu'à convergence

2.2 Métriques d'évaluation
- Inertie (WCSS) : Mesure de compacité des clusters (plus faible = mieux)
- Score de silhouette : Mesure de qualité du clustering (-1 à 1)
  - Proche de 1 : Clusters bien séparés et compacts
  - Proche de 0 : Clusters qui se chevauchent
  - Négatif : Points mal assignés

2.3 Outils utilisés

- Python 3.x
- Bibliothèques principales :
  - pandas : Manipulation de données
  - numpy : Calculs numériques
  - scikit-learn : K-Means, StandardScaler, métriques
  - matplotlib & seaborn : Visualisations


3. Préparation des données

3.1 Chargement et exploration

Le dataset contient 200 clients avec 5 variables. Aucune valeur manquante n'a été détectée, ce qui garantit la qualité des données pour l'analyse.

Statistiques descriptives :
- Âge : Moyenne de 38.9 ans (écart-type : 13.97), plage de 18 à 70 ans
- Revenu annuel : Moyenne de 60.6 k$ (écart-type : 26.26), plage de 15 à 137 k$
- Score de dépense : Moyenne de 50.2/100 (écart-type : 25.82), plage de 1 à 99

3.2 Sélection des variables

Pour le clustering, seules les variables numériques pertinentes ont été retenues :
- Variables sélectionnées :
  - Age
  - Annual Income (k$)
  - Spending Score (1-100)
- Variables exclues :
  - CustomerID : Identifiant unique, non pertinent pour le clustering
  - Gender : Variable catégorielle (peut être intégrée dans l'interprétation)

3.3 Normalisation

Les variables ont été normalisées à l'aide de StandardScaler pour mettre toutes les variables sur la même échelle (moyenne = 0, écart-type = 1). Cette étape est cruciale car :
- K-Means utilise les distances euclidiennes
- Sans normalisation, le revenu (15-137 k$) dominerait l'âge (18-70) et le score de dépense (1-100)
- La normalisation garantit que toutes les variables ont le même poids dans le clustering

Vérification : Après normalisation, les moyennes sont proches de 0 et les écarts-types proches de 1, confirmant la réussite de la transformation.

4. Analyse exploratoire

4.1 Distribution des variables

L'analyse des distributions révèle :
-   Âge :   Distribution relativement équilibrée avec une légère concentration autour de 30-40 ans
-   Revenu annuel :   Distribution assez uniforme avec quelques pics autour de 50-80 k$
-   Score de dépense :   Distribution bimodale suggérant deux groupes de comportement
-   Genre :   Répartition équilibrée (56% Female, 44% Male)

4.2 Analyse des corrélations

La matrice de corrélation montre des corrélations faibles entre les variables :
-   Age vs Revenu :   -0.012 (quasi-nulle)
-   Age vs Score de dépense :   -0.327 (corrélation négative modérée)
-   Revenu vs Score de dépense :   0.010 (quasi-nulle)

Ces faibles corrélations indiquent que les variables sont relativement indépendantes, ce qui est favorable pour le clustering.

4.3 Visualisation des relations
Le pairplot et les scatter plots révèlent des patterns intéressants :
- Le graphique "Revenu Annuel vs Score de Dépense" montre des regroupements naturels
-   Hypothèse initiale :   5 groupes potentiels identifiés visuellement
- Cette observation préliminaire guide le choix de tester k = 2 à 10


5. Application de K-Means

5.1 Détermination du nombre optimal de clusters

Test de différentes valeurs de k
Des tests ont été effectués pour k = 2 à k = 10. Les résultats sont présentés dans le tableau ci-dessous :

k  Inertie (WCSS) Score de silhouette 

2  389.39         0.335               
3  295.21         0.358               
4  205.23         0.404               
5  168.25         0.417               
6  133.87         0.428   ⭐ 
7  117.01         0.417               
8  103.87         0.408               
9  93.09          0.418               
10 82.39          0.407               

Méthode du coude :
La méthode du coude consiste à visualiser l'évolution de l'inertie en fonction de k. Un "coude" dans la courbe indique le nombre optimal de clusters. Dans notre cas, la courbe montre une décroissance régulière, rendant l'identification du coude moins évidente.

Score de silhouette : 
Le score de silhouette atteint son maximum à   k = 6   avec une valeur de   0.428  . Ce score indique une qualité acceptable du clustering :
- Les clusters sont relativement bien séparés
- Les points sont correctement assignés à leurs clusters
- Le score de 0.428 est dans la fourchette acceptable (0.3-0.5)

5.2 Analyse détaillée de la silhouette

L'analyse du score de silhouette par point révèle :
- La plupart des points ont un score positif, confirmant une bonne assignation
- Certains clusters présentent une meilleure cohérence que d'autres
- Le score moyen de 0.428 est cohérent avec une segmentation de qualité acceptable

5.3 Modèle final

Le modèle K-Means final a été entraîné avec   k = 6 clusters   et les paramètres suivants :
-   random_state = 42   : Pour la reproductibilité
-   n_init = 10   : 10 initialisations différentes, la meilleure est retenue

  Distribution des clusters :  
- Cluster 0 : 45 clients (22.5%)
- Cluster 1 : 39 clients (19.5%)
- Cluster 2 : 33 clients (16.5%)
- Cluster 3 : 39 clients (19.5%)
- Cluster 4 : 23 clients (11.5%)
- Cluster 5 : 21 clients (10.5%)

Les clusters sont de tailles relativement équilibrées, ce qui est favorable pour une segmentation actionnable.

6. Interprétation des résultats

6.1 Caractéristiques moyennes par cluster

Cluster | Taille | % | Âge moyen | Revenu (k$) | Score dépense | Genre (F/M) |

0  45  22.5%  56.3  54.3  49.1  26/19 
1  39  19.5%  26.8  57.1  48.1  25/14 
2  33  16.5%  41.9  88.9  16.9  14/19 
3  39  19.5%  32.7  86.5  82.1  21/18 
4  23  11.5%  25.0  25.3  77.6  13/10 
5  21  10.5%  45.5  26.3  19.4  13/8 

6.2 Profils détaillés des segments

Cluster 0 : Seniors économes (22.5%)

-   Caractéristiques :  
  - Âge moyen : 56.3 ans (le plus âgé)
  - Revenu moyen : 54.3 k$ (revenu modéré)
  - Score de dépense : 49.1/100 (dépense modérée)
  - Genre : 58% Female, 42% Male
-   Profil :   Clients seniors avec un revenu modéré et un comportement de dépense modéré. Ils représentent le segment le plus important en taille.

Cluster 1 : Profil mixte (19.5%)

-   Caractéristiques :  
  - Âge moyen : 26.8 ans (jeunes)
  - Revenu moyen : 57.1 k$ (revenu modéré-élevé)
  - Score de dépense : 48.1/100 (dépense modérée)
  - Genre : 64% Female, 36% Male
-   Profil :   Jeunes clients avec un revenu modéré et un comportement de dépense modéré. Profil équilibré sans caractéristique extrême.

Cluster 2 : Clients prudents à haut revenu (16.5%)

-   Caractéristiques :  
  - Âge moyen : 41.9 ans (âge moyen)
  - Revenu moyen : 88.9 k$ (revenu élevé - le plus élevé)
  - Score de dépense : 16.9/100 (dépense très faible - le plus faible)
  - Genre : 42% Female, 58% Male
-   Profil :   Clients avec un revenu élevé mais un comportement de dépense très prudent.   Segment à développer   : potentiel inexploité pour augmenter les ventes.

 Cluster 3 : Jeunes dépensiers à haut revenu (19.5%)

-   Caractéristiques :  
  - Âge moyen : 32.7 ans (jeunes-adultes)
  - Revenu moyen : 86.5 k$ (revenu élevé)
  - Score de dépense : 82.1/100 (dépense élevée - la plus élevée)
  - Genre : 54% Female, 46% Male
-   Profil :     Segment le plus prometteur  . Jeunes clients avec un revenu élevé et un comportement de dépense élevé. Cible idéale pour les produits premium et les programmes de fidélité.

 Cluster 4 : Jeunes dépensiers à faible revenu (11.5%)

-   Caractéristiques :  
  - Âge moyen : 25.0 ans (très jeunes - le plus jeune)
  - Revenu moyen : 25.3 k$ (revenu faible - le plus faible)
  - Score de dépense : 77.6/100 (dépense élevée)
  - Genre : 57% Female, 43% Male
-   Profil :   Très jeunes clients avec un revenu faible mais un comportement de dépense élevé. Segment intéressant pour les promotions et offres accessibles.

 Cluster 5 : Clients économes (10.5%)

-   Caractéristiques :  
  - Âge moyen : 45.5 ans (âge moyen-élevé)
  - Revenu moyen : 26.3 k$ (revenu faible)
  - Score de dépense : 19.4/100 (dépense très faible)
  - Genre : 62% Female, 38% Male
-   Profil :   Clients avec un revenu faible et un comportement de dépense très faible. Segment nécessitant des stratégies de relance.

6.3 Visualisations

Les visualisations 2D et 3D confirment la bonne séparation des clusters :
- Les clusters sont bien distincts dans l'espace des variables
- Les centroïdes (centres des clusters) sont bien positionnés
- La visualisation 3D permet d'apprécier la séparation dans l'espace complet


7. Recommandations business

7.1 Stratégies par segment

#### Cluster 0 : Seniors économes (22.5%)
  Stratégie :   Fidélisation et confort
-   Actions :  
  - Programmes de fidélité adaptés aux seniors
  - Offres sur les produits du quotidien
  - Facilité d'accès et service client renforcé
-   Marketing :  
  - Communication traditionnelle (email, courrier)
  - Mise en avant des valeurs durables et de la qualité
  - Horaires adaptés et parking facilité

#### Cluster 1 : Profil mixte (19.5%)
  Stratégie :   Équilibre et polyvalence
-   Actions :  
  - Offres variées couvrant différents besoins
  - Programmes de fidélité standard
  - Promotions régulières
-   Marketing :  
  - Communication multi-canal (email, réseaux sociaux)
  - Mise en avant du rapport qualité/prix

#### Cluster 2 : Clients prudents à haut revenu (16.5%) ⭐   PRIORITÉ  
  Stratégie :   Développement du potentiel
-   Actions :  
  - Promotions ciblées pour inciter à dépenser
  - Programmes de relance personnalisés
  - Offres exclusives et services premium
-   Marketing :  
  - Communication sur la qualité et l'exclusivité
  - Mise en avant des avantages et garanties
  - Événements VIP et démonstrations produits
-   Objectif :   Augmenter le score de dépense de 16.9 à au moins 40-50

#### Cluster 3 : Jeunes dépensiers à haut revenu (19.5%) ⭐   PRIORITÉ  
  Stratégie :   Maximisation de la valeur
-   Actions :  
  - Programmes de fidélité premium
  - Offres exclusives et produits haut de gamme
  - Services personnalisés et conseils
-   Marketing :  
  - Communication haut de gamme
  - Événements VIP et lancements produits
  - Partenariats avec marques premium
-   Objectif :   Maintenir et développer la relation avec ce segment à forte valeur

#### Cluster 4 : Jeunes dépensiers à faible revenu (11.5%)
  Stratégie :   Accessibilité et tendance
-   Actions :  
  - Promotions régulières et offres accessibles
  - Produits tendance à prix compétitifs
  - Programmes de paiement échelonné
-   Marketing :  
  - Réseaux sociaux et influenceurs
  - Expérience digitale optimisée
  - Campagnes jeunes et dynamiques

#### Cluster 5 : Clients économes (10.5%)
  Stratégie :   Relance et réactivation
-   Actions :  
  - Promotions agressives et coupons de réduction
  - Programmes de relance ciblés
  - Offres d'entrée de gamme
-   Marketing :  
  - Communication promotionnelle
  - Mise en avant des prix bas
  - Offres flash et soldes

### 8.2 Recommandations globales

#### Allocation des ressources marketing
-   40%   sur Cluster 3 (Jeunes dépensiers à haut revenu) - ROI élevé
-   30%   sur Cluster 2 (Clients prudents à haut revenu) - Potentiel de développement
-   20%   sur Clusters 0 et 1 (Segments importants en taille)
-   10%   sur Clusters 4 et 5 (Segments plus petits)

#### Actions transversales
1.   Personnalisation :   Utiliser la segmentation pour personnaliser toutes les communications
2.   Suivi :   Mettre en place un suivi régulier de l'évolution des segments
3.   Tests A/B :   Valider les recommandations avec des tests A/B
4.   Enrichissement :   Enrichir les segments avec des données comportementales supplémentaires (fréquence de visite, panier moyen, etc.)

---

## 9. Conclusion

L'analyse K-Means a permis d'identifier   6 segments distincts   de clients avec des profils clairs et actionnables. La qualité du clustering (score de silhouette = 0.428) est acceptable et permet une segmentation fiable.

1.   Compréhension approfondie   de la base client
2.   Segmentation objective   basée sur les données
3.   Profils distincts   permettant des stratégies ciblées
4.   Insights actionnables   pour améliorer la performance commerciale


-   Limites :  
  - Score de silhouette modéré (0.428) - pourrait être amélioré
  - Variables limitées (3 variables numériques)
  - Pas de données comportementales (fréquence, panier moyen, etc.)
-   Perspectives :  
  - Enrichir avec des données supplémentaires
  - Affiner les segments avec des tests A/B
  - Suivre l'évolution des segments dans le temps
  - Comparer avec d'autres méthodes de clustering (DBSCAN, GMM)


Cette segmentation fournit une base solide pour :
-   Décisions stratégiques   éclairées
-   Allocation optimale   des ressources marketing
-   Personnalisation   des offres et communications
-   Amélioration   de la satisfaction client et de la rentabilité





