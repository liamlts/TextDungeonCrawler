#ABOUT:

#This game was for an intro to scripting class I had to take back in January of 2023.

#The Elder Scrolls Daggerfall inspired many aspects/themes of this game.
#The goal of this game is to defeat the Necromancer Lord. To do this you need to obtain the key. The only way to get the key is to defeat the minotaur.
#Upon defeating the minotaur the key will drop, you can pick it up to unlock the Throne Room where the boss battle will take place
#The dagger, sword and bandage are all in game but can only be obtained by killing the enemies in the various rooms. Spider drop bandages, zombies drop the dagger and skeletons drop sword.
from os import system, name
import random

#this allows for a random generic enemy to spawn when we want an enemy to spawn that is not a boss.
#Moved generic_enemies list into this function to avoid it sitting in ram all game long. Now the list is created only when our game needs to spawn a random enemy
def get_random_enemy():
    generic_enemies = ["giant spider", "zombie", "skelton warrior", "giant spider", "zombie", "zombie", "giant spider", "giant spider", "giant spider", "giant spider"]
    random_enemy = random.randint(0, len(generic_enemies)-1)
    return generic_enemies[random_enemy]

def get_enemy_health(enemy):
    enemy_health = 0
    if enemy == "giant spider":
        enemy_health = 10
    elif enemy == "zombie":
        enemy_health = 30
    elif enemy == "skelton warrior":
        enemy_health = 60
    elif enemy == "Minotaur":
        enemy_health = 80
    return enemy_health

#Use weapon in inventory or nothing if player has no weapon
def no_weapon():
    move = input("Your Move: {punch / kick / jab} > ")
    damage = 0
    if move == 'punch':
        hit_chance = random.randint(1, 100)
        if hit_chance <= 10:
            print("You attempt to land your punch but... YOU MISS!!!")
        else:
            damage = random.randint(0, 20)
            print(f'HIT WITH: {damage} points of damage')
    elif move == "kick":
        hit_chance = random.randint(1, 100)
        if hit_chance <= 60:
            print("MISS: you fumble your kick and miss!!!")
        else:
            damage = random.randint(0, 40)
            print(f'HIT WITH: {damage} points of damage')
    elif move == "jab":
        hit_chance = random.randint(1, 100)
        if hit_chance <= 4:
            print("MiSS: somehow you miss your jab")
        else:
            damage = random.randint(0, 10)
            print(f'HIT WITH: {damage} points of damage')
    else:
        print("INVALID MOVE: YOUR TURN HAS BEEN FORFIETTED")
    return damage

#If the player has a dagger this function will run
def use_dagger():
    move = input("Your Move: {stab / slash / swing} > ")
    damage = 0
    if move == 'stab':
        hit_chance = random.randint(1, 100)
        if hit_chance <= 20:
            print("You attempt to stab but... YOU MISS!!!")
        else:
            damage = random.randint(0, 70)
            print(f'HIT WITH: {damage} points of damage')
    elif move == "slash":
        hit_chance = random.randint(1, 100)
        if hit_chance <= 80:
            print("MISS: you opponent dodge your slash!!!")
        else:
            damage = random.randint(0, 90)
            print(f'HIT WITH: {damage} points of damage')
    elif move == "swing":
        hit_chance = random.randint(1, 100)
        if hit_chance <= 10:
            print("MISS: somehow you miss your jab")
        else:
            damage = random.randint(0, 60)
            print(f'HIT WITH: {damage} points of damage')
    else:
        print("INVALID MOVE: YOUR TURN HAS BEEN FORFIETTED")
    return damage

