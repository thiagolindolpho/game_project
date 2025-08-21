def update_hero(hero):

    for item in hero[0]["backpack"]:
        if item["type"] == "attack":

            if hero[0]["damage_type"] == "physical":
                for item in hero[0]["backpack"]:
                    hero[0]["damage"] += item["damage"]

                hero[0]["backpack"].pop()

                return hero

            elif hero[0]["damage_type"] == "magic":
                for item in hero[0]["backpack"]:
                    if item["damage_type"] == "magic":
                        hero[0]["damage"] += item["damage"]

                hero[0]["backpack"].pop()

                return hero

        elif item["type"] == "defense":
                    hero[0]["armor"] += item["armor"]

                    hero[0]["backpack"].pop()

                    return hero

        elif item["type"] == "magic_defense":
                    hero[0]["magic_resistance"] += item["magic_resistance"]

                    hero[0]["backpack"].pop()

                    return hero


