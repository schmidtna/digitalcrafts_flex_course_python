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

class Goblin(Character):
    pass

hero = Hero(10, 5, "Human Warrior", 0)
healer = Healer(8, 2, "Elf Healer", 0, 2)
shadow = Hero(7, 6, " Halfling Rogue", 9)
goblin = Goblin(6, 2, "Goblin", 0)


def player_death():
    if hero.alive == False:
        print("You were slain by the {}!".format(goblin.creature_type))
    else:
        pass

def rpg_battle():
    print("You, the {} have been attacked by a {}!".format(hero.creature_type, goblin.creature_type))
    while hero.alive() and goblin.alive():
        print("""
        What do you do?!

        1. Attack the {}!!
        
        2. Do nothing
        
        3. Run away!\n""".format(goblin.creature_type))
        hero.status()
        
        goblin.status()

        user_choice = input("What do you do (1-3)?\n")
        if user_choice == "1":
            hero.crit_atk_20(goblin)
        elif user_choice == "2":
            print("You stare quizzically at the {}".format(goblin.creature_type))
            pass
        elif user_choice == "3":
            print("You flee in terror before your foe!")
            break
        else:
            print("Your choices are 1, 2, or 3 only.")

        if goblin.alive():
            goblin.attack(hero)
            if hero.alive == False:
                player_death()

        else:
            print("You have slain the {}!".format(goblin.creature_type))
        

if __name__ == "__main__":
    rpg_battle()


