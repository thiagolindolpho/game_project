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
import pandas as pd
from save_game import save_game

def main_menu():
    gold_bag = 1000
    while True:
        print("   --MAIN MENU--\n")
        print(" - type 1 for: start new game\n"
              " - type 2 for: load_game\n"
              " - type 3 for: quit\n\n")

        command = input("command: \n")

        if command == "1":
            ingame_hero_list = character_select()
            print(ingame_hero_list)
        elif command == "2":
            saved_heros_list = []
            saved_games_csv = pd.read_csv("saved_games")
            for index, row in saved_games_csv.iterrows():
                print(f"{index} - {row["name"]}")
                saved_heros_list.append(
                    {"name": row["name"],
                     "class": row["class"],
                     "damage_type": row["damage_type"],
                     "damage": row["damage"],
                     "health": row["health"],
                     "armor": row["armor"],
                     "magic_resistance": row["magic_resistance"],
                     "health_regen": row["health_regen"],
                     "backpack": [],
                     "level": row["level"]}
                )

            command = int(input("qual jogo deseja carregar?: "))

            ingame_hero_list = saved_heros_list[command]

            for i in range(0, 5):
                purchased_item = shop(gold_bag)
                gold_bag -= purchased_item["price"]
                ingame_hero_list = item_equip(purchased_item, ingame_hero_list)
                ingame_hero_list = update_hero(ingame_hero_list)
                save_hero = ingame_hero_list[0]
                save_game(save_hero)
                print(ingame_hero_list)
                map_selected = map_select()
                print(map_selected)
                gold_bag += combat_start(map_selected, ingame_hero_list, i)
                i += 1

            return None

        elif command == "3":
            print("exit")
            break
        else:
            print("erro inesperado,\ntenha certeza que o comando que digitou existe\n")

        for i in range(0, 5):
            purchased_item = shop(gold_bag)
            gold_bag -= purchased_item["price"]
            ingame_hero_list = item_equip(purchased_item, ingame_hero_list)
            ingame_hero_list = update_hero(ingame_hero_list)
            save_hero = ingame_hero_list[0]
            save_game(save_hero)
            print(ingame_hero_list)
            map_selected = map_select()
            print(map_selected)
            gold_bag += combat_start(map_selected, ingame_hero_list, i)
            i += 1


        return None

main_menu()
