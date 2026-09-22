import java.util.ArrayList;

// Interfaz para calcular el impacto de carbono
interface ImpactoEcologico {
    double obtenerImpactoEcologico();
}

// Clase Edificio
class Edificio implements ImpactoEcologico {
    private String nombre;
    private double consumoElectricoAnual;

    public Edificio(String nombre, double consumoElectricoAnual) {
        this.nombre = nombre;
        this.consumoElectricoAnual = consumoElectricoAnual;
    }
    
    // Cálculo simplificado: kWh multiplicados por factor de emisión de red
    @Override
    public double obtenerImpactoEcologico() {
        return consumoElectricoAnual * 0.5; // Kg de CO2
    }

    @Override
    public String toString() {
        return "Edificio: " + nombre;
    }
}

// Clase Auto
class Auto implements ImpactoEcologico {
    private String modelo;
    private double litrosGasolinaAnual;

    public Auto(String modelo, double litrosGasolinaAnual) {
        this.modelo = modelo;
        this.litrosGasolinaAnual = litrosGasolinaAnual;
    }

    // Cálculo: litros consumidos por factor de emisión de gasolina
    @Override
    public double obtenerImpactoEcologico() {
        return litrosGasolinaAnual * 2.3; // Kg de CO2
    }

    @Override
    public String toString() {
        return "Automóvil: " + modelo;
    }
}

// Clase Bicicleta
class Bicicleta implements ImpactoEcologico {
    private String marca;

    public Bicicleta(String marca) {
        this.marca = marca;
    }

    // La bicicleta tiene impacto cero en su uso
    @Override
    public double obtenerImpactoEcologico() {
        return 0.0;
    }

    @Override
    public String toString() {
        return "Bicicleta ecológica: " + marca;
    }
}

// Aplicación principal
public class EvaluadorEcologico {
    public static void main(String[] args) {
        // Colocar referencias en ArrayList utilizando polimorfismo
        ArrayList<ImpactoEcologico> listaEcologica = new ArrayList<ImpactoEcologico>();

        listaEcologica.add(new Edificio("Torre Central", 15000));
        listaEcologica.add(new Auto("Toyota Corolla", 1200));
        listaEcologica.add(new Bicicleta("Trek Mountain"));

        System.out.println("--- Reporte de Impacto Ecológico (Carbono) ---");
        
        // Procesamiento polimórfico iterando a través del objeto ArrayList
        for (ImpactoEcologico objetoActual : listaEcologica) {
            System.out.printf("%s %nImpacto de carbono: %.2f kg CO2%n%n", 
                objetoActual.toString(), 
                objetoActual.obtenerImpactoEcologico());
        }
    }
}