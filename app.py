from flask import Flask, render_template, request, redirect, url_for, session

from preguntas import PREGUNTAS


app = Flask(__name__)

app.secret_key = "clave_secreta_temporal_para_desarrollo"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cuestionario", methods=["GET", "POST"])
def cuestionario():

    if request.method == "POST":

        provincia = request.form.get("provincia")
        traslado = request.form.get("traslado")

        session["provincia"] = provincia
        session["traslado"] = traslado

        # Reiniciamos las respuestas del cuestionario
        session["respuestas"] = {}

        return redirect(url_for("pregunta", numero=1))

    return render_template("cuestionario.html")


@app.route("/pregunta/<int:numero>", methods=["GET", "POST"])
def pregunta(numero):

    # Evitamos números inválidos
    if numero < 1 or numero > len(PREGUNTAS):
        return redirect(url_for("inicio"))

    pregunta_actual = PREGUNTAS[numero - 1]

    if request.method == "POST":

        respuesta = request.form.get("respuesta")

        respuestas = session.get("respuestas", {})

        respuestas[str(numero)] = respuesta

        session["respuestas"] = respuestas

        # Si es la última pregunta
        if numero == len(PREGUNTAS):
            return redirect(url_for("resultados"))

        # Pasamos a la siguiente
        return redirect(url_for("pregunta", numero=numero + 1))

    return render_template(
        "pregunta.html",
        pregunta=pregunta_actual,
        numero=numero,
        total=len(PREGUNTAS)
    )


@app.route("/resultados")
def resultados():

    respuestas = session.get("respuestas", {})

    return render_template(
        "resultados.html",
        respuestas=respuestas
    )


if __name__ == "__main__":
    app.run(debug=True)