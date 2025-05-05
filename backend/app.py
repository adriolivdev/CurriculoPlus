from flask import Flask, request, send_file, jsonify, render_template
import pdfkit
import tempfile
from flask_cors import CORS

# Inicializa o app Flask
app = Flask(__name__)
CORS(app)  # Libera o acesso CORS para o frontend

# Configuração do caminho para o executável wkhtmltopdf no Render
config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

@app.route('/')
def home():
    return '✅ API Currículo+ está online!'

@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    try:
        # Dados recebidos do frontend (JSON)
        dados = request.get_json()

        # Renderiza o template HTML com os dados do currículo
        html = render_template("curriculo.html", dados=dados)

        # Cria um arquivo PDF temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            # Gera o PDF a partir do HTML renderizado
            pdfkit.from_string(html, f.name, configuration=config)

            # Define o nome do PDF com base no nome do usuário (ex: curriculo-Adriane-Oliveira.pdf)
            nome_formatado = dados.get("nome", "curriculo").strip().replace(" ", "-")
            nome_pdf = f"curriculo-{nome_formatado}.pdf"

            # Envia o arquivo como resposta para download
            return send_file(f.name, as_attachment=True, download_name=nome_pdf)

    except Exception as e:
        # Em caso de erro, retorna a mensagem para o frontend
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
