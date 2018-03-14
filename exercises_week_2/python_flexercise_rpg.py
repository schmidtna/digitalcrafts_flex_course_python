class Character:
    def __init__(self, health, power, creature_type):
       self.health = health
       self.power = power
       self.creature_type = creature_type

    def alive(self):
        if self.health > 0
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print("You deal {} damage to the goblin.".format(self.power))
        if enemy.alive = False
            print("You have killed {}")

    def status(self):
        print()


class Hero(Character):
    pass

class Goblin(Character):
    pass


