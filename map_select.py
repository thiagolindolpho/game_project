from middleware import verify_quantity
from maps import map_list
def map_select():
    map_quantity = verify_quantity(map_list)

    if map_quantity:
        return map_list[0]
    print("   --MAP SELECT --\n")
    print("mapas disponiveis: \n")
    for i in range(len(map_list)):
        print(f"{i + 1} - {map_list[i]["name"]}")

    command = int(input("\ndigite o index do mapa que quer jogar: ")) - 1

    for i in range(len(map_list)):
        if command == i:
            print(f"\n - mapa selecionado: {map_list[i]["name"]}")
            map = map_list[i]
            return map
        else:
            print("houve algum erro inesperado, talvez o indice não exista\n")