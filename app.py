import requests
from bs4 import BeautifulSoup

def requisicao():
    requisicao = requests.get("https://pages.hashtagtreinamentos.com/curso-basico-programacao?blog=1n4033rer&video=3zd56c2h7")
    
    # Verifica se a requisição foi bem-sucedida
    if requisicao.status_code == 200:
        soup = BeautifulSoup(requisicao.text, 'html.parser')

        #Extrair informações da pagina inicial
        info = soup.find('button',{'class':'general-button'})
        if info:
            info = info.text.strip() if info else "Botão não encontrado"
            print(f'Botão Encontrado:{info}')
            # Se o Botão for encontrado vai para proxima pagina 
            url_proxima = "https://drive.google.com/drive/folders/1eUC-F2Kw9aaYz0j5Fo_GEx7QKBaRD7G8"
            proxima = requests.get(url_proxima)

            if proxima.status_code == 200:
                print("Acessando a proxima pagina")
                print(proxima.text[:500])   # Exibe os primeiros 500 caracteres da nova página
            else:
                print(f"Erro ao acessar a proxima pagina{proxima.status_code}")
        else:
            print("Botão Não encontrado")            
    else:
        print(f"Erro ao acessar a página, código de status: {requisicao.status_code}")

# Chama a função
requisicao()
