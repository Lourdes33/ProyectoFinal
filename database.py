import sqlite3
import os


# Ruta donde se almacenará la base de datos
DATABASE_PATH = os.path.join(
    "database",
    "orientacion.db"
)


def obtener_conexion():
    """
    Crea y devuelve una conexión con la base de datos SQLite.
    """

    conexion = sqlite3.connect(DATABASE_PATH)

    # Permite acceder a las columnas por nombre
    conexion.row_factory = sqlite3.Row

    return conexion


def crear_base_datos():
    """
    Crea las tablas necesarias para la base de conocimientos
    del sistema de orientación vocacional.
    """

    conexion = obtener_conexion()

    cursor = conexion.cursor()


    # ==========================================
    # TABLA: FACULTADES
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facultades (

            id_facultad INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL UNIQUE,

            ciudad TEXT

        )
    """)


    # ==========================================
    # TABLA: AREAS
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS areas (

            id_area INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL UNIQUE,

            descripcion TEXT

        )
    """)


    # ==========================================
    # TABLA: CARRERAS
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carreras (

            id_carrera INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            id_facultad INTEGER NOT NULL,

            id_area INTEGER NOT NULL,

            duracion TEXT,

            modalidad TEXT,

            descripcion TEXT,

            activa INTEGER DEFAULT 1,

            FOREIGN KEY (id_facultad)
                REFERENCES facultades(id_facultad),

            FOREIGN KEY (id_area)
                REFERENCES areas(id_area)

        )
    """)

    # ==========================================
    # TABLA: CARACTERISTICAS
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS caracteristicas (

            id_caracteristica INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL UNIQUE,

            dimension TEXT NOT NULL,

            descripcion TEXT

        )
    """)

    # ==========================================
    # TABLA: CARRERA_CARACTERISTICAS
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carrera_caracteristicas (

            id_carrera INTEGER NOT NULL,

            id_caracteristica INTEGER NOT NULL,

            peso INTEGER NOT NULL CHECK (peso BETWEEN 1 AND 5),

            PRIMARY KEY (
                id_carrera,
                id_caracteristica
            ),

            FOREIGN KEY (id_carrera)
                REFERENCES carreras(id_carrera),

            FOREIGN KEY (id_caracteristica)
                REFERENCES caracteristicas(id_caracteristica)

        )
    """)

    # ==========================================
    # TABLA: SECCIONES
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS secciones (

            id_seccion INTEGER PRIMARY KEY,

            letra TEXT NOT NULL UNIQUE,

            titulo TEXT NOT NULL,

            descripcion TEXT,

            escala_descripcion TEXT,

            orden INTEGER NOT NULL UNIQUE

        )
    """)

    # ==========================================
    # TABLA: PREGUNTAS
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS preguntas (

            id_pregunta INTEGER PRIMARY KEY,

            id_seccion INTEGER NOT NULL,

            texto TEXT NOT NULL,

            tipo TEXT NOT NULL,

            orden INTEGER NOT NULL,

            FOREIGN KEY (id_seccion)
               REFERENCES secciones(id_seccion)

        )
    """)

    # ==========================================
    # TABLA: OPCIONES
    # ==========================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS opciones (

            id_opcion INTEGER PRIMARY KEY AUTOINCREMENT,

            id_pregunta INTEGER NOT NULL,

            texto TEXT NOT NULL,

            valor TEXT,

            orden INTEGER NOT NULL,

            UNIQUE (id_pregunta, valor),

            FOREIGN KEY (id_pregunta)
                REFERENCES preguntas(id_pregunta)

        )
    """)


    conexion.commit()

    conexion.close()


