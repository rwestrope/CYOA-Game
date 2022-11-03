import random
class Character:

    def __init__(self, type, name, specialty, damage):
        self.data = []
        self.type = type
        self.name = name
        self.training = ""
        self.specialty = specialty
        self.health = ""
        self.xp = 10.0
        self.damage = damage
        self.base_health = 10



    Character_Types = ["Farmer","Hunter","Warrior"]

    Warrior_Trainings = ["Cavalry","Archer","Swordsman"]

    @classmethod
    def getcharactertypes(cls):
        return cls.Character_Types

    @classmethod
    def getwarriortrainings(cls):
        return cls.Warrior_Trainings

    def ChangeCharacterType(self, type):
        while not type in Character.Character_Types:
            print("Sorry please type in your selection like from the list given")
            print(Character.getcharactertypes())
            type=input()
        self.type = type

    def NameCharacter(self, name):
        self.name = name

    def ChooseTraining(self, training):
        while not training in Character.Warrior_Trainings:
            print("Sorry please type in your selection like from the list given")
            print(Character.getwarriortrainings())
            training = input()
        self.training = training

    def FailedTraining(self):
        if player.Warrior_Trainings == []:
            print("It looks like the path of the warrior isn't for you.")
            player.Character_Types.remove("Warrior")
            print("Pick a different character.")
            print("What type of character would you like to play as?")
            print("Character Types:", Character.getcharactertypes())
            player.ChangeCharacterType(input())
            player.specialty = "failed"
    
    def CavalryTraining(self):
            choice = input('Choose a number between one and four.\n')
            while choice.isnumeric() == False:
                print("Please select a number")
                choice = input()
            choice = int(choice)
            success = random.randint(1,4)
            if success == choice:
                print("Congratulations! You are now a member of the cavalry!")
                self.specialty = 'Cavalry'
            elif success != choice:
                print("You fell off your horse. Pick a different specialty.")
                player.Warrior_Trainings.remove('Cavalry')
                self.FailedTraining()

    def ArcheryTraining(self):
            choice = input('Choose a number between one and two.\n')
            while choice.isnumeric() == False:
                print("Please select a number")
                choice = input()
            choice = int(choice)
            success = random.randint(1,2)
            if success == choice:
                print("Congratulations! You are now a member of the archery!")
                self.specialty = 'Archer'
            elif success != choice:
                player.Warrior_Trainings.remove('Archer')
                print("You missed the target. Pick a different specialty.")
                self.FailedTraining()


    def SwordsmanTraining(self):

            choice = input('Choose a number between one and ten.\n')          
            while choice.isnumeric() == False:
                print("Please select a number")
                choice = input()
            choice = int(choice)
            success = random.randint(1,10)               
            if success != choice and choice >= 1 and choice <= 10:
                print("Congratulations! You are now a member of the army!")
                self.specialty = 'Swordsman'
            elif success == choice or choice < 1 or choice > 10:
                print("You dropped your sword. Pick a different specialty.")               
                player.Warrior_Trainings.remove('Swordsman')
                self.FailedTraining()
    
    def GetSpecialty(self):
        global specialty
        specialty = player.specialty
        return specialty

    def SetBaseHealth(self):
        global specialty
        if specialty == 'Cavalry':
            self.health = 80
            self.base_health = 80
        elif specialty == 'Archer':
            self.health = 50
            self.base_health = 50
        elif specialty == 'Swordsman':
            self.health = 20
            self.base_health = 20

    

    def SetDamage(self):
        global specialty
        if specialty == 'Cavalry':
            self.damage = 25
        elif specialty == 'Archer':
            self.damage = 15
        elif specialty == 'Swordsman':
            self.damage = 5

if __name__ == "__main__":

    x=""

    player = Character("","","","")

    print("What type of character would you like to play as?")
    print("Character Types:", Character.getcharactertypes())
    player.ChangeCharacterType(input())
 
    
    while x != "y":
        player.NameCharacter(input("What would you like your character's name to be\n"))
        print(f"So your name is {player.name} then?")
        x=input("[y/n]\n")
    x=""

    print(f"You have chosen to play as a {player.type} named {player.name}")

    if player.type == 'Warrior':
        while player.specialty == "":
            print("What would you like to train as?")
            print("Training Options:", Character.getwarriortrainings())
            player.ChooseTraining(input(""))
            print(f'This is what training is set to: {player.training}')
            if player.training == 'Cavalry':
                player.CavalryTraining()

            elif player.training == 'Archer':
                player.ArcheryTraining()
            
            elif player.training == 'Swordsman':
                player.SwordsmanTraining()

        if player.specialty != "" and player.specialty != "failed":
            player.GetSpecialty()
            from combat import *
            player.SetBaseHealth()
            player.SetDamage()
            warrior = Battle(player.base_health, player.health, player.damage, "", player.name, player.xp, player.specialty)
            warrior.ChooseEnemy()
            #warrior.FightSequence()


        
            
    if player.type == 'Farmer':
        print('Now you are a farmer')

    if player.type == 'Hunter':
        print('Now you are a hunter')