#If the player has a sword this function will run
def use_sword():
    move = input("Your Move: {stab / slash / swing} > ")
    damage = 0
    if move == 'stab':
        hit_chance = random.randint(1, 100)
        if hit_chance <= 20:
            print("You attempt to stab but... YOU MISS!!!")
        else:
            damage = random.randint(0, 90)
            print(f'HIT WITH: {damage} points of damage')
    elif move == "slash":
        hit_chance = random.randint(1, 100)
        if hit_chance <= 80:
            print("MISS: you opponent dodges your slash!!!")
        else:
            damage = random.randint(0, 100)
            print(f'HIT WITH: {damage} points of damage')
    elif move == "swing":
        hit_chance = random.randint(1, 100)
        if hit_chance <= 10:
            print("MISS: you miss your swing")
        else:
            damage = random.randint(0, 80)
            print(f'HIT WITH: {damage} points of damage')
    else:
        print("INVALID MOVE: YOUR TURN HAS BEEN FORFIETTED")
    return damage


def enemy_attack(enemy):
    damage_delt = 0
    if enemy == "giant spider":
        print("giant spider: HISSSSSSS 'bites'")
        damage_delt = random.randint(0, 9)
        print(f"{enemy}'s fangs shred into your flesh and deal {damage_delt} points of damage")
        print("------------------------------")
    elif enemy == "zombie":
        print("zombie: arrrrugghhhh 'pummels'")
        damage_delt = random.randint(0, 15)
        print(f'{enemy} hits you for {damage_delt} damage points')
        print("------------------------------")
    elif enemy == "skelton warrior":
        print("skelton warrior: raaaaaugggghghh 'swings axe'")
        damage_delt = random.randint(0, 45)
        print(f"{enemy}'s sword comes down and hits you for {damage_delt} damage points")
        print("------------------------------")
    elif enemy == "Minotaur":
        print("Minotaur ROARS!!!! 'swings gaint hammer'")
        damage_delt = random.randint(0, 63)
        print(f"{enemy}'s hammer comes down and hits you for {damage_delt} damage points")
        print("------------------------------")
    return damage_delt


def combat(player_health, enemy, inventory):
    enemy_health = get_enemy_health(enemy)
    clear_screen()
    print("**** COMABT ****")

    while player_health > 0 and enemy_health > 0:
        print(f'CURRENTLY IN COMBAT WITH {enemy} WITH {enemy_health} HEALTH')
        #player turn against enemy
        if 'sword' in inventory:
            enemy_health-=use_sword()
        elif 'dagger' in inventory:
            enemy_health-=use_dagger()
        else:
            enemy_health-=no_weapon()
        #AI turn against player, only attack if they acutally have health left.
        if enemy_health >= 0:
            player_health-=enemy_attack(enemy)
        if player_health <= 0:
            clear_screen()
            print("GAME OVER. You died.")
            exit()
    return player_health

#Allows player to heal only if their health is under 100 and they have bandages.
def player_heal(inventory):
    amount_heal = 0
    if "bandage" in inventory:
        amount_heal += 15
        clear_screen()
        print(f"You heal {amount_heal} Health Points")
    else:
        clear_screen()
        print("You need bandages to heal")
    return amount_heal

#this element to my game is very important as it forces an acutal challege in the game
#to get the key for example one must defeat the mini boss which then unlocks the final boss
#to get the sword one must kill a skelton. To get a dagger that is dropped by zombies and finally bandages are dropped by spiders.
def generate_loot(dead_enemy):
    if dead_enemy == "dead Minotaur":
        print()
        print("'CLANG!!!' as the Minotuar falls a gold key falls to the gound as well")
        print()
        return "key"
    elif dead_enemy == "dead skelton warrior":
        print("The skeleton drops his sword")
        return "sword"
    elif dead_enemy == "dead zombie":
        print("It looks like the zombie had a dagger")
        return "dagger"
    elif dead_enemy == "dead giant spider":
        return "bandage"
    else:
        return ""

