from flask import Flask, request, send_file, jsonify, render_template
import pdfkit
import tempfile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Caminho para o wkhtmltopdf (ajuste para seu ambiente local ou Render)
config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

@app.route('/')
def home():
    return 'API Currículo+ online ✅'

@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    try:
        dados = request.get_json()

        # Renderiza o HTML com os dados recebidos
        html = render_template("curriculo.html", dados=dados)

        # Cria PDF temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            pdfkit.from_string(html, f.name, configuration=config)

            # Formata nome do arquivo com base no nome da pessoa
            nome_formatado = dados.get("nome", "curriculo").strip().replace(" ", "-")
            nome_pdf = f"curriculo-{nome_formatado}.pdf"

            return send_file(f.name, as_attachment=True, download_name=nome_pdf)

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
