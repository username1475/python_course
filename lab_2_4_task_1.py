class Mamas_album:
    """
    Базовый класс мамин фотоальбом
    (фотографии хозяйки и ее дочки!)

    :param owners_name: имя хозяйки
    :param photos: список вложенных фотографий
    :param post_stamps: список вложенных почтовых марок

    """
    def __init__(self, owners_name: str, photos: list, post_stamps: list):
        self._owners_name = owners_name
        # хозяйка у альбома меняться не может
        self.photos = photos
        self.post_stamps = post_stamps

    @property
    def owners_name(self) -> str:
        return self._owners_name

    @property
    def photos(self) -> list:
        return self._photos

    @photos.setter
    def photos(self, new_photos: list) -> None:
        if not isinstance(new_photos, list):
            raise TypeError("Вкладываемые фотографии должны быть типа list")
        self._photos = new_photos

    @property
    def post_stamps(self) -> list:
        return self._post_stamps

    @post_stamps.setter
    def post_stamps(self, new_post_stamps: list) -> None:
        if not isinstance(new_post_stamps, list):
            raise TypeError("Вкладываемые почтовые марки должны быть типа list")
        self._post_stamps = new_post_stamps

    def __str__(self) -> str:
        return f"Фотоальбом, принадлежащий {self.owners_name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(owners_name={self.owners_name!r}, photos={self.photos!r}, post_stamps={self.post_stamps!r})"

    def show_photos(self) -> None:
        """
        Показываем фотографии друзьям и близким
        """
        ...

    def compare_stamps(self, list_of_stamps: list) -> None:
        """
        Сравниваем марки с марками другого человека
        """
        ...


class Grannys_album(Mamas_album):
    """
    Дочерний класс бабушкин фотоальбом
    (мама стала бабушкой и ее альбом стал бабушкиным!)

    :param owners_name: имя хозяйки
    :param photos: список вложенных фотографий
    :param post_stamps: список вложенных почтовых марок
    :param notes: записки хозяйки

    """
    def __init__(self, owners_name: str, photos: list, post_stamps: list, notes: list):
        super().__init__(owners_name, photos, post_stamps)
        if not isinstance(notes, list):
            raise TypeError("Записки должны быть типа list")
        self._notes = notes
        # бабушкины записки изменять нельзя.. она же написала их своей рукой!

    @property
    def notes(self) -> list:
        return self._notes

    """
    наследуем метод __str__ так как пользователю достаточно знать только имя хозяйки
    перегружаем метод __repr__ для его корректной работы
    """
    def __repr__(self) -> str:
         return f"{self.__class__.__name__}(owners_name={self.owners_name!r}, photos={self.photos!r}, post_stamps={self.post_stamps!r}, notes={self.notes!r})"

    def find_out_stamps_price(self) -> float:
        """
        Марки стали антиквариатом! посмотрим сколько можно заработать если продать их)
        """
        ...

    def show_photos(self) -> None:
        """
        Перегружаем фунцию так как теперь для того чтобы вспомнить и рассказать истории с фотографий
        необходимо поболтать с родственницами и подружками-пенсионерками..
        """
        ...
