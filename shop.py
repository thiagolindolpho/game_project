from items import item_list

def shop(gold_bag):
    print("   --SHOP--\n")
    print(f"\n - ouro disponivel: {gold_bag}\n")

    #mostra os itens
    for i in range(len(item_list)):
        item = item_list[i]
        if item["type"] == "attack":
            print(f"{i + 1} - {item["name"]}, damage: {item["damage"]}, gold: {item["price"]}")
        elif item["type"] == "defense":
            print(f"{i + 1} - {item["name"]}, armor: {item["armor"]}, gold: {item["price"]}")

    #coleta o index do item que deseja e procura na lista de itens,
    # faz checagem se o gold é suficiente para compra

    command = int(input("digite o index do item que quer comprar: "))
    if gold_bag >= item_list[command - 1]["price"]:
        return item_list[command - 1]
    return "erro"
"""
    #mostra cada heroi da lista e o indice de cada heroi na lista
    for i in range(len(ingame_hero_list)):
        hero = ingame_hero_list[i]
        print(f"{i + 1} - {hero["name"]}")

    #coleta informação que corresponde ao indice do herói e faz uma checagem
    #para ver se é um indice disponivel
    command2 = int(
        input("\na qual heroi deseja atribuir o item?\n"
              "digite o numero que corresponde o posição do heroi: "))

    if command2 > 4 or command2 < 1:
        print("é preciso digitar um número entre 1 e 4.")
        return None

    #atribui o item ao herói e subtrai o gold pelo valor do item
    for i in range(len(item_list)):
        if int(command) - 1 == i:
            ingame_hero_list[command2 - 1]["backpack"].append(item_list[i])
            gold_bag -= item_list[i]["price"]

            print(f"ouro atualizado: {gold_bag}\n")
            print(ingame_hero_list)
"""