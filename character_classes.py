class Character:

    def __init__(self, type, name):
        self.data = []
        self.type = type 
        self.name = name

    Character_Types = {"Farmer","Hunter","Warrior"}

    @classmethod
    def getcharactertypes(cls):
        return cls.Character_Types

    def ChangeCharacterType(self, type):
            self.type = type
    def NameCharacter(self, name):
        self.name = name
    

if __name__ == "__main__":
    x=""

    player = Character("","")

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