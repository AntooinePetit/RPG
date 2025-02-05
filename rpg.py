import random
import time

class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie = 0, force = 0, ennemi = False):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        if self.classe == "Archer":
            self.points_de_vie = self.niveau * 17
            self.force = self.niveau * 6
        if self.classe == "Guerrier":
            self.points_de_vie = self.niveau * 28
            self.force = self.niveau * 3
        if self.classe == "Mage":
            self.points_de_vie = self.niveau * 22
            self.force = self.niveau * 4
        if self.classe == "Tank":
            self.points_de_vie = self.niveau * 33
            self.force = self.niveau * 2
        if self.classe == "Voleur":
            self.points_de_vie = self.niveau * 20
            self.force = self.niveau * 5
        if self.classe != "Archer" and self.classe != "Guerrier" and self.classe != "Mage" and self.classe != "Tank" and self.classe != "Voleur":
            self.points_de_vie = self.niveau * 20
            self.force = self.niveau * 3
        if ennemi == True:
            self.points_de_vie = points_de_vie
            self.force = force            
        self.potion = random.randint(0, 3)
        self.armure = random.randint(0, 50)
        self.points_de_vie += self.armure
        
    def afficher_informations(self):
        print(f"Nom : {self.nom}")
        print(f"Classe : {self.classe}")
        print(f"Niveau : {self.niveau}")
        print(f"Points de vie : {self.points_de_vie} (Armure : {self.armure})")
        print(f"Force : {self.force}")            

    def afficher_inventaire(self):
        print("Inventaire :")
        if self.potion > 0:
            print(f"- Potion({self.potion})")
        if self.armure > 0:
            print(f"- Armure({self.armure})")

    def attaquer(self, cible):
        if cible.points_de_vie > 0:
            attaque = self.force +- random.randint(1, 6)
            if attaque > 0 :
                print(f"{self.nom} attaque {cible.nom} avec une force de {attaque}.")
                cible.recevoir_degats(attaque)
            if attaque > self.force + 5 :
                print("Coup critique !")
            if attaque < self.force - 5 or attaque == 0:
                print(f"{self.nom} a fait un échec critique !")
        else:
            print(f"{self.nom} ne peut pas attaquer {cible.nom} car il est mort.")

    def recevoir_degats(self, degats):
        self.points_de_vie -= degats
        if self.points_de_vie > 0:
            print(f"{self.nom} a reçu {degats} points dégâts. Points de vie restant : {self.points_de_vie}.")
        else:
            self.points_de_vie = 0
            print(f"{self.nom} est mort.")
    
    def soin(self):
        if self.potion > 0:
            self.points_de_vie += 25
            self.potion -= 1
            print(f"Vous avez maintenant {self.points_de_vie}.")
            print(f"Il vous reste {self.potion} potion(s).")
        else:
            print("Vous n'avez plus de potions !")

class GenerateurEnnemi:
    def __init__(self):
        self.nom = ""
        self.classe = ""
        self.niveau = 0
        self.points_de_vie = 0
        self.force = 0

    def nomEnnemi(self):
        nom_possibles = ["Gobelin", "Troll", "Ours", "Squelette"]
        i = random.randint(0, 3)
        self.nom = nom_possibles[i]

    def classeEnnemi(self):
        i= random.randint(0, 4)
        self.classe = classes_disponibles[i]

    def niveauEnnemi(self):
        self.niveau = random.randint(joueur.niveau - 4, joueur.niveau + 2)
        if self.niveau <= 0:
            self.niveau = 1
    
    def hpEnnemi(self):
        if self.classe == "Archer":
            self.points_de_vie = 5 * self.niveau
        if self.classe == "Guerrier":
            self.points_de_vie = 10 * self.niveau
        if self.classe == "Mage":
            self.points_de_vie = 8 * self.niveau
        if self.classe == "Tank":
            self.points_de_vie = 15 * self.niveau
        if self.classe == "Voleur":
            self.points_de_vie = 7 * self.niveau
        
    def forceEnnemi(self):
        if self.classe == "Archer":
            self.force = 5 * self.niveau
        if self.classe == "Guerrier":
            self.force = 2 * self.niveau
        if self.classe == "Mage":
            self.force = 3 * self.niveau
        if self.classe == "Tank":
            self.force = 1 * self.niveau
        if self.classe == "Voleur":
            self.force = 4 * self.niveau

# Interactions possibles :

