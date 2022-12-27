public class EjercicioTema4 {
    
    public static void main(String[] args){

        // Parte del if:
        int numerolf = -5;

        System.out.println("IF, ElSE IF, ELSE:");

        if (numerolf == 0){
            System.out.println("numerolf = 0.");
        }else if (numerolf < 0){
            System.out.println("numerolf < 0.");
        }else {
            System.out.println("numerolf > 0.");
        }

        // Parte del while:
        System.out.println("WHILE:");

        int numeroWhile = 0;

        while (numeroWhile < 3){
            System.out.println(numeroWhile);
            numeroWhile ++;
        }
        
        // Parte del do while:
        System.out.println("DO WHILE:");

        // numeroWhile = 3 ahora. Se debe ejecutar una vez el do-while de todas formas. Aunque numeroWhile ya tenga el valor de 3.

        do{
            System.out.println(numeroWhile);
            numeroWhile ++;
        } while (numeroWhile < 3);

        // Parte del for:
        System.out.println("FOR:");

        for (int numeroFor = 0; numeroFor <= 3; numeroFor++){
            System.out.println(numeroFor); 
        }
        
        // Parte del switch:
        System.out.println("SWITCH:");

        var estacion = "VERANO";
        
        switch(estacion){
            case "INVIERNO":
                System.out.println("Es invierno.");
                break;
            case "PRIMAVERA":
                System.out.println("Es primavera.");
                break;
            case "VERANO":
                System.out.println("Es verano.");
                break;
            case "OTOÑO":
                System.out.println("Es otoño.");
                break;
            default:
                System.out.println("El valor de la variable 'estacion' no es una estación.");

        }
    }
}
