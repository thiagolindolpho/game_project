from attack import attack
from middleware import verify_quantity
def combat_start(map, hero, enemy):
    print(f" - enemy: {enemy["name"]}")
    hero_team = verify_quantity(hero)

    if hero_team:
        while True:
            print('1 - attack\n')
            hero_action = input(f"que ação deseja executar contra {enemy["name"]}?")
            if hero_action == "1":
                dmg = attack(hero_team, enemy)
                enemy["health"] - dmg
                if enemy["health"] < 0:
                    break

            print(f"vez de {enemy["name"]}")
            dmg = attack(enemy, hero_team)
            hero_team["health"] - dmg
            if hero_team["health"] < 0:
                break


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