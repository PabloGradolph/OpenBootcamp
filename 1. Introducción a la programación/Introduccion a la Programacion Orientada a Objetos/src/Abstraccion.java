public class Abstraccion {
    public static void main(String[] args){
        // DEFINICIÓN CLASE ABSTRACTA: Es una clase normal y corriente en la cuál nos dan una serie de métodos ya
        // programados y nos dicen que tenemos que programar otra serie de métodos nosotros.

        // EJEMPLO:
        /* Clase abstracta vehículo
         *       Privada tipo;
         *       Privada sonido;
         *
         *       Función settertipo(valor)
         *           Esta_clase.tipo = valor
         *       Función gettertipo()
         *           Devuelve Esta_clase.tipo
         *       Función abstracta settersonido(sonido)
         *           Esta_clase.sonido = sonido
         *       Función abstracta gettersonido()
         *           Devuelve Esta_clase.sonido
         *
         * Si queremos usar esta clase tenemos que derivarla (Herencia) y en mi nueva clase tengo que implementar sí o sí
         * las funciones abstractas.
         * */
    }
}

abstract class Transporte{
    private String sonido;
    private String tipo;
    private int velocidadMaxima;

    // Métodos abstractos
    abstract public void setSonido(String sonido);
    abstract public String getSonido();

    // Setters
    public void setVelocidadMaxima(int velocidadMaxima){
        this.velocidadMaxima = velocidadMaxima;
    }
    public void setTipo(String tipo){
        this.tipo = tipo;
    }

    // Getters
    public int getVelocidadMaxima(){
        return this.velocidadMaxima;
    }
    public String getTipo(){
        return this.tipo;
    }
}
