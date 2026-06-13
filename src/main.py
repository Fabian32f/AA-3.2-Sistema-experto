# =========================================================
# AA 3.2 Sistema experto de orientación vocacional
# Controlador: Python
# Motor de inferencia: Prolog
# =========================================================

from cuestionario import recopilar_intereses
from puente_prolog import consultar_prolog


def mostrar_perfil(intereses_usuario):
    print("\n=========================================================")
    print(" PERFIL CAPTURADO")
    print("=========================================================")

    if not intereses_usuario:
        print("No se registraron intereses afirmativos.")
        return

    for interes in intereses_usuario:
        print(f"- {interes}")


def mostrar_resultado(mejor_resultado, ranking):
    print("\n=========================================================")
    print(" RESULTADO DEL SISTEMA EXPERTO")
    print("=========================================================")

    if mejor_resultado is None:
        print("No se encontraron coincidencias claras.")
        print("Te recomendamos volver a contestar el cuestionario.")
        return

    print("\nCarrera ideal recomendada:")
    print(f"» {mejor_resultado['nombre']} «")
    print(f"Puntaje de coincidencia: {mejor_resultado['puntaje']}")

    print("\nRanking de carreras recomendadas:")
    for item in ranking:
        print(f"- {item['nombre']}: {item['puntaje']} coincidencias")


def main():
    print("=========================================================")
    print(" SISTEMA EXPERTO DE ORIENTACIÓN VOCACIONAL")
    print("=========================================================")
    print("Responde con 's' para sí o 'n' para no.\n")

    intereses_usuario = recopilar_intereses()
    mejor_resultado, ranking = consultar_prolog(intereses_usuario)

    mostrar_perfil(intereses_usuario)
    mostrar_resultado(mejor_resultado, ranking)


if __name__ == "__main__":
    main()
