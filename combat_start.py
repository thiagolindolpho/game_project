from attack import attack
from middleware import verify_quantity
from enemys import enemy_list

def combat_start(map, hero, index_monster):

    print(f" - enemy: {enemy_list[index_monster]["name"]}")
    hero_team = verify_quantity(hero)

    encounters = map["encounters"]
    life_monster = enemy_list[index_monster]["health"]

    if hero_team:
        while True:
            print('1 - attack\n')
            hero_action = input(f"que ação deseja executar contra {enemy_list[index_monster]["name"]}?")
            if hero_action == "1":
                dmg = attack(hero[0], enemy_list[index_monster])
                life_monster -= dmg

            if life_monster <= 0:
                encounters -= 1
                life_monster = enemy_list[index_monster]["health"]
            
            print("Encontros:", encounters)
            if encounters == 0:
                break

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