public class Main {
    public static void main(String[] args) {
        Coche coche = new Coche();
        coche.setSonido("BRRR");
        System.out.println(coche.getSonido());

        Moto moto = new Moto();
        moto.setSonido("BRRR");
        System.out.println(moto.getSonido());
    }
}

abstract class Vehiculo{
    int velocidadMaxima;
    String matricula;
    String sonido;

    public Vehiculo(){
        System.out.println("Estoy en el constructor de Vehículo");
    }

    abstract public String getSonido();
    abstract public void setSonido(String sonido);
}

// De esta manera se hace una clase que hereda.
// En este caso: la clase Coche hereda de la clase Vehículo.
// Una final class es una clase de la cuál ya no se puede heredar.
final class Coche extends Vehiculo{
    public String getSonido(){
        return "Soy un supersonido: " + this.sonido;
    }
    public void setSonido(String sonido){
        this.sonido = sonido;
    }
}

final class Moto extends Vehiculo{
    public String getSonido(){
        return "Soy un sonidillo de moto: " + this.sonido;
    }
    public void setSonido(String sonido){
        this.sonido = sonido;
    }
}