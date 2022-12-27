public class PrivacidadEncapsulacion {
    public static void main(String[] args){

        // Cuando podemos acceder a las propiedades de una clase desde fuera, esta es pública.
        // Una propiedad privada sólo se puede utilizar dentro de la propia clase.
        // Existe también las variables protegidas. Ya las veremos.

        Vehiculo vehiculo = new Vehiculo();
        vehiculo.setTipo("Coche");
        String tipo = vehiculo.getTipo();
        vehiculo.setVelocidadMaxima(120);
        System.out.println(tipo + " " + vehiculo.getVelocidadMaxima());

        Vehiculo moto = new Vehiculo();
        moto.setTipo("Scotter");
        moto.setVelocidadMaxima(90);
        System.out.println(moto.getTipo() + " " + moto.getVelocidadMaxima());
    }
}

class Vehiculo{
    private String tipo;
    private int velocidadMaxima;
    private boolean estado;

    // Para acceder a propiedades privadas usamos funciones conocidas como getters y setters.
    // A este proceso se le conoce como encapsulación.

    // Setters
    public void setVelocidadMaxima(int velocidadMaxima){
        this.velocidadMaxima = velocidadMaxima;
    }
    public void setTipo(String tipo){
        this.tipo = tipo;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }

    // Getters
    public int getVelocidadMaxima(){
        return this.velocidadMaxima;
    }
    public String getTipo(){
        return this.tipo;
    }
    // Getter para un boolean
    public boolean isEstado() {
        return this.estado;
    }
}