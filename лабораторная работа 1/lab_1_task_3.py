list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
half = len(list_players)//2
first = list_players[:half]
second = list_players[half:]
print(first)
print(second)
