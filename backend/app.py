# Importação das bibliotecas necessárias
from flask import Flask, request, send_file, jsonify, render_template
import pdfkit                       # Para converter HTML em PDF
import tempfile                    # Para criar arquivos temporários
from flask_cors import CORS        # Para permitir requisições de outros domínios (ex: frontend)
import os                          # Para interações com o sistema de arquivos

# Inicializa a aplicação Flask
app = Flask(__name__)

# Ativa o CORS para permitir comunicação com o frontend (como React ou Vue)
CORS(app)

# Configuração do caminho do wkhtmltopdf
# 🔧 Ajuste este caminho se estiver em outro sistema:
# No Linux: geralmente "/usr/bin/wkhtmltopdf"
# No Windows: use r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(
    wkhtmltopdf="/usr/bin/wkhtmltopdf"
)

# Rota principal para ver se a API está online
@app.route('/')
def home():
    return 'API Currículo+ online ✅'

# Rota responsável por gerar e retornar o PDF
@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    try:
        # Recebe os dados em JSON do frontend
        dados = request.get_json()

        # Renderiza o HTML (curriculo.html) com os dados recebidos
        html = render_template("curriculo.html", dados=dados)

        # Cria um arquivo PDF temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            # Converte o HTML para PDF e salva no arquivo temporário
            pdfkit.from_string(
                html,
                temp_pdf.name,
                configuration=config,
                options={"enable-local-file-access": ""}
            )

            # Formata o nome do PDF com base no nome do candidato
            nome_formatado = dados.get("nome", "curriculo").strip().replace(" ", "-")
            nome_pdf = f"curriculo-{nome_formatado}.pdf"

            # Retorna o arquivo como download para o navegador ou frontend
            return send_file(
                temp_pdf.name,
                mimetype="application/pdf",       # Tipo de arquivo
                as_attachment=True,               # Força o download
                download_name=nome_pdf            # Nome do arquivo baixado
            )

    except Exception as e:
        # Em caso de erro, imprime no terminal e retorna mensagem de erro
        print(f"Erro ao gerar PDF: {e}")
        return jsonify({
            "erro": "Erro ao gerar PDF",
            "detalhes": str(e)
        }), 500
