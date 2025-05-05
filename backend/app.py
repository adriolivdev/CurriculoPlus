from flask import Flask, request, send_file, jsonify, render_template
import pdfkit
import tempfile
from flask_cors import CORS

# Cria a aplicação Flask
app = Flask(__name__)

# Habilita o CORS para aceitar requisições do frontend (como Vercel, por exemplo)
CORS(app)

# Configura o caminho para o executável do wkhtmltopdf (ajuste esse caminho conforme o ambiente: Render ou local)
config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')


@app.route('/')
def home():
    """Rota raiz para verificação se a API está online."""
    return 'API Currículo+ online ✅'


@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    """
    Rota para geração de PDF a partir dos dados do currículo enviados via POST.
    Retorna o PDF gerado como arquivo para download.
    """
    try:
        # Pega os dados do currículo enviados em formato JSON
        dados = request.get_json()

        # Renderiza o HTML com os dados usando o template 'curriculo.html'
        html = render_template("curriculo.html", dados=dados)

        # Cria um arquivo temporário .pdf com o conteúdo HTML renderizado
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            # Gera o PDF a partir do HTML
            pdfkit.from_string(html, f.name, configuration=config)

            # Define o nome do arquivo com base no nome da pessoa (formatado para URL amigável)
            nome_formatado = dados.get("nome", "curriculo").strip().replace(" ", "-")
            nome_pdf = f"curriculo-{nome_formatado}.pdf"

            # Retorna o PDF como arquivo para download
            return send_file(f.name, as_attachment=True, download_name=nome_pdf)

    except Exception as e:
        # Em caso de erro, retorna o erro como JSON e código HTTP 500
        return jsonify({'erro': str(e)}), 500


# Executa o app localmente se rodar como script principal
if __name__ == '__main__':
    app.run(debug=False)
