def update_life(hero, hero_index, monster, index_monster, monster_life):
    print(f"vida de {hero[hero_index]["name"]}: {hero[hero_index]["health"]}")
    print(f"vida de {monster[index_monster]["name"]}: {monster_life}/{monster[index_monster]["health"]}")
