YES_EQUIVALENTS = ["o", "oui", "y", "yes", "1"]


def boolean_input(message: str) -> bool:
    """Retourne un boolean basé sur la réponse de l'utilisateur."""
    return input(message).lower().strip() in YES_EQUIVALENTS


while True:
    age = input("Entrez votre âge : ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("L'âge est incorrect.")

has_badge = boolean_input("Avez-vous un badge valide (o/n) ? : ")
has_acces_code = boolean_input("Connaissez-vous le code du jour (o/n) ? : ")
is_with_manager = boolean_input("Êtes-vous accompagné d'un responsable (o/n) ? : ")

if age < 18:  # Règle 1
    print("Accès refusé : zone interdite aux mineurs.")
elif has_badge and has_acces_code:  # Règle 2a
    print("Accès autorisé : accès complet validé.")
elif is_with_manager:  # Règle 2b
    print("Accès autorisé : entrée autorisée avec accompagnement.")
elif has_badge and not has_acces_code:  # Règle 4
    print("Accès refusé : badge valide, mais code du jour manquant.")
elif has_acces_code and not has_badge:  # Règle 5
    print("Accès refusé : code correct, mais badge valide manquant.")
else:  # Règle 3
    print("Accès refusé : autorisations insuffisantes.")
