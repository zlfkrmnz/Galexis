class Artwork:
    def __init__(self, _id: int, title: str, artist_id: int, year: int, medium: str, dimensions: str, price: float,
                 availability: bool) -> None:
        self.__id = _id
        self.__title = title
        self.__artist_id = artist_id
        self.__year = year
        self.__medium = medium
        self.__dimensions = dimensions
        self.__price = price
        self.__availability = availability

    def add_artwork(self) -> None:
        pass

    def update_artwork(self) -> None:
        pass

    def delete_artwork(self) -> None:
        pass

    def mark_as_sold(self) -> None:
        pass
