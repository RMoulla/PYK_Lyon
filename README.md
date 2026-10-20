# Formation PYK — Lyon

**Python, initiation au traitement de données**

**14 au 16 octobre 2026 · Lyon · Redha Moulla**

Ce dépôt rassemble le support de la session, les jeux de données et des notebooks corrigés pour pratiquer les bases de Python, l’analyse de données, la visualisation et la modélisation.

## Accès rapide

| Ressource | Accès | Données nécessaires |
| --- | --- | --- |
| Support de cours | [Ouvrir le PDF](PYK_Lyon.pdf) | — |
| Bases de Python | [Lire le notebook](Copie_de_TP_Introduction_Python.ipynb) · [Ouvrir dans Colab](https://colab.research.google.com/github/RMoulla/PYK_Lyon/blob/main/Copie_de_TP_Introduction_Python.ipynb) | Aucune |
| Analyse des prix immobiliers | [Lire le corrigé](TP_Seloger_Correction.ipynb) · [Ouvrir dans Colab](https://colab.research.google.com/github/RMoulla/PYK_Lyon/blob/main/TP_Seloger_Correction.ipynb) | [selogerdata.csv](selogerdata.csv) |
| Analyse des données de crédit | [Lire le notebook](Copie_de_TP_German_Credit.ipynb) · [Ouvrir dans Colab](https://colab.research.google.com/github/RMoulla/PYK_Lyon/blob/main/Copie_de_TP_German_Credit.ipynb) | [german_credit_data.csv](german_credit_data.csv) |
| Analyse descriptive du churn | [Lire le notebook](TP_Analyse_Données_Churn.ipynb) · [Ouvrir dans Colab](https://colab.research.google.com/github/RMoulla/PYK_Lyon/blob/main/TP_Analyse_Données_Churn.ipynb) | [customer_churn.csv](customer_churn.csv) |
| Analyse et prédiction du churn | [Lire le notebook](TP_churn.ipynb) · [Ouvrir dans Colab](https://colab.research.google.com/github/RMoulla/PYK_Lyon/blob/main/TP_churn.ipynb) | [customer_churn.csv](customer_churn.csv) |

Le support peut aussi être [téléchargé directement](https://raw.githubusercontent.com/RMoulla/PYK_Lyon/main/PYK_Lyon.pdf).

## Télécharger les fichiers

1. Ouvrez le fichier souhaité dans le tableau ci-dessus.
2. Cliquez sur **Download raw file**, l’icône de téléchargement située au-dessus du fichier. Si le bouton **Raw** affiche le texte, enregistrez ce contenu sur votre ordinateur.
3. Conservez le nom et l’extension du fichier. Les notebooks recherchent les CSV sous les noms exacts indiqués dans le tableau.

Si l’aperçu GitHub d’un notebook ou du PDF ne s’affiche pas, utilisez son lien Colab ou téléchargez le fichier.

## Exécuter les notebooks dans Google Colab

Un notebook (`.ipynb`) alterne explications et cellules de code. GitHub permet de le lire ; Colab permet de l’exécuter dans le navigateur.

1. Connectez-vous à votre compte Google, puis ouvrez le lien **Ouvrir dans Colab** du TP choisi.
2. Sélectionnez **Fichier → Enregistrer une copie dans Drive** pour conserver vos modifications.
3. Cliquez sur **Se connecter** et utilisez un environnement **Python 3 avec CPU**.
4. Pour un TP utilisant des données, téléchargez le CSV indiqué dans le tableau. Dans Colab, ouvrez **Fichiers** dans la barre latérale, puis **Importer**, et choisissez ce CSV. Attendez qu’il apparaisse dans `/content/`.
5. Exécutez les cellules **de haut en bas**, avec le bouton ▶ ou **Maj + Entrée**. Les premières cellules préparent les variables utilisées par les suivantes.
6. Lisez les résultats, modifiez une instruction ou un paramètre, puis relancez les cellules concernées pour comparer.

**Ouvrir le notebook depuis GitHub n’importe pas automatiquement ses données.** Après une réinitialisation de la session Colab, importez à nouveau les CSV et réexécutez les cellules.

Les notebooks contiennent le code corrigé. Leurs anciennes sorties ont été effacées : les tableaux et graphiques apparaîtront après exécution. Aucune clé API n’est nécessaire pour ces TP.

## Repères pour les exercices

- **Bases Python** : variables, types, conditions, boucles et listes.
- **Immobilier** : nettoyage des données, analyse exploratoire, visualisation et régression pour étudier les prix.
- **Crédit** : nettoyage, statistiques descriptives, création de variables, visualisation et modélisation.
- **Churn — analyse descriptive** : explorer les clients et comparer les groupes à l’aide de statistiques et de graphiques.
- **Churn — prédiction** : prolonger l’exploration par un modèle de prédiction du départ des clients.

## Compléments

| Fichier | Utilisation |
| --- | --- |
| [nettoyage_ville.py](nettoyage_ville.py) | Fonction de correction de caractères mal encodés dans les noms de villes. |
| [nettoyage_cuisine.py](nettoyage_cuisine.py) | Fonction de correction de caractères et de recodage de certaines catégories de cuisine. |
| [SKILL.md](SKILL.md) | Méthode pour préciser un besoin et rédiger des spécifications avec un assistant IA. |

Les deux scripts sont des exemples complémentaires. Le notebook immobilier contient son propre nettoyage et peut être exécuté sans les importer. Le skill peut être utilisé dans un outil prenant en charge les Skills, ou joint à une conversation avec un assistant IA.

## En cas de difficulté

| Problème | Que faire ? |
| --- | --- |
| `FileNotFoundError` | Importer le CSV dans les fichiers Colab et vérifier son nom exact, sans suffixe `(1)` ni extension supplémentaire. |
| Variable inconnue (`NameError`) | Reprendre les cellules depuis le début ou depuis la première cellule en erreur. |
| Bibliothèque manquante (`ModuleNotFoundError`) | Vérifier que le notebook utilise un environnement Python 3 ; installer la bibliothèque indiquée si vous utilisez votre propre environnement. |
| Résultats disparus après une reconnexion | Réimporter les données, puis réexécuter le notebook. |

Pour toute question : **redha.moulla@axia-conseil.com**.

Pour poursuivre la veille en IA : [Courants de fond](https://redhamoulla.substack.com).
