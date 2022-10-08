from auxFunctions import *


def ident(nodo): return car(nodo)


def estado(nodo): return cadr(nodo)


def id_padre(nodo): return caddr(nodo)


def operador(nodo): return car(cdddr(nodo))


def info(nodo): return cdr(cdddr(nodo))


def operadores(problema): return car(problema)


def funcion_info_adicional(problema): return cadr(problema)


def estado_inicial(problema): return caddr(problema)


def funcion_objetivo(problema): return car(cdddr(problema))


def info_inicial(problema): return car(cdr(cdddr(problema)))


def construye_nodo(ident, estado, id_padre, op, info):
    return [ident, estado, id_padre, op] + info


def busqueda(problema, estrategia, arbol):
    if (not candidatos(arbol)):
        return ['no_hay_solucion']
    else:
        nodo = selecciona_nodo(arbol)
        nuevo_arbol = elimina_seleccion(arbol)
        if solucion(problema, nodo):
            return camino(arbol, nodo)
        else:
            return busqueda(problema, estrategia,
                            expande_arbol(problema,
                                          estrategia,
                                          nuevo_arbol,
                                          nodo))


def hacer_busqueda(problema, estrategia):
    return busqueda(problema,
                    estrategia,
                    arbol_inicial(estado_inicial(problema),
                                  info_inicial(problema)))


def solucion(problema, nodo):
    ff = funcion_objetivo(problema)
    return ff(estado(nodo))


def rl_funcion_objetivo(estado):
    return estado == [1, 2, 3, 4]


def nodos_a_expandir(arbol):
    return car(arbol)


def nodos_expandidos(arbol):
    return cadr(arbol)


def selecciona_nodo(arbol):
    return car(nodos_a_expandir(arbol))


def candidatos(arbol):
    return bool(nodos_a_expandir(arbol))


def camino(arbol, nodo):
    if not id_padre(nodo):
        return []
    lp = camino(arbol, nodo_arbol(id_padre(nodo), arbol))
    return lp + [operador(nodo)]


def nodo_arbol(id_nodo, arbol):
    check_nodo = lambda nodo: ident(nodo) == id_nodo
    a_expandir = member_if(check_nodo, nodos_a_expandir(arbol))
    if bool(a_expandir):
        return car(a_expandir)
    return find_if(check_nodo, nodos_expandidos(arbol))


def expande_arbol(problema, estrategia, arbol, nodo):
    nuevos_nodos_a_expandir = expande_nodo(nodo,
                                           operadores(problema),
                                           funcion_info_adicional(problema))
    return construye_arbol(arbol,
                           estrategia,
                           nodo,
                           nuevos_nodos_a_expandir)


def construye_arbol(arbol, estrategia, nodo_expandido, nuevos_nodos_a_expandir):
    elm = estrategia(car(arbol), nuevos_nodos_a_expandir)
    return cons(elm, [cons(nodo_expandido, cadr(arbol))])


def elimina_seleccion(arbol):
    return cons(cdr(nodos_a_expandir(arbol)), cdr(arbol))


def arbol_inicial(estado, info):
    infres = info(estado)
    nodo = construye_nodo(gensym(), estado, [], [], [])
    tmp = [nodo + infres]
    return [tmp]


def expande_nodo(nodo, operadores, funcion):
    def elimina_estados_vacios(lista_nodos):
        return remove_if(lambda nodo: estado(nodo) == 'vacio',
                         lista_nodos)

    st = estado(nodo)
    id_nodo = ident(nodo)
    info_nodo = info(nodo)
    aux = []
    for op in operadores:
        nuevo_simbolo = gensym()
        ff = cadr(op)
        ffapp = ff(st, info_nodo)
        aux.append(construye_nodo(nuevo_simbolo,
                                  ffapp,
                                  id_nodo,
                                  car(op),
                                  funcion([st, info_nodo],
                                          ffapp,
                                          car(op))))
    return elimina_estados_vacios(aux)
