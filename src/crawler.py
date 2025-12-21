import requests

# Função para rastrear os dados
def crawler(url, headers):
    print(url)
    
    response = requests.get(url, headers=headers)

    if (response.status_code == requests.codes.ok):
        print(response.status_code)
        return response
    else: 
        return response.status_code