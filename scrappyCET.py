import requests
from bs4 import BeautifulSoup
import csv

# URL da página de trânsito da CET
url = 'http://www.cetsp.com.br/transito-agora/transito-nas-principais-vias.aspx'

# Enviar uma solicitação HTTP para a página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lista para armazenar as zonas e informações de trânsito
    zonas_e_informacoes = []

    # Encontrar e extrair as informações de trânsito para cada zona
    zonas = ['Norte', 'Oeste', 'Centro', 'Leste', 'Sul']
    for zona_nome in zonas:
        zona = soup.find('li', class_='txt' + zona_nome)
        if zona:
            zona_nome = zona.find('h3').text.strip()
            info_transito = zona.find('p').text.strip()
            zonas_e_informacoes.append((zona_nome, info_transito))

            # Imprimir os dados da zona
            print(f"Zona: {zona_nome}")
            print(f"Informação de Trânsito: {info_transito}")

    # Salvar os dados em um arquivo CSV
    with open('dados_transito.csv', 'w', newline='', encoding='latin1') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        # Escrever o cabeçalho
        writer.writerow(['Zona', 'Informação de Trânsito'])
        # Escrever os dados de trânsito para todas as zonas
        writer.writerows(zonas_e_informacoes)

    print('\nDados de trânsito foram salvos em dados_transito.csv com codificação latin1.')
else:
    print('Não foi possível acessar a página da CET.')