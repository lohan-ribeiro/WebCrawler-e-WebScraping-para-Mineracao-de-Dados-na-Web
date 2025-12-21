import json
from pathlib import Path

# Função para armazenar os dados em json.
def save_data(data, filename="news.json"):
    Path("data").mkdir(exist_ok=True)

    with open (f"data/{filename}", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)