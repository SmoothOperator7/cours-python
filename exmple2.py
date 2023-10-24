print("Welcome")

nom = input("Votre nom:")
nom = nom.upper()

prenom = input("Votre prénom :")

age = int(input("Votre âge :"))

taille = float(input("Votre taille :"))

fruits = input("Votre liste de fruits préférés :")
fruits = fruits.split()
fruits_result = ",".join(fruits)
message = input("Message de salutation :")

produit = {}
produit["nom"] = input("Nom du produit :")
produit["prix"] = input("Prix du produit :")

print(nom)
print(prenom)
print(age)
print(taille)
print(fruits_result)
print(message)
print(produit["nom"],",", produit["prix"],"€")