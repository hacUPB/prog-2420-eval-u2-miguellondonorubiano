
def main():
    def simulacion_desintegracion_orbital():
        
        altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en km): "))
        coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (por ejemplo, 0.01): "))
        altitud_minima_seguridad = float(input("Ingrese la altitud mínima de seguridad (en km): "))

        altitud_actual = altitud_inicial
        orbitas = 0
        altitud_perdida_total = 0
        
        while altitud_actual > altitud_minima_seguridad:

            altitud_perdida = coeficiente_arrastre * altitud_actual
            altitud_actual -= altitud_perdida
            altitud_perdida_total += altitud_perdida
            
            coeficiente_arrastre += 0.0001
            
            orbitas += 1

            if altitud_perdida < 0.01:
                print(f"\nEl satélite se ha estabilizado en una órbita baja.")
                print(f"Altitud final: {altitud_actual:.2f} km")
                print(f"Número de órbitas completadas: {orbitas}")
                return

        print(f"\nEl satélite ha reingresado a la atmósfera después de {orbitas} órbitas.")
        print(f"Altitud final: {altitud_actual:.2f} km (reingreso en la atmósfera).")

    simulacion_desintegracion_orbital()



if __name__ == "__main__":
    main()
