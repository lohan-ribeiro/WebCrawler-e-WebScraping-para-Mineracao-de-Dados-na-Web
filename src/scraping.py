
from bs4 import BeautifulSoup
import re

# Função para a raspagem de dados das notícias.
def scraping_news(site):
    soup = BeautifulSoup(site.text, "html.parser")
    #print(site.prettify())

    # Lista onde ficará armazenado os dados da notícia.
    dados = []
    
    # Iteração sobre as notícias da pagina
    for noticia in soup.find_all("tr", class_="athing"):
        subtext = noticia.find_next("td", class_="subtext") # Metadados da notícia(score, comments e autor)

        # Título e link da notícia.
        titulo_link_tag = noticia.find("span", class_="titleline" )
        titulo = titulo_link_tag.find("a").get_text()
        link= titulo_link_tag.find("a").get("href")

        # Autor da notícia.
        autor_tag= subtext.find("a", href = re.compile(r"^user\?id="))
        autor = autor_tag.get_text() if autor_tag else "Não Possui Autor"

        # Pontuação da notícia.
        score_tag = subtext.find("span", class_="score")if subtext else None
        score = score_tag.getText() if score_tag else "Nenhuma Avaliação"

        # Comentarios da notícia.
        comments_tag = subtext.find("a", href=re.compile(r"^item\?id="))

        # Cada notícia possui duas tags correspondete ao atributo do filtro, mas uma tem o "pai"="span".
        if comments_tag.parent.name == "span":  # Se a tag possuir o "pai"="span"
            comments_tag = comments_tag.find_next("a", href=re.compile(r"^item\?id=")) # Buscasse a proxima tag.

        comments = comments_tag.text if comments_tag else "Nenhum Comentario"

        # Formatação do comentário
        comments = int(comments.split()[0]) if comments and comments.split()[0].isdigit() else 0

        # Dados coletados da notícia.
        dados.append({
            "Título": titulo,
            "Link": link,
            "Autor": autor,
            "Pontuação(Score)": score,
            "Número de comentários": comments
        })

    return dados