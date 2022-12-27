public class EjercicioTema3 {
    
    public static void main(String[] args) {
        // Primera parte
        int resultado;
        resultado = SumaNumeros(10, 20, 30);
        System.out.println(resultado);

        // Segunda parte:
        Coche miCoche = new Coche();
        miCoche.IncrementarPuerta();
        System.out.println(miCoche.puertas);
    }

    public static int SumaNumeros(int a, int b, int c) {
        return a + b + c;
    }
}

class Coche {
    public int puertas = 5;

    public void IncrementarPuerta() {
        this.puertas++;
    }
}
