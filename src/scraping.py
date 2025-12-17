from bs4 import BeautifulSoup

dados = {}

def scraping_news(site):
    site = BeautifulSoup(site.text, "html.parser")
    print(site.prettify())