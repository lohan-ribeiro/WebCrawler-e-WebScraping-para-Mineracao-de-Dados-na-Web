# Web Crawler e Web Scraping de Notícias de Tecnologia

Implementar um web crawler e técnicas de web scraping, com o objetivo de coletar, processar e estruturar dados disponíveis na web. A aplicação explora conceitos de mineração de dados, automação de processos, análise de estruturas HTML e boas práticas de desenvolvimento.

## 🚀 Tecnologias Utilizadas

**Python 3.13+ |
[Requests](https://requests.readthedocs.io/en/latest/) |
[BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/#)**


## 🎯 Objetivo

Implementação de um web crawler e técnicas de web scraping, com o objetivo de coletar dados do site [Hacker News](https://news.ycombinator.com/), extraindo título, autor, pontuação e número de comentários. 

### Crawler

Um web crawler é um programa que navega automaticamente pela web, seguindo links entre páginas. Ele serve para descobrir URLs e mapear sites, coletando páginas para serem processadas depois.
Será usado para:

- Acessar a página inicial;

- Capturar links de notícias;

- Navegar para a próxima página (?p=2, ?p=3);

- Limitar para 3 páginas.

### Scraping

O web scraping é o processo de extrair informações específicas de uma página web já encontrada. Será usado para:

#### Para cada notícia, extrair:

📰 Título.

🔗 Link.

👤 Autor.

⭐ Pontuação (score).

💬 Número de comentários.

#### Salvar tudo em json, exemplo:
```json
{  
  "title": "OpenAI launches new model",  
  "url": "https://...",  
  "author": "pg",  
  "points": 321,  
  "comments": 85  
} 
```
## ⚙️ Funcionalidades
- Crawler de múltiplas páginas;
- Extração de dados estruturados;
- Salvamento em JSON;
- Tratamento básico de erros.

## 🚧 Limitações
- O scraping depende da estrutura HTML do site;
- O projeto respeita limites básicos de requisição.


## 📚 Estrutura do Projeto
```
web_crawler_hn/  
├── src/  
│   ├── main.py           inicia o programa.
│   ├── crawler.py        responsável por navegar entre páginas e coletar URLs.
│   ├── scraper.py        responsável por extrair dados de cada página.
│   └── storage.py        responsável por armazenar os dados.
├── data/  
|   └── news.json         local onde os dados estão armazenados.
├── requirements.txt      requisitos para rodar o programa.
└── README.md  
```
## 🔧 Como Executar
```
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows  

pip install -r requirements.txt  
python src/main.py
```

## ⚠️ Aviso
Este projeto é apenas para fins educacionais.
Respeite os termos de uso dos sites coletados.