import java.util.Random;

public class Benchmarking {

    private MetodosOrdenamiento mO;
    private Random rd;

    public Benchmarking() {
        long incioMillis = System.currentTimeMillis();
        long inicioNano = System.nanoTime();
        System.out.println(incioMillis);
        System.out.println(inicioNano);
        mO = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(100000);
        Runnable tarea = () -> mO.burbujaTradicional(arreglo);
        double tiempoNano = medirConNatoTime(tarea);
        double tiempoMilis = medirConCurrentTime(tarea);
        System.out.println("Tiempo con nano time: " + tiempoNano);
        System.out.println("Tiempo con currentTimeMillis: " + tiempoMilis);
    }

    private int[] generarArregloAleatorio(int tamanio) {
        //valores entre 0 y 99,999
        int [] arreglo = new int[tamanio];
        rd = new Random();
        for(int i = 0; i < tamanio; i++) {
            arreglo[i] = rd.nextInt(100_000);
        }
        return new int[] {};
    }

    public double medirConNatoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }

    public double medirConCurrentTime(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1000.0;        
    }
}
