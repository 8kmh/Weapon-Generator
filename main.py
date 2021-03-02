import random

# Avoir un bouton qui génère un seul item
# Ce bouton est clickable uniquement 2 fois par jour 
# avoir tout type d'item (tête, torse...)                                                                                    DONE
# Stocker les items reçu dans une sorte d'inventaire 
# Pouvoir vendre les items et récupérer des GOLDS à la place  

# Agrandir le randint de item_quality pour que les légendaire soit beaucoup plus rare où regarder une autre solution         DONE
# Essayer de mettre cette app sous forme graphique avec KIVY

# Quand l'item est de qualité supérieur (magique, rare, légendaire) il faut qu'il est des stats supplémentaire 
# Stocker toutes les stats randomizer d'un un seul item 

class Weapon():
    # Génération d'un booléen aléatoire
    # random_bit = random.getrandbits(1)
    # item_magic_or_not = bool(random_bit)

    weapon_type = ["Hache à une main", "Hache à deux mains", "Arc", "Arbalette", "Dague", "Masse", "Épée à une main", "Épée à deux mains"]
    armor_type = ["Tête", "Torse", "Ceinture", "Bague", "Amulette", "Gants", "Bottes"]

    unique_weapon = []
    unique_armor = []

    item_quality = random.randint(0, 200)
    
    damage = 0
    cold_resistance = 0
    fire_resistance = 0
    light_resistance = 0

def generate_weapon():
    print(random.choice(Weapon.weapon_type + Weapon.armor_type))
    
    if Weapon.item_quality <= 100:
        Weapon.damage = random.randint(1, 10)
        Weapon.cold_resistance = random.randint(1, 5)
        Weapon.fire_resistance = random.randint(1, 5)
        Weapon.lightning_resistance = random.randint(1, 5)
        print("Normal")
    elif Weapon.item_quality > 100 and Weapon.item_quality <= 150:
        Weapon.damage = random.randint(10, 20)
        Weapon.cold_resistance = random.randint(5, 10)
        Weapon.fire_resistance = random.randint(5, 10)
        Weapon.lightning_resistance = random.randint(5, 10)
        print("Magique")
    elif Weapon.item_quality > 150 and Weapon.item_quality <= 199:
        Weapon.damage = random.randint(20, 30)
        Weapon.cold_resistance = random.randint(10, 20)
        Weapon.fire_resistance = random.randint(10, 20)
        Weapon.lightning_resistance = random.randint(10, 20)
        print("Rare")
    else:
        Weapon.damage = random.randint(30, 40)
        Weapon.cold_resistance = random.randint(20, 40)
        Weapon.fire_resistance = random.randint(20, 40)
        Weapon.lightning_resistance = random.randint(20, 40)
        print("Légendaire")

    print("Damage : " + str(Weapon.damage))
    print("Cold Resistance : " + str(Weapon.cold_resistance))
    print("Fire Resistance : " + str(Weapon.fire_resistance))
    print("Lightning Resistance : " + str(Weapon.lightning_resistance))
    
    # if Weapon.item_magic_or_not:
    #     print("Magic")
    # else:
    #     print("Normal")

generate_weapon()


