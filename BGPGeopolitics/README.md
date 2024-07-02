Attention : les chemins vers des dossiers doivent toujours finir par un / car sinon il peut y avoir des problèmes.
En effet, les concaténation des chemins sont visiblement gérées uniquement par des +, donc c'est pas bien gérée

Pour les fichiers obligatoires, il faut toujours avoir as.sqlite dans le dossier resources, sinon ça peut causer un bug à l'ouverture de la base de données

Dans ce dossier on va stocker tous les fichiers nécéssaires à la compilation, puis on va gérer les différentes configurations dans des dossiers différents. De cette manière, 
si les commandes sont executées dans le bon ordre dans le fichier, on gagne énormement à la construction de l'image grâce aux layers !

De manière générale il faut fragmenter au plus le code afin de gagner du temps au moment de la construction de l'image.