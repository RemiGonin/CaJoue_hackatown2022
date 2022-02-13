# ÇaJoue !

Projet développé dans le cardre du Hackatown de PolyHx du vendredi 11 au dimanche 13 février 2022.

## Inspiration

Cette saison est notre premier hiver à Montréal et nous sommes très agréablement surpris du très grand nombre de patinoires publiques dans tous les parcs de Montréal, que ce soit pour patiner ou bien jouer au hockey. Cependant le hockey étant un sport collectif, il n'est facile de savoir si d'autres joueurs sont présents à la patinoire pour pouvoir jouer. Nous avons donc décider de travailler sur un projet pour faciliter le lien social par le sport collectif, en particulier le hockey en cette belle saison d'hiver.

## Ce que ça fait

ÇaJoue répertorie l'ensemble des patinoires de Montréal sur une carte en fonction de leur état (type de patinoire, ouverture...). L'ajout de l'application est de pouvoir trouver les patinoires sur lesquelles "ÇaJoue" actuellement, et donc de pouvoir si rendre sans craindre de se retrouver tout seul pour jouer !
Pour cela le concept est assez intuitif, lorsque l'on commence à jouer sur une patinoire, on y dépose une noix de "ÇaJoue" avec un certain délai pour indiquer aux autres utilisateurs qu'il y a actuellement du jeu à cette patinoire. Après ce délai sans remise, la noix est retirée pour indiquer qu'il n'y a plus de joueurs sur place.

## Comment cela a été construit ?

Le frontend est une application mobile (Android & iOS) developpée en React Native, et permet notamment d'afficher la carte avec l'ensemble des patinoires, de trouver les patinoires où "ÇaJoue" et d'indiquer lorsque "ÇaJoue" ou "ÇaJouePlus" sur une patinoire. Le frontend communique avec le backend developpé avec FastAPI, un framework Python et les données relatives aux patinoires sont stockées dans une base de donnée MySQL. Le backend est hébergé chez OVH Cloud sous la forme d'un cluster Kubernetes implémentant une mise à l'échelle automatique pour faire face à tout type de charge. La base de donnée MySQL et elle aussi hébergée chez OVH Cloud, pour centraliser son accès depuis les différents pods de FastAPI, et offrir une certaine tolérance aux fautes. Nous avons donc utilisé Docker pour packager l'application, et appri à utiliser les services OpenStack d'OVH Cloud pour le déployer. 

## Difficultées rencontrée

Ce weekend fut notre toute première expérience de hackaton et nous en avons profiter pour apprendre de nouvelles technologies qui nous étaient complètement inconnues. Nous sommmes donc partie de zéro pour apprendre React Native, FastAPI ou encore le fonctionnement de Kubernetes et de déploiement sur le Cloud. De nombreuses erreurs et de longues heures de deboggage et de lectures de tutoriels ont donc rythmé notre weekend.

## Ce dont nous sommes fier

Nous n'avions pas d'ambitions particulières pour ce weekend, mais le projet nous a beaucoup plu et nous a permis d'apprendre énorméménet de choses en très peu de temps. Nous ne pensions pas être capable de produire un tel résultat (certe modeste) en si peu de temps !

## Et après ?

Nous avons beaucoup aimé travailler sur ce projet, tant il touche à de nombreux aspects complètement différents (Frontend, Backend, architecture cloud etc). Nous avons aussi beaucoup d'idées pour enrichir l'application, comme un système de patinoires favorites pour être notifié lorsque "ÇaJoue" sur une de nos patinoires favorites. Enfin, le concept de ÇaJoue peut facilement être étendu à n'importe quel sport collectif pouvant ce jouer sur les terrains de la ville: Basketball, Soccer, Tennis etc, pour rendre ÇaJoue incontournable à chaque saison !