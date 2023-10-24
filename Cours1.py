nom = "Koch" #chaine de caractère
age= 21 #integer
taille = 1.87 #float
est_etudiant = True #booléen
est_intervenant = False

print(nom)
print(age)
print(taille)
print(est_etudiant)
print(est_intervenant)



#Affichera les infos du print (Déclarer une variable en Python)

#Terminal python exemple.py

for i in range(5):
        print("Répétition n°", i)

#commence par 0 donc une liste de 0 à 4 

i = 1

while i <= 10:
    print("Répétition n°", i)
    i += 2

#
fruits =["pomm","banane","orange"]
print (fruits[0])
#ça va afficher juste pomme

def saluer(nom):
    print("Bonjour," +nom)
    
saluer("Alice")

#
personne = {"nom":"Steph", "age":24, "ville":"Marseille"}

# Demander à l'utilisateur de saisir son nom
nom = input("Entrez votre nom: ")
nom = nom.upper()

#Demander à l'utilisateur de saisir son prénom
prenom = input("Entrez votre prénom : ")

# Demander à l'utilisateur de saisir son âge
age = input("Entrez votre âge : ")

# Demander à l'utilisateur de saisir sa taille
taille = input("Entrez votre taille : ")

# Demander à l'utilisateur de saisir sa liste de fruits préférés
fruits = input("Entrez votre liste de fruits préférés : ")
fruits = fruits.split(",")

# Demander à l'utilisateur de saisir un message de salutation personnalisé
message = input("Entrez un message de salutation personnalisé : ")

# Demander à l'utilisateur de saisir les propriétés d'un produit
produit = {}
produit["nom","prix"] = input("Entrez le nom du produit et son prix : ")


# Afficher les informations saisies par l'utilisateur
print("Nom : ", nom)
print("Prénom : ", prenom)
print("Âge : ", age)
print("Taille : ", taille)
print("Liste de fruits préférés : ", fruits)
print("Message de salutation personnalisé : ", message)
print("Nom du produit : ", produit["nom", "prix"])