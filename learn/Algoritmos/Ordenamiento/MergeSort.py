import random

def mergeSort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        mergeSort(izquierda)
        mergeSort(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
                
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamaño será la lista?"))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    print('-'*20)

    lista_ordenada = mergeSort(lista)
    print(lista_ordenada)