"""
SPECIAL
Strength, Perception, Endurance, Charisma, Intelligence, Agility, Luck
                      (ARMOR)                                   (BİR ŞEKİLDE YÜZDELİK VEYA
                                                                İHTİMAL GÖREVİ GÖRDÜRÜLECEK)
1 - 10

base				giant
str  = 3			str=7
end = 3     		end=6
int=3				int=1-2
agl = 3				agl=2
luck=3              luck=2

soldier				support
str=4				str=2
end=4				end=3
int=3				int=7
agl=4				agl=5
luck=3              luck=6

base_stat
attack = 100			attack = attack + attack*str
hp = 300				hp = hp + hp * end
dodge = %10		    	dodge = dodge + dodge*agl
critical = %10          crit = crit + crit*luck
kritik hasar = attack + (crit)/100(wip)
"""
import random

class BaseHuman:
    str,end,int,agl,luck=3
    attack=100*str
    hp=200*end
    dodge_chance = 10*agl*luck
    crit = 10*str*luck

    def __init__(self , name , team):
        self.name = name
        self.team = team
    
    def attack(self, obj)->None:
        dmg=self.attack+self.attack*self.str
        if obj.team != self.team:
            obj.hp -= self.attack()
        return dmg

    def critical(self):
        crit_dam= self.attack *(self.crit + self.crit * self.luck)
        return crit_dam
    
    def dodge(self,obj)->None:
        dodged_atck=obj.dmg - (self.dodge_chance*self.luck)
        self.hp=self.hp-dodged_atck
        return self.hp
 
    def die(self):
        if self.hp == 0:
            print(f"{self.name} öldü...")
        del self

class Giant(BaseHuman):
     str=7
     end=6
     int=1
     agl=2
     luck=2

class Solider(BaseHuman):
     str,end,agl=4


class Support(BaseHuman):
     str=2
     int=7
     agl=5
     luck=6


     def heal(self, obj):
          obj.hp += 150+(self.int * (self.int * obj.luck))

     def self_heal(self):
        self.hp += 200+(self.int * (self.int * self.luck))


