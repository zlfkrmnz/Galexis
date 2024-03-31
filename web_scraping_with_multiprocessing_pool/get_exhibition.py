from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as CHR_SER
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime, timedelta
import json
import re
import multiprocessing as mp

user_agent = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/92.0.4515.107 Safari/537.36"]


chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
service = CHR_SER(ChromeDriverManager().install())


def open_webdriver(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    _driver = webdriver.Chrome(service=service, options=chrome_options)
    _driver.maximize_window()
    try:
        _driver.get(url)
        time.sleep(1)

        # Sayfanın kaynak kodunu al
        source = _driver.page_source

        # `events_json` değişkenini içeren JavaScript kodunu çekmek için regex kullan
        pattern = r'var events_json = (\[.*?\]);'
        match = re.search(pattern, source, re.DOTALL)

        if match:
            # JSON string'ini yakala
            json_string = match.group(1)

            # JSON string'ini Python listesine dönüştür
            events_list = json.loads(json_string)
            with open('events.json', 'a', encoding="utf-8") as f:
                for event in events_list:
                    f.write(json.dumps(event, indent=4, ensure_ascii=False, sort_keys=True) + ',')
            print(f"{_driver.current_url} tamamlandı.")
        else:
            print("events_json değişkeni bulunamadı.")

    except WebDriverException as e:
        print(f"Hata oluştu: {e}")

    # Tarayıcıyı kapat
    _driver.quit()


if __name__ == "__main__":
    _date = datetime.today()
    start_time = time.time()
    while _date >= datetime(2022, 10, 6):
        _urls = []
        for i in range(1, 7):
            _urls.append("https://www.themagger.com/etkinlikler/?tarih=" + _date.strftime("%Y-%m-%d") + "&kategori=sanat")
            _date -= timedelta(days=30)
        pool = mp.Pool()
        results = pool.map(open_webdriver, _urls)
        pool.close()
        pool.join()
        end_time = time.time()
        print(f"Geçen Süre: {end_time - start_time}")