def cargar_cuestionario():

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    secciones = [

        (
            1,
            "A",
            "Contexto",
            (
                "Estas preguntas nos permiten conocer algunas condiciones "
                "personales y geográficas que pueden influir en la elección "
                "de una carrera."
            ),
            None,
            1
        ),

        (
            2,
            "B",
            "Intereses",
            (
                "Seleccioná las opciones que mejor representen tus intereses "
                "y las actividades que te resultan más atractivas."
            ),
            None,
            2
        ),

        (
            3,
            "C",
            "Autoeficacia",
            (
                "Indicá qué tan capaz te considerás para realizar las "
                "siguientes actividades."
            ),
            "1 = Nada capaz | 5 = Muy capaz",
            3
        ),

        (
            4,
            "D",
            "Habilidades percibidas",
            (
                "Estas preguntas permiten identificar las fortalezas y "
                "preferencias académicas que percibís en vos mismo/a."
            ),
            None,
            4
        ),

        (
            5,
            "E",
            "Expectativas de resultado",
            (
                "Indicá la importancia que tienen para vos los siguientes "
                "aspectos al pensar en tu futuro profesional."
            ),
            "1 = Nada importante | 5 = Muy importante",
            5
        ),

        (
            6,
            "F",
            "Estilo de trabajo",
            (
                "Por último, seleccioná las opciones que mejor representen "
                "el tipo de trabajo en el que te imaginás en el futuro."
            ),
            None,
            6
        )

    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO secciones (
            id_seccion,
            letra,
            titulo,
            descripcion,
            escala_descripcion,
            orden
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, secciones)

    preguntas = [

        # =====================================
        # SECCIÓN A - CONTEXTO
        # =====================================

        (
            1,
            1,
            "¿En qué provincia residís actualmente?",
            "select",
            1
        ),

        (
            2,
            1,
            "¿Estarías dispuesto/a a mudarte para estudiar?",
            "radio",
            2
        ),

        (
            3,
            1,
            "¿Trabajás actualmente?",
            "radio",
            3
        ),

        (
            4,
            1,
            "¿Cuántas horas por semana podrías dedicar al estudio?",
            "radio",
            4
        ),


        # =====================================
        # SECCIÓN B - INTERESES
        # =====================================

        (
            5,
            2,
            "¿Qué actividad te resulta más atractiva?",
            "radio",
            1
        ),

        (
            6,
            2,
            "¿Disfrutás aprender sobre nuevas tecnologías?",
            "escala",
            2
        ),

        (
            7,
            2,
            "¿Te interesan los avances científicos?",
            "escala",
            3
        ),

        (
            8,
            2,
            "¿Te gustaría ayudar a mejorar la salud de las personas?",
            "escala",
            4
        ),

        (
            9,
            2,
            "¿Te interesa comprender leyes y normas?",
            "escala",
            5
        ),

        (
            10,
            2,
            "¿Te gustaría dirigir empresas o emprendimientos?",
            "escala",
            6
        ),

        (
            11,
            2,
            "¿Te interesa trabajar con animales?",
            "escala",
            7
        ),

        (
            12,
            2,
            (
                "¿Te interesa trabajar con cultivos, suelos "
                "o producción agropecuaria?"
            ),
            "escala",
            8
        ),


        # =====================================
        # SECCIÓN C - AUTOEFICACIA
        # =====================================

        (
            13,
            3,
            (
                "¿Qué tan capaz te considerás para resolver "
                "problemas matemáticos?"
            ),
            "escala",
            1
        ),

        (
            14,
            3,
            "¿Qué tan capaz te considerás para aprender programación?",
            "escala",
            2
        ),

        (
            15,
            3,
            (
                "¿Qué tan capaz te considerás para analizar "
                "información compleja?"
            ),
            "escala",
            3
        ),

        (
            16,
            3,
            "¿Qué tan capaz te considerás para comunicarte oralmente?",
            "escala",
            4
        ),

        (
            17,
            3,
            "¿Qué tan capaz te considerás para liderar grupos?",
            "escala",
            5
        ),

        (
            18,
            3,
            "¿Qué tan capaz te considerás para realizar investigaciones?",
            "escala",
            6
        ),

        (
            19,
            3,
            (
                "¿Qué tan capaz te considerás para trabajar "
                "con pacientes o personas?"
            ),
            "escala",
            7
        ),


        # =====================================
        # SECCIÓN D - HABILIDADES
        # =====================================

        (
            20,
            4,
            "¿Cuál considerás que es tu principal fortaleza?",
            "radio",
            1
        ),

        (
            21,
            4,
            (
                "¿Qué materias te resultaban más fáciles en la escuela? "
                "(Podés seleccionar más de una opción)"
            ),
            "checkbox",
            2
        ),

        (
            22,
            4,
            (
                "¿Qué materias disfrutabas más? "
                "(Podés seleccionar más de una opción)"
            ),
            "checkbox",
            3
        ),


        # =====================================
        # SECCIÓN E - EXPECTATIVAS
        # =====================================

        (
            23,
            5,
            (
                "¿Qué tan importante es para vos tener una alta "
                "salida laboral?"
            ),
            "escala",
            1
        ),

        (
            24,
            5,
            (
                "¿Qué tan importante es para vos obtener buenos "
                "ingresos económicos?"
            ),
            "escala",
            2
        ),

        (
            25,
            5,
            (
                "¿Qué tan importante es para vos ayudar a otras personas?"
            ),
            "escala",
            3
        ),

        (
            26,
            5,
            (
                "¿Qué tan importante es para vos generar "
                "conocimiento científico?"
            ),
            "escala",
            4
        ),

        (
            27,
            5,
            (
                "¿Qué tan importante es para vos innovar y desarrollar "
                "tecnología?"
            ),
            "escala",
            5
        ),

        (
            28,
            5,
            (
                "¿Qué tan importante es para vos dirigir organizaciones "
                "o proyectos?"
            ),
            "escala",
            6
        ),


        # =====================================
        # SECCIÓN F - ESTILO DE TRABAJO
        # =====================================

        (
            29,
            6,
            "¿Con qué tipo de tareas te sentís más cómodo/a?",
            "radio",
            1
        ),

        (
            30,
            6,
            "¿Dónde te imaginás trabajando dentro de 10 años?",
            "radio",
            2
        )

    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO preguntas (
            id_pregunta,
            id_seccion,
            texto,
            tipo,
            orden
        )
        VALUES (?, ?, ?, ?, ?)
    """, preguntas)

    opciones = [

        # =====================================
        # PREGUNTA 1 - PROVINCIAS
        # =====================================

        (1, "Buenos Aires", "Buenos Aires", 1),
        (1, "Catamarca", "Catamarca", 2),
        (1, "Chaco", "Chaco", 3),
        (1, "Chubut", "Chubut", 4),
        (1, "Ciudad Autónoma de Buenos Aires", "Ciudad Autónoma de Buenos Aires", 5),
        (1, "Córdoba", "Córdoba", 6),
        (1, "Corrientes", "Corrientes", 7),
        (1, "Entre Ríos", "Entre Ríos", 8),
        (1, "Formosa", "Formosa", 9),
        (1, "Jujuy", "Jujuy", 10),
        (1, "La Pampa", "La Pampa", 11),
        (1, "La Rioja", "La Rioja", 12),
        (1, "Mendoza", "Mendoza", 13),
        (1, "Misiones", "Misiones", 14),
        (1, "Neuquén", "Neuquén", 15),
        (1, "Río Negro", "Río Negro", 16),
        (1, "Salta", "Salta", 17),
        (1, "San Juan", "San Juan", 18),
        (1, "San Luis", "San Luis", 19),
        (1, "Santa Cruz", "Santa Cruz", 20),
        (1, "Santa Fe", "Santa Fe", 21),
        (1, "Santiago del Estero", "Santiago del Estero", 22),
        (1, "Tierra del Fuego", "Tierra del Fuego", 23),
        (1, "Tucumán", "Tucumán", 24),


        # =====================================
        # PREGUNTA 2
        # =====================================

        (2, "Sí", "Sí", 1),
        (2, "No", "No", 2),
        (2, "Tal vez", "Tal vez", 3),


        # =====================================
        # PREGUNTA 3
        # =====================================

        (3, "Sí", "Sí", 1),
        (3, "No", "No", 2),


        # =====================================
        # PREGUNTA 4
        # =====================================

        (4, "Menos de 10 horas", "Menos de 10 horas", 1),
        (4, "Entre 10 y 20 horas", "Entre 10 y 20 horas", 2),
        (4, "Entre 20 y 30 horas", "Entre 20 y 30 horas", 3),
        (4, "Más de 30 horas", "Más de 30 horas", 4),


        # =====================================
        # PREGUNTA 5
        # =====================================

        (5, "Programar sistemas", "Programar sistemas", 1),
        (5, "Resolver problemas matemáticos", "Resolver problemas matemáticos", 2),
        (5, "Investigar fenómenos científicos", "Investigar fenómenos científicos", 3),
        (5, "Atender pacientes", "Atender pacientes", 4),
        (5, "Gestionar organizaciones", "Gestionar organizaciones", 5),
        (5, "Defender derechos", "Defender derechos", 6),
        (5, "Enseñar", "Enseñar", 7),
        (5, "Trabajar con animales", "Trabajar con animales", 8),
        (5, "Trabajar en producción agropecuaria", "Trabajar en producción agropecuaria", 9),


        # =====================================
        # PREGUNTA 20
        # =====================================

        (20, "Lógica", "Lógica", 1),
        (20, "Creatividad", "Creatividad", 2),
        (20, "Comunicación", "Comunicación", 3),
        (20, "Empatía", "Empatía", 4),
        (20, "Liderazgo", "Liderazgo", 5),
        (20, "Organización", "Organización", 6),
        (20, "Observación científica", "Observación científica", 7),


        # =====================================
        # PREGUNTA 21
        # =====================================

        (21, "Matemática", "Matemática", 1),
        (21, "Física", "Física", 2),
        (21, "Química", "Química", 3),
        (21, "Biología", "Biología", 4),
        (21, "Historia", "Historia", 5),
        (21, "Lengua", "Lengua", 6),
        (21, "Economía", "Economía", 7),
        (21, "Informática", "Informática", 8),


        # =====================================
        # PREGUNTA 22
        # =====================================

        (22, "Matemática", "Matemática", 1),
        (22, "Física", "Física", 2),
        (22, "Química", "Química", 3),
        (22, "Biología", "Biología", 4),
        (22, "Historia", "Historia", 5),
        (22, "Lengua", "Lengua", 6),
        (22, "Economía", "Economía", 7),
        (22, "Informática", "Informática", 8),


        # =====================================
        # PREGUNTA 29
        # =====================================

        (29, "Computadoras y tecnología", "Computadoras y tecnología", 1),
        (29, "Números y análisis", "Números y análisis", 2),
        (29, "Personas", "Personas", 3),
        (29, "Investigación científica", "Investigación científica", 4),
        (29, "Gestión empresarial", "Gestión empresarial", 5),
        (29, "Aspectos legales", "Aspectos legales", 6),
        (29, "Animales", "Animales", 7),
        (29, "Producción agropecuaria", "Producción agropecuaria", 8),


        # =====================================
        # PREGUNTA 30
        # =====================================

        (30, "Empresa tecnológica", "Empresa tecnológica", 1),
        (30, "Laboratorio científico", "Laboratorio científico", 2),
        (30, "Hospital o clínica", "Hospital o clínica", 3),
        (30, "Estudio jurídico", "Estudio jurídico", 4),
        (30, "Empresa privada", "Empresa privada", 5),
        (30, "Universidad", "Universidad", 6),
        (30, "Campo o establecimiento agropecuario", "Campo o establecimiento agropecuario", 7),
        (30, "Organismo público", "Organismo público", 8)

    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO opciones (
            id_pregunta,
            texto,
            valor,
            orden
        )
        VALUES (?, ?, ?, ?)
    """, opciones)

    conexion.commit()

    conexion.close()

    print("Cuestionario cargado correctamente.")


def obtener_secciones():

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM secciones
        ORDER BY orden
    """)

    secciones = cursor.fetchall()

    conexion.close()

    return secciones

def obtener_seccion(id_seccion):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM secciones
        WHERE id_seccion = ?
    """, (id_seccion,))

    seccion = cursor.fetchone()

    conexion.close()

    return seccion

