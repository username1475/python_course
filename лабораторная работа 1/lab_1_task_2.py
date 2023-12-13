# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 * 2**(10+10)
pages_in_book = 100
strings_on_page = 50
symbols_in_string = 25
bytes_in_symbol = 4

bytes_in_book = pages_in_book*strings_on_page*symbols_in_string*bytes_in_symbol
num = volume//bytes_in_book
print("Количество книг, помещающихся на дискету:", int(num))