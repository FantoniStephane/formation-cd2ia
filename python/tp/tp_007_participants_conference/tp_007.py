import requests


def build_url(nb_participants: int) -> str:
    """Construit l'URL de l'API avec le nombre de participants souhaité."""
    return f"https://randomuser.me/api/?results={nb_participants}"


def ask_api(url: str) -> dict | None:
    """Envoie une requête GET et retourne la réponse JSON."""
    try:
        reponse = requests.get(url)
        return reponse.json()
    except requests.exceptions.RequestException:
        print("Erreur : impossible de récupérer les données.")
        return None


def extract_info_user(user: dict) -> dict:
    """Extrait les informations utiles d'un utilisateur retourné par l'API."""
    return {
        "prenom"     : user["name"]["first"],
        "nom"        : user["name"]["last"],
        "email"      : user["email"],
        "ville"      : user["location"]["city"],
        "pays"       : user["location"]["country"],
        "nationalite": user["nat"]
    }


def afficher_badge_participant(infos: dict):
    """Affiche les informations d'un participant sous forme de badge."""
    print(f"Nom complet : {infos['prenom']} {infos['nom']}")
    print(f"Email       : {infos['email']}")
    print(f"Ville       : {infos['ville']}")
    print(f"Pays        : {infos['pays']}")
    print(f"Nationalité : {infos['nationalite']}\n")


def main():
    """Programme principal — coordonne l'exécution."""
    print("Bienvenue dans le générateur de participants fictifs.\n")

    while True:
        try:
            nb = int(input("Combien de participants voulez-vous générer ? : "))
            if nb > 0:
                break
            print("Valeur invalide. Entrez un nombre supérieur à 0.")
        except ValueError:
            print("Valeur invalide. Entrez un nombre entier.")

    print("\nRécupération des participants...")

    url = build_url(nb)
    donnees = ask_api(url)

    if donnees is None:
        print("Impossible d'afficher les participants.")
        return

    for i, user in enumerate(donnees["results"], start=1):
        print(f"\n--- Participant {i} ---\n")
        infos = extract_info_user(user)
        afficher_badge_participant(infos)


main()
