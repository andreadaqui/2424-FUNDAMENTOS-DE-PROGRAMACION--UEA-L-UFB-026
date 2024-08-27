#Creación de un arreglo bidimencional de 3x3
#utilizando la funcion quicksort
#Establecemos las condiciones con las que quicksort trabarajá
#Esta función recibe una lista con elementos desordenados
def quicksort(lista):       #Revisemos el caso base
    if len (lista) <=1:     #si el numero de elemento de la lista es menor o igual a 1
        return lista        #el número regresa a las lista
    pivote = lista.pop()    #creamos un pivote; el cual divide a la lista, escogemos un pivote mediante la funcion pop
    lista1 = []             #creamos 2 sublistas vacias donde se
    lista2 = []             #almacenan los elementos
    for e in lista:         #recorremos la lista para ver que elementos son menores y mayores
        if e <= pivote:
            lista1.append(e)
        else:
            lista2.append(e)
#Una vez ordenados los elemento llamamos a nuestra función de forma recursiva
#para asegurarnos que en ambos lados estan los numeros ordenado
    lista1 = quicksort(lista1)
    lista2 = quicksort(lista2)
#regresamos la lista1 + pivote + lista2 asi concatenamos la lista

    return lista1 + [pivote] + lista2
#Creamos 3 listas con 3 elementos
lista_a = [17, 30, 25]
lista_b = [48, 60, 30]
lista_c = [0, 19, 100]
#concatenamos las 3 listas en una sola matriz
lista = [lista_a, lista_b, lista_c]
#imprimimos la lista original en desorden
print(lista)
#Finalmente imprimimos la lista ordenada
print(quicksort(lista))



