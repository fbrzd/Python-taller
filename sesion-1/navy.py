# metainformacion (tags)
# texto (lo principal)
# imagen (fuentes en otros formatos)
# links (referencias)

PAGES = {
    "facebook": ("social", "red social + chat + post + grupos... [cuenta]", "imagen", ("youtube", "agario", "jmonline")),
    "github": ("info", "red para colaborar/subir/bajar proyectos informaticos", "imagen", ("wikipedia","facebook")),
    "youtube": ("social", "plataforma popular para ver/subir videos", "imagen", ("youtube", "facebook")),
    "wikipedia": ("info", "plataforma de conocimiento popular, gratis, abierta", "imagen", ("wikipedia", "mineduc")),
    "vimeo": ("social", "plataforma profesional para compartir videos", "imagen", ("vimeo", "wikipedia")),
    "agario": ("juego", "juego mmo de celulas, minimalista, todos-contra-todos", "imagen", ("youtube",)),
    "mineduc": ("pais", "ministerio de educacion, chile", "imagen", tuple()),
    "dinorpg": ("juego", "rpg de dinosarios por turnos diarios... muy viejo", "imagen", ("vimeo",)),
    "jmonline": ("empresa", "comprar pasajes de bus jm, ida-vuelta, horarios", "img", ("facebook",)),
    "bancoestado": ("empresa", "banco, transacciones, cuentas... [rut]", "img", tuple()),
    "itchio": ("juego", "foro de juego indies, comprar-vender-donar", "img", ("",))
}

#AQUI INICIALIZAR NODO "MAIN" Y UN "RANKING" VACIO

# loop ejemplo
while 1:
    # AQUI MOSTRAR LOS DATOS DE LA PAGINA COMO USTED QUIERA
    # ... SOLO IMAGENES, REFERENCIAS CON OTRO COLOR, ETC

    comando = input()
    if comando[:2] == "mv": # comprobamos que sea un comando para moverse de nodo
        destino = comando[2:] # separamos el comando en la parte que nos interesa
        # AQUI COMPROBAR SI EL DESTINO ES ACCESIBLE DESDE DONDE ESTAMOS
        # SI LO ES ACTUALIZAR EL NODO Y SUMARLO AL "RANKING"
        # SI NO, MOSTRAR UN MENSAJE DE "ERROR" O NO HACER NADA, ETC
    
    if comando == "close": # comprobamos que el comando sea "close" para terminar
        break # "rompemos" el ciclo while

# MOSTRAMOS EL RANKING DE NODOS VISITADOS, RECORRIENDO LA ESTRUCTURA QUE SE HAYA DECIDIDO USAR