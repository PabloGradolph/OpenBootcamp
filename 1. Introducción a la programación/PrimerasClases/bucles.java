public class bucles {
    
    public static void main(String[] args){
        int contador = 10;

        // Bucle while
        while (contador > 0){
            System.out.println(contador);
            contador = contador - 1;
        }

        // Bucle do while
        // Hay una sutíl diferencia pero se suele usar más el while a secas.
        contador = 10;
        do {
            System.out.println(contador);
            contador = contador - 1;
        } while (contador > 0);

        // Bucle for 
        // for (INICIALIZACIÓN; COMPARACIÓN; ACCIÓN)
        // for (CONTADOR MAYOR QUE 0; CONTADOR IGUAL A CONTADOR MENOS 1; CONTADOR IGUAL A CONTADOR MÁS UNO){}
        for (int contadores = 1; contadores <= 10; contadores = contadores + 1){
            System.out.println(contadores);
            // La ACCIÓN se ejecuta después de esta línea
        }

        // Recorriendo un array con un bucle for
        int valores[] = {10, 20, 30, 40, 50};

        for (int i = 0; i < valores.length; i++) {
            System.out.println(valores[i]);
        }

        // CASOS
        var estacion = "VERANO";

        // Se escribe con dos puntos cada caso.
        // Cuando se ejecuta un case, se ejecuta todo lo que hay debajo hasta que se encuentre un break.
        switch(estacion){
            case "VERANO":
                System.out.println("es verano");
                break;
            case "INVIERNO":
                System.out.println("es invierno");
                break;
            default:
                System.out.println("Estoy en default.");
        }
        
        // Visualizamos un caso donde podría ser útil.
        var hoy_es = "MARTES";

        switch(hoy_es){
            case "LUNES":
            case "MARTES":
            case "MIERCOLES":
            case "JUEVES":
            case "VIERNES":
                System.out.println("HOY ES LABORABLE");
                break;
            default:
                System.out.println("HOY NO ES LABORALBE");
        }
    }
}
