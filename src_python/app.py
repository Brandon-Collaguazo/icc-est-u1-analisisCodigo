
# import benchmarking as Ben
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print("Funciona")
    metodos = MetodosOrdenamiento()
    benchmark = Benchmarking()
    tamanio = 10000
    arreglo = benchmark.buildArreglo(tamanio)
    metodos = {
        'Burbuja': metodos.sortByBubble,
        'Seleccion': metodos.sort_seleccion,
    }
    resultados = []
    for nombre, metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo)
        tuplaResultado = (tamanio, nombre, tiempo)
        resultados.append(tuplaResultado)
    for resultado in resultados:
        tamanio, nombre, tiempo = resultado
        print(f'Tamaño: {tamanio}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos')
