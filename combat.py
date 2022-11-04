import random
import time
class Battle:

    def __init__(self, base_health, health, damage, selection, name, xp, specialty):
        self.data = ""
        self.specialty = ""
        self.base_health = base_health
        self.health = health
        self.damage = damage
        self.selection = selection
        self.name = name
        self.xp = xp
        self.specialty = specialty




    def ChooseEnemy(self):

        global BattleFoe

        Goomba = Battle(1, 5.0, 5, 1, "Goomba", "","")
        FootSoldier = Battle(1, 10.0, 5, 2, "Foot Soldier", "","")
        ArmoredSoldier = Battle(1, 20.0, 10, 3, "Armored Soldier", "","")
        Archer = Battle(1, 30.0, 15, 4, "Archer", "","")
        ExpertSoldier = Battle(1, 40.0, 20, 5, "Expert Soldier", "","")
        Horseman = Battle(1, 80.0, 40, 6, "Horseman", "","")
        Minotaur = Battle(1, 120.0, 70, 7, "Minotaur", "","")
        Centaur = Battle(1, 150.0, 100, 8, "Centaur", "","")
        Griffin = Battle(1, 180.0, 130, 9, "Griffin", "","")
        Dragon = Battle(1, 250.0, 180, 10, "Dragon", "","")
        #EvilKing = Battle(1, 300, 200, 11, "Evil King", "","")

        Opponent1 = random.randint(1,3)
        Opponent2 = random.randint(4,6)
        Opponent3 = random.randint(7,10)

        OpponentList = [Goomba, FootSoldier, ArmoredSoldier, Archer, ExpertSoldier, Horseman, Minotaur, Centaur, Griffin, Dragon]

        OpponentChoices = []

        @classmethod
        def getopponentchoices(cls):
            return cls.OpponentChoices

        for opponent in OpponentList:
            if opponent.selection == Opponent1:
                OpponentChoices.append(opponent.name)
            if opponent.selection == Opponent2:
                OpponentChoices.append(opponent.name)
            if opponent.selection == Opponent3:
                OpponentChoices.append(opponent.name)

        print("You walk into battle and three different opponents immediately catch your eye.")
        for opponent in OpponentChoices:
            print(opponent)
        print("Who would you like to fight?")
        BattleFoe = input(":")
        while not BattleFoe in OpponentChoices:
            print("Please enter the enemy's name like from the list given")
            BattleFoe = input(":")
        
        for opponent in OpponentList:
            if BattleFoe == opponent.name:
                BattleFoe = opponent
                
        
        print(f"you have chosen to fight the {BattleFoe.name}")
        self.FightSequence()

    def CalculateDamage(self):
        global BattleFoe, player_damage_inflicted, foe_damage_inflicted
        player_damage_inflicted = round(self.damage*random.uniform(0.75,1.25), 2)
        foe_damage_inflicted = round(BattleFoe.damage*random.uniform(0.75,1.25), 2)
        #return player_damage_inflicted, foe_damage_inflicted

    def SetNewHealth(self, damage):        
        self.health = self.health - damage
        return self.health

    def GetHealth(self):
        return self.health

    def Surrender(self):
        global stored_health
        stored_health = self.health
        self.health = 0
        self.xp = self.xp - round(self.xp*(0.1),2)
        print(f'Your current xp is: {self.xp}')
        self.HealthXP()
        self.DamageXP()
        self.ResetHealth()
        self.ChooseEnemy()

    def Win(self):
        self.xp = self.xp + round(self.xp*(0.2),2)
        print(f'Your current xp is: {self.xp}')
        time.sleep(1)
        if self.xp in range(0, 25):
            print("Get to 25 xp to Reach level 2")
        elif self.xp in range(25, 50):
            print("Get to 50 xp to Reach level 3")
        elif self.xp in range(50, 75):
            print("Get to 75 xp to Reach level 4")
        elif self.xp in range(75, 100):
            print("Get to 100 xp to Reach level 5")
        elif self.xp in range(100, 125):
            print("Get to 125 xp to Reach level 6")
        #elif self.xp in range(125, 150):
            #print("Get to 150 xp to Reach level 7")
        #elif self.xp in range(150, 175):
            #print("Get to 175 xp to Reach level 8")
        elif self.xp >= 125:
            print("Until the next patch notes... YOU ARE MAX LEVEL")

    
    def ResetHealth(self):
        self.health = self.base_health

    def HealthXP(self):
        if self.specialty == 'Cavalry':
            if self.xp > 25:
                self.base_health = 120
            elif self.xp > 50:
                self.base_health = 170
            elif self.xp > 75:
                self.base_health = 230
            elif self.xp > 100:
                self.base_health = 300
            elif self.xp > 125:
                self.base_health = 350
        elif self.specialty == 'Archer':
            if self.xp > 25:
                self.base_health = 90
            elif self.xp > 50:
                self.base_health = 140
            elif self.xp > 75:
                self.base_health =190
            elif self.xp > 100:
                self.base_health = 260
            elif self.xp > 125:
                self.base_health = 310
        elif self.specialty == 'Swordsman':
            if self.xp >25:
                self.base_health = 60
            elif self.xp > 50:
                self.base_health = 110
            elif self.xp >75:
                self.base_health = 160
            elif self.xp > 100:
                self.base_health = 210
            elif self.xp > 125:
                self.base_health = 260

    def DamageXP(self):
        if self.specialty == 'Cavalry':
            if self.xp >25:
                self.damage = 40
            elif self.xp > 50:
                self.damage = 60
            elif self.xp > 75:
                self.damage = 100
            elif self.xp > 100:
                self.damage = 170
        if self.specialty == 'Archer':
            if self.xp >25:
                self.damage = 30
            elif self.xp > 50:
                self.damage = 50
            elif self.xp > 75:
                self.damage = 80
            elif self.xp > 100:
                self.damage = 130
            elif self.xp > 125:
                self.damage = 170
        if self.specialty == 'Swordsman':
            if self.xp <= 25:
                self.damage = 5
            elif self.xp >25:
                self.damage = 20
            elif self.xp > 50:
                self.damage = 40
            elif self.xp > 75:
                self.damage = 70
            elif self.xp > 100:
                self.damage = 120
            elif self.xp > 125:
                self.damage = 160
            elif self.xp > 150:
                self.damage = 180

    def FightSequence(self):
        global BattleFoe

        while self.health > 0 and BattleFoe.health > 0:
            print(f"Your current health is {self.GetHealth()}. Your opponent's current health is {BattleFoe.GetHealth()}. Would you like to fight or surrender? (f/s)")
            fight_decision = input(":")

            if fight_decision == 'f':
                self.DamageXP()
                self.CalculateDamage()
                self.SetNewHealth(foe_damage_inflicted)
                BattleFoe.SetNewHealth(player_damage_inflicted)
                if self.health > 0 and BattleFoe.health > 0:
                    self.FightSequence()
                elif self.health >= 0 and BattleFoe.health <= 0:
                    print(f"Congratulations! You killed the enemy {BattleFoe.name}! You have gained some experience!")
                    time.sleep(1)
                    self.Win()
                    self.HealthXP()
                    self.DamageXP()
                    self.ResetHealth()
                    self.ChooseEnemy()
                elif self.health <= 0 and BattleFoe.health <= 0:
                    print(f"You killed the enemy {BattleFoe.name}, but you died from battle wounds soon afterwards.\nGame Over")
                elif self.health <= 0 and BattleFoe.health > 0:
                    print(f"You put up a fight, but the enemy {BattleFoe.name} killed you.\nGameOver")



            elif fight_decision == 's':
                print("You chose to surrender. You have lost some of your warrior experience")
                self.Surrender()

            else:
                print("Please enter either 'f' or 's' to choose whether or not to fight.")
                self.FightSequence()
                


        
           

    

if __name__ == "__main__":

    dummy  = Battle(100, 10, "", "bozo")
    

    


    print("You walked into a battle")
    
    print(dummy.specialty)
    dummy.ChooseEnemy()
    dummy.FightSequence()
    
