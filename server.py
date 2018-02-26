# -*- coding: utf-8 -*-
# Created by Lambert ROSIQUE

from flask import Flask, session, redirect, url_for, escape, request, jsonify
import re
app = Flask(__name__)

def creer_page_html(num_defi, title_defi, content):
    return '''
        <!DOCTYPE html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
            body {
                font-family: "Lato", sans-serif;
            }
            
            .sidenav {
                height: 100%;
                width: 200px;
                position: fixed;
                z-index: 1;
                top: 0;
                left: 0;
                background-color: #111;
                overflow-x: hidden;
                padding-top: 20px;
            }
            
            .sidenav a {
                padding: 6px 6px 6px 32px;
                text-decoration: none;
                font-size: 25px;
                color: #818181;
                display: block;
            }
            
            .sidenav a:hover {
                color: #f1f1f1;
            }
            
            .main {
                margin-left: 250px; /* Same as the width of the sidenav */
            }
            
            @media screen and (max-height: 450px) {
              .sidenav {padding-top: 15px;}
              .sidenav a {font-size: 18px;}
            }
            </style>
           <title>PPGA</title>
           <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
        </head>
        <body>
            <div class="sidenav">
              <a href="introduction">I. Introduction</a>
              <a href="1">1) Installer Python</a>
              <a href="2">2) Gestion de packages</a>
              <a href="3">3) IDE Spyder</a>
              <a href="4">4) Appels HTTP</a>
            </div>
            '''+'''
            <div class="main" style="width: 1200px;">
            <h1>PPGA Python Programing Game Adventure ! {}</h1>
            <h2>{}</h2>
            {}
            </div>
        </body>
            '''.format(num_defi,title_defi, content)

page_introduction = creer_page_html("", "Les présentations", """
                         <p><ul><li>Bonjour, je m'appelle Lambert ROSIQUE, data scientist et passionné d'intelligence artificielle (vous pouvez d'ailleurs me retrouver sur Pensée Artificielle)</li>
                          <li>Nous n'allons pas aborder ces thématiques ici, puisque notre but est... d'apprendre les rudiments du Python ensemble (en s'amusant !)</li>
                          <li>Comme vous le verrez, il n'y a pas énormément de pages (4 pages de tutoriel, 2 de conclusion, 7 de "cours"), donc tout devrait être terminé d'ici 1h (et vous pourrez alors marquer sur votre CV expert... Ou mieux, vous pourrez suivre et participer à nos TP d'intelligence artificielle en Python !!!)</li>
                          <li>Pré-requis : connaître les principes de programmation, voire programmer en Java car on ne reviendra pas sur les concepts !</li>
                          <li>Bon courage, on se retrouve à la fin :)</li>
                          <li>PS : je suis très nul en design et en html/css, ne m'en voulez pas, ce n'était pas l'objectif de ce cours</li></ul></p>
                         <p>Pour continuer, <a href="1">cliquez ici</a></p>""")     
page_1 = creer_page_html("", "Il faut bien commencer quelque part...", """
                         <p><ul><li>Téléchargez et installez <a href='https://www.python.org/downloads/windows/'>Python</a> (si ce n'est pas déjà fait)</li>
                             <li>Ouvrez une fenêtre de commande et tapez "python"</li>
                             <li>Essayez de saisir les instructions suivantes :
                                 <ul><li>3 + 7</li><li>10 / 3</li><li>x = 5</li><li>x</li><li>x += 3.2</li><li>x</li><li>x == 1</li><li>s1 = 'toto'</li><li>s2 = "toto"</li><li>s1 == s2</li></ul></li>
                             <li>Bravo ! Vous pouvez faire des maths avec la commande Windows !</li></ul></p>
                         <p>Pour continuer, <a href="2">cliquez ici</a></p>""")     
page_2 = creer_page_html("", "Les packages (courage, les TP arrivent bientôt !)", """
                         <p><ul><li>Un gestionnaire de package similaire à <i>npm</i> et <i>maven</i> s'est automatiquement installé avec Python : <b>pip</b></li></ul></p>
                         <p><ul><li>(<b>très facultatif</b>) Il existe un package qui permet de créer des environnements de travail virtuels, puis y installer des librairies (version spécifique)</li>
                                 <ul><li>Dans la console windows, saisissez : <g>pip install virtualenv</g> (attention si vous avez un proxy il faut passer par ntlm)</li>
                                  <li>ATTENTION : si vous êtes sur un réseau entreprise, il n'est pas dit que vous puissiez lancer virtualenv (à cause des droits sur votre ordinateur)!</li>
                                  <li>Une fois virtualenv installé, pour créer un nouvel environnement faites (dans le dossier de votre projet) : <i>virtualenv ppga</i></li>
                                  <li>Lancez ensuite toujours dans la console <i>ppga/bin/activate</i></li></ul></ul></p>
                        <p><ul><li>On va maintenant installer l'IDE Spyder pour coder du Python (équivalent d'Eclipse) : <b>pip install spyder</b></li></ul></p> 
                        <p>Pour continuer, <a href="3">cliquez ici</a></p>""")
