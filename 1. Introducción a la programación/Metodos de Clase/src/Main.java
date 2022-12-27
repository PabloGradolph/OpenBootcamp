public class Main {
    public static void main(String[] args) {
        Coche coche = new Coche();
        Moto moto = new Moto();
        EjecutarAcelerar(coche);
        EjecutarAcelerar(moto);
    }

    // La interfaz obliga al programador a incluir un método Acelerar.
    // En esta función pido como parámetro un objeto de una clase que implemente dicha interfaz.
    public static void EjecutarAcelerar(Vehiculo vehiculo){
        vehiculo.Acelerar(15);
    }
}

// La firma de la función declara si la función/método es:
// [Visibilidad] [nombre_método] (parámetros) (valor)
// Publica leerLibros(texto libro) Texto contenido.
interface Vehiculo{
    void Acelerar(int cuantaVelocidad);
    void Frenar(int cuantaVelocidad);
}
class Coche implements Vehiculo{
    public void Acelerar(int cuantaVelocidad){
        System.out.println("Coche() -> Acelerar");
    }
    public void Frenar(int cuantaVelocidad){
        System.out.println("Coche() -> Frenar");
    }
}

class Moto implements Vehiculo{
    public void Acelerar(int cuantaVelocidad){
        System.out.println("Moto() -> Acelerar");
    }
    public void Frenar(int cuantaVelocidad){
        System.out.println("Moto() -> Frenar");
    }
}