#TODO make and actual endgame
def end_game(player_health, inventory):
    clear_screen()
    print("as you enter the Throne Room The Necromancer Lord awakens...")
    print("**** BOSS BATTLE ****")
    boss_health = 100
    boss_deal_damage = 0

    while player_health > 0 and boss_health > 0:
        #player turn
        if "sword" in inventory:
            boss_health-=use_sword()
        elif "dagger" in inventory:
            boss_health-=use_dagger()
        else:
            boss_health-=no_weapon()
        #BOSS TURN make sure the boss has health to fight
        if boss_health >= 0:
            spells = ["Fire Ball", "Ice Storm", "Lightening"]
            spell_to_use = random.randint(0, len(spells)-1)
            if spells[spell_to_use] == "Fire Ball":
                print("Necromancer Lord casts a massive fireball toward your face")
                boss_deal_damage = random.randint(0, 30)
                print(f'The fireball hits you for {boss_deal_damage} points')
                player_health -=boss_deal_damage
                print("--------------------------------")
            elif spells[spell_to_use] == "Ice Storm":
                print("Necromancer Lord casts a giant ice strom toward your general direction")
                boss_deal_damage = random.randint(0, 70)
                print(f'The ice storm bombards you and makes you lose {boss_deal_damage} points of health')
                print("--------------------------------")
            elif spells[spell_to_use] == "Lightening":
                print("Bolts of electricity fly our from the Necromancer's hands")
                boss_deal_damage = random.randint(0, 40)
                print(f'Electricity hits you and deals {boss_deal_damage} points of damage')
                print("--------------------------------")
        if player_health <= 0:
            print("You have been defeated by the Necromancer Lord. Your story ends here")
            exit()
        elif boss_health <= 0:
            print("-----------------------------")
            print("As the Necromancer Lord collapses a doorway leading to the surface opens... You have found your escape.")
            print("You Win!")
            exit()

