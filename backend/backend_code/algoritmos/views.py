from django.shortcuts import render
from django.http import JsonResponse
#from request import Request

import json

from time import time
#from django.http import JSON

#from array.forms import FormularioPost

# Create your views here.

#Funciones auxiliares


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse



def quicksort_method(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort_method(arreglo, izquierda, indiceParticion)
        quicksort_method(arreglo, indiceParticion + 1, derecha)

def particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda]
    while True:
        # Mientras cada elemento desde la izquierda esté en orden (sea menor que el
        # pivote) continúa avanzando el índice
        while arreglo[izquierda] < pivote:
            izquierda += 1

        # Mientras cada elemento desde la derecha esté en orden (sea mayor que el
        # pivote) continúa disminuyendo el índice
        while arreglo[derecha] > pivote:
            derecha -= 1

        """
            Si la izquierda es mayor o igual que la derecha significa que no
            necesitamos hacer ningún intercambio
            de variables, pues los elementos ya están en orden (al menos en esta
            iteración)
        """
        if izquierda >= derecha:
            # Indicar "en dónde nos quedamos" para poder dividir el arreglo de nuevo
            # y ordenar los demás elementos
            return derecha
        else:
            # Nota: yo sé que el else no hace falta por el return de arriba, pero así el algoritmo es más claro
            """
                Si las variables quedaron "lejos" (es decir, la izquierda no superó ni
                alcanzó a la derecha)
                significa que se detuvieron porque encontraron un valor que no estaba
                en orden, así que lo intercambiamos
            """
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            """
                Ya intercambiamos, pero seguimos avanzando los índices
            """
            izquierda += 1
            derecha -= 1

def burbuja_method(arreglo):
    for i in range(1,len(arreglo)):
        for j in range(0,len(arreglo)-i):
            if(arreglo[j+1] < arreglo[j]):
                aux=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=aux

def burbuja2(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort_method(arreglo, izquierda, indiceParticion)
        quicksort_method(arreglo, indiceParticion + 1, derecha)

#Métodos
@csrf_exempt
def quicksort(request):
    data = json.loads(request.body)
    arreglo = data['array_inicial']
    start_time = time()
    quicksort_method(arreglo, 0, len(arreglo) - 1)
    elapsed_time = time() - start_time

    return JsonResponse(arreglo, safe = False)

@csrf_exempt
def burbuja(request):
     
    data = json.loads(request.body)
    arreglo = data['array_inicial']
    start_time = time()
    burbuja2(arreglo, 0, len(arreglo) - 1)
    elapsed_time = time() - start_time

    pythonDictionary = {}
    pythonDictionary['Burbuja'] = {'array_final':arreglo, 'tiempo':elapsed_time}
    pythonDictionary['Quicksort'] = {'array_final':arreglo, 'tiempo':elapsed_time}

    dictionaryToJson = json.dumps(pythonDictionary)
    return JsonResponse(pythonDictionary, safe = False)

@csrf_exempt
def all_methods(request):

    data = json.loads(request.body)
    arreglo = data['array_inicial']

    #Método burbuja
    arreglo_burbuja = arreglo[:]
    start_time_burbuja = time()
    burbuja_method(arreglo_burbuja)
    elapsed_time_burbuja = time() - start_time_burbuja

    #Método quicksort
    arreglo_quicksort = arreglo[:]
    start_time_quicksort = time()
    quicksort_method(arreglo_quicksort, 0, len(arreglo) - 1)
    elapsed_time_quicksort = time() - start_time_quicksort

    #Creación del JSON de salida
    lista = []
    lista.append({'metodo':"Burbuja", 'array_final':arreglo_burbuja, 'tiempo':elapsed_time_burbuja})
    lista.append({'metodo':"Quicksort", 'array_final':arreglo_quicksort, 'tiempo':elapsed_time_quicksort})

    return JsonResponse(lista, safe = False)

def crear_post(request):
    if request.method == "POST":
        request.mensaje