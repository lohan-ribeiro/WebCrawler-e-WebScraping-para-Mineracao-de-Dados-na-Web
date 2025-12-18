from bs4 import BeautifulSoup

dados = {}

def scraping_news(site):
    site = BeautifulSoup(site.text, "html.parser")
    return print("eu consigo coletar os dados")