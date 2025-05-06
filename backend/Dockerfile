# Dockerfile atualizado para uso com wkhtmltopdf no Render
FROM python:3.10-slim

# Instala wkhtmltopdf e dependências
RUN apt-get update && \
    apt-get install -y wkhtmltopdf libxrender1 libxext6 libfontconfig1 libjpeg62-turbo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . /app

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