#For better UX we can clear screen to reduce clutter. This function also allows the game to be portable across UNIX(Linux/MacOS) and Windows Operating systems.
def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def game_main():
    player_health = 100
    #this is our map
    rooms = {
        'Cave Enterance': {'East': 'Catacombs'},
        'Crypt': {'East': 'Abyss', 'South': 'Catacombs'},
        'Abyss': {'West': 'Crypt'},
        'Catacombs': {'West': 'Cave Enterance', 'East': 'Dining Hall', 'North': 'Crypt', 'South': 'Armory'},
        'Dining Hall': {'North': 'Throne Room', 'West': 'Catacombs'},
        'Armory': {'North': 'Catacombs', 'East': 'Labyrinth'},
        'Throne Room': {'South': 'Dining Hall'},
        'Labyrinth': {'West': 'Armory'}
    }

    #keep track of enemies and items in each room. Use list to allow nice and easy add/remove item and enemies as needed throughout game
    #side note: I had to reduce randomness as now that weapons are only accessible after killing enemy the odds can be very hard against the player
    #if the player has bad luck. So to remedy this I made certian spawns hard coded.
    room_contents = {
        'Cave Enterance': {'enemies': [], 'items': []},
        'Crypt': {'enemies': ['zombie'], 'items': []},
        'Abyss': {'enemies': [get_random_enemy()], 'items': []},
        'Catacombs': {'enemies': [get_random_enemy()], 'items': []},
        'Dining Hall': {'enemies': [get_random_enemy()], 'items': []},
        'Armory': {'enemies': ["skelton warrior"], 'items': ['Chest Plate', 'Helmet']},
        'Throne Room': {'enemies': ['Necromancer Lord'], 'items': []},
        'Labyrinth': {'enemies': ['Minotaur'], 'items': []},
    }

    inventory = []

    user_input = '-'

    current_location = 'Cave Enterance'

    while (user_input != 'q') and (user_input != "exit"):

        possible_moves = list(rooms[current_location].keys())

        possible_moves = ' | '.join(possible_moves)

        print(f'You are currently in the {current_location}')
        print(f'Inventory: {inventory}')
        print('-------------------------------------------')
        print(f'There are doors leading: {possible_moves}')
        print()
        print("Enter your move")
        user_input = input("[go (Direction) / get (Item) / look / attack]> ")

        user_input = user_input.split()

        #USER INPUT PARSING AND RESPONSE BELOW
        if len(user_input) == 2:
            command = user_input[0]
            args = user_input[1]

            if command == 'go' and args in possible_moves:
                #Player tried to trigger end game fight without having key, make sure they need to have key to get into throne room
                if rooms.get(current_location, {}).get(args, current_location) == "Throne Room" and "key" not in inventory:
                    clear_screen()
                    print("You try to push the doors open but they won't budge, to enter looks like you need a key...")
                #IF the player has killed the minotaur and picked up they key the end game will be available.
                elif rooms.get(current_location, {}).get(args, current_location) == "Throne Room" and "key" in inventory:
                    #Put the player in the endgame room
                    current_location = rooms.get(current_location, {}).get(args, current_location)
                    #Start the boss fight
                    end_game(player_health, inventory)
                else:
                    #current_location = rooms[current_location][args] --> this also works but produces key error so we used line below to avoid a runtime crash
                    current_location = rooms.get(current_location, {}).get(args, current_location) #--> this call will instead return cur location to avoid crashing when a keyError would occur
                    clear_screen()
            else:
                clear_screen()
                print("Cannot go that way")
        #get item command and response
        elif len(user_input) == 1 and user_input[0] == 'get':
            items_in_room = room_contents[current_location]['items']
            if len(items_in_room) <= 0:
                clear_screen()
                print("There is nothing to get in this room")
            else:
                clear_screen()
                inventory.append(items_in_room[0])
                print(f'added {items_in_room[0]} to inventory')
                room_contents[current_location]['items'].remove(items_in_room[0])
        #look around command and response
        elif len(user_input) == 1 and user_input[0] == 'look':
            clear_screen()
            room_enemies = room_contents[current_location]['enemies']
            room_items = room_contents[current_location]['items']
            #Armor will increase the player health by a large amount
            if 'Chest Plate' or 'Helmet' in inventory:
                if 'Chest Plate' in inventory:
                    player_health+=40
                    clear_screen()
                    inventory.remove('Chest Plate')
                    print("You equip the Chest Plate")
                elif 'Helmet' in inventory:
                    player_health+=30
                    inventory.remove('Helmet')
                    print("You equip the Helmet")
            print(f'Enemies in room: {", ".join(room_enemies)}')
            print(f'Items in room: {", ".join(room_items)}')
            if player_health < 100 and "bandage" in inventory:
                choice = input(f"You health is low would you like to heal? {player_health} out of 100 (Y/n): ")
                if choice.lower() == 'y':
                    player_health+=player_heal(inventory)
                    if player_health > 100:
                        player_health = 100
                    inventory.remove("bandage")
                    print("bandage has been removed from your inventory")
                    print(f"Your health is now {player_health} HP")
            else:
                print(f'HEALTH {player_health} HP')
        #attack command and response
        elif len(user_input) == 1 and user_input[0] == 'attack':
            room_enemies = room_contents[current_location]['enemies']
            if len(room_enemies) <= 0 or "dead" in room_enemies[0]:
                clear_screen()
                print('Nothing to attack')
            else:
                #one enemy per room
                room_enemy = room_contents[current_location]['enemies'][0]
                clear_screen()
                player_health = combat(player_health, room_enemy, inventory)
                room_contents[current_location]['enemies'][0] = f"dead {room_enemy}"
                #spawn in loot after enemy is killed player uses get to pick up
                loot = generate_loot(f"dead {room_enemy}")
                if loot == "key":
                    room_contents[current_location]['items'].append(loot)
                elif loot == "sword":
                    room_contents[current_location]['items'].append(loot)
                elif loot == "dagger":
                    room_contents[current_location]['items'].append(loot)
                elif loot == "bandage":
                    room_contents[current_location]['items'].append(loot)
        elif len(user_input) <= 0:
            clear_screen()
        elif user_input[0] not in ["q", "exit", "go", "look", "get"]:
            clear_screen()
            print('Invalid input')
        else:
            clear_screen()
        #END USER INPUT PARSING
        user_input = ' '.join(user_input)
    print("Thanks for playing, goodbye!")

game_main()
