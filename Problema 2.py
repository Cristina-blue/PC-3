def get_NOTAS():
    while True:
        try:
        
            NOTAS_input = input("Ingrese las calificaciones separadas por comas: ")
            
            NOTAS_list = NOTAS_input.split(",") 
        
            NOTAS = [int(NOTAS.strip()) for NOTAS in NOTAS_list]
            
            return NOTAS
        
        except ValueError:

            print("Error: Revise las calificaciones colocadas, hay error de tipeo.")

NOTAS = get_NOTAS()
print(f"Las calificaciones ingresadas son: {NOTAS}")
