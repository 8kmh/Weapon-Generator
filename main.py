import random

class Armor:
    def __init__(self, armor_type):

        self.armor_type = ["Tête", "Torse", "Ceinture", "Bague", "Amulette", "Gants", "Bottes"]



class Weapon:
    def __init__(self, weapon_type):

        self.weapon_type = ["Hache à une main", "Hache à deux mains", "Arc", "Arbalette", "Dague", "Masse", "Épée à une main", "Épée à deux mains"]
        

class Item(Armor, Weapon):
    def __init__(self, armor_type, weapon_type):
        Armor.__init__(self, armor_type)
        Weapon.__init__(self, weapon_type)

        self.generateQuality()
        self.selectArmorOrWeapon()

    def generateQuality(self):

        #self.quality = 500
        self.quality = random.randint(0, 500)

    def selectArmorOrWeapon(self):
        self.type_item = random.choice(self.armor_type + self.weapon_type)

    def checkType(self, type_item, armor_type):
        for i in self.armor_type:
            if i == self.type_item:
                return ("armure")
        return ("arme")

    def generateStats(self):

        if self.checkType(self.type_item, self.armor_type) == "armure" and self.quality <= 300:
            print("ceci est une armure NORMAL")
            armor = random.randint(1, 9)
            cold_resistance = random.randint(1, 5)
            fire_resistance = random.randint(1, 5)
            lightning_resistance = random.randint(1, 5)
            print("Armure : " + str(armor))
            print("Résistance au froid : " + str(cold_resistance))
            print("Résistance au feu : " + str(fire_resistance))
            print("Résistance électrique : " + str(lightning_resistance))

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality > 300 and self.quality <= 450:
            print("ceci est une armure MAGIQUE")
            armor = random.randint(10, 19)
            cold_resistance = random.randint(6, 10)
            fire_resistance = random.randint(6, 10)
            lightning_resistance = random.randint(6, 10)
            print("Armure : " + str(armor))
            print("Résistance au froid : " + str(cold_resistance))
            print("Résistance au feu : " + str(fire_resistance))
            print("Résistance électrique : " + str(lightning_resistance))

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality > 450 and self.quality <= 499:
            print("ceci est une armure RARE")
            armor = random.randint(20, 29)
            cold_resistance = random.randint(11, 19)
            fire_resistance = random.randint(11, 19)
            lightning_resistance = random.randint(11, 19)
            print("Armure : " + str(armor))
            print("Résistance au froid : " + str(cold_resistance))
            print("Résistance au feu : " + str(fire_resistance))
            print("Résistance électrique : " + str(lightning_resistance))

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality == 500:
            print("ceci est une armure LÉGENDAIRE")
            armor = random.randint(30, 40)
            cold_resistance = random.randint(20, 40)
            fire_resistance = random.randint(20, 40)
            lightning_resistance = random.randint(20, 40)
            print("Armure : " + str(armor))
            print("Résistance au froid : " + str(cold_resistance))
            print("Résistance au feu : " + str(fire_resistance))
            print("Résistance électrique : " + str(lightning_resistance))

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality <= 300:
            print("ceci est une arme NORMAL")
            damage = random.randint(1, 9)
            print("Dégats : " + str(damage))

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality > 300 and self.quality <= 450:
            print("ceci est une arme MAGIQUE")
            damage = random.randint(10, 19)
            print("Dégats : " + str(damage))

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality > 450 and self.quality <= 499:
            print("ceci est une arme RARE")
            damage = random.randint(20, 29)
            print("Dégats : " + str(damage))
            
        else:
            print("ceci est une arme LÉGENDAIRE")
            damage = random.randint(30, 40)
            print("Dégats : " + str(damage))
        
        
item1 = Item("", "")
item1.generateStats()