page_3 = creer_page_html("", "Spyder et bientôt appels de service (enfin !)", """
                         <p><ul><li>Pour lancer spyder, dans la console, écrivez <b>spyder3</b></li></ul></p>
                         <p><img src="http://i63.tinypic.com/33mwo6s.png" alt="Smiley face" height="600" width="800"></img></p>
                         <p><ul><li>A gauche vous avez l'espace où coder. Ecrivez du code python : x=3, sélectionnez-le et exécutez-le en faisant CTRL + ENTER</li>
                                <li>En bas à droite, le code exécuté vient d'apparaitre. Tout ce que vous exécutez reste en place (à l'inverse de Java), <b>c'est une console interactive</b> ! Dans la console, tapez x puis ENTER</li>
                                <li>Enfin, à droite vous avez l'explorateur de fichiers et celui de variables. Dans les variables, vous retrouverez tout ce qui est exécuté et stocké (sous réserve que le type soit simple), dont votre x. Vous pouvez d'ailleurs le modifier et remplacer le 3 par 4.</li>
                                <li><b>N'hésitez pas à expérimenter avant de passer à la suite</b></li></ul></p> 
                        <p>Pour continuer, <a href="4">cliquez ici</a></p>""")
page_4 = creer_page_html("", "Appels HTTP avant de commencer", """
                         <p><ul><li>Pour pouvoir résoudre les exercices qui vous seront proposés (oui vous allez travailler pour apprendre !), on va devoir faire des appels HTTP au serveur, en Python</li>
                             <li>Le package pour les appels http est <a href="http://docs.python-requests.org/en/master/">requests</a> : saisissez dans la console <b>pip install requests</b>(après avoir fermé Spyder)</li>
                             <li>Lancez ensuite Spyder puis exécutez le bloc de code suivant :</li>
                             <li><b>Remarque pour toute la suite : si le serveur ne répond pas immédiatement à une requête HTTP, actualisez une page web qui appelle le serveur : parfois la console a du mal à envoyer/récupérer les données</b></li>
                         </ul></p> 
                         <p><textarea rows="15" cols="500">
# Import de la librairie pour faire des requêtes HTTP
import requests, json

# URL du serveur en Flask (Python) pour le PPGA (à changer !)
url_server = "http://127.0.0.1:5000/"

# Exemple d'appel GET, avec désérialisation de la réponse et récupération d'un paramètre reçu
g = requests.get(url_server+"examples")
g_json = json.loads(g.text)

print(g_json['response'])

# Exemple d'appel POST, avec envoie d'information
###Finalement j'ai changé d'avis, vous trouverez bien comment faire... (essayez au moins le GET)
###Remarque : vous n'avancerez pas sans essayer ;)
</textarea></p>""")
page_42 = creer_page_html("", "Règles et première mission (Gl&Hf !)", """
                         <p><h3> Disclaimer (quoi que ça veuille dire)</h3></p>
                         <p><ul><li>Tout d'abord merci d'essayer de ne pas (trop) casser le serveur, il est codé en Python rapidement (le but était de fournir un outil pédagogique simple)</li>
                          <li>Pour toute question ou remarque, n'hésitez pas à vous adresser à Lambert ROSIQUE</li></ul></p>
                         <p><h3>Règles</h3></p>
                         <p><ul><li>Internet tu utiliseras</li>
                          <li>Les épreuves tu ne cheateras</li>
                          <li>HTML : les URL tu remplaceras</li>
                          <li>HTTP : les services tu appelleras</li>
                          <ul><li>Avec "message" tu communiqueras</li>
                              <li>Avec "response" tu enchaineras</li>
                              <li>Avec "mdp" l'énigme finale tu débloqueras</li></ul>
                          <li>Python tu sauras !</li></ul></p>
                         <p><h3>Première épreuve !</h3></p>
                         <p><ul><li>
                             On va commencer par utiliser les fonctions mathématiques : allez à la page <a href="3.14">3.14</a>
                         </li></ul></p>
                         """)
