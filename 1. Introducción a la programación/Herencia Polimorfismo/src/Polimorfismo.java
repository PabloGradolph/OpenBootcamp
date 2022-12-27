public class Polimorfismo {

    public static void main(String[] args) {
        Carro carro = new Carro();
        carro.diHola();
        // Dependiendo del tipo de datos llama a un método (polimórfico) o a otro.
        System.out.println(carro.sumaNumeros(1,2));
        System.out.println(carro.sumaNumeros((float)1,(float)2));
        carro.sumaNumeros(12.1,1.3);
    }
}

// Polimorfismo: Al tener el mismo método en la clase padre como en la clase hijo, ejecutaré el método de la clase hija.
// También puede haber métodos polimorficos dentro de la misma clase
class Transporte{
    public void diHola(){
        System.out.println("Hola!!");
    }
}

class Carro extends Transporte{
    public void diHola(){
        System.out.println("Hola soy un carro");
    }

    public int sumaNumeros(int a, int b){
        return a + b;
    }

    public float sumaNumeros(float a, float b){
        return a + b * (float)9.0;
    }

    public void sumaNumeros(double a, double b){
        System.out.println("El resultado es: " + (a + b));
    }
}