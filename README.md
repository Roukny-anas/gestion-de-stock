# gestion-de-stock
## Introduction :

Le projet consiste à créer une application de gestion de stock en utilisant une approche orientée objet pour faciliter la maintenance et l'évolutivité du code. Les informations des produits et des utilisateurs seront stockées dans une base de données relationnelle. L'interface utilisateur sera conviviale pour faciliter l'utilisation de l'application.

Les principales fonctionnalités de l'application seront la création de comptes utilisateurs avec un nom d'utilisateur et un mot de passe, le stockage des informations des utilisateurs dans une table de la base de données, la connexion des utilisateurs avec leur nom d'utilisateur et leur mot de passe, l'affichage de la liste des produits avec leurs attributs (nom, description, prix unitaire, quantité en stock, seuil d'alerte de stock, date de dernière entrée en stock, date de dernière sortie de stock, image du produit), la recherche de produits par nom, prix unitaire, quantité et date de dernière entrée en stock.

Pour réaliser ce projet, nous utiliserons le langage de programmation Python pour l'implémentation, une base de données pour stocker les informations des produits et des utilisateurs, et la bibliothèque PyQT5 pour créer l'interface utilisateur conviviale.

## Developpement:
Diagramme cas d'utilisation 
![WhatsApp Image 2023-05-11 at 01 25 47 (1)](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/e0100b42-d795-4617-9d42-e08e7b7c5237)

Diagramme de class 
![WhatsApp Image 2023-05-11 at 01 25 47](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/d3a0baa9-390b-45b4-b9d6-b61e82c560cb)



![777](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/331c9056-bff6-47f2-962a-8fd88aa3bbfb)
Cette classe Python loginscreen est une définition pour une interface graphique d'écran de connexion utilisant PyQt5.

La méthode loginfunction récupère le nom d'utilisateur et le mot de passe entrés par l'utilisateur et les compare à une valeur d'authentification enregistrée en base de données. Si l'utilisateur entre des champs vides, un message d'erreur est affiché. Si les identifiants sont corrects, un message de réussite est affiché et la boîte de dialogue est fermée. Sinon, un message d'erreur est affiché.

La méthode gotoregistration affiche une nouvelle instance d'une interface graphique appelée registrationscreen en utilisant la méthode addWidget de l'objet Widget.

![22](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/f4592a1e-2289-4b7d-bccf-f274ef231564)
Cette partie de code correspond à une classe registrationscreen qui est une boîte de dialogue (QDialog).
La fonction registrationfunction est appelée lorsque le bouton pushButton est cliqué. Elle récupère les informations d'inscription de l'utilisateur à partir des champs de texte lineEdit et vérifie que les champs sont remplis. Elle vérifie ensuite si les mots de passe correspondent et si le mot de passe contient au moins 8 caractères et un caractère spécial. Enfin, si tout est valide, elle se connecte à une base de données SQLite, insère les informations de l'utilisateur et ferme la connexion.

La fonction gotologin est appelée lorsque le bouton pushButton_2 est cliqué. Elle crée une instance de la classe loginscreen et affiche la page de connexion en réduisant l'index de la page actuelle dans le widget Widget.


![1a](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/197b4db9-c411-477e-bce0-50458db423ac)

On a utilise la classe main pour la page d'admin.
si l'admin clique sur l'un des boutons il sera dirige vers la page souhaite.

![2](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/b891f775-867e-441f-8525-aa72e2bd0e64)

On a utilise la classe main pour la page d'utilisateur.
si l'utilisateur clique sur l'un des boutons il sera dirige vers la page souhaite.

![3](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/e2f3d9bb-f802-4bc7-b536-dc9adb873baf)

![4](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/a7f2f2ac-6361-466f-8d9f-b1f2d54c010c)

La classe search pour la page de recherche des produits par l'utilisateur.
la fonction gotomain2 sers a retourner vers la page d'admin s'il clique sur le bouton
retourner.
pour la fonction searchp:
*On fait la connection de la base de donnee.
*On lit la valeur d'un input(le nom a rechercher)
*On fait le controle de saisie sur l'input(si le nom est vide ou contient des caracteres ou des nombres)
on affiche un message d'erreur dans ce cas.
*On verifie si le nom ne figure pas dans la base de donne.(on affiche un message d'erreur dans ce cas)
*sinon on selectionne les champs de la ligne qui a le nom rentre dans la base de donnee et on les affiche
dans des output.

![5](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/83265ab4-266b-4598-add6-1d3d4d58f04b)

La classe displayall4 pour afficher tout les produits pour l'utilisateur.
On lit toute les lignes de la base de donnee et on les ajoute au table widget.

![6](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/78d2f5d1-5b51-45bc-afb2-6b1886b388fe)

La classe displayall3 pour afficher tout les produits pour l'admin avec le meme traitement de la classe 
precedente.

![7](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/af018c6d-3d7c-4e23-ac08-081e67000364)

La classe modifier pour la modification des produits par l'admin.
La fonction displayproduct:D'abord on affiche tous les produits stocke dans la base de donne dans une tabe widget.
La fonction gotomain2 pour retourner sur la page d'admin s'il clicque sur le bouton retourner.

![8](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/8ac16912-6548-42a2-8157-45a4a6b89c19)

La fonction onItemClicked pour remplir les input depuis la table widget apres l'appuie sur une ligne dans la table.
(Les lignes sont deja affichees)
La fonction edite qui lit les valeurs des inputs (qui sont remplis de la table) et apres la modification de ces lignes
on les modifie dans la base de donne et apres dans la table widget.

![9](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/5f1e4608-65b6-46a0-9808-e8fbff476611)

![10](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/5085ca1f-ffe8-491c-ae0d-d82718164b2e)

![11](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/9c912ee1-e780-4d92-95e6-17511283786e)

La classe delete pour supprimer les produits par l'admin.
La fonction displayproduct pour afficher les produits pour l'admin.
La fonction deleteproduct :
*sers a lire la valeur du nom a supprimer.
*Si le champ est vide on affiche un message d'erreur.
*Si le champ ne respecte pas les critaires(sans caracteres et sans nombres)
*Si le nom n'existe pas sur la base de donnee.
*Sinon on le supprime de la base de donnee et de la table widget.

![12](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/81626f39-22aa-4cb2-a58a-3601daf9ecfc)

![13](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/50df6739-6788-49b5-9e14-843fcc23918d)

![14](https://github.com/Roukny-anas/gestion-de-stock/assets/121769827/4cb49198-6b52-49e7-a91f-2bdac4f0861e)
La classe add pour l'ajout des produits par l'admin.
La fonction display2 affiche les produits deja ajoutes dans la base de donnee.
La fonction addproduct lit les champs des inputs et verifie si les champs sont vide ou ne respecte pas:
-Nom chaine sans caracteres sans nombre.
-Prix unitaire,Quantite et seuil d'alerte sont des nombres positif.
La fonction check_name verifie avans ajouter un produit si se nom se figure dans la base de donnee(le nom doit etre unique)
Si les champs verifient toute les critaires precedents on ajout le produit dans la base de donnee et dans la table widget.

## Conclusion :

Nous sommes satisfaits de notre application de gestion de stock qui répond aux exigences fonctionnelles établies dès le début du projet. Nous avons utilisé une approche orientée objet pour faciliter la maintenance et l'évolutivité du code, et stocké les informations des produits et des utilisateurs dans une base de données relationnelle. Nous avons également créé une interface utilisateur conviviale en utilisant la bibliothèque PyQT5.
