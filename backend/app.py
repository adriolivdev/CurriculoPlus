from flask import Flask, request, send_file, jsonify, render_template
import pdfkit
import tempfile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Caminho do wkhtmltopdf (ajuste para Render ou ambiente local)
config = pdfkit.configuration(
    wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
)

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

if __name__ == '__main__':
    app.run(debug=True)
