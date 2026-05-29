def saisir_n_batterie() -> int:
    """Demande le niveau de batterie et valide la saisie."""
    while True:
        try:
            n_batterie = int(input("Batterie du drone : "))
            if 0 <= n_batterie <= 100:
                return n_batterie
            print("Valeur invalide. Entrez un nombre entre 0 et 100.")
        except ValueError:
            print("Valeur invalide. Entrez un nombre entier.")


def saisir_texte_securise(message: str, valeurs_autorisees: list) -> str:
    """Demande une saisie parmi les valeurs autorisées et recommence si invalide."""
    while True:
        choix = input(message).strip().lower()
        if choix in valeurs_autorisees:
            return choix
        print(f"Valeur invalide. Choix possibles : {valeurs_autorisees}")


def verifier_decollage(batterie: int, meteo: str, type_zone: str, autorisation_speciale: str) -> bool:
    """Retourne True si les conditions de décollage sont réunies."""
    if batterie < 20:
        return False
    if meteo == "pluie":
        return False
    if type_zone == "zone_securisee" and autorisation_speciale != "oui":
        return False
    return True


def calculer_score_risque(meteo: str, zone: str, batterie: int, priorite: str) -> int:
    """Calcule et retourne le score de risque de la mission."""
    score = 0
    if meteo == "vent":
        score += 2
    if meteo == "nuageux":
        score += 1
    if zone == "toiture":
        score += 2
    if zone == "zone_securisee":
        score += 3
    if 20 <= batterie <= 35:
        score += 2
    if priorite == "critique":
        score += 2
    if priorite == "haute":
        score += 1
    return score


def transformer_score_en_risque(score: int) -> str:
    """Retourne le niveau de risque selon le score."""
    if 0 <= score <= 2:
        return "faible"
    elif 3 <= score <= 5:
        return "modéré"
    else:
        return "élevé"


def determiner_decision(decollage: bool, n_risque: str) -> str:
    """Retourne la décision finale selon le décollage et le niveau de risque."""
    if not decollage:
        return "Mission refusée"
    elif n_risque == "élevé":
        return "Mission autorisée avec vigilance renforcée"
    return "Mission autorisée"


def afficher_rapport_final(nom_mission: str, n_batterie: int, meteo: str, zone: str,
                           priorite: str, autorisation_speciale: str, score: int,
                           n_risque: str, decision: str):
    """Affiche le rapport complet de la mission."""
    print("\nAnalyse de la mission en cours...\n")
    print("Rapport de mission")
    print(f"Mission : {nom_mission}")
    print(f"Batterie : {n_batterie} %")
    print(f"Météo : {meteo}")
    print(f"Zone : {zone}")
    print(f"Priorité : {priorite}")
    print(f"Autorisation spéciale : {autorisation_speciale}")
    print(f"Score de risque : {score}")
    print(f"Niveau de risque : {n_risque}")
    print(f"Décision : {decision}")
