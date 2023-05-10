# gestion-de-stock
## Introduction :

Le projet consiste à créer une application de gestion de stock en utilisant une approche orientée objet pour faciliter la maintenance et l'évolutivité du code. Les informations des produits et des utilisateurs seront stockées dans une base de données relationnelle. L'interface utilisateur sera conviviale pour faciliter l'utilisation de l'application.

Les principales fonctionnalités de l'application seront la création de comptes utilisateurs avec un nom d'utilisateur et un mot de passe, le stockage des informations des utilisateurs dans une table de la base de données, la connexion des utilisateurs avec leur nom d'utilisateur et leur mot de passe, l'affichage de la liste des produits avec leurs attributs (nom, description, prix unitaire, quantité en stock, seuil d'alerte de stock, date de dernière entrée en stock, date de dernière sortie de stock, image du produit), la recherche de produits par nom, prix unitaire, quantité et date de dernière entrée en stock.

Pour réaliser ce projet, nous utiliserons le langage de programmation Python pour l'implémentation, une base de données pour stocker les informations des produits et des utilisateurs, et la bibliothèque PyQT5 pour créer l'interface utilisateur conviviale.

## Developpement:
![1](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/80084244-d576-480c-8253-ba02177d0f7a)
Cette classe Python loginscreen est une définition pour une interface graphique d'écran de connexion utilisant PyQt5.

La méthode loginfunction récupère le nom d'utilisateur et le mot de passe entrés par l'utilisateur et les compare à une valeur d'authentification enregistrée en base de données. Si l'utilisateur entre des champs vides, un message d'erreur est affiché. Si les identifiants sont corrects, un message de réussite est affiché et la boîte de dialogue est fermée. Sinon, un message d'erreur est affiché.

La méthode gotoregistration affiche une nouvelle instance d'une interface graphique appelée registrationscreen en utilisant la méthode addWidget de l'objet Widget.

![22](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/f4592a1e-2289-4b7d-bccf-f274ef231564)
Cette partie de code correspond à une classe registrationscreen qui est une boîte de dialogue (QDialog).
La fonction registrationfunction est appelée lorsque le bouton pushButton est cliqué. Elle récupère les informations d'inscription de l'utilisateur à partir des champs de texte lineEdit et vérifie que les champs sont remplis. Elle vérifie ensuite si les mots de passe correspondent et si le mot de passe contient au moins 8 caractères et un caractère spécial. Enfin, si tout est valide, elle se connecte à une base de données SQLite, insère les informations de l'utilisateur et ferme la connexion.

La fonction gotologin est appelée lorsque le bouton pushButton_2 est cliqué. Elle crée une instance de la classe loginscreen et affiche la page de connexion en réduisant l'index de la page actuelle dans le widget Widget.

## Conclusion :

Nous sommes satisfaits de notre application de gestion de stock qui répond aux exigences fonctionnelles établies dès le début du projet. Nous avons utilisé une approche orientée objet pour faciliter la maintenance et l'évolutivité du code, et stocké les informations des produits et des utilisateurs dans une base de données relationnelle. Nous avons également créé une interface utilisateur conviviale en utilisant la bibliothèque PyQT5.
