from flask import Flask, request, send_file, jsonify, render_template
import pdfkit
import tempfile
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Caminho para o wkhtmltopdf no ambiente do Render
config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")

@app.route('/')
def home():
    return 'API Currículo+ online ✅'

@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    try:
        dados = request.get_json()

        # Renderiza o HTML com os dados
        html = render_template("curriculo.html", dados=dados)

        # Cria PDF temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
            pdfkit.from_string(html, temp.name, configuration=config, options={"enable-local-file-access": ""})

            nome_formatado = dados.get("nome", "curriculo").strip().replace(" ", "-")
            nome_pdf = f"curriculo-{nome_formatado}.pdf"

            return send_file(temp.name, as_attachment=True, download_name=nome_pdf)

    except Exception as e:
        print("Erro ao gerar PDF:", e)
        return jsonify({'erro': f'Falha ao gerar PDF: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=False)
