import requests
from bs4 import BeautifulSoup

def scrape_products(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    products = []
    for item in soup.select(".grid-product__content"):
        title_tag = item.select_one(".grid-product__title")
        price_tag = item.select_one(".grid-product__price")
        img_tag = item.select_one("img")

        if not title_tag or not price_tag or not img_tag:
            continue

        title = title_tag.text.strip()
        price = int("".join(filter(str.isdigit, price_tag.text)))
        image_url = img_tag.get("src")

        products.append({"title": title, "price": price, "image_url": image_url})

    return products
