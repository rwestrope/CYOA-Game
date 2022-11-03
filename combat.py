import random

class Enemy:

    def __init__(self, name, health, damage):
        self.data =""
        self.name = name
        self.health = health
        self.damage = damage

    #def InitiateBattle(self):


    def damagedealt(self):
        damagedealt = random.randint(self.damage - 1, self.damage + 2)
        return damagedealt

if __name__ == "__main__":

    Goomba = Enemy("Goomba", 10, 3)

    print("You walked into a battle")
    player.InitiateBattle()
    print("Goomba goes first")
    while current_opponent.health > 0 and player.health > 0:
        player.health = player.health - Goomba.damagedealt()
        print(f"{Goomba.name} dealt {damagedealt}")