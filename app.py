from flask import Flask, render_template, request, redirect, url_for, session

from database import (
    obtener_secciones,
    obtener_cuestionario_seccion
)


app = Flask(__name__)

app.secret_key = "clave_secreta_temporal_para_desarrollo"



# ==========================================
# PÁGINA DE INICIO
# ==========================================

@app.route("/")
def inicio():

    return render_template("index.html")


# ==========================================
# INICIO DEL CUESTIONARIO
# ==========================================

@app.route("/cuestionario")
def cuestionario():

    # Reiniciamos las respuestas del cuestionario
    session["respuestas"] = {}

    # Comenzamos con la primera sección
    return redirect(
        url_for(
            "seccion",
            numero=1
        )
    )


# ==========================================
# SECCIONES DEL CUESTIONARIO
# ==========================================

@app.route("/seccion/<int:numero>", methods=["GET", "POST"])
def seccion(numero):

    # Obtenemos todas las secciones
    secciones = obtener_secciones()

    total_secciones = len(secciones)

    # Evitamos acceder a una sección inexistente
    if numero < 1 or numero > total_secciones:

        return redirect(
            url_for("inicio")
        )

    # Obtenemos la sección completa
    seccion_actual = obtener_cuestionario_seccion(numero)

    # Si no existe la sección
    if seccion_actual is None:

        return redirect(
            url_for("inicio")
        )

    # ======================================
    # GUARDAR RESPUESTAS
    # ======================================

    if request.method == "POST":

        # Recuperamos las respuestas anteriores
        respuestas = session.get(
            "respuestas",
            {}
        )

        # Guardamos las respuestas de todas las preguntas
        # de la sección actual
        for pregunta in seccion_actual["preguntas"]:

            id_pregunta = str(
                pregunta["id_pregunta"]
            )

            nombre_campo = f"pregunta_{id_pregunta}"

            # Preguntas con múltiples respuestas
            if pregunta["tipo"] == "checkbox":

                respuesta = request.form.getlist(
                    nombre_campo
                )

            # Preguntas con una sola respuesta
            else:

                respuesta = request.form.get(
                    nombre_campo
                )

            respuestas[id_pregunta] = respuesta

        # Guardamos las respuestas en la sesión
        session["respuestas"] = respuestas

        # Si es la última sección
        if numero == total_secciones:

            return redirect(
                url_for("resultados")
            )

        # Pasamos a la siguiente sección
        return redirect(
            url_for(
                "seccion",
                numero=numero + 1
            )
        )

    # ======================================
    # MOSTRAR SECCIÓN
    # ======================================

    return render_template(
        "seccion.html",
        seccion=seccion_actual,
        numero=numero,
        total_secciones=total_secciones
    )


# ==========================================
# RESULTADOS
# ==========================================

@app.route("/resultados")
def resultados():

    respuestas = session.get(
        "respuestas",
        {}
    )

    return render_template(
        "resultados.html",
        respuestas=respuestas
    )


# ==========================================
# EJECUTAR APLICACIÓN
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)