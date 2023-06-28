import requests
import lxml
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com/dp/B08DZ5TWLN/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(PRODUCT_URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
amount_spans = soup.find(class_="a-price-whole").getText()
amount_as_float = float(amount_spans) 
print(amount_as_float)