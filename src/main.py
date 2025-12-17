from scraping import scraping_news
from storage import save_data
from crawler import crawler

url = "https://news.ycombinator.com/"
# Headers são para específicar qual navegador será feito a requisição 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

site = crawler(url, headers)
dados = scraping_news(site)
save_data(dados)