page_314 = creer_page_html("", "Opérations mathématiques, fonctions, variables", """
                         <p><h3>Des Variables et des Mathématiques</h3></p>
                         <p><ul><li>Elles s'écrivent <b>nom_variable = valeur</b></li>
                         <li>Remarque : on ne précise pas le type (comme en Javascript), et on utilise un style d'écriture avec des _ et des minuscules</li>
                         <li>Attention : certains mots-clés sont réservés ! and, del, from, none, true, as, elif, global, etc...</li>
                         <li>Les nombres peuvent être écrits comme entiers (int, long) x=3 ou comme float x=3.14 ou comme complex : vous pouvez connaitre le type en faisant <b>type(x)</b></li>
                         <li>Pour afficher la valeur d'une variable, vous pouvez la sélectionner et faire CTRL+ENTER (via Spyder) ou écrire <b>print(x)</b> et exécuter le code</li>
                         <li>Enfin, le module <b>math</b> (installé par défaut) fournit beaucoup de méthodes pratiques comme ceil, floor, pi, exp; log, cos...</li>
                         <li>Bonus : pour inverser deux valeurs a et b, faites <b>a,b = b,a</b></li>
                         <li>Bonus : pour initialiser deux variables à la même valeur, vous avez <b>x = y = 1</b></li>
                         </ul></p>
                         <p style="color:red"><b>Exercice</b> = Envoyez à <i>exercices/maths</i> :
                           <ul><li><i>la somme divisée par 2 entre le périmètre et l'aire d'un cercle de rayon 3cm (arrondie à 2 chiffres après la virgule)</i></li>
                           </ul>
                         </p>
                         <p><h3>Les Fonctions</h3></p>
                         <p><ul><li>Contrairement à beaucoup de langages de programmation, en Python, l'indentation entre les blocs de code a une importance !</li>
                          <li>Il n'y a donc pas besoin d'accolades, il faudra simplement mettre ":" et indenter correctement ensuite</li>
                          <li>Pour déclarer une fonction, on utilise la syntaxe : <b>def ma_fonction(mon_parametre):</b></li>
                          <li>Par exemple 
                          <p><textarea rows="2" cols="500">
def fct_carre(x):
    return x**2</textarea></p></li>
                          <li>Puis pour l'appeler : fct_carre(3)</li>
                          <li>Vos fonctions peuvent être récursives</li>
                          <li>Bonus : vous pouvez nommer les paramètres et leur donner des valeurs par défaut</li>
                          <li>Par exemple, 
                          <p><textarea rows="8" cols="500">
import math

def fct_log(x, base=10):
    return math.log(x,base)

print("Log(10) = ",fct_log(10))
print("Log(2) en base e = ",fct_log(2,base=math.e))
print("Log(2) en base 2 = ",fct_log(2,base=2))</textarea></p></li>
                          <li>Bonus : vous pouvez créer des fonctions attendant un nombre inconnu de paramètres grâce à la syntaxe <b>def ma_fct(*parametres):</b></li>
                         </ul></p>
                         <p style="color:red"><b>Exercice</b> = Envoyez à <i>exercices/fonction</i> :
                           <ul><li><i>le résultat du calcul suivant (valeurs par défaut des paramètres 1 et 1) :</i> <b>puissance(10, exposant=0.5, arrondi=3) + puissance(3.55)</b></li>
                           </ul>
                         </p>
                         """)
page_siseulement = creer_page_html("", "Booléens, conditions et boucles", """
                         <p><h3>Booléens</h3></p>
                         <p><ul><li>Il n'y a pas grand chose à en dire, à part qu'il faut mettre une majuscule : <b>True</b> et <b>False</b></li>
                          <li>Le "null" de Java est, en Python, un <b>None</b></li></ul></p>
                          <li>Essayez les codes suivants :
                             <p><textarea rows="8" cols="500">
b = True
b == False
4 == 4
b+1
not b
4 > 2
b == None
None == None</textarea></p></li></ul></p>
                          <p><h3>Conditions</h3></p>
                          <p><ul>
                           <li>Pour écrire une condition, on utilise <b>if condition_1: ... elif condition_2: ... else: ...</b> (en indentant bien évidemment les sous-blocs)</li>
                           <li>Par exemple (à jouer 3 fois) 
                            <p><textarea rows="15" cols="500">
x=0
def test_boucle(x):
    if x == 0:
        print('if')
        x += 3
    elif x < 4:
        print("elif")
        x += 1
    else:
        print('else')
    return x

x = test_boucle(x)
x = test_boucle(x)
x = test_boucle(x)</textarea></p></li></ul></p>
                           <li>Les mots-clés pour lier les conditions sont <b>and, or, not</b></li>
                           <li>Par exemple : <b>3 == 2 or 3 > 2</b></li>
                           <li>Bonus : la syntaxe ternaire est <b>resultat_1 if condition else resultat_2</b></li>
                          </p></ul>
                          <p style="color:red"><b>Exercice</b> = Envoyez à <i>exercices/condition</i> :
                           <ul><li><i>la factorielle de 8 (écrire la fonction de manière récursive)</i></li>
                           </ul>
                          </p>
                          <p><h3>Boucles</h3></p>
                          <p><ul><li>La boucle while s'écrit <b>while condition:</b></li>
                           <li>Par exemple 
                           <p><textarea rows="6" cols="500">
nb=9
i=0

while i<10:
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1</textarea></p></li>
                           <li>La boucle for ne s'applique qu'à des éléments d'une séquence (liste...) : <b>for element in sequence:</b></li>
                           <li>Astuce : la méthode "range" crée une liste d'entiers successifs. <b>range(10)</b> va donc créer la "liste" 0, 1, 2, 3, ..., 9.</li>
                           <li>Par exemple 
                           <p><textarea rows="2" cols="500">
for i in range(10):
    print(i)</textarea></p></li>
                           <li>Astuce : la liste peut être mise à l'envers grâce à la fonction reversed, comme dans <b>reversed(range(10))</b></li>
                           <li>Astuce : vous pouvez choisir les bornes (10 et 3) ainsi que l'incrément de range avec <b>range(10,3,-1)</b></li>
                           <li>Bonus : vous avez accès aux mots-clés <b>break et continue</b></li></ul></p>
                          <p style="color:red"><b>Exercice</b> = Envoyez à <i>exercices/boucle</i> :
                           <ul><li><i>la somme des factorielles de 1 à 7 (écrire la fonction à l'aide d'une boucle for (pour la somme) et d'une boucle while (pour la factorielle))</i></li>
                           </ul>
                          </p>
                         """)
