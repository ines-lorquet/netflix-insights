Veille IA

Voulant pousser votre apprentissage de l’intelligence artificielle, vous réalisez
une veille sur les différents aspects suivants. Définissez simplement ce qu’est :

● L’intelligence artificielle

Toute technologie algorithmique qui permet de résoudre des problèmes complexes qu’on aurait cru réservé à l’intelligence humaine

Etapes du traitement des données
Analyse, récupération, nettoyage, exploration, modélisation, évaluation, mise en production, maintenance

L'intelligence artificielle (IA) est un domaine de l'informatique qui se concentre sur la création de systèmes capables d'effectuer des tâches qui nécessitent généralement l'intelligence humaine. Ces tâches peuvent inclure la reconnaissance de la parole, la traduction de langues, la prise de décision, la résolution de problèmes, l'apprentissage et l'adaptation à partir d'expériences passées, entre autres.

Les techniques d'intelligence artificielle utilisent souvent des modèles mathématiques et statistiques pour permettre aux ordinateurs de "penser" de manière autonome et de résoudre des problèmes de manière similaire à un être humain. Les principaux domaines de l'IA incluent l'apprentissage automatique, qui consiste à entraîner des algorithmes à partir de données pour effectuer des tâches spécifiques, et le traitement du langage naturel, qui vise à permettre aux ordinateurs de comprendre et de générer un langage humain.

L'IA est devenue de plus en plus répandue dans de nombreux aspects de la vie quotidienne, des recommandations de produits en ligne aux voitures autonomes en passant par les systèmes de soins de santé. Son potentiel à transformer de nombreux secteurs de l'économie et de la société est immense, mais il soulève également des questions éthiques, juridiques et sociales sur des sujets tels que la vie privée, la sécurité et l'impact sur l'emploi.


● Le Machine Learning (ou l’apprentissage automatique)

 Le Machine Learning (ou apprentissage automatique) est une branche de l’intelligence artificielle (IA) qui se concentre sur la création de systèmes capables d’apprendre ou d’améliorer leurs performances en fonction des données qu’ils traitent.


 Voici quelques points clés à retenir :
Définition : Le Machine Learning consiste à laisser des algorithmes découvrir des motifs récurrents dans des ensembles de données. Ces données peuvent être des chiffres, des mots, des images, des statistiques, ou tout ce qui peut être stocké numériquement. En détectant ces motifs, les algorithmes apprennent et améliorent leurs performances dans l’exécution de tâches spécifiques. En résumé, les algorithmes de Machine Learning apprennent de manière autonome à effectuer des tâches ou à faire des prédictions à partir de données, et ils s’améliorent avec le temps.


Fonctionnement : Le développement d’un modèle de Machine Learning se déroule en quatre étapes principales :
Sélection et préparation des données d’entraînement : Ces données sont utilisées pour nourrir le modèle et lui apprendre à résoudre un problème spécifique. Elles peuvent être étiquetées (pour indiquer les caractéristiques à identifier) ou non étiquetées (pour que le modèle les identifie lui-même).
Choix de l’algorithme : Le type d’algorithme dépend du type et du volume des données d’entraînement ainsi que du problème à résoudre.
Entraînement de l’algorithme : C’est un processus itératif où les variables sont exécutées à travers l’algorithme, et les résultats sont comparés à ceux attendus. Les poids et le biais sont ajustés pour améliorer la précision.
Modèle de Machine Learning : Une fois entraîné, l’algorithme devient le modèle de Machine Learning capable de détecter des motifs dans de nouvelles données.

Utilisations : Le Machine Learning est utilisé dans divers domaines tels que la reconnaissance d’image, la prédiction de tendances, la recommandation de produits, la détection de fraudes, la médecine, et bien plus encore.


● Le pré-traitement des données

