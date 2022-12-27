public class Main {
    public static void main(String[] args) {

        // Creamos un objeto coche de la clase Coche.
        Coche coche = new Coche(2, 90);
        System.out.printf("Puertas: %d\n", coche.numeroDePuertas);
        System.out.println(coche.velocidadActual);
        coche.acelerar();
        System.out.println(coche.velocidadActual);
        coche.decelerar();
        System.out.println(coche.velocidadActual);

        Coche coche2 = new Coche();
        Coche cohce3 = new Coche(5,150);
        System.out.println(coche2.velocidadActual);
    }
}

// Creamos la clase Coche.
class Coche {
    int numeroDePuertas;
    int velocidadMaxima;
    float velocidadActual;

    // Este es el constructor dónde se pueden inicializar valores.
    public Coche(int numeroDePuertas, int velocidadMaxima){
        this.numeroDePuertas = numeroDePuertas;
        this.velocidadMaxima = velocidadMaxima;
        System.out.println("Estoy en el constructor con parámetros");
    }

    // Otro constructor sin parámetros.
    public Coche() {
        numeroDePuertas = 4;
        velocidadMaxima = 120;
        System.out.println("Estoy en el constructor sin parámetros");
    }

    // Métodos
    public void acelerar(){
        velocidadActual += 15;
    }

    public void decelerar(){
        velocidadActual -= 10;
    }
}