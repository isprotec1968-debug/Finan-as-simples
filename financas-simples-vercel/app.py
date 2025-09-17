from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulação de banco de dados em memória
transacoes = []

@app.route("/")
def index():
    return render_template("index.html", transacoes=transacoes)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        descricao = request.form["descricao"]
        valor = float(request.form["valor"])
        tipo = request.form["tipo"]  # entrada ou saída
        transacoes.append({"descricao": descricao, "valor": valor, "tipo": tipo})
        return redirect(url_for("index"))
    return render_template("adicionar.html")

@app.route("/relatorio")
def relatorio():
    total_entrada = sum(t["valor"] for t in transacoes if t["tipo"] == "entrada")
    total_saida = sum(t["valor"] for t in transacoes if t["tipo"] == "saida")
    saldo = total_entrada - total_saida
    return render_template("relatorio.html", 
                           total_entrada=total_entrada, 
                           total_saida=total_saida, 
                           saldo=saldo)

if __name__ == "__main__":
    app.run(debug=True)
