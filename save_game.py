import pandas as pd


def save_game(hero):
    saved_hero = hero
    saved_games_csv = pd.read_csv("saved_games")
    saved_games_list = []

    for index, row in saved_games_csv.iterrows():
        saved_games_list.append(
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

    saved_games_list.append(
        {"name": saved_hero["name"],
         "class": saved_hero["class"],
         "damage_type": saved_hero["damage_type"],
         "damage": saved_hero["damage"],
         "health": saved_hero["health"],
         "armor": saved_hero["armor"],
         "magic_resistance": saved_hero["magic_resistance"],
         "health_regen": saved_hero["health_regen"],
         "backpack": [],
         "level": saved_hero["level"]}
    )

    pd.DataFrame(saved_games_list).to_csv("saved_games")