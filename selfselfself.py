class baseFile():
    def __init__(self, name, title, vision, weaponType, signatureWeapon, baseHp, baseAtk, baseDef, special, skill, skillDmg, burst, burstDmg):
        self.name = name
        self.title = title
        self.vision = vision
        self.weaponType = weaponType
        self.signatureWeapon = signatureWeapon
        self.baseHp = baseHp
        self.baseAtk = baseAtk 
        self.baseDef = baseDef
        self.special = special
        self.skill = skill
        self.skillDmg = skillDmg
        self.burst = burst
        self.burstDmg = burstDmg
      
        pass  

#EXMAPLE
Sol = baseFile("Sol Badguy", "TitleDiff","Pyro", "Claymore", "Junkyard Dog", 500, 25, 30, "Pyro DMG", "Gunflame", 55, "Heavy Mob Cemetary", 110)

#character list starts here:
Diluc = baseFile("Diluc Ragnvindr", "The Dark Side Of Dawn","Pyro", "Claymore", "Wolf's Gravestone", 1011, 26, 61, "Crit Rate", "Searing Onslaught", 25, "Dawn", 53)
YaeMiko = baseFile("Yae Miko", "Astute Amusement", "Electro", "Catalyst", "Kagura's Verity", 807, 26, 44, "Crit Rate", "Yakan Evocation: Sesshou Sakura", 24, "Great Secret Art: Tenko Kenshin", 67)



#printing character lists starts here:
#print("name = ", Sol.name, "\ntitle = ", Sol.title, "\nvision = ",Sol.vision,"\nweapon type = ",Sol.weaponType,"\nsignature weapon = ",Sol.signatureWeapon, "\nbaseHp = ", Sol.baseHp, "\nbaseAtk = ", Sol.baseAtk, "\nbaseDef = ", Sol.baseDef, "\nspecial stat = ", Sol.special, "\nskill = ", Sol.skill, "\nskill DMG = ", Sol.skillDmg, "\nburst = ", Sol.burst, "\nburst DMG = ", Sol.burstDmg, "\n")
print("name = ",Diluc.name,"\ntitle = ", Diluc.title, "\nvision = ",Diluc.vision,"\nweapon type = ",Diluc.weaponType,"\nsignature weapon = ",Diluc.signatureWeapon,"\nbaseHp = ",Diluc.baseHp,"\nbaseAtk = ",Diluc.baseAtk,"\nbaseDef = ",Diluc.baseDef,"\nspecial stat = ",Diluc.special,"\nskill = ",Diluc.skill,"\nskill DMG = ",Diluc.skillDmg,"\nburst = ",Diluc.burst,"\nburst DMG = ",Diluc.burstDmg,"\n")
print("name = ",YaeMiko.name,"\ntitle = ", YaeMiko.title, "\nvision = ",YaeMiko.vision,"\nweapon type = ",YaeMiko.weaponType,"\nsignature weapon = ",YaeMiko.signatureWeapon,"\nbaseHp = ",YaeMiko.baseHp,"\nbaseAtk = ",YaeMiko.baseAtk,"\nbaseDef = ",YaeMiko.baseDef,"\nspecial stat = ",YaeMiko.special,"\nskill = ",YaeMiko.skill,"\nskill DMG = ",YaeMiko.skillDmg,"\nburst = ",YaeMiko.burst,"\nburst DMG = ",YaeMiko.burstDmg,"\n")
