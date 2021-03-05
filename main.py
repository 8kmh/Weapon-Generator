import random

class Armor:
    def __init__(self, armor_type):

        self.armor_type = ["Tête", "Torse", "Ceinture", "Bague", "Amulette", "Gants", "Bottes"]
        self.armor_attribute = ["Intelligence", "Maximum Life", "Armor", "Cold Resistance", "Fire Resistance", "Lightning resistance"]

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
        self.weapon_attribute = ["Dégats Physique", "Dégats de feu", "Dégats de foudre", "Dégats de froid"]

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

        # self.generateQuality()
        # self.selectArmorOrWeapon()
        # self.checkType(self.type_item, self.armor_type)
        # self.getRandomAttribute()
        # self.getRandomAttributeStats()
    
    # Choix d'un nombre aléatoire entre 0 et 500 pour définir la qualité de l'item
    def generateQuality(self):

        #self.quality = 500
        self.quality = random.randint(0, 500)

        if self.quality <= 300:
            print("NORMAL")

        elif self.quality > 300 and self.quality <= 450:
            print("MAGIQUE")

        elif self.quality > 450 and self.quality <= 499:
            print("RARE")

        else:
            print("Légendaire")

    # Stockage dans la variable type_item d'un choix aléatoire entre les deux tableau : armor_type, weapon_type
    def selectArmorOrWeapon(self):
        self.type_item = random.choice(self.armor_type + self.weapon_type)
        print(self.type_item)

    # Si l'élément choisi dans type_item se retrouve dans le tableau armor_type : return ("armure") sinon return ("arme")
    def checkType(self, type_item, armor_type):
        for i in self.armor_type:
            if i == self.type_item:
                return ("armure")
        return ("arme")

    # Si CheckType return ("armure") attribute_choose = 1 à 3 stats aléatoire choisis dans armor_attribute
    def getRandomAttribute(self):
        if self.checkType(self.type_item, self.armor_type) == ("armure") and self.quality <= 300:
            self.attribute_choose = random.sample(self.armor_attribute, random.randint(0, 1))
            

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality > 300 and self.quality <= 450:
            self.attribute_choose = random.sample(self.armor_attribute, random.randint(1, 2))
            

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality > 450 and self.quality <= 499:
            self.attribute_choose = random.sample(self.armor_attribute, random.randint(2, 3))
            

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality == 500:
            self.attribute_choose = random.sample(self.armor_attribute, random.randint(3, 4))
            

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality <= 300:
            self.attribute_choose = random.sample(self.weapon_attribute, random.randint(0, 1))
            
        
        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality > 300 and self.quality <= 450:
            self.attribute_choose = random.sample(self.weapon_attribute, random.randint(1, 2))
            

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality > 450 and self.quality <= 499:
            self.attribute_choose = random.sample(self.weapon_attribute, random.randint(2, 3))
            

        else:
            self.attribute_choose = random.sample(self.weapon_attribute, random.randint(3, 4))
            

    def getRandomAttributeStats(self):
        for i in self.attribute_choose:
            if self.quality <= 300:
                print(i + " " + str(random.randint(1, 5)))
            elif self.quality > 300 and self.quality <= 450:
                print(i + " " + str(random.randint(6, 10)))
            elif self.quality > 300 and self.quality <= 450:
                print(i + " " + str(random.randint(11, 19)))
            else:
                print(i + " " + str(random.randint(20, 40)))

    def execute(self):
        
        self.generateQuality()
        self.selectArmorOrWeapon()
        self.getRandomAttribute()
        self.getRandomAttributeStats()

    
item1 = Item("", "")
item1.execute()


