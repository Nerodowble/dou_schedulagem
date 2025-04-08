# Use uma imagem base leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências e instala-os
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do código para a imagem
COPY . .

# Define o comando que o container executará ao iniciar
CMD ["python", "app.py"]
