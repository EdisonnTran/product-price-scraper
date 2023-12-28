from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.ca/s?k=plush"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "en-US,en;q=0.9",}


page = requests.get(URL, headers=headers)
# print(page.content)

soup1 = BeautifulSoup(page.content, "html.parser")
soup = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")

price = soup.find_all('span', class_="a-offscreen")

for i, item in enumerate(title):
    print(item.get_text().strip(), price[i].get_text().strip())