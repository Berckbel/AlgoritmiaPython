import random

def busqueda_lineal(lista, objetivo,iter_lin=0):
    match = False

    for elemento in lista:
        iter_lin+=1
        if elemento == objetivo:
            match = True
            break

    return (match,iter_lin)

if __name__ == '__main__':

    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_lineal(lista, 0, len(lista), objetivo)

    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')