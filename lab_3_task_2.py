# TODO Напишите функцию find_common_participants
def find_common_participants(strng1, strng2, splt = ','):
    strng1 = strng1.split(splt)
    strng2 = strng2.split(splt)
    group = []
    for person in strng1:
        if person in strng2:
            group.append(person)
    return sorted(group)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