page_dico = creer_page_html("", "Chaînes de caractères, listes et dictionnaires (le plus important)", """
                         <p><h3>Chaînes de caractères</h3></p>
                         <p><ul><li>Vous pouvez soit les encadrer par des doubles quotes <b>"chaine"</b> soit par des simples <b>'chaine'</b>, et si vous <b>triplez</b>, vous pouvez écrire sur plusieurs lignes !</li>
                          <li>Les commentaires Python s'écrivent avec <b>#</b> (on ne peut commenter qu'une ligne à la fois malheureusement)</li>
                          <li>Les tests se font comme pour tout le reste avec <b>==</b></li>
                          <li>Par exemple <b>'chaine' == "chaine"</b></li>
                          <li>Au niveau des méthodes, vous avez accès aux méthodes habituelles dont len(ma_chaine) pour avoir la longueur, des regex, split, join (pour fusionner les éléments de la liste), etc... Les substring s'utilisent grâce aux listes (voir après)</li>
                          <p><h3>Listes</h3></p>
                          <li>Utilisées quasiment partout (de manière transparente ou non), les listes Python sont très simples d'utilisation</li>
                          <li>Syntaxe : <b>ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]</b></li>
                          <li>Pour récupérer un élément, il suffit de donner sa position : <b>ma_liste[0]</b></li>
                          <li>Pour en connaitre la longueur, <b>len(ma_liste)</b></li>
                          <li>Pour ajouter un élément à la fin <b>ma_liste.append(10)</b></li>
                          <li>Et surtout pour en extraire des sous-listes, on utilise la notation étendue d'un seul élément (appelée "slice") : <b>ma_liste[index1:index2]</b> qui nous renverra tous les éléments entre ces positions</li>
                          <li>Par exemple, ma_liste[3:6] renvoie [4,5,6]</li>
                          <li>Astuce : vous pouvez mettre des index <b>-1</b>, -2... pour compter à l'envers !!! Et enlever index1 ou 2 pour utiliser une <b>wildcard</b> !!!</li>
                          <li>Par exemple, ma_liste[-1] renvoie 9, ma_liste[2:] renvoie [3,4,5,6,7,8,9]...</li>
                          <li>Que renvoient : <ul><li>ma_liste[-2:]</li><li>ma_liste[:-2]</li><li>ma_liste[-1:-1]</li><li>ma_liste[6:3]</li><li>ma_liste[-6:-3]</li></ul></li>
                          <li>Encore mieux : vous pouvez réaliser des opérations sur les éléments des listes, voire directement sur les listes !</li>
                          <li>Essayez <b>ma_liste2 = 2*ma_liste</b> (concaténation) et <b>ma_liste3 = [2*a for a in ma_liste if a%2 == 0]</b></li>
                          <li>Maintenant, essayez <b>ma_liste4 = [a+b for a,b in zip(ma_liste,ma_liste3)]</b> ... Incroyable n'est-ce pas ?</li>
                          <li>Vous pouvez insérer dans la liste grâce à append, insert et extend. Vous pouvez supprimer grâce à del et remove. La méthode enumerate permet de parcourir la liste en gardant trace de la position courante !</li>
                          <li>Par exemple, 
                          <p><textarea rows="3" cols="500">
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, elt in enumerate(ma_liste):
    print("À l'indice {} se trouve {}.".format(i, elt))</textarea></p></li>
                          <li>Les <b>tuples</b> renvoyés par enumerate <b>(a,b)</b> sont comme des listes sauf qu'on ne peut pas les modifier ensuite. Vous l'avez utilisé en faisant a,b = b,a (les parenthèses sont facultatives)</li></ul></p>
                          <p style="color:red"><b>Exercice</b> = Envoyez à <i>exercices/liste</i> le résultat final de l'algorithme suivant :
                           <ul><li><i>Prendre le titre de la page (Chaînes de ...) et n'en garder que les caractères entre le 6e en partant du début et le 8e en partant de la fin</i></li>
                               <li><i>Couper cette chaîne en deux morceaux a et b</i></li>
                               <li><i>inverser la position de a et b (vous obtenez donc ba)</i></li>
                               <li><i>inverser le sens de lecture de b uniquement</i></li>
                           </ul>
                          </p>
                          <p><h3>Dictionnaires</h3></p>
                            <p><ul>
                        	<li>Ils sont extrêmement pratiques et permettent de résoudre beaucoup de problèmes en très peu de lignes de code (ils sont équivalents aux hashmap de Java)</li>
                        	<li>Syntaxe : <b>mon_dict = {'nom':'Rosique', 'prenom':'Lambert', 'site':'Pensée Artificielle', 'age':28}</b></li>
                        	<li>Pour récupérer un élément, il suffit alors de faire <b>mon_dict['prenom']</b></li>
                        	<li>Astuce : vous pouvez mettre par exemple des tuples en clé de votre dictionnaire</li>
                        	<li>Pour supprimer une entrée, vous pouvez utiliser del ou pop</li>
                        	<li>Bonus : si vous ne mettez pas les : dans votre dictionnaire, vous créez un <b>set</b> set = {'nom','prenom','site','age'}</li>
                        	<li>Astuce : Vous pouvez également stocker des fonctions !!! operations = ['addition':addition] (où addition a été défini comme une somme de 2 nombres). Vous pouvez alors appeler operations['addition'](3,5) et obtenir 8</li>
                        	<li>Attention : les dictionnaires n'ont pas d'ordre ! Si vous parcourez les clés avec <b>for cle in mon_dict</b>, les données  ne remonteront pas comme on l'a créé (elles seront dans l'ordre alphabétique). Pour parcourir les valeurs, faites <b>for val in mon_dict.values()</b>. Enfin, vous pouvez obtenir les deux en même temps grâce à <b>mon_dict.items()</b></li>
                        	<li>Bonus : Les paramètres nommés sont en réalité stockés dans un dictionnaire pour vos fonctions. Au lieu de mettre 1 *, vous en mettez 2 (nombre inconnu de params nommés) et les récupérez dans le dico !</li>
                        	<li>Par exemple, <b>def ma_fct(**params_nommes):</b> aura ses paramètres nommés dans <b>params_nommes</b></li></ul></p>
                           <p style="color:red"><b>Exercice</b> = Envoyez à <i>exercices/dico</i> le dictionnaire complet suivant :
                            <ul><li><i>Les caractères (lettres non accentuées uniquement) et leurs fréquences de la phrase suivante (tout en minuscule) :</i></li>
                             <li><i>PPGA (Python Programing Game Adventure), créé en 42 minutes (ou pas), m'a rendu apte à faire de la data science et de l'intelligence artificielle en Python... En tout cas, on l'espère !</i></li>
                             <li><i>ATTENTION : vous ne devrez pas renvoyer l'object "dico" mais repr(dico) ! De plus, les clés devront être ajoutées dans l'ordre ALPHABETIQUE (sinon la solution sera refusée)</i></li>
                            </ul>
                           </p>
                           <p><ul><li><i>ASTUCE (à ne lire qu'après avoir cherché sa solution !)</i></li>
                                <li><i>Vous pouvez donner une valeur par défaut...</i></li>
                                <li><i>Encore mieux (2e solution) : vous pouvez utiliser la syntaxe de remplissage vue avec les listes...</i></li>
                           </ul>
                           </p>
                        """)
