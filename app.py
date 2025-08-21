from enemys import enemy_list
from heros import hero_list
from shop import shop
from maps import map_list
from map_select import map_select
from items import item_list
from combat_start import combat_start
from attack import attack
from character_select import character_select
from item_equip import  item_equip
from middleware import verify_quantity
from update_hero import update_hero

def main_menu():
    gold_bag = 1000
    levels = ["1", "2", "3", "4", "5"]
    while True:
        print("   --MAIN MENU--\n")
        print(" - type 1 for: start new game\n"
              " - type 2 for: quit\n\n")

        command = input("command: \n")

        if command == "1":
            ingame_hero_list = character_select()
            print(ingame_hero_list)
        elif command == "2":
            print("exit")
            break
        else:
            print("erro inesperado,\ntenha certeza que o comando que digitou existe\n")


        purchased_item = shop(gold_bag)
        gold_bag -= purchased_item["price"]
        ingame_hero_list = item_equip(purchased_item, ingame_hero_list)
        ingame_hero_list = update_hero(ingame_hero_list)
        print(ingame_hero_list)
        map_selected = map_select()
        print(map_selected)
        gold_bag += combat_start(map_selected, ingame_hero_list, 0)


        #print(ingame_hero_list)
        #purchased_item = shop(gold_bag)
        #gold_bag -= purchased_item["price"]
        #ingame_hero_list = item_equip(purchased_item, ingame_hero_list)
        #ingame_hero_list = update_hero(ingame_hero_list)
        #print(ingame_hero_list)
        #gold_bag += combat_start(map_selected, ingame_hero_list, 1)

        return None

main_menu()
