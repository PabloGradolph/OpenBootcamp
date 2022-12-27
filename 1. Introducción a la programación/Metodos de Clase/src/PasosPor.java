public class PasosPor {
    public static void main(String[] args) {
        // Paso por valor:
        // Al llamar a la función suma se crea una copia de los valores dentro de dicha función.
        // Las variables que pasamos no se modifican fuera de ésta.
        // Es un problemón al hablar de memoria RAM.
        int valA = 5;
        int valB = 10;

        suma(valA, valB);
        System.out.println(valA);
        System.out.println(valB);

        // Paso por referencia:
        // Manipulamos directamente las variables originales modificando su valor y optimizando la memoria.
        // Se hace con punteros. Aunque en java esto no esté muy claro como en otros lenguajes.
        Car coche = new Car(); // Aquí aunque no lo veamos se crea un puntero.
        cocheChanger(coche);
        cocheChanger(coche);
        // Se altera directamente la velocidad. Manipulamos su memoria haciendo el paso por referencia (de memoria).
        System.out.println(coche.velocidad);

        // Llamamos a la función recursiva factorial
        factorial(5);
    }

    public static int suma(int a, int b){
        // Dentro de esta función las variables a y b son copias de las variables valA y valB.
        return a + b;
    }

    public static void cocheChanger(Car coche){
        coche.velocidad += 50;
    }

    // Función factorial de forma recursiva. Recursiva --> Función que se llama así misma.
    public static int factorial(int numero){
        int resultado;
        if (numero == 1){
            return 1;
        }

        resultado = factorial(numero - 1) * numero;
        return resultado;
    }
}

class Car{
    int velocidad = 0;
}
