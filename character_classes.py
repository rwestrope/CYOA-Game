import random

class Character:

    def __init__(self, type, name, training, specialty):
        self.data = []
        self.type = type 
        self.name = name
        self.training = training
        self.specialty = specialty


    Character_Types = {"Farmer","Hunter","Warrior"}

    Warrior_Trainings = ["Cavalry","Archer","Swordsman"]

    @classmethod
    def getcharactertypes(cls):
        return cls.Character_Types

    @classmethod
    def getwarriortrainings(cls):
        return cls.Warrior_Trainings

    def ChangeCharacterType(self, type):
            self.type = type
    def NameCharacter(self, name):
        self.name = name

    def ChooseTraining(self, training):
        self.training = training

    
    def CavalryTraining(self):
            choice = input('Choose a number between one and four.\n')
            success = random.randint(1,4)
            if success == choice:
                print("Congratulations! You are now a member of the cavalry!")
                self.specialty = 'Cavalry'
            else:
                print("You fell off your horse. Pick a different specialty.")
                player.Warrior_Trainings.remove('Cavalry')

    def ArcheryTraining(self):
            choice = input('Choose a number between one and two.\n')
            success = random.randint(1,2)
            if success == choice:
                print("Congratulations! You are now a member of the archery!")
                self.specialty = 'Archer'
            else:
                print("You missed the target. Pick a different specialty.")
                player.Warrior_Trainings.remove('Archer')

    def SwordsmanTraining(self):
            choice = input('Choose a number between one and ten.\n')
            success = random.randint(1,10)
            if success != choice:
                print("Congratulations! You are now a member of the army!")
                self.specialty = 'Swordsman'
            else:
                print("You dropped your sword. Pick a different specialty.")
                player.Warrior_Trainings.remove('Warrior')
    

if __name__ == "__main__":
    x=""

    player = Character("","","","")

    print("What type of character would you like to play as?")
    print("Character Types:", Character.getcharactertypes())
    player.ChangeCharacterType(input())
 
    while not player.type in Character.Character_Types:
        print("Sorry please type in your selection like from the list given")
        print(Character.getcharactertypes())
        player.type=input()
    while x != "y":
        player.NameCharacter(input("What would you like your character's name to be\n"))
        print(f"So your name is {player.name}?")
        x=input("[y/n]\n")

    print(f"You have chosen to play as a {player.type} named {player.name}")

    if player.type == 'Warrior':
        while player.specialty == "":
            print(f'What would you like to train as?')
            print("Training Options:", Character.getwarriortrainings())
            player.ChooseTraining(input(""))
            if player.training == 'Cavalry':
                player.CavalryTraining()

            elif player.training == 'Archer':
                player.ArcheryTraining()
            
            elif player.training == 'Swordsman':
                player.SwordsmanTraining()

    elif player.type == 'Farmer':
        print('')

    elif player.type == 'Hunter':
        print('')