page_objection = creer_page_html("", "Les exceptions (qui font peur)", """
                         <p><ul><li>Enfin un cours facile ! Commencez par faire un petit 1/0 dans la console :)</li>
                                <li>La syntaxe des try catch est la suivante : <b>try: ... except: ... else: ... finally: ...</b></li>
                                <li>Remarque : except peut prendre le type de l'erreur et même lui donner un alias : except TypeError:, except TypeError as te:</li>
                                <li>Remarque : le else n'est quasiment jamais utilisé. Il sert à mettre le code exécuté s'il n'y a pas d'exception (dans la pratique on met dans le try ou en dehors)</li>
                                <li>Bonus : le mot-clé <b>pass</b> permet de continuer (dans un except notamment), ce qui n'est jamais très pertinent...</li>
                                <li>Vous pouvez mettre dans le code des <b>assert</b> ! (on récupère une AssertionError si elle est fausse)</li>
                                <li>Pour lever une exception, on utilise <b>raise TypeDeLException("message à afficher")</b></li>
                                <li>Exemple récapitulatif : 
                                   <p><textarea rows="24" cols="500">
# Récupération de l'année saisie à la console
annee = input("Saisissez une année supérieure à 0 :")

try:
    # Conversion en int (peut crash si on met des lettres)
    annee = int(annee)
    
    # Vérifications de l'année
    assert annee != 0
    
    # Deuxième vérification
    if annee > 0:
       print('OK')
    else:
        raise ValueError("negative !")
        
except ValueError as ve:
    print('value!',ve)
    
except AssertionError:
    print('assert error')
    
finally:
    print('merci pour votre aide')</textarea></p></li>
                                <li>Bonus : <b>Exception</b> catch absolument tout</li>
                                <li>Bonus : pour connaitre le type de l'exception (on verra pourquoi dans le prochain cours), faites : <b>print(type(e).__name__)</b>
                            </ul></p>
                          <p style="color:red"><b>Exercice</b> = Envoyez à <i>exercices/finally</i> (ne criez pas victoire, c'est l'avant dernier cours et non le dernier) le type des exceptions suivantes (à mettre dans une : liste = [type1,type2,type3] et à envoyer sous la forme repr(liste)) :
                            <ul><li><i>Enlevez la condition d'arrêt de votre factorielle récursive : que se passe-t-il ?</i></li>
                            <li><i>Ecrivez une fonction qui ajoute 1 à l'entier qu'on lui donne. Envoyez une liste à cette fonction</i></li>
                            <li><i>Enfin, déclarez une variable locale dans une fonction puis affichez-la en dehors. ATTENTION : n'oubliez pas que vos variables restent (donc si vous l'appelez 'phrase', il n'y aura pas d'erreur (si vous avez utilisé la variable phrase plus haut)...)</i></li>
                            </ul>
                           </p>
                         """)
