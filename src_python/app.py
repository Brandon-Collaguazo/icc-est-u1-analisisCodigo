
# import benchmarking as Ben
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Funciona")
    m_ordenamiento = MetodosOrdenamiento()
    benchmark = Benchmarking()
    #tamanio = 10000
    tamanios = [500, 1000, 2000]
    resultados = []
    for tam in tamanios:
        arreglo = benchmark.buildArreglo(tam)
        metodos = {
            'Burbuja': m_ordenamiento.sortByBubble,
            'Seleccion': m_ordenamiento.sort_seleccion,
    }
        
        for nombre, metodo in metodos.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo)
            tuplaResultado = (tam, nombre, tiempo)
            resultados.append(tuplaResultado)
            
        for resultado in resultados:
            tamanio, nombre, tiempo = resultado
            print(f'Tamaño: {tamanios}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos')
    
    tiempos_by_metodo = {
        "Burbuja" : [],
        "Seleccion" : [],
    }

    #Clasificar los tiempos segun el método
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)

    #Crear una gráfica
    plt.figure(figsize=(10, 6))

    #Graficar una linea de tiempo para cada de tiempo
    #Eje y sean los tiempos obtenidos
    #Eje x sea el tamaño del arreglo
    for nombre, tiempo in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempo, label=nombre, marker='o')
    
    #Agregar parametros
    plt.title("Análisis de Métodos de Ordenamiento\nBrandon Collaguazo 2025-05-07", fontsize=12)
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo")
    plt.grid()
    plt.show()
