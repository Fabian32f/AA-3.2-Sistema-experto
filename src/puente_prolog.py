# =========================================================
# Puente entre Python y Prolog
# Python controla la interacción y Prolog realiza la inferencia
# =========================================================

import os
from swiplserver import PrologMQI


NOMBRES_CARRERAS = {
    "sistemas_computacionales": "Ingeniería en Sistemas Computacionales",
    "ciencia_de_datos": "Ingeniería en Ciencia de Datos",
    "administracion": "Licenciatura en Administración",
    "industrial": "Ingeniería Industrial",
    "alimentarias": "Ingeniería en Industrias Alimentarias",
    "desarrollo_comunitario": "Ingeniería en Desarrollo Comunitario",
    "gestion_empresarial": "Ingeniería en Gestión Empresarial",
}


def ruta_base_conocimiento():
    directorio_src = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(os.path.dirname(directorio_src), "knowledge_base", "carreras.pl")
    return ruta.replace("\\", "/")


def convertir_a_lista_prolog(intereses_usuario):
    return "[" + ",".join(intereses_usuario) + "]"


def consultar_prolog(intereses_usuario):
    """
    Envía el perfil del usuario a Prolog.
    Prolog calcula la mejor carrera y el ranking de coincidencias.
    """
    ruta_pl = ruta_base_conocimiento()
    perfil_prolog = convertir_a_lista_prolog(intereses_usuario)

    with PrologMQI() as mqi:
        with mqi.create_thread() as hilo_prolog:
            hilo_prolog.query(f"consult('{ruta_pl}')")

            mejor = hilo_prolog.query(
                f"mejor_carrera({perfil_prolog}, Carrera, Puntaje)"
            )

            ranking = hilo_prolog.query(
                f"recomendar_carrera({perfil_prolog}, Carrera, Puntaje)"
            )

    mejor_resultado = None
    if isinstance(mejor, list) and len(mejor) > 0:
        carrera = str(mejor[0]["Carrera"])
        mejor_resultado = {
            "id": carrera,
            "nombre": NOMBRES_CARRERAS.get(carrera, carrera),
            "puntaje": int(mejor[0]["Puntaje"])
        }

    ranking_resultados = tuple(
        sorted(
            map(
                lambda item: {
                    "id": str(item["Carrera"]),
                    "nombre": NOMBRES_CARRERAS.get(str(item["Carrera"]), str(item["Carrera"])),
                    "puntaje": int(item["Puntaje"])
                },
                ranking if isinstance(ranking, list) else []
            ),
            key=lambda item: item["puntaje"],
            reverse=True
        )
    )

    return mejor_resultado, ranking_resultados
