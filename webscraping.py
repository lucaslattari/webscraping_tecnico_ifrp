# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1o2f8Eh13GaZcnO4ULqls9dV5P_UoU-9J

#Web Scraping

Certo, agora vamos além!

A ideia do programa abaixo é extrair o texto de um artigo da Wikipedia.
"""

import requests
from bs4 import BeautifulSoup

entrada = input("Você quer um artigo sobre o quê?")

# URL do artigo da Wikipedia que queremos fazer o scraping
url = 'https://pt.wikipedia.org/wiki/' + entrada

# Se conecta ao site da Wikipedia
response = requests.get(url)

# Verifica se a conexão foi bem-sucedida
if response.status_code == 200:
    # Obtém o conteúdo HTML da resposta
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra o parágrafo do resumo do artigo
    # Na Wikipedia, o resumo está dentro dos parágrafos <p> imediatamente após o div com a classe mw-parser-output
    summary_paragraphs = soup.find('div', class_='mw-parser-output').find_all('p', recursive=False)

    # Extrai e imprime o texto de cada parágrafo do resumo
    for paragraph in summary_paragraphs:
      print(paragraph.text)
else:
    print("Falha na requisição: Status Code", response.status_code)

