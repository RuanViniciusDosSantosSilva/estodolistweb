from datetime import date
from flask import Flask, render_template, request, session, redirect, flash
from database import consultar_tarefas, inserir_tarefa
...

app = Flask(__name__)
app.secret_key = 'senai' #Chave secreta para a sessão do Flask

ADMIN_EMAIL = 'ruan.silva.senai@gmail.com'
ADMIN_SENHA = '1234'

CATEGORIAS = ["Escola", "Trabalho", "Projetos", "Pessoal", "Saúde", "Outros"]

def validar_tarefa(nome, descricao, categoria, prazo, prioridade):
    erros = []
    if len(nome) < 5 or len(nome) > 30 or nome.isdigit():
        erros.append("Nome: de 5 a 30 caracteres, não só números.")
    if len(descricao) > 100:
        erros.append("Descrição: no máximo 100 caacteres.")
    if len(categoria) < 5 or len(categoria) > 30 or categoria.isdigit():
        erros.append("Categoria: de 5 a 30 caracteres, não só números.")
    if prioridade not in ("ALTA", "MEDIA", "BAIXA"):
        erros.append("Prioridade inválida.")


    try:
        data = date.fromisoformat(prazo)
        if data < date.today():
            erros.append("Prazo> a data não pode ser no passado.")
    except ValueError:
        erros.append("Prazo: Informe uma data válida")
    return erros

@app.route("/adicionar", methods = ["GET", "POST"])
def adicionar():
    if request.method == "GET":
        return render_template("formulario.html", categorias=CATEGORIAS, dados={}, erros={})
    # POST: ler o que veio do formulário
    nome_tarefa = request.form.get("nome_tarefa", "").strip()
    descricao = request.form.get("descricao", "").strip()
    categoria = request.form.get("categoria", "").strip()
    data_prazo = request.form.get("data_prazo", "")
    prioridade = request.form.get("prioridade", "")

    erros = validar_tarefa(nome_tarefa, descricao, categoria, data_prazo, prioridade)

    if erros:
        return render_template("formulario.html", categoria=CATEGORIAS, dados=request.form, erros=erros)
    
    if inserir_tarefa(nome_tarefa, descricao, categoria, data_prazo, prioridade):
        flash("Tarefa adicionada com sucesso!")
    else:
        flash("Não foi possível salvar. Confira a conexão com o banco.")
    return redirect("/")


@app.route("/")
def home():
    tarefas = consultar_tarefas()
    return render_template("index.html", tarefas=tarefas)

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")

    # POST
    email = request.form.get('email') #Pegando o email que estava no form HTML
    senha = request.form.get('senha')

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session['logado'] = True
        return redirect('/') #Redireciona para a rota inicial
    else:
        return render_template('login.html', msgerro = "E-mail ou senha incorretos")

if __name__=="__main__":
    app.run(debug=True, port=5000)
