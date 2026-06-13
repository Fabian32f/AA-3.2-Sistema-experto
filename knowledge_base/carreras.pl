% =========================================================
% AA 3.2 Sistema experto
% Base de conocimientos y motor de inferencia en Prolog
% =========================================================

% carrera(NombreCarrera, ListaDeCaracteristicas).
% Cada carrera contiene intereses, habilidades y rasgos de perfil.

carrera(sistemas_computacionales, [
    programacion,
    redes,
    desarrollo_software,
    tecnologia,
    logica,
    resolver_problemas
]).

carrera(ciencia_de_datos, [
    matematicas,
    estadistica,
    analisis_datos,
    programacion,
    investigacion,
    logica
]).

carrera(administracion, [
    liderazgo,
    finanzas,
    organizacion,
    comunicacion,
    toma_decisiones,
    gestion_recursos
]).

carrera(industrial, [
    procesos,
    logistica,
    optimizacion,
    produccion,
    calidad,
    mejora_continua
]).

carrera(alimentarias, [
    quimica,
    biologia,
    control_calidad,
    alimentos,
    laboratorio,
    higiene
]).

carrera(desarrollo_comunitario, [
    gestion_social,
    proyectos_sostenibles,
    comunidad,
    empatia,
    trabajo_social,
    desarrollo_local
]).

carrera(gestion_empresarial, [
    negocios,
    innovacion,
    estrategias,
    emprendimiento,
    marketing,
    planificacion
]).

% ---------------------------------------------------------
% Reglas de inferencia
% ---------------------------------------------------------

coincidencia(PerfilUsuario, CaracteristicasCarrera, Caracteristica) :-
    member(Caracteristica, PerfilUsuario),
    member(Caracteristica, CaracteristicasCarrera).

puntaje_carrera(PerfilUsuario, Carrera, Puntaje) :-
    carrera(Carrera, CaracteristicasCarrera),
    findall(
        Caracteristica,
        coincidencia(PerfilUsuario, CaracteristicasCarrera, Caracteristica),
        Coincidencias
    ),
    length(Coincidencias, Puntaje).

recomendar_carrera(PerfilUsuario, Carrera, Puntaje) :-
    puntaje_carrera(PerfilUsuario, Carrera, Puntaje),
    Puntaje > 0.

mejor_carrera(PerfilUsuario, Carrera, Puntaje) :-
    findall(
        P-C,
        recomendar_carrera(PerfilUsuario, C, P),
        Resultados
    ),
    sort(0, @>=, Resultados, [Puntaje-Carrera|_]).
