from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Lista para armazenar pedidos
pedidos = []

@app.route("/", methods=["GET", "POST"])
def pedido():
    if request.method == "POST":
        nome = request.form["nome"]
        bairro = request.form["bairro"]
        tipo = request.form["tipo"]
        lat = request.form.get("lat", "-15.1167")
        lon = request.form.get("lon", "39.2667")
        pedido = {"nome": nome, "bairro": bairro, "tipo": tipo, "lat": lat, "lon": lon, "estado": "Pendente"}
        pedidos.append(pedido)
        return "<h3>Pedido enviado com sucesso!</h3>"
    return render_template("pedido.html")

@app.route("/central")
def central():
    return render_template("central.html", pedidos=pedidos)

@app.route("/enviar/<int:id>")
def enviar(id):
    pedidos[id]["estado"] = "Enviado"
    return jsonify({
        "nome": pedidos[id]["nome"],
        "bairro": pedidos[id]["bairro"],
        "lat": pedidos[id]["lat"],
        "lon": pedidos[id]["lon"],
        "tipo": pedidos[id]["tipo"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
