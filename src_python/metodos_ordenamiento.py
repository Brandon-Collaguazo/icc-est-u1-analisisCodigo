
class MetodosOrdenamiento:
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    #aux = arreglo[i]
                    #arreglo[i] = arreglo[j]
                    #arreglo[j] = aux
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo
    
    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(array)
        for i in range(n):
            indexMenor = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[indexMenor]:
                    indexMenor = j
            # aux = arreglo[indexMenor]
            # arreglo[indexMenor] = arreglo[i]
            # arreglo[i] = aux
            arreglo[i] =  arreglo[indexMenor] = arreglo[indexMenor] = arreglo[i]
        return arreglo
