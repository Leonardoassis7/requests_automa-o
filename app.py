import requests
from bs4 import BeautifulSoup

def requisicao():
    # Realiza a requisição para a página principal da C&A
    requisicao = requests.get("https://www.cea.com.br/tenis-casual-com-recortes-ace-branco-1073154-branco-1/p")
    
    # Verifica se a requisição foi bem-sucedida
    if requisicao.status_code == 200:
        # bs4 retorna o html na requisicao.text
        soup = BeautifulSoup(requisicao.text, 'html.parser')
        
        # preco e a variavel que retorna o valor da class do preço do produto 
        preco = soup.find('span', {'class': 'vtex-product-price-1-x-installmentsTotalValue vtex-product-price-1-x-installmentsTotalValue--pdp-installments'}).text 
        if preco:
            preco = preco.strip()   #preco é uma string
        else:
            preco = "Preço não encontrado"

        imagem = soup.find('img', class_='cea-store-components-0-x-figure cea-store-components-0-x-figure--desktop')  
        if imagem:
            imagem_url = imagem['src']
        else:
            imagem_url = "Imagem não encontrada"

        # Tente encontrar a avaliação do produto
        avaliacao_produto = soup.find('div', {'class': 'cea-cea-store-theme-2-x-opinion__item'})
        if avaliacao_produto:
            avaliacao = avaliacao_produto.text.strip()
        else:
            avaliacao = "Avaliação não encontrada"

        # Exibir as informações
        print(f"Preço: {preco}")
        print(f"Imagem: {imagem_url}")
        print(f"Avaliação: {avaliacao}")
    else:
        print(f"Erro ao acessar a página, código de status: {requisicao.status_code}")

# Chama a função
requisicao()
