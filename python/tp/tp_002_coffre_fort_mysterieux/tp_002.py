FIRSTNAME_SPECIAL = ["admin", "agent007"]

secret_code = "PY123"

print("Bienvenue dans le système de sécurité.")

firstname = input("Quel est votre prénom ? ").strip()
is_code_correct = input("Entrez le code secret : ").strip() == secret_code

while True:
    age = input("Quel âge avez-vous ? ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Âge incorrect.")

if firstname.lower() in FIRSTNAME_SPECIAL:  # Cas 4
    print("Bienvenue cher utilisateur spécial <3 !")

if age >= 18 and is_code_correct:  # Cas 1
    print(f"Accès autorisé. Bienvenue {firstname}. Le coffre est maintenant ouvert.")
elif is_code_correct:  # Cas 3
    print("Code correct, mais accès interdit aux mineurs.")
else:  # Cas 2
    print("Code incorrect. Accès refusé.")
