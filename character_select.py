from heros import hero_list

def character_select():
    ingame_hero_list = []
    print("   --CHARACTER SELECT--\n")
    print(" - type 1 for: magnus\n")
    print(" - type 2 for: erin\n")
    print(" - type 3 for: mikayla\n")
    print(" - type 4 for: neruel\n")

    command = int(input("command: \n"))
    if command > 4 or command < 1:
        return "erro"

    hero = hero_list[command - 1]
    ingame_hero_list.append(hero)

    return ingame_hero_list
