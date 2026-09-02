def calcular_perfiles(respuestas):

    perfiles = {

        "TEC": 0,
        "MAT": 0,
        "SAL": 0,
        "CIE": 0,
        "ECO": 0,
        "JUR": 0,
        "HUM": 0,
        "AGR": 0

    }

    for id_pregunta, respuesta in respuestas.items():

        if id_pregunta in REGLAS_PERFILES:

            reglas = REGLAS_PERFILES[id_pregunta]

            # Algunas respuestas pueden ser múltiples
            if isinstance(respuesta, list):

                for perfil, peso in reglas.items():

                    perfiles[perfil] += len(respuesta) * peso

            # Preguntas con valores numéricos
            else:

                try:

                    valor = int(respuesta)

                    for perfil, peso in reglas.items():

                        perfiles[perfil] += valor * peso

                except (ValueError, TypeError):

                    pass

    return perfiles

REGLAS_PERFILES = {

    "6": {
        "TEC": 1
    },

    "7": {
        "CIE": 1
    },

    "8": {
        "SAL": 1
    },

    "9": {
        "JUR": 1
    },

    "10": {
        "ECO": 1
    },

    "11": {
        "AGR": 1
    },

    "12": {
        "AGR": 1
    }

}