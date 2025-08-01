from middleware import verify_quantity

def item_equip(item, hero):
    condition = verify_quantity(hero)

    if condition:
        hero[0]["backpack"].append(item)
        return hero
    return "erro"