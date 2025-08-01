def attack(attacker, target):
    if attacker["damage_type"] == "physical":
        if target["armor"] >= attacker["damage"]:
            print(f"{attacker["name"]} causou {0} de dano a {target["name"]}")
            return 0
        elif target["armor"] < attacker["damage"]:
            dmg = attacker["damage"] - target["armor"]
            print(f"{attacker["name"]} causou {dmg} de dano a {target["name"]}")
            dmg_taken = target["health"] - dmg
            return dmg_taken
        else:
            print("ocorreu um erro inesperado")
            return 0

    elif attacker["damage_type"] == "magic":
        if target["magic_resistance"] >= attacker["damage"]:
            print(f"{attacker["name"]} causou {0} de dano a {target["name"]}")
            return 0
        elif target["armor"] < attacker["damage"]:
            dmg = attacker["damage"] - target["magic_resistance"]
            print(f"{attacker["name"]} causou {dmg} de dano a {target["name"]}")
            dmg_taken = target["health"] - dmg
            return dmg_taken
        else:
            print("ocorreu um erro inesperado")
            return 0