import os
from swiplserver import PrologMQI

def obtener_carreras(intereses_usuario):
    """Usa el servidor oficial de Prolog (swiplserver) para evitar crashes de memoria."""
    directorio_src = os.path.dirname(os.path.abspath(__file__))
    # Transformamos las diagonales para que Prolog en Windows no falle
    ruta_pl = os.path.join(os.path.dirname(directorio_src), "knowledge_base", "carreras.pl").replace('\\', '/')
    
    carreras_encontradas = []
    
    # PrologMQI crea un proceso seguro y aislado
    with PrologMQI() as mqi:
        with mqi.create_thread() as hilo_prolog:
            # Cargamos la base de conocimientos
            hilo_prolog.query(f"consult('{ruta_pl}').")
            
            # Consultamos cada interés del usuario
            for interes in intereses_usuario:
                interes_san = interes.lower().replace(" ", "_")
                resultado = hilo_prolog.query(f"sugerir_por_interes(Carrera, {interes_san}).")
                
                # Si hay coincidencias, Prolog devuelve una lista de diccionarios
                if isinstance(resultado, list):
                    # PARADIGMA FUNCIONAL: Usamos map para extraer solo los valores
                    nombres = list(map(lambda r: r["Carrera"], resultado))
                    carreras_encontradas.extend(nombres)
                    
    return carreras_encontradas