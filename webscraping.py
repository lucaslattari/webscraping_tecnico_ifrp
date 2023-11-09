# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1o2f8Eh13GaZcnO4ULqls9dV5P_UoU-9J

#Web Scraping

É a técnica de extrair dados de websites. Nessa situação o seu código faz o papel de um navegador, acessando a página web, coletando dados específicos e, então, analisando, modificando e salvando a informação coletada.

O web scraping é permitido quando realizado em **dados públicos** e sem violar termos de uso ou direitos autorais. É crucial verificar a política de uso do site e o arquivo robots.txt, que é como se fosse um "manual de instruções" do que é permiti ou não.

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

"""Vamos aproveitar o código acima e extrair o título do site!"""

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

"""Certo, agora vamos além!

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

"""Agora vamos extrair os nomes de todos os professores do Campus Rio Pomba e guardá-los em uma lista!"""

import requests
from bs4 import BeautifulSoup

# URL da página que contém os nomes dos professores
url = 'https://www.ifsudestemg.edu.br/riopomba/institucional/corpo-docente'

# Se conecta ao site do campus
response = requests.get(url)

# Verifica se a conexão foi bem-sucedida
if response.status_code == 200:

  # Obtém o html
  html_content = response.text

  # Carrega o HTML no BeautifulSoup
  soup = BeautifulSoup(html_content, 'html.parser')

  # Encontra a tabela com a classe 'listing'
  table = soup.find('table', class_='listing')

  # Inicializa uma lista para armazenar os nomes
  names = []

  # "Anda" por todas as linhas da tabela
  for row in table.find_all('tr'):

      # Encontra todas as tags 'span' em cada linha da tabela
      spans = row.find_all('span')

      for span in spans:

        # Extrai o texto e adiciona na lista de nomes
        name = span.text

        if name and name not in names:  # Verifica se o nome não está vazio e se o nome já não foi inserido na lista
          names.append(name)

  # Imprime a lista de nomes
  for name in names:
      print(name)
else:
    print("Falha na requisição: Status Code", response.status_code)

"""Quer ir além? Indicamos esse tutorial: [clique aqui!](https://realpython.com/python-web-scraping-practical-introduction/)

Uma vez que entendeu, procure por todos os e-mails na página ["Fale Conosco" do IF Sudeste MG - Campus Rio Pomba](https://www.ifsudestemg.edu.br/riopomba/fale-conosco).
"""