page_weirdo = creer_page_html("", "Héritage, décorateurs, et autres fonctionnalités bizarres", """
                         <p><ul><li>Le temps qu'il nous reste pour boucler cette "mini" formation étant presque alloué (je ne paie pas les heures sup que vous faites), on va lister plusieurs fonctionnalités bien pratiques et vous pourrez expérimenter comme bon vous semble</li></ul></p>
                         <p><h3>Classes et fonctions spéciales</h3></p>
                         <p><ul><li>Pour définir une classe, on utilise <b>class Personne:</b></li>
                          <li>Qui doit contenir au moins un constructeur: <b>def __init__(self):</b></li>
                          <li>Pour désigner les éléments de la classe (attributs), on utilise donc <b>self</b></li>
                          <li>Quelques fonctions sont spéciales en Python et sont entourées de double underscore. Elles ont pour particularité d'être appelées automatiquement
                           <ul><li>__init__ : construteur d'un objet</li>
                            <li>__del__ : à la destruction de l'objet</li>
                            <li>__repr__ : change la manière dont est affiché un objet lorsqu'on l'appelle directement (sans print)</li>
                            <li>__str__ : idem mais pour la méthode print (et la méthode str qui convertit en chaîne)</li>
                            <li>__getattr__ : pour changer les accès aux attributs (par exemple si un attribut n'existe pas, que faire)</li>
                            <li>__setattr__ : similaire pour setter</li>
                            <li>__delattr__ : similaire pour supprimer</li>
                            <li>etc... par exemple pour les conteneurs ([]) : getitem, setitem, delitem, contains (pour le "in"), len (pour la longueur) --> vous pourriez donc faire en sorte que liste[1] renvoie le 0ème élément de la liste !</li>
                            <li>Pareil pour les mathématiques, vous pouvez redéfinir les opérations : add, sub, floordiv, etc... qui surchargent donc les symboles correspondants +, -, ..., iadd pour +=...</li>
                            <li>Idem pour les comparateurs (eq, ne, gt, ge, lt, le)</li>
                            <li>Enfin pour la sérialisation avec getstate (de Pickle) etc...</li>
                            <li>Pour plus de détails (il y en a d'autres), la lecture d'un cours complet sur le sujet est indispensable !</li>
                          </ul></li>
                          <li>Exemple : 
                              <p><textarea rows="17" cols="500">
class Person:

    # Constructeur
    def __init__(self, nom='Ori'):
        self.nom = nom

    # Surcharge du "+"
    def __add__(self,radd):
        self.nom = self.nom+' et '+radd.nom
        return self.nom

# Instantiation de 2 objets
ori = Person()
naru = Person(nom='Naru')

# La somme redéfinit ori !
print(ori + naru)</textarea></p></li>
                          <li>Vous pouvez créer des fonctions dans vos classes (sans les __ sauf pour les spéciales), en pensant bien à passer self en argument</li>
                          <li><b>self</b> est vraiment important, ne le raccourcicez pas et ne l'oubliez pas</li>
                          <li>Remplacez self par <b>cls</b> pour que la méthode soit static et travaille donc sur la classe et non l'instance !</li>
                          <li>Bonus : les attributs de classe sont également possibles, en les mettant en dehors du __init__ (donc tout en haut)</li>
                         </ul></p>
                         <p><h3>Introspection</h3></p>
                         <p><ul>
                           <li><b>dir</b> permet d'afficher les attributs et méthodes d'un objet. Par exemple, dir(toto)</li>
                           <li>Attribut spécial : après les fonctions spéciales, on a la même chose pour les attributs (créé automatiquement par Python)</li>
                           <li>Vous avez donc <b>__dict__</b> qui renvoie sous forme de dictionnaire les attributs et leurs valeurs d'un objet : toto.__dict__</li>
                           <li>Il y en a d'autres donc regardez en détail</li>
                         </ul></p>
                         <p><h3>Propriétés et résumé</h3></p>
                         <p><ul>
                           <li>En Python, par défaut, tout est public (les get/set sont automatiques)</li>
                           <li>Si vous voulez changer les get/set, on ne parle plus d'un attribut mais d'une <b>propriété</b>. Elle est déclarée comme un attribut mais commence par un underscore _</li>
                           <li>Ensuite, vous avez accès aux méthodes def _get_mapropriete(self): et def _set_mapropriete(self,val):</li>
                           <li>Enfin, il faut préciser à Python que cet attribut est une propriété grâce à la ligne : <b>genre = property(_get_genre,_set_genre)</b></li>
                           <li>La propriété reste accessible de manière naturelle : obj.mapropriete mais cela appellera bien vos deux méthodes</li>
                           <li>Exemple :
                               <p><textarea rows="28" cols="500">
class PersonRobot:
    # Attribut de classe
    matiere = 'métal'
    
    # Constructeur
    def __init__(self, nom='toto'):
        self.nom = nom
        # Le genre est une propriété
        self._genre = "robot"

    # Getter du genre
    def _get_genre(self):
        return self._genre

    # Setter du genre
    def _set_genre(self, val):
        print("Dé-so-lé la fffonction n'est pas imppp-lémentée")

    # Genre est déclaré comme propriété
    genre = property(_get_genre,_set_genre)

# Définition d'un objet
moi = PersonRobot(nom='Moi')
moi.genre = "humain"

print("Mon genre a-t-il changé ? ",moi.genre == "humain")
print("De quoi sont fait tous les robots ? ",PersonRobot.matiere)</textarea></p></li>
                         </ul></p>
                         <p><h3>Héritage</h3></p>
                         <p><ul>
                           <li>Pour l'héritage simple, lorsque vous définissez votre classe, précisez entre parenthèses de qui elle hérite : <b>class B(A):</b> (B hérite de A)</li>
                           <li>Dans ce cas, lorsqu'on appellera une méthode ou un attribut sur B, il cherchera d'abord dans B puis remontera à A. Si vous avez redéfini l'init, les attributs de A non copiés dans B seront donc perdus ! Il faut donc mettre dans l'init de B : <b>A.__init__(self, valeurs)</b></li>
                           <li>Remarque : toutes les classes créées héritent de "object"</li>
                           <li>Astuce : <b>isinstance</b> vous dit si un objet vient d'une classe ou de ses filles. <b>issubclass</b> vérifie si une classe est sous-classe d'une autre</li>
                           <li>Pour l'héritage <b>multiple</b> (oui, vous m'avez bien lu), la syntaxe est <b>class C(A,B):</b></li>
                           <li>Le principe est le même que tout à l'heure : les méthodes sont cherchés dans C puis A puis B</li>
                           <li>Bonus : ce principe marche pour les exceptions ! (il faut les faire hériter de l'exception voulue)</li>
                         </ul></p>
                         <p><h3>Décorateurs</h3></p>
                         <p><ul>
                           <li>Vous les connaissez de Java, les décorateurs servent à modifier une fonction "à la volée" en en appelant une autre avant, après...</li>
                           <li>Au-dessus de votre déclaration de fonction, ajoutez <b>@mon_decoracteur</b> où mon_decorateur est une fonction prenant en paramètre une fonction. Cela revient donc à faire un appel "mon_decorateur(ma_fonction)" si on ne passe pas par l'annotation</li>
                           <li>Si le décorateur retourne une fonction (que l'on déclare dans le décorateur) alors on peut contrôler ce qu'il se passe avant ou après l'exécution</li>
                           <li>Vous pouvez aussi passer des paramètres à vos décorateurs</li>
                           <li>Pour plus de <a href="https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-decorateurs">détails</a></li>
                           <li><b>Dans la pratique, ils servent pour le pattern Sigleton et pour vérifier les paramètres envoyés à une fonction</b></li>
                         </ul></p>
                         <p><h3>Métaclasses</h3></p>
                         <p><ul>
                           <li>Pour conclure, les métaclasses sont le moyen de générer des classes à partir d'autres classes ou dynamiquement</li>
                           <li>Une fois encore, leur utilisation reste à la marge et vous êtes invités à <a href="https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-metaclasses">creuser</a> si ça vous intéresse</li>
                         </ul></p>
                         <p><h3>Exercice</h3></p>
                         <p><ul>
                           <li style="color:red">Cette partie était très dense, donc le mieux ça reste de vous laisser expérimenter librement (comme on l'a dit). Envoyez 'ready' en message à exercice/heritage quand vous serez prêts à continuer</li>
                           <li>Remarque : un aigle est à la fois un animal et un oiseau, qui vit comme "tous" les animaux, pond (ou vole) comme "tous" les oiseaux, mais qui est le seul à représenter les USA (il a donc les attributs qui découlent de ses capacités, à vous de vous inventer votre TP de 3 classes !).</li>
                         </ul></p>
                         """)
