users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
presence = {"Общее количество" : 0, "Уникальные посещения": 0}
presence["Общее количество"] = len(users)
uniq = set(users)
presence["Уникальные посещения"] = len(uniq)
print(presence)
