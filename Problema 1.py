def get_fraction():
    while True:
        try:
            fraction = input("Ingrese una fracción en formato X/Y:")
            
            x, y = fraction.split("/")    
           
            if "." in x or "." in y:
                raise ValueError("Solo se permiten números enteros.")
           
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser 0.")

            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
            
            porcentaje = (x / y) * 100
            if porcentaje <= 1:
                return "E"
            elif porcentaje >= 99:
                return "F"
            else:
                return f"{round(porcentaje)}%"
        
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser 0.")


print(get_fraction())
