def input_default(prompt: str, default_value: str = "N/A") -> str:
    """Retourne la saisie utilisateur ou la valeur par défaut si vide."""
    return input(prompt).strip() or default_value


def generer_email_defaut(nom: str, prenom: str) -> str:
    """Génère une adresse e-mail par défaut à partir du nom et prénom."""
    return f"{prenom.lower().strip()}.{nom.lower().strip()}@entreprise.com


def saisir_informations() -> dict:
    """Demande les informations à l'utilisateur et retourne un dictionnaire."""
    nom = input_default("Nom : ", "Dupont")
    prenom = input_default("Prénom : ", "Jean")
    poste = input_default("Poste : ", "Collaborateur")
    telephone = input_default("Téléphone : ")
    email = input_default("Adresse e-mail : ", generer_email_defaut(nom, prenom))

    return {
        "nom": nom,
        "prenom": prenom,
        "poste": poste,
        "telephone": telephone,
        "email": email
    }


def generer_signature(infos: dict):
    """Affiche la signature formatée à partir des informations."""
    print("\n--- SIGNATURE GÉNÉRÉE ---")
    print(f"{infos['prenom'].capitalize()} {infos['nom'].upper()}")
    print(infos['poste'].capitalize())
    print(f"Tél : {infos['telephone']}")
    print(f"Email : {infos['email']}")


def main():
    """Coordonne l'exécution du programme."""
    print("=== Générateur de signature e-mail ===\n")
    generer_signature(saisir_informations())


main()
