import Exhibition
from Report import Report
from ui import UI


def main_menu() -> str:
    menu = UI("MAIN MENU", ["Exhibitions", "Quit"])
    return menu.create_menu()


class GalleryInventoryManagementSystem:

    def __init__(self, _exhibition: Exhibition) -> None:
        self.__exhibition = _exhibition

    def manage_exhibitions(self) -> None:
        while True:
            menu = UI("EXHIBITION", ["Display All Exhibitions", "Display a Exhibition",
                                     "Add Exhibition", "Update Exhibition", "Delete Exhibition", "Back to Main Menu"])
            _option = menu.create_menu()
            try:
                if _option == "1":
                    exhibitions = self.__exhibition.display_exhibitions()
                    while True:
                        response = input("Do you want to generate result report? [Y/N]: ").lower()
                        if response == "y":
                            report = Report()
                            report.generate_exhibition_report(exhibitions)
                            print("Exhibition report generated successfully.")
                            break
                        elif response == "n":
                            break
                        else:
                            print("Invalid response. Please try again.")
                elif _option == "2":
                    event_id = int(input("Event id: "))
                    self.__exhibition.display_exhibition(event_id)
                elif _option == "3":
                    event_id = int(input("Event id: "))
                    title = input("Event Title: ")
                    start_date = input("Event Start Date: ")
                    end_date = input("Event End Date: ")
                    location = input("Event Location: ")
                    self.__exhibition.add_exhibition(event_id, title, start_date, end_date, location)
                elif _option == "4":
                    event_id = int(input("Event id: "))
                    title = input("Event Title: ")
                    start_date = input("Event Start Date: ")
                    end_date = input("Event End Date: ")
                    location = input("Event Location: ")
                    self.__exhibition.update_exhibition(event_id, title, start_date, end_date, location)
                elif _option == "5":
                    event_id = int(input("Event id: "))
                    self.__exhibition.delete_exhibition(event_id)
                elif _option == "6":
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid entry. Please try again.")
            except ValueError:
                print("Invalid event id. Please try again.")
        del self.__exhibition


if __name__ == "__main__":
    print("Welcome to the GALEXIS!".center(100))
    while True:
        exhibition = Exhibition.Exhibition()
        manager = GalleryInventoryManagementSystem(exhibition)
        option = main_menu()
        if option == "1":
            manager.manage_exhibitions()
        elif option == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid entry. Please try again.")
