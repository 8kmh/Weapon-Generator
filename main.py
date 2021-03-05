import random

class Armor:
    def __init__(self, armor_type):

        self.armor_type = ["Tête", "Torse", "Ceinture", "Bague", "Amulette", "Gants", "Bottes"]

    def getArmor(self, min, max):
        self.armor = random.randint(min, max)
        print("Armure : " + str(self.armor))

    def getColdResistance(self, min, max):
        self.cold_resistance = random.randint(min, max)
        print("Résistance au froid : " + str(self.cold_resistance))

    def getFireResistance(self, min, max):
        self.fire_resistance = random.randint(min, max)
        print("Résistance au feu : " + str(self.fire_resistance))

    def getLightningResistance(self, min, max):
        self.lightning_resistance = random.randint(min, max)
        print("Résistance à la foudre : " + str(self.lightning_resistance))



class Weapon:
    def __init__(self, weapon_type):

        self.weapon_type = ["Hache à une main", "Hache à deux mains", "Arc", "Arbalette", "Dague", "Masse", "Épée à une main", "Épée à deux mains"]

    def getAttackSpeed(self, min, max):
        self.attack_speed = random.randint(min, max)
        print("Vitesse d'attaque : " + str(self.attack_speed))

    def getDamage(self, min, max):
        self.damage = random.randint(min, max)
        print("Dégats : " + str(self.damage))
        

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
            self.getArmor(1, 9)
            self.getColdResistance(1, 5)
            self.getFireResistance(1, 5)
            self.getLightningResistance(1, 5)
            

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality > 300 and self.quality <= 450:
            print("ceci est une armure MAGIQUE")
            self.getArmor(10, 19)
            self.getColdResistance(6, 10)
            self.getFireResistance(6, 10)
            self.getLightningResistance(6, 10)

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality > 450 and self.quality <= 499:
            print("ceci est une armure RARE")
            self.getArmor(20, 29)
            self.getColdResistance(11, 19)
            self.getFireResistance(11, 19)
            self.getLightningResistance(11, 19)

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality == 500:
            print("ceci est une armure LÉGENDAIRE")
            self.getArmor(30, 40)
            self.getColdResistance(20, 40)
            self.getFireResistance(20, 40)
            self.getLightningResistance(20, 40)

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality <= 300:
            print("ceci est une arme NORMAL")
            self.getDamage(1, 9)
            self.getAttackSpeed(1, 5)

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality > 300 and self.quality <= 450:
            print("ceci est une arme MAGIQUE")
            self.getDamage(10, 19)
            self.getAttackSpeed(6, 10)

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality > 450 and self.quality <= 499:
            print("ceci est une arme RARE")
            self.getDamage(20, 29)
            self.getAttackSpeed(11, 19)
            
        else:
            print("ceci est une arme LÉGENDAIRE")
            self.getDamage(20, 40)
            self.getAttackSpeed(20, 30)
        
        
item1 = Item("", "")
item1.generateStats()


