public class Interfaces {
    public static void main(String[] args) {

    }
}

// Una interfaz es similar a una clase abstracta.
interface Metodos{
    void Acelerar(int cuantaVelocidad);
    void Frenar(int cuantaVelocidad);
}

// Cuando implemento en la clase avión todas los métodos de la interfaz, se considera que la interfaz está correctamente
// implementada.
class Avion implements Metodos{
    public void Acelerar(int cuantaVelocidad){

    }
    public void Frenar(int cuantaVelocidad){

    }
}
