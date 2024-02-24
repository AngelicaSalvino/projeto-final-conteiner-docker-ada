import psycopg2
import time
from flask import Flask, request, redirect
from urllib.parse import quote  # Adicionando a importação do módulo urllib.parse

app = Flask(__name__)

def wait_for_postgres():
    max_retries = 10
    retries = 0
    while retries < max_retries:
        try:
            psycopg2.connect(
                host="postgres",
                port="5432",
                database="postgres",
                user="postgres",
                password="postgres",
            )
            return True
        except psycopg2.OperationalError as e:
            retries += 1
            print(f"Erro ao conectar ao banco de dados. Tentativa {retries}/{max_retries}.")
            time.sleep(2)  # Aguarda 2 segundos antes de tentar novamente

    print("Não foi possível conectar ao banco de dados. Encerrando.")
    return False

@app.route("/")
def index():
    return open("index.html", "rb").read()

@app.route("/salvar", methods=["POST"])
def salvar():
    nome = request.form["nome"]
    endereco = request.form["endereco"]
    telefone = request.form["telefone"]
    email = request.form["email"]

    if not wait_for_postgres():
        return "Erro ao conectar ao banco de dados", 500

    conexao = psycopg2.connect(
        host="postgres",
        port="5432",
        database="postgres",
        user="postgres",
        password="postgres",
    )
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO public.dados_cadastrais (nome, endereco, telefone, email)
        VALUES (%s, %s, %s, %s)
        """,
        (nome, endereco, telefone, email),
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

