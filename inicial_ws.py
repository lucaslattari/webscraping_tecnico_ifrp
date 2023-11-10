"""
Original file is located at
    https://colab.research.google.com/drive/1o2f8Eh13GaZcnO4ULq>

#Web Scraping

É a técnica de extrair dados de websites. Nessa situação o seu >

O web scraping é permitido quando realizado em **dados públicos>

## Primeiros passos

Para começar, vamos pegar o conteúdo HTML de uma página Web.
"""
import requests

# Endereço do site em que vamos fazer o scraping
url = 'http://pudim.com.br/'

# Realiza uma conexão ao site acima, obtendo uma resposta
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Exibe o HTML da página
    print(response.text)
else:
    print("Falha na requisição: Status Code", response.status_code)

# Obtém o código HTML do site
html_content = response.text

# Procura por <title> dentro do HTML
start_index = html_content.find('<title>')

# Adiciona o tamanho da tag <title> para encontrar o "começo" do título
start_index += len('<title>')

# Encontra o final da tag </title>
end_index = html_content.find('</title>')

# "Pega" a parte do HTML que está entre o começo e o fim de title, ou seja, <title> </title>
title = html_content[start_index:end_index]

print("O título do site é:", title)
