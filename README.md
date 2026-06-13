# Sistema Experto de Orientación Vocacional

**Actividad:** AA 3.2 Sistema experto  
**Materia:** Programación Lógica y Funcional  
**Institución:** TecNM Campus Felipe Carrillo Puerto  
**Modalidad:** Colaborativa, 2 integrantes  
**Autores:** Martin Adrian Ayala Uc y Fabian Kinil Adame

## Descripción

Este proyecto desarrolla un sistema experto para recomendar una carrera ideal a estudiantes de nuevo ingreso del Tecnológico.

El sistema integra dos paradigmas:

1. **Paradigma lógico:** Prolog funciona como motor de inferencia. En Prolog se encuentra la base de conocimientos con las carreras, habilidades, intereses y reglas para determinar la carrera recomendada.
2. **Paradigma funcional:** Python funciona como controlador. Python aplica el cuestionario interactivo, captura el perfil del usuario y se comunica con Prolog. En el código se usan `map`, `filter` e inmutabilidad mediante tuplas.

## Carreras consideradas

Aunque el objetivo menciona 6 opciones, las instrucciones enlistan 7 carreras. Por eso se incluyen:

1. Ingeniería en Sistemas Computacionales
2. Ingeniería en Ciencia de Datos
3. Licenciatura en Administración
4. Ingeniería Industrial
5. Ingeniería en Industrias Alimentarias
6. Ingeniería en Desarrollo Comunitario
7. Ingeniería en Gestión Empresarial

## Estructura del proyecto

```text
AA-3.2 Sistema experto/
│
├── knowledge_base/
│   └── carreras.pl
│
├── src/
│   ├── cuestionario.py
│   ├── main.py
│   └── puente_prolog.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Requisitos previos

- Python 3.x
- SWI-Prolog instalado
- SWI-Prolog agregado al PATH del sistema
- pip

## Instalación

Clonar el repositorio o descargar el proyecto.

Entrar a la carpeta raíz del proyecto:

```bash
cd "AA-3.2 Sistema experto"
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecutar el archivo principal:

```bash
python src/main.py
```

El programa mostrará un cuestionario interactivo. El usuario debe responder con `s` para sí o `n` para no.

Al finalizar, Python enviará el perfil del usuario a Prolog. Prolog realizará la inferencia y devolverá la carrera recomendada junto con un ranking de coincidencias.

## Funcionamiento general

1. Python muestra un cuestionario interactivo.
2. Las respuestas afirmativas se convierten en características del perfil.
3. Python envía el perfil a Prolog mediante `swiplserver`.
4. Prolog compara el perfil con la base de conocimientos.
5. Prolog calcula el puntaje de cada carrera.
6. Python muestra la carrera ideal recomendada.

## Uso del paradigma lógico

El archivo `knowledge_base/carreras.pl` contiene hechos como:

```prolog
carrera(sistemas_computacionales, [programacion, redes, desarrollo_software]).
```

También contiene reglas de inferencia como:

```prolog
puntaje_carrera(PerfilUsuario, Carrera, Puntaje).
recomendar_carrera(PerfilUsuario, Carrera, Puntaje).
mejor_carrera(PerfilUsuario, Carrera, Puntaje).
```

Estas reglas permiten determinar qué carrera se ajusta mejor a una combinación de características.

## Uso del paradigma funcional

El archivo `src/cuestionario.py` aplica características funcionales:

- `map`: transforma cada pregunta en una característica o `None`.
- `filter`: elimina los valores `None`.
- Inmutabilidad: las preguntas, respuestas e intereses se manejan como tuplas.

## Dependencias

La dependencia principal es:

```text
swiplserver
```

Esta permite la comunicación entre Python y SWI-Prolog.

## Integrantes

- Martin Adrian Ayala Uc
- Fabian Kinil Adame
