import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izqueirda = lista[:medio]
        derecha = lista[medio:]
        print(izqueirda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izqueirda)
        ordenamiento_por_mezcla(derecha)

        # iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # iterador para la lista principal
        k = 0

        while i  < len(izqueirda) and j < len(derecha):
            if izqueirda[i] < derecha[j]:
                lista[k] = izqueirda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j +=1

            k += 1
        
        while i < len(izqueirda):
            lista[k] = izqueirda[i]
            i+=1
            k+=1
        
        while j< len(derecha):
            lista[k] = derecha[j]
            j+=1
            k+=1
        
        print(f'izquierda {izqueirda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista

if __name__ == '__main__':

    tamano_de_lista = int(input('De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)