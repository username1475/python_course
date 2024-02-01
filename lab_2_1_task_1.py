import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Pen:
    def __init__(self, ink_color: str, percentage_of_remaining_ink: float):
        """
        Создание и подготовка к работе объекта "Ручка"

        :param ink_color: цвет чернил ручки
        :param percentage_of_remaining_ink: остаток чернил в процентах (в новой ручке остаток равен 1, а в полностью использованной - 0)

        Примеры:
        >>> black_pen = Pen('black', 1)  # инициализация экземпляра класса
        """
        if not isinstance(percentage_of_remaining_ink, (int, float)):
            raise TypeError("остаток чернил в процентах должен быть типа int или float")
        if (percentage_of_remaining_ink < 0) or (percentage_of_remaining_ink > 1):
            raise ValueError("остаток чернил в процентах должен быть числом от 0 до 1")
        self.percentage_of_remaining_ink = percentage_of_remaining_ink

        if not isinstance(ink_color, str):
            raise TypeError("цвет чернил ручки должн быть str")
        self.ink_color = ink_color

    def is_empty_pen(self) -> bool:
        """
        Функция которая проверяет является ли ручка полнотсью использованной (т. е. в ней не осталось чернил)

        :return: исписана ли ручка

        Примеры:
        >>> black_pen = Pen('black', 1)
        >>> black_pen.is_empty_pen()
        """
        ...

    def refill_pen(self, new_ink_color: str, remaining_ink: float) -> None:
        """
        Замена стержня ручки.
        :param new_ink_color: цвет чернил в новом стержне
        :param remaining_ink: остаток чернил в процентах в новом стержне


        :raise TypeError: если остаток чернил не является числом, то вызываем ошибку
        :raise ValueError: если остаток чернил не является числом от 0 до 1, то вызываем ошибку
        :raise TypeError: если цвет чернил в новом стержне не является str, то вызываем ошибку

        Примеры:
        >>> black_pen = Pen('black', 1)
        >>> black_pen.refill_pen('blue', 0.5)
        """
        if not isinstance(remaining_ink, (int, float)):
            raise TypeError("остаток чернил в процентах должен быть типа int или float")
        if (remaining_ink < 0) or (remaining_ink > 1):
            raise ValueError("остаток чернил в процентах должен быть числом от 0 до 1")

        if not isinstance(new_ink_color, str):
            raise TypeError("цвет чернил ручки должн быть str")
        ...

class Wireless_headphones:
    def __init__(self, headphones_are_on: bool, charge_level: int, connected_device: str):
        """
        Создание и подготовка к работе объекта "Беспроводные наушники"

        :param headphones_are_on: влючены ли наушники
        :param charge_level: уровень заряда наушников
        :param connected_device: подключенное устройство

        Примеры:
        >>> wireless_headphones = Wireless_headphones(True, 100, 'my_phone')  # инициализация экземпляра класса
        """

        if not isinstance(headphones_are_on, bool):
            raise TypeError("параметр включены ли наушники должен быть bool")
        self.headphones_are_on = headphones_are_on

        if not isinstance(charge_level, int):
            raise TypeError("заряд наушников должен быть типа int")
        if (charge_level < 0) or (charge_level > 100):
            raise ValueError("заряд наушников должен быть числом от 0 до 100")
        self.charge_level = charge_level

        if not isinstance(connected_device, str):
            raise TypeError("подключенное устройство должно быть типа str")
        self.connected_device = connected_device

    def charge_headphones(self, charging_time: float) -> int:
        """
        Зарядка наушников
        :param charging_time: время которое наушники заряжались в минутах

        :raise TypeError: если время которое наушники заряжались не является числом, то вызываем ошибку
        :raise ValueError: если время которое наушники заряжались не является неотрицательным числом, то вызываем ошибку

        :return: уровень заряда наушников

        Примеры:
        >>> wireless_headphones = Wireless_headphones(True, 50, 'my_phone')
        >>> wireless_headphones.charge_headphones(30)
        """
        if not isinstance(charging_time, (int, float)):
            raise TypeError("время которое наушники заряжались в минутах должено быть типа int или float")
        if charging_time < 0:
            raise ValueError("время которое наушники заряжались в минутах должено быть неотрицательным числом")
        ...

    def connect_device(self, new_device: str) -> None:
        """
        Подключение наушников к новому устройству
        :param new_device: название устройства, к которому подключаются наушники

        :raise TypeError: если название подключаемого устройства не является строкой, то вызываем ошибку

        Примеры:
        >>> wireless_headphones = Wireless_headphones(True, 50, 'my_phone')
        >>> wireless_headphones.connect_device("my_bestie's_phone")
        """
        if not isinstance(new_device, str):
            raise TypeError("название устройства, к которому подключаются наушники, должно быть str")
        ...

class Notebook:
    def __init__(self, amount_of_pages: int, lines_per_page: int, number_of_clean_lines: int):
        """
        Создание и подготовка к работе объекта "Блокнот"

        :param amount_of_pages: количество страниц в блокноте
        :param lines_per_page: количество строчек на странице
        :param number_of_clean_lines: количество оставшихся чистых строчек

        Примеры:
        >>> notebook = Notebook(10, 20, 200)  # инициализация экземпляра класса
        """
        if not isinstance(amount_of_pages, int):
            raise TypeError("количество страниц должено быть типа int")
        if amount_of_pages <= 0:
            raise ValueError("количество страниц должено быть положительным числом")
        self.amount_of_pages = amount_of_pages

        if not isinstance(lines_per_page, int):
            raise TypeError("количество строчек на странице должно быть int")
        if lines_per_page < 0:
            raise ValueError("количество строчек на странице не может быть отрицательным числом")
        self.lines_per_page = lines_per_page

        if not isinstance(number_of_clean_lines, int):
            raise TypeError("количество оставшихся чистых строчек должно быть int")
        if number_of_clean_lines < 0:
            raise ValueError("количество оставшихся чистых строчек не может быть отрицательным числом")
        self.number_of_clean_lines = number_of_clean_lines

    def add_record(self, new_page: bool, record_length: int) -> None:
        """
        Добавление записи в блокнот
        :param new_page: начать ли запись с новой страницы
        :param record_length: столько строчек занимает запись

        :raise ValueError: Если длина новой записи больше чем кол-во путсых строк, то вызываем ошибку

        Примеры:
        >>> notebook = Notebook(10, 20, 200)
        >>> notebook.add_record(True, 13)
        """
        if not isinstance(new_page, bool):
            raise TypeError("переменная начать ли запись с новой страницы должна быть типа bool")
        if not isinstance(record_length, int):
            raise TypeError("длина новой записи должна быть типа int")
        if record_length <= 0:
            raise ValueError("длина новой записи должна быть неотрицательным числом")
        ...

    def insert_sheets(self, number_of_sheets: int) -> int:
        """
        Владывание дополнительных страничек в блокнот

        :param number_of_sheets: кол-во вкладываемых страничек

        :return: кол-во чистых строчек

        Примеры:
        >>> notebook = Notebook(10, 20, 0)
        >>> notebook.insert_sheets(5)
        """
        if not isinstance(number_of_sheets, int):
            raise TypeError("кол-во вкладываемых страничек должно быть типа int")
        if number_of_sheets <= 0:
            raise ValueError("кол-во вкладываемых страничек должно быть неотрицательным числом")
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
