# =========================================================
# Cuestionario interactivo
# Paradigma funcional: map, filter e inmutabilidad
# =========================================================

# Tupla inmutable de tuplas: (pregunta, caracteristica).
PREGUNTAS = (
    ("¿Te gusta programar y desarrollar software?", "programacion"),
    ("¿Te interesa el diseño de redes y conectividad?", "redes"),
    ("¿Te interesa crear aplicaciones o sistemas?", "desarrollo_software"),
    ("¿Te gusta resolver problemas usando lógica?", "logica"),
    ("¿Te apasiona el análisis de grandes volúmenes de datos?", "analisis_datos"),
    ("¿Te llaman la atención las matemáticas?", "matematicas"),
    ("¿Te interesa la estadística?", "estadistica"),
    ("¿Te gusta investigar y encontrar patrones?", "investigacion"),
    ("¿Te gustaría liderar equipos?", "liderazgo"),
    ("¿Te interesa administrar finanzas o recursos?", "finanzas"),
    ("¿Te consideras una persona organizada?", "organizacion"),
    ("¿Tienes facilidad para comunicar ideas?", "comunicacion"),
    ("¿Te interesa optimizar procesos de producción?", "procesos"),
    ("¿Te interesa la logística?", "logistica"),
    ("¿Te interesa la calidad y mejora continua?", "calidad"),
    ("¿Te gusta la química?", "quimica"),
    ("¿Te gusta la biología?", "biologia"),
    ("¿Te interesa el control de calidad de alimentos?", "control_calidad"),
    ("¿Te gustaría trabajar con alimentos o laboratorio?", "alimentos"),
    ("¿Te motiva desarrollar proyectos de impacto social?", "gestion_social"),
    ("¿Te interesa apoyar a comunidades?", "comunidad"),
    ("¿Te consideras una persona empática?", "empatia"),
    ("¿Te interesa el mundo de los negocios?", "negocios"),
    ("¿Te interesa la innovación empresarial?", "innovacion"),
    ("¿Te gustaría emprender?", "emprendimiento"),
    ("¿Te interesa el marketing o la planificación?", "marketing"),
)


def normalizar_respuesta(respuesta):
    return respuesta.strip().lower()


def es_afirmativa(respuesta):
    return respuesta in ("s", "si", "sí", "y", "yes")


def preguntar(pregunta_caracteristica):
    pregunta, caracteristica = pregunta_caracteristica
    respuesta = normalizar_respuesta(input(f"{pregunta} (s/n): "))
    return caracteristica if es_afirmativa(respuesta) else None


def recopilar_intereses(preguntas=PREGUNTAS):
    """
    map: transforma cada pregunta en una característica o None.
    filter: elimina las respuestas negativas representadas como None.
    inmutabilidad: preguntas, respuestas e intereses se manejan como tuplas.
    """
    respuestas = tuple(map(preguntar, preguntas))
    intereses_usuario = tuple(filter(lambda interes: interes is not None, respuestas))
    return intereses_usuario