def action():
    inter = random.randint(1, 10)
    if inter == 1 or inter == 4 or inter == 6:
        print("Vous trouvez une potion de soin !")
        joueur.potion += 1
        print(f"Vous avez maintenant {joueur.potion} potions.")
        return 1
    if inter == 2 or inter == 7 or inter == 10:
        correct = False
        armure = random.randint(1, 70)
        print(f"Vous trouvez un armure de {armure} points de résistance !")
        print(f"Votre armure est de {joueur.armure} points de résistance.")
        while correct == False:
            print("Voulez-vous échanger votre armure avec celle que vous venez de trouver ?")
            print("'O' - Oui")
            print("'N' - Non")
            changer_armure = str(input())
            if changer_armure == "O" and armure < joueur.armure:
                print("Votre armure est meilleure que celle que vous venez de trouver, êtes vous sûr de vouloir échanger ?")
                print("'O' - Oui")
                print("'N' - Non")
                changer_armure = str(input())
                while correct == False:
                    if changer_armure == "O":
                        print("Vous échanger votre armure.")
                        joueur.points_de_vie += armure - joueur.armure
                        joueur.armure = armure
                        time.sleep(1)
                        print(f"Vous avez maintenant {joueur.points_de_vie} points de vie, dont {joueur.armure} points d'armure")
                        correct = True
                    if changer_armure == "N":
                        print("Vous gardez votre armure.")
                        correct = True
                    if changer_armure != "N" and changer_armure != "O":
                        print("Commande inconnue.")
            if changer_armure == "O" and armure > joueur.armure:
                print("Vous échanger votre armure.")
                joueur.points_de_vie += armure - joueur.armure
                joueur.armure = armure
                time.sleep(1)
                print(f"Vous avez maintenant {joueur.points_de_vie} points de vie, dont {joueur.armure} points d'armure")
                correct = True
            if changer_armure == "N":
                print("Vous gardez votre armure.")
                correct = True
            if changer_armure != "N" and changer_armure != "O":
                print("Commande inconnue.")
        return 1
    if inter == 3 or inter == 5 or inter == 8 or inter == 9:
        print("Vous rencontrez un ennemi !")
        return combat()

# Combat

def combat():
    degats_recus = 0
    ennemi_genere = GenerateurEnnemi()
    ennemi_genere.nomEnnemi()
    ennemi_genere.classeEnnemi()
    ennemi_genere.niveauEnnemi()
    ennemi_genere.hpEnnemi()
    ennemi_genere.forceEnnemi()
    ennemi = Personnage(ennemi_genere.nom, ennemi_genere.classe, ennemi_genere.niveau, ennemi_genere.points_de_vie, ennemi_genere.force, True)
    time.sleep(1)
    print("Ennemi :")
    ennemi.afficher_informations()
    time.sleep(2)
    fuir = False
    points_de_vie = joueur.points_de_vie
    while joueur.points_de_vie > 0 and ennemi.points_de_vie > 0 and fuir == False:
        print("Que voulez-vous faire ?")
        print("1. Attaquer")
        print("2. Se soigner")
        print("3. Voir l'inventaire")
        print("4. Fuir")
        choix = int(input())
        if choix == 1:
            joueur.attaquer(ennemi)
            if ennemi.points_de_vie > 0:
                ennemi.attaquer(joueur)
            time.sleep(1)
        if choix == 2:
            joueur.soin()
            time.sleep(1)
        if choix == 3:
            joueur.afficher_inventaire()
            time.sleep(1)
        if choix == 4:
            fuir = True
        if choix < 1 or choix > 4:
            print("Commande inconnue, réessayez.")
            time.sleep(1)
    time.sleep(2)

    if fuir == False and joueur.points_de_vie > ennemi.points_de_vie:
        print(f"Vous avez vaincu {ennemi.nom} !")
        if joueur.points_de_vie < points_de_vie:
            joueur.points_de_vie += (points_de_vie - joueur.points_de_vie)/2
        print(f"Il vous reste {joueur.points_de_vie} points de vie.")
        return 1
    if fuir == False and ennemi.points_de_vie > joueur.points_de_vie:
        print(f"Vous avez été vaincu par {ennemi.nom}")
        return 1
    if fuir == True:
        print("Vous avez pris la fuite.")
        return -1

# Définitions des classes de personnage

classes_disponibles = ["Archer", "Guerrier", "Mage", "Tank", "Voleur"]

# Création de personnage utilisateur

print("Quel est votre nom de personnage ? ")
nomjoueur = input()
print(f"Quelle est votre classe ? {classes_disponibles}")
classejoueur = input()
joueur = Personnage(nomjoueur, classejoueur, random.randint(1, 5))
time.sleep(1)

# # Affichage des informations

print("Joueur :")
joueur.afficher_informations()
time.sleep(2)

# Début du jeu

print("Vous êtes perdu dans un labyrinthe et vous devez en sortir")
duree_du_jeu = random.randint(1, 10)
interaction = 0
mort = False
while interaction < duree_du_jeu and mort == False:
    print("Que voulez-vous faire ?")
    print("1. Aller à gauche")
    print("2. Aller tout droit")
    print("3. Aller à droite")
    print("4. Quitter le jeu")
    direction = int(input())
    time.sleep(1)
    if direction == 4:
        quitter = True
        break
    if direction == 1 or direction == 2 or direction == 3:
        result = action()
        if result == 1:
            interaction += result
        if result == 0:
            mort = True
        print(interaction)
    if direction < 1 and direction > 4:
        print("Commande inconnue.")
    time.sleep(1)

if interaction == duree_du_jeu:
    print("Vous vous êtes échappés du labyrinthe !")
if mort == True:
    print("Vous avez perdu, vous êtes mort")
if mort == False and interaction < duree_du_jeu:
    print("Vous avez quitté la partie.")

