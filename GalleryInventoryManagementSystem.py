import Artist
import Artwork
import Customer
import Exhibition
import Sale


def main_menu() -> None:
    print("Welcome to the GALEXIS!")
    pass


class GalleryInventoryManagementSystem:

    def __init__(self, artists: list[Artist], artworks: list[Artwork], customers: list[Customer],
                 exhibitions: list[Exhibition], sales: list[Sale]) -> None:
        self.__artists = artists
        self.__artworks = artworks
        self.__customers = customers
        self.__exhibition = exhibitions
        self.__sales = sales

    def manage_artists(self) -> None:
        pass

    def manage_artworks(self) -> None:
        pass

    def manage_customers(self) -> None:
        pass

    def manage_exhibitions(self) -> None:
        pass
