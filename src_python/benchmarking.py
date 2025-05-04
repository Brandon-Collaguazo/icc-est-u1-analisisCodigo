
import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    def __init__(self):
        print('Bench inicializado')
    
    def ejemplo(self):
        self.mOrdenamiento = MetodosOrdenamiento()
        arreglo = self.buildArreglo(10000)
        # tarea = () ->
        tarea = lambda: self.mOrdenamiento.sortByBubble(arreglo)
        tareaBM = lambda: self.mOrdenamiento.sort_seleccion(arreglo)
        tiempoMillis = self.contar_con_curren_time_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)

        print(f'Tiempo {tiempoMillis} ')
        print(f'Tiempo {tiempoNano}')

    def buildArreglo(self, tamanio):
        array = []
        for i in range(tamanio):
            numero = random.randint(0, 10000)
            array.append(numero)
        return array
    
    def contar_con_curren_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio
    
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0
    
    def medir_tiempo(self, func, array):
        inicio = time.perf_counter()
        func(array)
        fin = time.perf_counter()
        return fin - inicio
