import sqlite3


class Exhibition:
    def __init__(self) -> None:
        self.__conn = sqlite3.connect('C:\\Users\\zlfkr\\PycharmProjects\\Galexis\\db\\galexis.sqlite3')
        self.__cursor = self.__conn.cursor()

    def __del__(self) -> None:
        self.__cursor.close()
        self.__conn.close()

    def __check_id(self, _id: int) -> bool:
        try:
            command = "SELECT id FROM Exhibition"
            self.__cursor.execute(command)
            ids = self.__cursor.fetchall()
            if (_id,) in ids:
                return True
            else:
                return False
        except Exception as e:
            print("An error occured while trying to check exhibition id. ", e)

    @staticmethod
    def print_exhibition(exhibition) -> None:
        print("*" * 100)
        print(f"Event ID: {exhibition[0]}".center(100))
        print(f"Event Title: {exhibition[1]}".center(100))
        print(f"Event Start Date: {exhibition[2]}".center(100))
        print(f"Event End Date: {exhibition[3]}".center(100))
        print(f"Event Location: {exhibition[4]}".center(100))
        print("*" * 100)

    def display_exhibitions(self) -> list:
        try:
            command = "SELECT * FROM Exhibition"
            self.__cursor.execute(command)
            exhibitions = self.__cursor.fetchall()
            print("EXHIBITIONS".center(100))
            for exhibition in exhibitions:
                self.print_exhibition(exhibition)
            print(f"{len(exhibitions)} exhibitions displayed successfully.")
        except Exception as e:
            print("An error occurred while trying to display exhibitions. ", e)
        return exhibitions

    def display_exhibition(self, _id: int) -> None:
        try:
            if self.__check_id(_id):
                command = "SELECT * FROM Exhibition WHERE id=?"
                self.__cursor.execute(command, (_id,))
                exhibition = self.__cursor.fetchone()
                self.print_exhibition(exhibition)
                print("Exhibition displayed successfully.")
            else:
                print("No exhibition found for this id.")
        except Exception as e:
            print("An error occurred while trying to display exhibition. ", e)

    def add_exhibition(self, _id: int, title: str, start_date: str, end_date: str, location: str) -> None:
        try:
            command = "INSERT INTO Exhibition VALUES (?,?,?,?,?)"
            self.__cursor.execute(command, (_id, title, start_date, end_date, location))
            print("Exhibition added successfully.")
        except Exception as e:
            print("An error occurred while adding exhibition. ", e)
        self.__conn.commit()

    def update_exhibition(self, _id: int, title: str, start_date: str, end_date: str, location: str) -> None:
        try:
            if self.__check_id(_id):
                command = "UPDATE Exhibition SET title = ?, start_date = ?, end_date = ?, location = ? WHERE id = ?"
                self.__cursor.execute(command, (title, start_date, end_date, location, _id))
                print("Exhibition updated successfully.")
            else:
                print("No exhibition found for this id.")
        except Exception as e:
            print("An error occurred while adding exhibition. ", e)
        self.__conn.commit()

    def delete_exhibition(self, _id: int) -> None:
        try:
            if self.__check_id(_id):
                command = "DELETE FROM Exhibition WHERE id =?"
                self.__cursor.execute(command, (_id,))
                print("Exhibition deleted successfully.")
            else:
                print("No exhibition found for this id.")
        except Exception as e:
            print("An error occurred while deleting. ", e)
        self.__conn.commit()