Le pré-traitement des données est une étape cruciale dans le domaine de la science des données. Voici ce que cela implique :
Nettoyage des données : Cette première étape consiste à traiter les données incorrectes, incomplètes ou manquantes. Voici quelques méthodes courantes pour gérer ces problèmes :
Suppression des données manquantes : Si certaines données sont manquantes dans le jeu de données, vous pouvez les ignorer, surtout si la base de données est suffisamment grande et que de nombreuses données manquent dans la même ligne.
Remplissage des données manquantes : Vous pouvez remplacer les valeurs manquantes par la moyenne, la médiane ou la modalité la plus fréquente (mode) pour les variables catégorielles. Par exemple, en utilisant Pandas en Python, vous pouvez remplir les valeurs manquantes comme suit :

df = df.fillna(0)  # Remplace les NAs par 0
df = df.fillna(method='pad')  # Remplace chaque NA par la dernière valeur non NA de sa colonne
df = df.fillna({'col_1': val_1, 'col_2': 'val_2'})  # Remplace les NAs de la colonne 'col_1' par val_1 et celles de la colonne 'col_2' par val_2
df = df.fillna(df.mean())  # Remplace les NAs de chaque colonne par la moyenne de la colonne
df = df.fillna(df.median())  # Remplace les NAs de chaque colonne par la médiane
df['Colonne'] = df['Colonne'].fillna(df['Colonne'].mode()[0])  # Remplace les NAs de chaque colonne par la médiane

Réduction du bruit : Parfois, les données peuvent contenir du bruit parasite d’acquisition. Il est essentiel de nettoyer ce bruit pour que les données puissent être correctement traitées par un ordinateur.
En résumé, le pré-traitement des données vise à convertir les données primaires en un format exploitable pour le traitement, les rendant ainsi plus compréhensibles et adaptées à une analyse approfondie. 

● L’analyse descriptive des données

L’analyse descriptive des données est un ensemble d’outils statistiques qui servent à décrire et résumer les caractéristiques principales d’un ensemble de données pour faciliter leur compréhension et leur interprétation 
Statistiques descriptives:
mesure de la moyenne, la médiane, le mode, l'écart-type, la variance.
Visualisation des données :
histogrammes, les diagrammes en boîte, les diagrammes à moustaches, les diagrammes en barres, etc
Analyse de tendance centrale: 
identification de valeurs centrales autour desquelles les données semblent se regrouper, telles que la moyenne, la médiane et le mode.
Analyse de dispersion: 
l'examen de la répartition des valeurs autour de la tendance centrale, mesurée par des indicateurs tels que l'écart-type, l'étendue, les quartiles, etc.
Analyse de la forme de distribution:
identification de la forme de la distribution des données, qu'elle soit symétrique, asymétrique, uniforme, en forme de cloche, etc.


Choisissez un domaine (la santé, la finance, l’environnement, le juridique,
l’immobilier, etc) et expliquez ce qu’il est possible de faire dans ce domaine
grâce à l’intelligence artificielle.



Veille sur l’outil Jupyter Notebook

Jupyter Notebook est une plateforme en ligne qui facilite la création et le partage de documents numériques. Elle offre une interface simple et centrée sur le document. JupyterLab est la nouvelle interface web interactive pour les notebooks, le code et les données. Elle offre une flexibilité aux utilisateurs pour configurer et organiser leurs workflows en science des données, en informatique scientifique, en journalisme computationnel et en apprentissage automatique. Jupyter supporte plus de 40 langages de programmation, incluant Python, R, Julia et Scala. Les notebooks peuvent être partagés avec d’autres via e-mail, Dropbox, GitHub et le Jupyter Notebook Viewer. Votre code peut générer une sortie interactive et riche : HTML, images, vidéos, LaTeX et types MIME personnalisés. Vous pouvez utiliser des outils de big data, comme Apache Spark, en Python, R et Scala. Jupyter offre aussi une version multi-utilisateur du notebook, conçue pour les entreprises, les salles de classe et les laboratoires de recherche. Vous pouvez essayer certains outils de Project Jupyter pour l’informatique interactive sans avoir à installer quoi que ce soit. 
