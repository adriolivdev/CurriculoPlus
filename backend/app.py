from flask import Flask, request, send_file, jsonify, render_template
import pdfkit
import tempfile
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Define o caminho do wkhtmltopdf no ambiente do Render
WKHTMLTOPDF_PATH = "/usr/bin/wkhtmltopdf"

# Verifica se o binário existe no sistema (previne erros silenciosos)
if not os.path.isfile(WKHTMLTOPDF_PATH):
    raise RuntimeError(f"wkhtmltopdf não encontrado em {WKHTMLTOPDF_PATH}. Verifique o caminho.")

# Configuração do pdfkit com caminho correto
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

@app.route('/')
def home():
    return '✅ API Currículo+ está no ar!'

@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    try:
        # Recebe os dados JSON enviados pelo frontend
        dados = request.get_json(force=True)
        if not dados or not isinstance(dados, dict):
            return jsonify({'erro': 'Dados inválidos enviados ao servidor.'}), 400

        # Renderiza o HTML com os dados usando Jinja2
        html = render_template("curriculo.html", dados=dados)

        # Cria um arquivo PDF temporário a partir do HTML gerado
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
            pdfkit.from_string(
                html,
                temp.name,
                configuration=config,
                options={"enable-local-file-access": ""}
            )

            # Formata o nome do PDF com base no nome da pessoa
            nome_formatado = dados.get("nome", "curriculo").strip().replace(" ", "-")
            nome_pdf = f"curriculo-{nome_formatado}.pdf"

            return send_file(temp.name, as_attachment=True, download_name=nome_pdf)

    except Exception as e:
        print("❌ Erro ao gerar PDF:", e)
        return jsonify({'erro': f'Erro interno ao gerar PDF: {str(e)}'}), 500

if __name__ == '__main__':
    # Desativa debug no ambiente de produção
    app.run(debug=False)