def obtener_preguntas_seccion(id_seccion):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM preguntas
        WHERE id_seccion = ?
        ORDER BY orden
    """, (id_seccion,))

    preguntas = cursor.fetchall()

    conexion.close()

    return preguntas

def obtener_opciones_pregunta(id_pregunta):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM opciones
        WHERE id_pregunta = ?
        ORDER BY orden
    """, (id_pregunta,))

    opciones = cursor.fetchall()

    conexion.close()

    return opciones

def obtener_cuestionario_seccion(id_seccion):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    # Obtener la sección
    cursor.execute("""
        SELECT *
        FROM secciones
        WHERE id_seccion = ?
    """, (id_seccion,))

    seccion = cursor.fetchone()

    if seccion is None:

        conexion.close()

        return None

    # Convertimos la sección a diccionario
    seccion_dict = dict(seccion)

    # Obtener las preguntas
    cursor.execute("""
        SELECT *
        FROM preguntas
        WHERE id_seccion = ?
        ORDER BY orden
    """, (id_seccion,))

    preguntas = cursor.fetchall()

    preguntas_lista = []

    for pregunta in preguntas:

        pregunta_dict = dict(pregunta)

        # Obtener opciones de la pregunta
        cursor.execute("""
            SELECT *
            FROM opciones
            WHERE id_pregunta = ?
            ORDER BY orden
        """, (pregunta["id_pregunta"],))

        opciones = cursor.fetchall()

        pregunta_dict["opciones"] = [
            dict(opcion)
            for opcion in opciones
        ]

        preguntas_lista.append(pregunta_dict)

    seccion_dict["preguntas"] = preguntas_lista

    conexion.close()

    return seccion_dict

if __name__ == "__main__":

    crear_base_datos()

    cargar_cuestionario()

    print("Base de datos y cuestionario inicializados correctamente.")