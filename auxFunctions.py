import sys
import random

sys.setrecursionlimit(1000000)


# No es lo mismo que el gensym de Lisp, pero es más que
# suficiente para lo que necesitamos
def gensym():
    return 'symb' + str(int(10000000 * random.random())).rjust(7, '0')


def car(lst): return ([] if not lst else lst[0])


def cdr(lst): return ([] if not lst else lst[1:])


def caar(lst): return car(car(lst))


def cadr(lst): return car(cdr(lst))     # 2º elemento


def cdar(lst): return cdr(car(lst))


def cddr(lst): return cdr(cdr(lst))


def caddr(lst): return car(cdr(cdr(lst)))    # 3º elemento


def cdddr(lst): return cdr(cdr(cdr(lst)))


def caadr(lst): return car(car(cdr(lst)))


def cadadr(lst): return car(cdr(car(cdr(lst))))


def cadddr(lst): return car(cdr(cdr(cdr(lst))))     # 4º elemento


# Este cons no hace lo mismo que el cons de Lisp, pero ya nos va bien

def cons(elem, lst):
    tmp = lst.copy()
    tmp.insert(0, elem)
    return tmp


def member_if(prd, lst):
    ll = lst.copy()
    leng = len(lst)
    while leng > 0:
        elem = ll[0]
        if prd(elem):
            return ll
        ll.pop(0)
        leng -= 1
    return []


def find_if(prd, lst):
    for elem in lst:
        if prd(elem):
            return elem
    return []


def remove_if(prd, lst):
    results = []
    for elem in lst:
        if not prd(elem):
            results.append(elem)
    return results


def mapcar(f, lst):
    return list(map(f, lst))
