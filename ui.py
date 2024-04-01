class UI:
    def __init__(self, menu_name: str, menu_items: list) -> None:
        self.menu_name = menu_name
        self.menu_items = menu_items

    @staticmethod
    def line(text=""):
        if text == "":
            return "-" * 100
        else:
            return "|" + text.center(98, " ") + "|"

    def create_menu(self):
        text = self.line()
        text += f"\n{self.line(f'{self.menu_name}')}\n"
        text += self.line()
        no = 0
        for element in self.menu_items:
            no += 1
            element = f"{no}..{element}"
            text += f"\n{self.line(element)}"
        text += "\n" + self.line()
        print(text)
        option = input(f"Please choose an option between [1-{len(self.menu_items)}]: ")
        return option