page_the_end = creer_page_html("", "Fin du calvaire (et statistiques hihi)", """
                         <p><ul><li><b>FELICITATIONS !!! Vous avez terminé le PPGA v0.000001 !</b></li>
                          <li>J'espère que ça vous aura plu et pas pris trop de temps</li>
                          <li>Si vous avez des suggestions ou remarques, vous pouvez contacter directement Lambert ROSIQUE</li>
                          <li>Dans tous les cas, je ferai peut-être une autre version dédiée à la data science / deep learning / intelligence artificielle, en mode petite présentation et exercices (comme là) pour que tout le monde ait le même background :)</li>
                          <li>Pour aller plus loin, je vous encourage à regarder tout ce qu'on a pu rater, dont la gestion de fichiers (ouvrir, fermer, enregistrer, c'est très simple), les serveurs/appels de services (regardez mon "beau" code flask), les regex, les interfaces graphiques (Python sert beaucoup à créer des sites web ne l'oublions pas), les threads, les programmes qui se réécrivent en temps réel (oui ! vous pouvez, comme en assembleur, modifier le code à la volée et même changer de ligne), les tests unitaires, les matrices (listes de listes)...</li>
                          <li>Vous pouvez lire aussi le tutoriel du Site du Zéro (Openclassroom pour les jeunes) : https://openclassrooms.com/courses/apprenez-a-programmer-en-python/premiere-approche-des-classes</li>
                          <li>Et garder dans un coin la feuille de <b>cheat</b> que j'aime bien : http://www.datasciencefree.com/python.pdf</li>
                          <li>A très bientôt j'espère</li>
                          <li><b>Votre webmaster de penseeartificielle.fr préféré (suivez-nous sur Facebook et Twitter pour moins de pubs dans les outils qu'on offre et plus de news, tutos, tests, partages... :p)</b></li></ul></p>
                          <p style="color:red"><b>Exercice</b> = Allez sur la page formée par tous les mots-de-passe concaténés pour avoir TOUTES les solutions ! C'est cadeau !
                            <li>Vous n'avez vraiment pas trouvé ? Bon d'accord, essayez de demander de l'aide à <i>exercices/help-i-am-desperate</i> en donnant votre prénom dans message !</li>
                            </ul>
                           </p>
                           <p><b>Rappel de toutes les pages :</b>
                           <ul><li><a href="42">42</a> : Règles et première mission (Gl&Hf !)</li>
                            <li><a href="3.14">3.14</a> : Opérations mathématiques, fonctions, variables</li>
                            <li><a href="siseulement">siseulement</a> : Booléens, conditions et boucles</li>
                            <li><a href="dico">dico</a> : Chaînes de caractères, listes et dictionnaires (le plus important)</li>
                            <li><a href="objection!">objection!</a> : Les exceptions (qui font peur)</li>
                            <li><a href="weirdo">weirdo</a> : Héritage, décorateurs, et autres fonctionnalités bizarres</li>
                            <li><a href="the_end">the_end</a> : Fin du calvaire (et statistiques hihi)</li>
                            <li>Comme si on allait vous donner le lien : Solutions (parmi tant d'autres) (bon <a href="gg_vous_avez_termodynamique_sans_h">ok</a> mais c'était mieux de faire l'exercice)</li></ul>
                           </p>
                         """)
