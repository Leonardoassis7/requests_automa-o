import requests
import os
from bs4 import BeautifulSoup

def requisicao():
    requisicao = requests.get("https://pages.hashtagtreinamentos.com/curso-basico-programacao?blog=1n4033rer&video=3zd56c2h7")
    
    # Verifica se a requisição foi bem-sucedida
    if requisicao.status_code == 200:
        soup = BeautifulSoup(requisicao.text, 'html.parser')
        
        # Extrair informações da página inicial
        info = soup.find('button', {'class': 'general-button'})
        if info:
            info_text = info.text.strip() if info else "Botão não encontrado"
            href = info.get('href')  
            if href:
                print(f'Botão encontrado: {info_text}')
                print(f'HREF encontrado: {href}')
                # Se o HREF for encontrado, acessa a próxima página
                proxima = requests.get("https://drive.google.com/drive/folders/1eUC-F2Kw9aaYz0j5Fo_GEx7QKBaRD7G8?usp=sharing")
                print(f'Status da requisição: {proxima.status_code}')
            else:
                print("HREF não encontrado no botão.")
        else:
            print("Botão não encontrado.")           
    else:
        print(f"Erro ao acessar a página, código de status: {requisicao.status_code}")

def baixar_pdf_google_drive(file_id, output_name):
    # link de download do Google Drive
    url = f"https://drive.google.com/uc?id={file_id}&export=download"
    folder_path = "./.pdf"
    os.makedirs(folder_path, exist_ok=True)
    
    # Caminho completo do arquivo de saída
    output_path = os.path.join(folder_path, output_name)
    
    try:
        # Fazer a requisição para o link de download
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Salvar o conteúdo do arquivo localmente
            with open(output_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"Download do arquivo concluído e salvo como '{output_path}'.")
        else:
            print(f"Erro ao baixar o arquivo. Código de status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao processar o download: {e}")

# ID do arquivo e nome do arquivo de saída
file_id = "1r0tmy7gnGVdX3ZEWfDgL1iJ6MsCwBdnP"
output_name = "arquivo_baixado.pdf"

# Chama a função
baixar_pdf_google_drive(file_id, output_name)
# Chama a função
requisicao()
