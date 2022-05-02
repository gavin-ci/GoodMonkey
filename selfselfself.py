class baseFile():
    def __init__(self, name, baseHp, baseAtk, baseDef, baseSpecial, baseSpecialStat, skill, skillDmg, burst, burstDmg):
        self.name = name
        self.baseHp = baseHp
        self.baseAtk = baseAtk 
        self.baseDef = baseDef
        self.baseSpecial = baseSpecial
        self.baseSpecialStat = baseSpecialStat
        self.skill = skill
        self.skillDmg = skillDmg
        self.burst = burst
        self.burstDmg = burstDmg
      
        pass  

Sol = baseFile("Sol Badguy", 500, 25, 30, 5, "Pyro DMG", "Gunflame", 55, "Heavy Mob Cemetary", 110)

print("name = ", Sol.name, "\nbaseHp = ", Sol.baseHp, "\nbaseAtk = ", Sol.baseAtk, "\nbaseDef = ", Sol.baseDef, "\nspecial stat = ", Sol.baseSpecial, "\nbaseSpecial = ", Sol.baseSpecialStat, "\nskill = ", Sol.skill, "\nskill DMG = ", "\nbaseBurst = ", Sol.burst, "\nburst DMG = ", Sol.burstDmg)

