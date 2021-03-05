import random

class Armor:
    # armor_type = ["Tête", "Torse", "Ceinture", "Bague", "Amulette", "Gants", "Bottes"]
    # armor_attribute = ["Intelligence", "Maximum Life", "Cold Resistance", "Fire Resistance", "Lightning resistance"]
    def __init__(self):
        pass
        self.armor_type = ["Tête", "Torse", "Ceinture", "Bague", "Amulette", "Gants", "Bottes"]
        self.armor_attribute = ["Intelligence", "Maximum Life", "Cold Resistance", "Fire Resistance", "Lightning resistance"]

    # Stats qui apparait toujours dans une armure
    def getArmor(self, min, max):
        self.armor = random.randint(min, max)
        print("Armure : " + str(self.armor))


class Weapon:
    def __init__(self):

        self.weapon_type = ["Hache à une main", "Hache à deux mains", "Arc", "Arbalette", "Dague", "Masse", "Épée à une main", "Épée à deux mains"]
        self.weapon_attribute = ["Dégats de feu", "Dégats de foudre", "Dégats de froid", "Chance de coup critique"]

    # Stats qui apparait toujours dans une arme
    def getDamage(self, min, max):
        self.damage = random.randint(min, max)
        print("Dégats : " + str(self.damage))

        

class Item(Armor, Weapon):
    def __init__(self):

        Armor.__init__(self)
        Weapon.__init__(self)

    
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

    # Si CheckType return ("armure") attribute_choose = 1 à 4 stats aléatoire choisis dans armor_attribute
    # Si CheckType return ("arme") attribute_choose = 1 à 4 stats aléatoire choisis dans weapon_attribute
    def getRandomAttribute(self):
        if self.checkType(self.type_item, self.armor_type) == ("armure") and self.quality <= 300:
            self.attribute_choose = random.sample(self.armor_attribute, random.randint(0, 0))
            self.getArmor(1, 5)
            
        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality > 300 and self.quality <= 450:
            self.attribute_choose = random.sample(self.armor_attribute, random.randint(1, 2))
            self.getArmor(6, 10)

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality > 450 and self.quality <= 499:
            self.attribute_choose = random.sample(self.armor_attribute, random.randint(2, 3))
            self.getArmor(11, 15)

        elif self.checkType(self.type_item, self.armor_type) == "armure" and self.quality == 500:
            self.attribute_choose = random.sample(self.armor_attribute, random.randint(3, 4))
            self.getArmor(16, 20)

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality <= 300:
            self.attribute_choose = random.sample(self.weapon_attribute, random.randint(0, 0))
            self.getDamage(1, 10)
        
        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality > 300 and self.quality <= 450:
            self.attribute_choose = random.sample(self.weapon_attribute, random.randint(1, 2))
            self.getDamage(11, 20)

        elif self.checkType(self.type_item, self.armor_type) != "armure" and self.quality > 450 and self.quality <= 499:
            self.attribute_choose = random.sample(self.weapon_attribute, random.randint(2, 3))
            self.getDamage(21, 30)

        else:
            self.attribute_choose = random.sample(self.weapon_attribute, random.randint(3, 4))
            self.getDamage(31, 40)

    # Attribut des statistiques aléatoire dans les attribut sélectionné aléatoirement selon la qualité de l'item 
    def getRandomAttributeStats(self):
        for i in self.attribute_choose:
            if self.quality <= 300:
                print(i + " " + str(random.randint(1, 5)))
            elif self.quality > 300 and self.quality <= 450:
                print(i + " " + str(random.randint(6, 10)))
            elif self.quality > 450 and self.quality <= 499:
                print(i + " " + str(random.randint(11, 19)))
            else:
                print(i + " " + str(random.randint(20, 40)))

    # Execution du programme pour creer un item 
    def execute(self):
        
        self.generateQuality()
        self.selectArmorOrWeapon()
        self.getRandomAttribute()
        self.getRandomAttributeStats()

    
item1 = Item()
item1.execute()


