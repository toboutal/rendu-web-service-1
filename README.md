# WebService-rendu-1
 
##Exercice 1 - Envoyer des requêtes en tant que client

Installer postman et envoyer une requête http à l’URL https://nowledgeable.com/http-exercice

###Quel est le type de la donnée renvoyée ?

JSON

Avec python et la librairie requests envoyer une requête http à l’url précédente et récupérer la réponse sous forme de dictionnaire

Avec postman envoyer une requête à l’URL https://nowledgeable.Com/http-exercice2. Faire en sorte que le corps de la requête envoie un json avec la clé “secret” et la valeur 42 (pas sous forme de chaine de caractère)

Faire de même avec la librairie requests



##Exercice 2 - Faire sa première API 

On veut faire une petite API qui permet de gérer une liste de tâches. 

Installer python si ce n’est pas déjà fait 

installer la librairie Flask et avec le get-started créer un premier serveur web qui renvoie un json contenant la clé “message” avec la valeur “hello first api”

Tester votre api avec Postman

Faire un endpoint qui accepte des requêtes de type Post. Faire en sorte d’afficher les données reçues par le client

Avec postman, envoyer des données json et vérifier que le serveur les reçoit bien

FastApi est une alternative à Flask qui est intéressante car elle permet de générer automatiquement la documentation de l’API grâce à du type des données reçues. Reprendre cet exercice avec FastAPI et vérifier que la documentation de votre api est automatiquement générée



##Exercice - veille

###Expliquer à quoi sert les méthodes HTTP Put et Patch
	
	PUT, remplace les données par celle qui sont envoyées dans la requête.
	
	PATCH, permet la modification partielle d'une ressource en fusionnant les données envoyées avec les données déjà présentes ou grâce à l'utilisation d'opération de modification.

###Que veut dire qu’un protocole soit stateless ?

Un processus ou une application sans état est indépendant. Il ne stocke pas de données et ne fait référence à aucune transaction passée. Chaque transaction est effectuée à partir de rien, comme si c'était la première fois. Les applications sans état fournissent un service ou une fonction et utilisent un réseau de diffusion de contenu, le web ou des serveurs d'impression pour traiter ces requêtes à court terme. 

###Qu’est ce que openAPI et quel est son intérêt ? 

OpenAPI est une norme de description des interfaces de programmation (API). La spécification OpenAPI définit un format de description ouvert et indépendant pour les services API. Plus particulièrement, OpenAPI permet de décrire, développer, tester et documenter des API conformes à l’architecture REST.

