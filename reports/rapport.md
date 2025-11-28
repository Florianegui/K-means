Rapport d’Analyse : Segmentation Client par K-Means
Projet

Segmentation de la clientèle d’un centre commercial à l’aide de l’algorithme K-Means.
Ce travail a été réalisé par Guillou Floriane et Jari Jenna.

Pour plus d’informations, les graphiques sont disponibles dans le PowerPoint associé.

1. Introduction
1.1 Contexte

La segmentation client constitue un enjeu central pour les entreprises qui souhaitent personnaliser leurs actions marketing et optimiser leurs campagnes. Dans ce cadre, analyser les clients d’un centre commercial permet d’identifier des groupes homogènes se distinguant par des critères tels que l’âge, le revenu ou encore le comportement d’achat.

1.2 Objectifs

L’objectif de ce travail est d’identifier des segments de clients distincts, de comprendre leurs caractéristiques, de proposer des recommandations stratégiques adaptées à chacun, et d’évaluer la qualité de la segmentation obtenue.

2. Données

Le dataset analysé, issu de Kaggle, contient les informations de 200 clients. Les variables disponibles sont : un identifiant unique (CustomerID), le genre, l’âge, le revenu annuel et un score de dépense allant de 1 à 100.

Aucune valeur manquante n’a été détectée, ce qui garantit une base de données propre pour réaliser le clustering. (ce qui est normal car le dataset provient de Kaggle)

3. Méthodologie

3.1 Algorithme K-Means

L’algorithme K-Means repose sur une approche itérative consistant à initialiser des centroïdes, à assigner chaque individu au centroïde le plus proche, puis à recalculer les centroïdes jusqu’à obtenir une stabilisation. L’objectif est de minimiser la somme des distances intra-clusters.

3.2 Métriques d’évaluation

La qualité du clustering a été évaluée à l’aide de deux indicateurs principaux :

L’inertie (WCSS), qui mesure la compacité des clusters.

Le score de silhouette, qui mesure à quel point les clusters sont séparés et cohérents.

3.3 Outils utilisés

L’analyse a été réalisée en Python à l’aide des bibliothèques pandas, numpy, scikit-learn ainsi que matplotlib et seaborn pour les visualisations.

4. Préparation des données
4.1 Exploration

L’exploration montre que les 200 clients ont un âge moyen de 38,9 ans, un revenu annuel moyen de 60,6 k$, et un score de dépense moyen de 50,2.

4.2 Sélection des variables

Les variables retenues pour le clustering sont l’âge, le revenu annuel et le score de dépense. Les variables CustomerID et Gender n’ont pas été incluses car elles ne sont pas pertinentes pour l’algorithme, même si le genre a été utilisé pour interpréter les clusters.

4.3 Normalisation

Les variables numériques ont été normalisées à l’aide de StandardScaler afin de leur donner une importance équivalente dans le calcul des distances. Après normalisation, leurs moyennes sont proches de zéro et leurs écarts-types proches de un, ce qui confirme la bonne préparation des données.

5. Analyse exploratoire

L’étude des distributions montre que l’âge est assez équilibré, que le revenu annuel est réparti de manière relativement homogène, et que le score de dépense présente une distribution bimodale. Les corrélations entre les variables sont faibles, ce qui indique qu’elles apportent chacune une information complémentaire utile pour le clustering.

L’analyse visuelle des données suggère déjà la présence de plusieurs regroupements naturels.

6. Application de K-Means
6.1 Choix du nombre de clusters

Plusieurs valeurs de k, allant de 2 à 10, ont été testées. Le score de silhouette est maximal lorsque k = 6, avec une valeur de 0,428. Même si la méthode du coude ne révèle pas un point très clair, ce score indique que six clusters constituent le nombre optimal.

6.2 Modèle final

Le modèle final utilise donc six clusters avec un random_state de 42 et dix initialisations. La répartition des clusters est globalement équilibrée, ce qui rend la segmentation opérationnelle.

7. Interprétation des résultats
7.1 Présentation des segments

L’analyse des moyennes montre que :

Le Cluster 0 regroupe des seniors économes, âgés en moyenne de 56 ans, ayant un revenu modéré et un score de dépense moyen.

Le Cluster 1 correspond à un profil mixte composé de jeunes adultes au revenu modéré et au niveau de dépense équilibré.

Le Cluster 2 rassemble des clients prudents à haut revenu, présentant le revenu moyen le plus élevé mais un score de dépense très faible ; il s’agit d’un segment au potentiel fortement inexploité.

Le Cluster 3 représente des jeunes dépensiers à haut revenu, constituant le segment le plus prometteur grâce à leur fort pouvoir d’achat et leur score de dépense particulièrement élevé.

Le Cluster 4 regroupe de très jeunes clients ayant un faible revenu mais un niveau de dépense étonnamment élevé.

Le Cluster 5 rassemble des clients économes disposant d'un revenu faible et d’un comportement d’achat très réduit.

7.2 Visualisations

Les visualisations 2D et 3D confirment la bonne séparation des clusters et la cohérence des centroïdes.

8. Recommandations business
8.1 Stratégies par segment

Pour les seniors économes, l’accent doit être mis sur la fidélisation, le confort et la mise en avant de la qualité.
Le profil mixte nécessite des offres polyvalentes et un marketing multicanal.
Les clients prudents à haut revenu doivent être stimulés par des offres exclusives, des relances personnalisées et une communication centrée sur la qualité.
Les jeunes dépensiers à haut revenu doivent bénéficier d’avantages premium et d’expériences d’achat haut de gamme.
Les jeunes dépensiers à faible revenu réagiront davantage aux promotions accessibles et aux campagnes dynamiques sur les réseaux sociaux.
Les clients économes nécessitent une stratégie de relance basée sur des prix attractifs et des offres promotionnelles.

8.2 Recommandations globales

Il est recommandé d’allouer la majorité du budget marketing aux clusters 2 et 3, qui représentent les segments les plus lucratifs ou à plus fort potentiel. Une personnalisation des communications, un suivi régulier des segments et des tests A/B permettront d’améliorer encore les performances. L’ajout de nouvelles données pourrait également enrichir la segmentation.

9. Conclusion

La segmentation réalisée permet d’identifier six groupes de clients clairement distincts. Le score de silhouette de 0.428 confirme une qualité acceptable du clustering. Cette segmentation offre une compréhension approfondie de la clientèle et constitue une base solide pour orienter les décisions marketing du centre commercial.
Même si certaines limites subsistent, notamment le nombre restreint de variables, cette approche fournit des résultats actionnables visant à optimiser la satisfaction client et la rentabilité globale.