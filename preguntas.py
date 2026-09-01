SECCIONES = [

    {
        "id": 1,
        "letra": "A",
        "titulo": "Contexto",
        "descripcion": (
            "Estas preguntas nos permiten conocer algunas condiciones "
            "personales y geográficas que pueden influir en la elección "
            "de una carrera."
        ),
        "preguntas": [

            {
                "id": 1,
                "texto": "¿En qué provincia residís actualmente?",
                "tipo": "select",
                "opciones": [
                    "Buenos Aires",
                    "Catamarca",
                    "Chaco",
                    "Chubut",
                    "Ciudad Autónoma de Buenos Aires",
                    "Córdoba",
                    "Corrientes",
                    "Entre Ríos",
                    "Formosa",
                    "Jujuy",
                    "La Pampa",
                    "La Rioja",
                    "Mendoza",
                    "Misiones",
                    "Neuquén",
                    "Río Negro",
                    "Salta",
                    "San Juan",
                    "San Luis",
                    "Santa Cruz",
                    "Santa Fe",
                    "Santiago del Estero",
                    "Tierra del Fuego",
                    "Tucumán"
                ]
            },

            {
                "id": 2,
                "texto": "¿Estarías dispuesto/a a mudarte para estudiar?",
                "tipo": "radio",
                "opciones": [
                    "Sí",
                    "No",
                    "Tal vez"
                ]
            },

            {
                "id": 3,
                "texto": "¿Trabajás actualmente?",
                "tipo": "radio",
                "opciones": [
                    "Sí",
                    "No"
                ]
            },

            {
                "id": 4,
                "texto": "¿Cuántas horas por semana podrías dedicar al estudio?",
                "tipo": "radio",
                "opciones": [
                    "Menos de 10 horas",
                    "Entre 10 y 20 horas",
                    "Entre 20 y 30 horas",
                    "Más de 30 horas"
                ]
            }
        ]
    },

    {
        "id": 2,
        "letra": "B",
        "titulo": "Intereses",
        "descripcion": (
            "Seleccioná las opciones que mejor representen tus intereses "
            "y las actividades que te resultan más atractivas."
        ),
        "preguntas": [

            {
                "id": 5,
                "texto": "¿Qué actividad te resulta más atractiva?",
                "tipo": "radio",
                "opciones": [
                    "Programar sistemas",
                    "Resolver problemas matemáticos",
                    "Investigar fenómenos científicos",
                    "Atender pacientes",
                    "Gestionar organizaciones",
                    "Defender derechos",
                    "Enseñar",
                    "Trabajar con animales",
                    "Trabajar en producción agropecuaria"
                ]
            },

            {
                "id": 6,
                "texto": "¿Disfrutás aprender sobre nuevas tecnologías?",
                "tipo": "escala"
            },

            {
                "id": 7,
                "texto": "¿Te interesan los avances científicos?",
                "tipo": "escala"
            },

            {
                "id": 8,
                "texto": "¿Te gustaría ayudar a mejorar la salud de las personas?",
                "tipo": "escala"
            },

            {
                "id": 9,
                "texto": "¿Te interesa comprender leyes y normas?",
                "tipo": "escala"
            },

            {
                "id": 10,
                "texto": "¿Te gustaría dirigir empresas o emprendimientos?",
                "tipo": "escala"
            },

            {
                "id": 11,
                "texto": "¿Te interesa trabajar con animales?",
                "tipo": "escala"
            },

            {
                "id": 12,
                "texto": (
                    "¿Te interesa trabajar con cultivos, suelos "
                    "o producción agropecuaria?"
                ),
                "tipo": "escala"
            }
        ]
    },

    {
        "id": 3,
        "letra": "C",
        "titulo": "Autoeficacia",
        "descripcion": (
            "Indicá qué tan capaz te considerás para realizar las "
            "siguientes actividades."
        ),
        "escala_descripcion": "1 = Nada capaz | 5 = Muy capaz",
        "preguntas": [

            {
                "id": 13,
                "texto": (
                    "¿Qué tan capaz te considerás para resolver "
                    "problemas matemáticos?"
                ),
                "tipo": "escala"
            },

            {
                "id": 14,
                "texto": "¿Qué tan capaz te considerás para aprender programación?",
                "tipo": "escala"
            },

            {
                "id": 15,
                "texto": (
                    "¿Qué tan capaz te considerás para analizar "
                    "información compleja?"
                ),
                "tipo": "escala"
            },

            {
                "id": 16,
                "texto": "¿Qué tan capaz te considerás para comunicarte oralmente?",
                "tipo": "escala"
            },

            {
                "id": 17,
                "texto": "¿Qué tan capaz te considerás para liderar grupos?",
                "tipo": "escala"
            },

            {
                "id": 18,
                "texto": "¿Qué tan capaz te considerás para realizar investigaciones?",
                "tipo": "escala"
            },

            {
                "id": 19,
                "texto": (
                    "¿Qué tan capaz te considerás para trabajar "
                    "con pacientes o personas?"
                ),
                "tipo": "escala"
            }
        ]
    },

    {
        "id": 4,
        "letra": "D",
        "titulo": "Habilidades percibidas",
        "descripcion": (
            "Estas preguntas permiten identificar las fortalezas y "
            "preferencias académicas que percibís en vos mismo/a."
        ),
        "preguntas": [

            {
                "id": 20,
                "texto": "¿Cuál considerás que es tu principal fortaleza?",
                "tipo": "radio",
                "opciones": [
                    "Lógica",
                    "Creatividad",
                    "Comunicación",
                    "Empatía",
                    "Liderazgo",
                    "Organización",
                    "Observación científica"
                ]
            },

            {
                "id": 21,
                "texto": (
                    "¿Qué materias te resultaban más fáciles en la escuela?"
                ),
                "tipo": "checkbox",
                "opciones": [
                    "Matemática",
                    "Física",
                    "Química",
                    "Biología",
                    "Historia",
                    "Lengua",
                    "Economía",
                    "Informática"
                ]
            },

            {
                "id": 22,
                "texto": "¿Qué materias disfrutabas más?",
                "tipo": "checkbox",
                "opciones": [
                    "Matemática",
                    "Física",
                    "Química",
                    "Biología",
                    "Historia",
                    "Lengua",
                    "Economía",
                    "Informática"
                ]
            }
        ]
    },

    {
        "id": 5,
        "letra": "E",
        "titulo": "Expectativas de resultado",
        "descripcion": (
            "Indicá la importancia que tienen para vos los siguientes "
            "aspectos al pensar en tu futuro profesional."
        ),
        "escala_descripcion": "1 = Nada importante | 5 = Muy importante",
        "preguntas": [

            {
                "id": 23,
                "texto": (
                    "¿Qué tan importante es para vos tener una alta "
                    "salida laboral?"
                ),
                "tipo": "escala"
            },

            {
                "id": 24,
                "texto": (
                    "¿Qué tan importante es para vos obtener buenos "
                    "ingresos económicos?"
                ),
                "tipo": "escala"
            },

            {
                "id": 25,
                "texto": (
                    "¿Qué tan importante es para vos ayudar a otras personas?"
                ),
                "tipo": "escala"
            },

            {
                "id": 26,
                "texto": (
                    "¿Qué tan importante es para vos generar "
                    "conocimiento científico?"
                ),
                "tipo": "escala"
            },

            {
                "id": 27,
                "texto": (
                    "¿Qué tan importante es para vos innovar y desarrollar "
                    "tecnología?"
                ),
                "tipo": "escala"
            },

            {
                "id": 28,
                "texto": (
                    "¿Qué tan importante es para vos dirigir organizaciones "
                    "o proyectos?"
                ),
                "tipo": "escala"
            }
        ]
    },

    {
        "id": 6,
        "letra": "F",
        "titulo": "Estilo de trabajo",
        "descripcion": (
            "Por último, seleccioná las opciones que mejor representen "
            "el tipo de trabajo en el que te imaginás en el futuro."
        ),
        "preguntas": [

            {
                "id": 29,
                "texto": "¿Con qué tipo de tareas te sentís más cómodo/a?",
                "tipo": "checkbox",
                "opciones": [
                    "Computadoras y tecnología",
                    "Números y análisis",
                    "Personas",
                    "Investigación científica",
                    "Gestión empresarial",
                    "Aspectos legales",
                    "Animales",
                    "Producción agropecuaria"
                ]
            },

            {
                "id": 30,
                "texto": "¿Dónde te imaginás trabajando dentro de 10 años?",
                "tipo": "checkbox",
                "opciones": [
                    "Empresa tecnológica",
                    "Laboratorio científico",
                    "Hospital o clínica",
                    "Estudio jurídico",
                    "Empresa privada",
                    "Universidad",
                    "Campo o establecimiento agropecuario",
                    "Organismo público"
                ]
            }
        ]
    }
]