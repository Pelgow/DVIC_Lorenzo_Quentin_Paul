# DVIC_Lorenzo_Quentin_Paul

# Introduction

Ce projet consiste en la création d'un piano interactif à l'aide d'une Raspberry Pi Pico, d'un buzzer et de l'utilisation de technologies web tels que Vue.js et Node.js (Express). Le but est de créer un système qui permet de jouer des notes de musique à l'aide d'un clavier virtuel et de faire en sorte que le buzzer réagisse en fonction de la note jouée.


## Fonctionnement
 
Le projet fonctionne de la manière suivante : l'interface utilisateur (créée avec Vue.js) affiche un clavier virtuel qui permet de sélectionner les notes à jouer. Lorsqu'un bouton est pressé, un signal est envoyé au serveur Node.js (Express) qui envoie à son tour un signal à la carte Raspberry Pi Pico pour que celle-ci joue la note correspondante sur le buzzer. En même temps, le buzzer change de lumière en fonction de la note jouée.

# Installation

## Prérequis

* Raspberry Pi Pico
* Buzzer
* Breadboard
* Fils de connexion
* Un ordinateur avec un environnement de développement Python

## Étapes d'installation

* Connectez le buzzer à la Raspberry Pi Pico à l'aide d'une breadboard et de fils de connexion.
* Installez les bibliothèques Python nécessaires à la Raspberry Pi Pico. Vous pouvez les trouver sur le site officiel de Raspberry Pi.

## Clonez le projet depuis GitHub.

* Ouvrez une console dans le dossier du projet.
* Exécutez nodemen serveur.js pour installer les dépendances nécessaires.
* Exécutez npm run dev pour démarrer le serveur Node.js (Express).
* Ouvrez votre navigateur et accédez à l'adresse http://127.0.0.1:5173/ pour accéder à l'interface utilisateur du piano.

## Conclusion
Félicitations, vous avez mis en place un piano interactif utilisant une Raspberry Pi Pico, Vue.js et Node.js. Vous pouvez maintenant jouer de la musique en utilisant un clavier virtuel et en faire profiter vos amis et votre famille.
