def choose_character():
    print("""
    Welcome adventurer, choose your avatar (1-3):
    1. Human Warrior - Straight forward, strong and durable.
    2. Elf Healer - Below average health and power, chance to heal self.
    3. Halfling Rogue - Low health, high power, very hard to hit.
    """)

    user_choice = input("Who do you choose (1-3)?\n")
        if user_choice == "1":
            player = warrior
        elif user_choice == "2":
            player = healer
        elif user_choice == "3":
            player = rogue
        else:
            print("Your choices are 1, 2, or 3 only.")