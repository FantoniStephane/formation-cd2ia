VEHICULES = {
    "moto": 2,
    "voiture": 5,
    "camion": 10
}

print("Bienvenue au péage automatique.")

while True:
    vehicule_type = input("Type de véhicule : ").lower().strip()
    if vehicule_type not in VEHICULES:
        print("Type de véhicule invalide.\nVeuillez recommencer.")
        continue

    passenger_count = input("Nombre de passagers : ")
    if not passenger_count.isdigit():
        print("Saisie invalide.\nVeuillez recommencer.")
        continue

    passenger_count = int(passenger_count)

    # Un camion avec 0 passager est invalide
    if vehicule_type == "camion" and passenger_count < 1:
        print("Saisie invalide.\nVeuillez recommencer.")
        continue

    break

has_subscription = input("Abonnement ? (o/n) : ").lower().strip() == "o"

price = VEHICULES[vehicule_type]
print(f"Tarif initial : {price} €")

if vehicule_type == "voiture" and passenger_count >= 4:
    print("Réduction covoiturage : 1 €")
    price -= 1

if has_subscription:
    print("Réduction abonnement : 2 €")
    price -= 2

# Le prix ne peut jamais être négatif
price = max(0, price)

print(f"Tarif final : {price} €")
print("Passage autorisé.")
