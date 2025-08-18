from attack import attack
from middleware import verify_quantity
from enemys import enemy_list
from update_life import update_life


def combat_start(map, hero, index_monster):

    print(f" - enemy: {enemy_list[index_monster]["name"]}")
    hero_team = verify_quantity(hero)

    encounters = map["encounters"]
    life_monster = enemy_list[index_monster]["health"]


    dmg_hero = 0
    monster_dmg = 0

    print("Iniciando Combate")

    if hero_team:
        while True:
            if encounters == 0:
                break

            print(f"--turno de {hero[0]["name"]}--")
            print(f"Monster position: {encounters}, life {life_monster}")
            print("1 - attack\n")
            hero_action = input(
                f"que ação deseja executar contra {enemy_list[index_monster]["name"]}?\n"
            )
            print(f"Encontros: {encounters}\n")

            if life_monster - dmg_hero <= 0:
                encounters -= 1
                print("Monster has ben killed.\n")
                life_monster = enemy_list[index_monster]["health"]
                continue

            if hero_action == "1":
                dmg_hero = attack(hero[0], enemy_list[index_monster])
                life_monster -= dmg_hero
                print(f"Monster Life on attack:, {life_monster}")

            print(f" --turno de {enemy_list[index_monster]["name"]}--")

            if hero[0]["health"] - enemy_list[index_monster]["damage"] <= 0:
                print(f"{enemy_list[index_monster]["name"]} ganhou o combate!")

            monster_dmg = attack(enemy_list[index_monster], hero[0])
            hero[0]["health"] -= monster_dmg
            print(f"hero Life on attack:, {hero[0]["health"]}")




            # print(f"vez de {enemy["name"]}")
            # dmg = attack(enemy, hero_team)
            # hero_team["health"] - dmg
            # if hero_team["health"] < 0:
            #     break


"""   
    while True:

        command = input("\ndigite o indice do herói que deseja usar: \n")
        print('1 - attack\n')
        hero_action = input(f"que ação deseja executar contra {enemy["name"]}?")

        if hero_action == "1":
            for i in range(len(ingame_hero_list)):
                hero_selected = ingame_hero_list[i]
                if command == i:
                    enemy["health"] = attack(hero_selected, enemy)
                    print(enemy["health"])
                else:
                    print("erro inesperado")
        else:
            print("essa ação não existe")
 """
