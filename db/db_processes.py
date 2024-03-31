import json
import sqlite3

conn = sqlite3.connect("galexis.sqlite3")
cursor = conn.cursor()

command = """
    CREATE TABLE Exhibition (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        title TEXT NOT NULL,
        start_Date DATE,
        end_Date DATE,
        location TEXT)
    """

try:
    cursor.execute(command)
except Exception as e:
    print("An error occurred: ", e)

try:
    with open("C:\\Users\\zlfkr\\PycharmProjects\\Galexis\\web_scraping_with_multiprocessing_pool\\events.json", "r",
              encoding="utf-8") as file:
        events_list = json.load(file)
        events = []
        for event in events_list:
            if event not in events:
                events.append(event)
        command = "INSERT INTO Exhibition VALUES (?,?,?,?,?)"
        for event in events:
            cursor.execute(command, (event["event"], event["title"], event["beginning_date"],
                                     event["ending_date"], event["address"]))

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred: ", e)
cursor.close()
conn.commit()
conn.close()
