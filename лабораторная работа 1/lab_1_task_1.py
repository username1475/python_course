numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum = 0
for i in range(len(numbers)):
    if type(numbers[i]) == int:
        sum += numbers[i]
average = sum/len(numbers)
i = 0
while i < len(numbers):
    if numbers[i] is None:
        numbers[i] = average
        i = len(numbers)
    i += 1
print("Измененный список:", numbers)