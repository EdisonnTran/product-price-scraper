from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "en-US,en;q=0.9",}

def scrape(item):

    page = 1
    url = f"https://www.amazon.ca/s?k={item}&page={page}"
    page = requests.get(url, headers=headers)
    
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup = BeautifulSoup(soup1.prettify(), "html.parser")

    try:
        pages = soup.find('span', class_="s-pagination-item s-pagination-disabled").get_text().strip()
    except:
        print(f"Can not find number of pages in {item}. Setting to 1.")
        pages = 1
        
    ret = set()
    
    for page in range(1, int(pages) + 1):

        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        objs = soup.find_all('div', class_="a-section a-spacing-base")

        for obj in objs:

            title = obj.find('span', class_="a-size-base-plus a-color-base a-text-normal").get_text().strip()

            # there can sometimes be 2 prices in one search (if using obj.find_all), price[0] = sale price, price[1] = old price
            try:
                price = obj.find('span', class_="a-offscreen").get_text().strip()
            except:
                try:
                    price = obj.find('span', class_="a-color-base").get_text().strip()
                except:
                    print(title, "failed to find price")

            link = obj.find_all('a', class_="a-link-normal")[0]['href']
            linkURL = f"https://amazon.ca/{link}"
            img = obj.find_all('img', class_="s-image")[0]['src']

            ret.add(tuple([title, price, linkURL, img]))

    return ret

if __name__ == '__main__':
    ret = scrape("avocado plush miniso big")
    print(ret)