import random
target_number = random.randint(1, 100)

print("Bienvenue dans le jeu Devine le nombre.")
print("Essayez de trouver le nombre secret.\n")

while True:
    user_number = input("Votre essai : ")
    if not user_number.isdigit():
        print("Saisie incorrecte")
        continue

    user_number = int(user_number)

    if user_number > target_number:
        print("Le nombre est plus petit !")
    elif user_number < target_number:
        print("Le nombre est plus grand !")
    else:
        print(f"Bravo ! Vous avez bien deviné {target_number}")
        break