page_solution = creer_page_html("", "Solutions (parmi tant d'autres)", """
                         <p><ul><li>Vous pensiez que ça allait être simple pour les avoir ? Vous aviez raison ! (Ce sera votre dernier travail, promis)</li>
                          <li>Elles sont dans le fichier <b>top_secret.ipynb</b> qui est un notebook Jupyter : c'est un cahier virtuel dans lequel vous avez à la fois du texte et du code exécutable (Python), ce qui permet de faire des tutoriels très interractifs ! (souvent utilisé avec Github)</li>
                          <li>Par <a href="https://gist.github.com/kenjyco/69eeb503125035f21a9d">exemple</a></li>
                          <li>Pour l'utiliser, commencez par faire <b>pip install jupyter</b></li>
                          <li>Puis pour le lancer : <b>jupyter notebook</b></li>
                          <li>Ouvrez votre fichier normalement et faites "run cell" pour exécuter le code où vous avez la souris et voir le résultat apparaitre (ça marche aussi avec les graphiques !)</li></ul></p>
                         """)

pages = {"introduction":page_introduction, "1":page_1, "2":page_2, "3":page_3, "4":page_4, "42":page_42, "3.14":page_314, "dico":page_dico, "siseulement":page_siseulement, "objection!":page_objection, "weirdo":page_weirdo, "the_end":page_the_end, "gg_vous_avez_termodynamique_sans_h":page_solution}  

@app.route('/exercices/<code>', methods=['POST'])
def get_exercice(code):
    if request.method == 'POST':
        if 'message' in request.form:
            if code == 'maths':
                if request.form['message'] == '23.56':
                    return jsonify(response="Bravo c'était ça !", mdp="gg_")
            elif code == 'fonction':
                if request.form['message'] == '6.662':
                    return jsonify(response="Bravo ! Continuons notre exploration Python avec les booléens, sur la page 'siseulement'",mdp="vous_")  
            elif code == 'condition':
                if request.form['message'] == '40320':
                    return jsonify(response="Bravo c'était ça !", mdp="av")
            elif code == 'boucle':
                if request.form['message'] == '5913':
                    return jsonify(response="Bravo c'était ça ! Passons à la page 'dico' !", mdp="ez_")
            elif code == 'liste':
                if request.form['message'] == 'pmi sulp el( seriannoitcides de caractères, listes et':
                    return jsonify(response="Bien joué, ce n'était pas évident ce coup-ci !", mdp="ter")    
            elif code == 'dico':
                phrase = "PPGA (Python Programing Game Adventure), créé en 42 minutes (ou pas), m'a rendu apte à faire de la data science et de l'intelligence artificielle en Python... En tout cas, on l'espère !"
                phrase = ''.join(sorted(re.sub('[^a-z]', '', phrase.lower())))
                dico = {a:phrase.count(a) for a in phrase}
                if request.form['message'] == repr(dico):
                    return jsonify(response="Bien joué, c'était facile mais instructif non ? Si vous n'y voyez aucune 'objection!' rendez-vous à la page", mdp="modynamique_")    
            elif code == 'finally':
                if request.form['message'] == repr(['RecursionError', 'TypeError', 'NameError']):
                    return jsonify(response="Bien joué, j'espère que c'était reposant... On se retrouve en tout cas à la page des 'weirdo'", mdp="sans_")
            elif code == 'help-i-am-desperate':
                return jsonify(response="Honte à "+request.form['message']+" qui a osé sauter des exercices (d'ailleurs, comment es-tu arrivé jusqu'ici :o)... Non je plaisante, c'est en cherchant mais surtout en demandant de l'aide et en apprenant des autres qu'on progresse ! Le mot-de-passe était 'gg_vous_avez_termodynamique_sans_h' (tu peux aller sur cette page, je t'ai donné l'accès jk), bonnes corrections ;)")
            elif code == 'heritage':
                if request.form['message'] == 'ready':
                    return jsonify(response="Et voilà ! Rendez-vous sur la page de conclusion : 'the_end'", mdp="h")    
    return jsonify(response="Ce n'est pas ça, merci de réessayer !")

@app.route('/examples', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return jsonify(response="Votre GET a fonctionné, essayez le POST à présent ! Essayez donc de regarder l'attribut 'suite' de cette réponse...",
                       suite="Essayez le code suivant : p = requests.post(url_server+'examples', data={'message': 'wow'})")
    else:
        if not 'message' in request.form:
            return jsonify(response="Le POST a marché mais vous ne m'avez rien dit :'( réessayez svp") 
        else:
            return jsonify(response="Votre POST a fonctionnné, vous m'avez dit : "+request.form['message']+". A présent, merci de vous rendre sur la page secrète '42'.")

@app.route('/pages/<numero>')
def get_page(numero):
    return pages[str(numero)]

if __name__ == '__main__': 
    app.run(debug = True)