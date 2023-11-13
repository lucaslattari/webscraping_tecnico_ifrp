# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1o2f8Eh13GaZcnO4ULqls9dV5P_UoU-9J

#Web Scraping

Agora vamos extrair os nomes de todos os professores do Campus Rio Pomba e guardá-los em uma lista!
"""

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
