import pandas as pd

from items import item_list

items_save = pd.DataFrame(item_list)
items_save.to_csv("save_game")

total_bonus_dmg = 0

for item in item_list:
    if item["type"] == "attack" and item["damage_type"] == "physical":
        total_bonus_dmg += item["damage"]
        
print(total_bonus_dmg)