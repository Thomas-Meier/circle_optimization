# circle_optimization

L'objectif de ce repository est de proposer une solution pour le problème suivant :

**Packing n circles in the unit square with the largest possible radius**


## Définition du problème

Soit *n* un nombre naturel, il s'agit de déterminer le rayon *r* maximal de *n* cercles enfermés dans un carré de côté unitaire sans que ces cercles ne se chevauchent. On représentera par (*x<sub>i</sub>*, *y<sub>i</sub>*) les coordonnées du centre du *i*-ème cercle.
<br/>On peut alors écrire le problème de la manière suivante : 

![GitHub Logo](/images/formules_mathematiques.png)


## Première stratégie

Recherche historique des solutions (articles)


## Placement initial des points

Problème du positionnement des centres des cercles (selon des lignes mais normalement aléatoire) avec un rayon 1=r*sqrt(n).
Ainsi le nombre de ligne et de colonne identique et seule la dernière ligne reste a être remplie. On débute donc pas très loin de la taille moyenne des cercles d'après [14 : global optimisation] ou r=1.07456993182354/sqrt(n)
=> le problème avec ce placement déjà optimisé est qu'il est difficile  de changer de configuration radicalement.(alors que c'est possibble si l'on commence avec des cercles de rayon très petit).s
Une autre possibilité pour trouver des solutions faisable est de placer des points de rayon 0, dans le domaine [0, 1]^2.

## Choix du solveur local

## Choix de la perturbation

## Comparaison avec l'algorithme Multistart

## Conclusion

Cours de la prof : aller plus loin dans le projet
