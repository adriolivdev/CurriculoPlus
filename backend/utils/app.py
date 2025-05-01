from flask import Flask, request, send_file, jsonify
import pdfkit
import tempfile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

config = pdfkit.configuration(
    wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # ajuste se estiver em outro local
)

@app.route('/')
def home():
    return 'API Currículo+ online ✅'

@app.route('/gerar-pdf', methods=['POST'])
def gerar_pdf():
    try:
        dados = request.get_json()

        html = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
          <meta charset="UTF-8">
          <title>Currículo - {dados['nome']}</title>
          <style>
            body {{ font-family: Arial, sans-serif; padding: 30px; color: #333; }}
            h1 {{ font-size: 24px; color: #00796b; margin-bottom: 0; }}
            h2 {{ font-size: 18px; margin-top: 30px; }}
            p, li {{ font-size: 14px; margin: 2px 0; }}
            ul {{ padding-left: 20px; }}
            .tag {{ display: inline-block; background: #e0f2f1; color: #00695c; padding: 4px 10px; margin: 3px 4px 3px 0; border-radius: 4px; font-size: 12px; }}
            .section {{ margin-top: 20px; }}
            .center {{ text-align: center; }}
            .foto {{ width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin: 10px auto; display: block; }}
          </style>
        </head>
        <body>

          {f"<img src='{dados['foto']}' class='foto' />" if dados.get('foto') else ''}
          <h1 class="center">{dados['nome']}</h1>

          <p class="center">
            {f"Idade: {dados['idade']}" if dados.get('idade') else ''}
            {' • ' if dados.get('idade') and dados.get('estadoCivil') else ''}
            {f"Estado Civil: {dados['estadoCivil']}" if dados.get('estadoCivil') else ''}
          </p>
          <p class="center">Email: {dados['email']}</p>

          {f"<div class='section'><h2>Objetivo</h2><p>{dados['objetivo']}</p></div>" if dados.get('objetivo') else ''}

          {f"<div class='section'><h2>Formação Acadêmica</h2><ul>" +
            ''.join(
              f"<li>{f['tipo']}" +
              (f" – {f['nomeEscola']}" if f.get('nomeEscola') else "") +
              (f" | Curso: {f['nomeCurso']}" if f.get('nomeCurso') else "") +
              (f" ({f['inicio'] or '?'} a {f['fim'] or '?'})" if f.get('inicio') or f.get('fim') else "") +
              "</li>"
              for f in dados['formacoes']
              if f['tipo']
            ) +
          "</ul></div>" if dados.get('formacoes') else ''}


          {
            f"<div class='section'><h2>Experiência Profissional</h2><p>Estou em busca da minha primeira oportunidade profissional.</p></div>"
            if dados.get('statusExperiencia') == 'Em busca do primeiro emprego'
            else
            (
              f"<div class='section'><h2>Experiência Profissional</h2><p>Já tive experiências anteriores nas seguintes empresas:</p><ul>" +
              ''.join(
                f"<li><strong>{e['cargo']}</strong> – {e['empresa']} ({e['periodo']})<br><small>{e['atividades']}</small></li>"
                for e in dados['experiencias']
                if e['empresa'] and e['cargo'] and e['periodo']
              ) +
              "</ul></div>"
              if dados.get('experiencias') else ''
            )
          }

          {f"<div class='section'><h2>Habilidades</h2>" +
            ''.join(f"<span class='tag'>{h}</span>" for h in dados['habilidades']) +
           "</div>" if dados.get('habilidades') else ''}

          {f"<div class='section'><h2>Idiomas</h2>" +
            ''.join(f"<span class='tag'>{i}</span>" for i in dados['idiomas']) +
           "</div>" if dados.get('idiomas') else ''}

          {f"<div class='section'><h2>Cursos Complementares</h2>" +
            ''.join(f"<span class='tag'>{c}</span>" for c in dados['cursos']) +
           "</div>" if dados.get('cursos') else ''}

          {f"<div class='section'><h2>Disponibilidade</h2>" +
            ''.join(f"<span class='tag'>{d}</span>" for d in dados['disponibilidades']) +
           "</div>" if dados.get('disponibilidades') else ''}

        </body>
        </html>
        """

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            pdfkit.from_string(html, f.name, configuration=config)
            return send_file(f.name, as_attachment=True, download_name="curriculo.pdf")

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
