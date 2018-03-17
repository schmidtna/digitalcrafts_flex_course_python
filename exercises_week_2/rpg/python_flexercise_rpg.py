import random


class Character:
    def __init__(self, health, power, creature_type, dodge):
       self.health = health
       self.power = power
       self.creature_type = creature_type
       self.dodge = dodge

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        hit_chance = random.randint(1, 10)
        if hit_chance > enemy.dodge:
            enemy.health -= self.power
            print("The {} deals {} damage to the {}!!".format(self.creature_type,self.power, enemy.creature_type))
            if enemy.alive == False:
                print("{} has killed {}!")

    def crit_atk_20(self, enemy):
        hit_chance = random.randint(1, 10)
        if hit_chance > enemy.dodge:
            crt_chance = random.randint(1, 100)
            if crt_chance >= 80:
                enemy.health -= self.power * 2
                print("Critical hit! You deal {} damage to the {}!!".format(self.power * 2, enemy.creature_type))
            else:
                enemy.health -= self.power
                print("The {} deals {} damage to the {}!!".format(self.creature_type,self.power, enemy.creature_type))
            
            if enemy.alive == False:
                print("You have killed the {}!".format(enemy.creature_type))




    def status(self):
        print("The {} has {} health remaining and {} attack power.".format(self.creature_type, self.health, self.power))


def player_death():
    if hero.alive == False:
        print("You were slain by the {}!".format(goblin.creature_type))
    else:
        pass
        
class Hero(Character):
    pass

class Healer(Character):
    def __init__(self,health, power, creature_type, dodge, heal):
        self.heal = heal
        super().__init__(health, power, creature_type, dodge)

    def heal_spell(self):
        heal_chance = random.randint(1, 100)
        if heal_chance >= 80:
            self.health += self.heal
            print("Your magic has healed you for {} points!".format(self.heal))
        else:
            pass

class Monster(Character):
    pass

## player classes ##
warrior = Hero(10, 5, "Human Warrior", 0)
healer = Healer(8, 2, "Elf Healer", 0, 2)
rogue = Hero(5, 6, "Halfling Rogue", 9)

## monsters ##
goblin = Monster(6, 2, "Goblin", 0)
shadow = Monster(1, 3, "Shadow Beast", 9)



def rpg_battle():
    print("You, the {} have been attacked by a {}!".format(player.creature_type, enemy.creature_type))
    while player.alive() and enemy.alive():
        print("""
        What do you do?!

        1. Attack the {}!!
        
        2. Do nothing
        
        3. Run away!\n""".format(enemy.creature_type))
        player.status()
        enemy.status()

        user_choice = input("What do you do (1-3)?\n")
        if user_choice == "1":
            player.crit_atk_20(enemy)
        elif user_choice == "2":
            print("You stare quizzically at the {}".format(enemy.creature_type))
            pass
        elif user_choice == "3":
            print("You flee in terror before your foe!")
            break
        else:
            print("Your choices are 1, 2, or 3 only.")

        if enemy.alive():
            enemy.attack(player)

            if player.alive == False:
                player_death()

        else:
            print("You have slain the {}!".format(enemy.creature_type))
        

if __name__ == "__main__":
    rpg_battle()


