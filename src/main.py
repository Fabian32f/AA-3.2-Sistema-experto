from puente_prolog import obtener_carreras
from cuestionario import PREGUNTAS, recopilar_intereses

def evaluar_mejor_opcion(carreras_sugeridas):
    """Determina de forma funcional la carrera con mayor puntaje."""
    if not carreras_sugeridas:
        return "No se encontraron coincidencias claras. Te recomendamos explorar los perfiles académicos."
    
    # PARADIGMA FUNCIONAL: Mapeamos los elementos únicos a tuplas inmutables (carrera, conteo)
    conteo_carreras = list(map(lambda c: (c, carreras_sugeridas.count(c)), set(carreras_sugeridas)))
    
    # Obtenemos el elemento con el conteo máximo sin usar bucles for/while
    mejor_opcion = max(conteo_carreras, key=lambda x: x[1])
    return mejor_opcion[0]

def main():
    print("=========================================================")
    print("  SISTEMA EXPERTO DE ORIENTACIÓN VOCACIONAL - TECNOLÓGICO  ")
    print("=========================================================\n")
    print("Por favor, responde 's' (sí) o 'n' (no) a las siguientes preguntas:\n")
    
    # 1. Ejecutar cuestionario recursivo (100% funcional y puro)
    intereses_alumno = recopilar_intereses(PREGUNTAS)
    
    # 2. Consultar al motor lógico (Prolog) de manera segura
    todas_las_sugerencias = obtener_carreras(intereses_alumno)
    
    # 3. Procesar inferencia analítica
    resultado_final = evaluar_mejor_opcion(todas_las_sugerencias)
    
    # 4. Desplegar diagnóstico
    carrera_formateada = resultado_final.upper().replace("_", " ")
    print("\n=========================================================")
    print(f" DIAGNÓSTICO: La carrera ideal para tu perfil es:\n » {carrera_formateada} «")
    print("=========================================================")

if __name__ == "__main__":
    main()