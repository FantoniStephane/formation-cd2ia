def demande_notes(nom: str, nb_notes: int = 3) -> list:
    """Demande nb_notes notes pour une matière et les retourne dans une liste."""
    print(f"\nSaisir les {nb_notes} notes de {nom} :")
    notes = []
    i = 0
    while i < nb_notes:
        try:
            note = float(input(f"Note {i + 1} : "))
            notes.append(note)
            i += 1
        except ValueError:
            print("Note saisie invalide.")
    return notes


def calculer_moyenne(notes: list) -> float:
    """Calcule et retourne la moyenne d'une liste de notes."""
    if not notes:
        return 0.0
    return sum(notes) / len(notes)


def determiner_mention(moyenne: float) -> str:
    """Retourne la mention correspondant à la moyenne."""
    if moyenne < 10:
        return "Ajourné"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 14:
        return "Assez bien"
    elif moyenne < 16:
        return "Bien"
    else:
        return "Très bien"


def afficher_bilan_final():
    """Orchestre la saisie des notes et affiche le bilan complet."""
    print("Bienvenue dans le simulateur de bulletin scolaire.")

    notes_maths = demande_notes("mathématiques")
    notes_fr = demande_notes("français")
    notes_en = demande_notes("anglais")

    moyenne_maths = calculer_moyenne(notes_maths)
    moyenne_fr = calculer_moyenne(notes_fr)
    moyenne_en = calculer_moyenne(notes_en)

    moyenne_generale = calculer_moyenne([moyenne_maths, moyenne_fr, moyenne_en])
    mention = determiner_mention(moyenne_generale)

    print("\nBilan de l'élève :")
    print(f"Moyenne de mathématiques : {moyenne_maths:.2f}")
    print(f"Moyenne de français : {moyenne_fr:.2f}")
    print(f"Moyenne d'anglais : {moyenne_en:.2f}")
    print(f"Moyenne générale : {moyenne_generale:.2f}")
    print(f"Mention : {mention}")


afficher_bilan_final()
