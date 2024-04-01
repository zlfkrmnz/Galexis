class Report:

    @staticmethod
    def generate_exhibition_report(exhibitions) -> None:
        try:
            with open("exhibition_report.txt", "w", encoding="utf-8") as report:
                for exhibition in exhibitions:
                    report.write(str(exhibition))
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")
        except TypeError:
            print("Type not supported by this script.")
        except Exception as e:
            print("An error occurred while generating the exhibition report. ", e)
