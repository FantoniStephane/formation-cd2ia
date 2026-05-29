TARIFS = {
    "logo": 70,
    "site": 90,
    "affiche": 50
}


def obtenir_tarif_horaire(prestation: str) -> int:
    """Retourne le tarif horaire selon la prestation."""
    return TARIFS[prestation]


def calculer_prix_base(tarif_horaire: int, nb_heures: int) -> float:
    """Calcule et retourne le prix de base."""
    return tarif_horaire * nb_heures


def appliquer_majoration(prix_de_base: float, urgence: bool, taux: float = 0.3) -> float:
    """Applique une majoration de 30% si la livraison est urgente."""
    if urgence:
        return prix_de_base * (1 + taux)
    return prix_de_base


def appliquer_reduction_fidelite(tarif_actuel: float, fidele: bool, taux: float = 0.1) -> float:
    """Applique une réduction de 10% si le client est fidèle."""
    if fidele:
        return tarif_actuel * (1 - taux)
    return tarif_actuel


def afficher_recap(prestation: str, nb_heures: int, prix_final: float):
    """Affiche le récapitulatif du devis."""
    print("\nRécapitulatif du devis :")
    print(f"Prestation : {prestation}")
    print(f"Nombre d'heures : {nb_heures}")
    print(f"Prix final estimé : {round(prix_final, 2)} €")


def demander_utilisateur() -> tuple:
    """Demande les informations à l'utilisateur avec validation."""
    while True:
        prestation = input("Type de prestation (logo/site/affiche) : ").lower().strip()
        if prestation in TARIFS:
            break
        print("Prestation invalide. Choisissez parmi : logo, site, affiche.")

    while True:
        nb_heures = input("Nombre d'heures : ")
        if nb_heures.isdigit() and int(nb_heures) > 0:
            nb_heures = int(nb_heures)
            break
        print("Nombre d'heures invalide.")

    urgence = input("Livraison urgente ? (oui/non) : ").lower().strip() == "oui"
    fidele = input("Client fidèle ? (oui/non) : ").lower().strip() == "oui"

    return prestation, nb_heures, urgence, fidele


# Programme principal
print("\nBienvenue dans le calculateur de devis.")

prestation, nb_heures, urgence, fidele = demander_utilisateur()
tarif_horaire = obtenir_tarif_horaire(prestation)
prix_base = calculer_prix_base(tarif_horaire, nb_heures)
prix_avec_urgence = appliquer_majoration(prix_base, urgence)
prix_final = appliquer_reduction_fidelite(prix_avec_urgence, fidele)

afficher_recap(prestation, nb_heures, prix_final)
