from scraping import scraping_news
from storage import save_data
from crawler import crawler

# Headers são para específicar qual navegador será feito a requisição 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

# Iterando site para pegar as 3 primeiras páginas
for i in range(1,4):
    if i == 1:
        url = "https://news.ycombinator.com/"
    else:
        url = f"https://news.ycombinator.com/?p={i}"

    site = crawler(url, headers)
    dados = scraping_news(site)
    save_data(dados)
