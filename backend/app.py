from flask import Flask, request, send_file, jsonify, render_template
import pdfkit
import tempfile
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuração do wkhtmltopdf no ambiente Render (ajuste local se necessário)
config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

@app.route('/')
def home():
    return 'API Currículo+ online ✅'

@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    try:
        dados = request.get_json()
        html = render_template("curriculo.html", dados=dados)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            pdfkit.from_string(html, f.name, configuration=config)
            return send_file(f.name, as_attachment=True, download_name="curriculo.pdf")

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# 🔥 Esta parte aqui é o que corrige o erro no Render:
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
