import requests

# Função para rastrear os dados e retornar em HTML
def crawler(url, headers):
    response = requests.get(url, headers=headers)
    if (response.status_code == requests.codes.ok):
        return response
    else: 
        return response.status_code