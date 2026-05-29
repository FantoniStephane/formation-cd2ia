from mission_drone_functions import (
    saisir_n_batterie,
    saisir_texte_securise,
    verifier_decollage,
    calculer_score_risque,
    transformer_score_en_risque,
    determiner_decision,
    afficher_rapport_final
)

print("\nBienvenue dans le système de préparation des missions de drone.")

nom_mission = input("Nom de la mission : ")
n_batterie = saisir_n_batterie()
type_meteo = saisir_texte_securise("Météo : ", ["soleil", "nuageux", "vent", "pluie"])
type_zone = saisir_texte_securise("Zone : ", ["entrepot", "parking", "toiture", "zone_securisee"])
type_priorite = saisir_texte_securise("Priorité : ", ["basse", "normale", "haute", "critique"])
autorisation_speciale = saisir_texte_securise("Autorisation spéciale : ", ["oui", "non"])

decollage = verifier_decollage(n_batterie, type_meteo, type_zone, autorisation_speciale)
score = calculer_score_risque(type_meteo, type_zone, n_batterie, type_priorite)
n_risque = transformer_score_en_risque(score)
decision = determiner_decision(decollage, n_risque)

afficher_rapport_final(
    nom_mission, n_batterie, type_meteo, type_zone,
    type_priorite, autorisation_speciale, score, n_risque, decision
)
