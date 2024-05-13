def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):
    if indice >= len(mochila):
        return False, objetos_sacados
    
    if mochila[indice] == "sable de luz":
        return True, objetos_sacados
    
    sacado_siguiente_objeto = usar_la_fuerza(mochila, indice + 1, objetos_sacados + 1)
    return sacado_siguiente_objeto

mochila = ["comida", "botiquín", "sable de luz", "ropa"]

encontro_sable, objetos_necesarios = usar_la_fuerza(mochila)

if encontro_sable:
    print("El Jedi encontró un sable de luz después de sacar", objetos_necesarios, "objetos de la mochila.")
else:
    print("El Jedi no encontró un sable de luz en la mochila.")

print (mochila)