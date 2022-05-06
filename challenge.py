import json 

with open("playerlist.json") as file:
    players = json.load(file)['values']

def sum_player_height(height_input: int, players: list):
    auxiliar_list = []
    auxiliar_height = 0
    print(f'Auxiliar height -> {auxiliar_height}')
    count = 0
    while True:
        for index, player in enumerate(players):
            auxiliar_list.append(player)
            auxiliar_height += int(player['h_in'])
            if index != 0 and auxiliar_height != height_input:
                auxiliar_list.remove(player)
                auxiliar_height -= int(player['h_in'])
            if index == len(players) and auxiliar_height != height_input:
                players.remove(auxiliar_list[0])
                sum_player_height(height_input)
        if len(auxiliar_list) == 2 and auxiliar_height == height_input:
            print(f'Matches found {auxiliar_list}')
            break
        else:
            print("No matches where found")
