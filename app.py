import requests
from datetime import datetime
import time
import re

# Links das seções do DOU
dou_links = {
    "Seção 1": "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=do1&exactDate=dia&sortType=0",
    "Seção 2": "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=do2&exactDate=dia&sortType=0",
    "Seção 3": "https://www.in.gov.br/consulta/-/buscar/dou?q=*&s=do3&exactDate=dia&sortType=0",
}


# Função para checar publicação
def checar_publicacao():
    for secao, url in dou_links.items():
        try:
            response = requests.get(url)
            response.raise_for_status()  # Lança uma exceção para status codes de erro (4xx ou 5xx)
            
            texto = response.text
            match = re.search(r"(\d+ resultados)", texto)
            if match:
                agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{agora}] {secao} publicou: {match.group(1)}")
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] {secao} ainda não publicou.")

        except requests.exceptions.RequestException as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Erro ao acessar {secao}: {e}")
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Erro ao processar {secao}: {e}")


# Loop principal (pinga a cada 5 minutos)
try:
    while True:
        checar_publicacao()
        time.sleep(300)  # espera 5 minutos (300 segundos)
except KeyboardInterrupt:
    print("Finalizado pelo usuário.")