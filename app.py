from flask import Flask, render_template, request, redirect, url_for, session

from preguntas import SECCIONES


app = Flask(__name__)

app.secret_key = "clave_secreta_temporal_para_desarrollo"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cuestionario")
def cuestionario():

        # Reiniciamos las respuestas del cuestionario
        session["respuestas"] = {}

        # Comenzamos con la primera sección
        return redirect(url_for("seccion", numero=1))



@app.route("/seccion/<int:numero>", methods=["GET", "POST"])
def seccion(numero):

    # Evitamos acceder a una sección inexistente
    if numero < 1 or numero > len(SECCIONES):
        return redirect(url_for("inicio"))

    seccion_actual = SECCIONES[numero - 1]

    if request.method == "POST":

        # Recuperamos las respuestas guardadas
        respuestas = session.get("respuestas", {})

        # Guardamos las respuestas de todas las preguntas
        # de la sección actual
        
        for pregunta in seccion_actual["preguntas"]:

            id_pregunta = str(pregunta["id"])

            nombre_campo = f"pregunta_{id_pregunta}"

            # Si permite seleccionar varias opciones
            if pregunta["tipo"] == "checkbox":

                respuesta = request.form.getlist(nombre_campo)

            # Para preguntas con una sola respuesta
            else:

                respuesta = request.form.get(nombre_campo)

            respuestas[id_pregunta] = respuesta

        # Guardamos nuevamente las respuestas en la sesión
        session["respuestas"] = respuestas

        # Si es la última sección
        if numero == len(SECCIONES):

            return redirect(url_for("resultados"))

        # Pasamos a la siguiente sección
        return redirect(
            url_for(
                "seccion",
                numero=numero + 1
            )
        )

    return render_template(
        "seccion.html",
        seccion=seccion_actual,
        numero=numero,
        total_secciones=len(SECCIONES)
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