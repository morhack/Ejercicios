titulo = "Hola, Bienvenido a la Tienda Oficial Del Futbol Club Barcelona"

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

articulo = input("En que estaria interesado\n"
                 "A - Camiseta\n"
                 "B - Equipacion Oficial\n"
                 "C - Merchandising\n")
if articulo == "A":
    talla = input("¿Que talla de camiseta quiere?: \n"
          "A - S\n"
          "B - M\n"
          "C - L\n")
    if talla == "A":
        print("Tu talla de camiseta es la S")
        nombre = input("¿Quieres Poner un nombre a su camiseta?: (SI/NO)\n"
                       "SI - Pon un nombre\n"
                       "NO - No pon nombre\n")
        numero = input("¿Quieres poner un numero a su camiseta?: (SI/NO)\n"
                       "SI - Pon un numero\n"
                       "No - No pon numero\n")
        if nombre == "SI" and numero == "SI":
            nombre = input("Introduce tu nombre: \n")
            numero = input("Introduce tu numero: \n")
            print("Tu camiseta es de la talla S con el nombre {} y el numero {}".format(nombre, numero))
        elif nombre == "SI" and numero == "NO":
            nombre = input("Introduce tu nombre: \n")
            print("Tu camiseta de la talla S con el nombre {}".format(nombre))
        elif nombre == "NO" and numero == "SI":
            numero = input("Introduce tu numero: \n")
            print("Tu camiseta de la talla S con el numero {}".format(numero))
        elif nombre == "NO" and numero == "NO":
            print("Tu camiseta de la talla S no sera serigrafiada")
    if talla == "B":
        print("Tu talla de camiseta es la M")
        nombre = input("¿Quieres Poner un nombre a su camiseta?: (SI/NO)\n"
                       "SI - Pon un nombre\n"
                       "NO - No pon nombre\n")
        numero = input("¿Quieres poner un numero a su camiseta?: (SI/NO)\n"
                       "SI - Pon un numero\n"
                       "No - No pon numero\n")
        if nombre == "SI" and numero == "SI":
            nombre = input("Introduce tu nombre: \n")
            numero = input("Introduce tu numero: \n")
            print("Tu camiseta es de la talla M con el nombre {} y el numero {}".format(nombre, numero))
        elif nombre == "SI" and numero == "NO":
            nombre = input("Introduce tu nombre: \n")
            print("Tu camiseta de la talla M con el nombre {}".format(nombre))
        elif nombre == "NO" and numero == "SI":
            numero = input("Introduce tu numero: \n")
            print("Tu camiseta de la talla M con el numero {}".format(numero))
        elif nombre == "NO" and numero == "NO":
            print("Tu camiseta de la talla M no sera serigrafiada")
    if talla == "C":
        print("Tu talla de camiseta es la L")
        nombre = input("¿Quieres Poner un nombre a su camiseta?: (SI/NO)\n"
                       "SI - Pon un nombre\n"
                       "NO - No pon nombre\n")
        numero = input("¿Quieres poner un numero a su camiseta?: (SI/NO)\n"
                       "SI - Pon un numero\n"
                       "No - No pon numero\n")
        if nombre == "SI" and numero == "SI":
            nombre = input("Introduce tu nombre: \n")
            numero = input("Introduce tu numero: \n")
            print("Tu camiseta es de la talla L con el nombre {} y el numero {}".format(nombre, numero))
        elif nombre == "SI" and numero == "NO":
            nombre = input("Introduce tu nombre: \n")
            print("Tu camiseta de la talla L con el nombre {}".format(nombre))
        elif nombre == "NO" and numero == "SI":
            numero = input("Introduce tu numero: \n")
            print("Tu camiseta de la talla L con el numero {}".format(numero))
        elif nombre == "NO" and numero == "NO":
            print("Tu camiseta de la talla L no sera serigrafiada")
elif articulo == "B":
    talla = input("¿Que talla de equipacion quiere?: \n"
                  "A - S\n"
                  "B - M\n"
                  "C - L\n")
    if talla == "A":
        print("Tu talla de equipacion es la S")
        equipacion = input("¿Que equipacion quieres?: \n"
                           "A - Primera Equipacion\n"
                           "B - Segunda Equipacion\n")
        if equipacion == "A":
            print("Tu equipacion es la Primera")
            equipacion = input("¿Quieres poner un nombre a su equipacion?: (SI/NO)\n"
                                 "SI - Pon un nombre\n"
                                 "NO - No pon nombre\n")
            if equipacion == "SI":
                nombre = input("Introduce tu nombre: \n")
                print("Tu equipacion es la Primera con el nombre {}".format(nombre))
            elif equipacion == "NO":
                print("Tu equipacion es la Primera Sin Nombre")
        elif equipacion == "B":
            print("Tu equipacion es la Segunda")
            equipacion = input("¿Quieres poner un nombre a su equipacion?: (SI/NO)\n"
                               "SI - Pon un nombre\n"
                               "NO - No pon nombre\n")
            if equipacion == "SI":
                nombre = input("Introduce tu nombre: \n")
                print("Tu equipacion es la Segunda con el nombre {}".format(nombre))
            elif equipacion == "NO":
                print("Tu equipacion es la Segunda Sin Nombre")
    if talla == "B":
        print("Tu talla de equipacion es la M")
        equipacion = input("¿Que equipacion quieres?: \n"
                           "A - Primera Equipacion\n"
                           "B - Segunda Equipacion\n")
        if equipacion == "A":
            print("Tu equipacion es la Primera")
            equipacion = input("¿Quieres poner un nombre a su equipacion?: (SI/NO)\n"
                                 "SI - Pon un nombre\n"
                                 "NO - No pon nombre\n")
            if equipacion == "SI":
                nombre = input("Introduce tu nombre: \n")
                print("Tu equipacion es la Primera con el nombre {}".format(nombre))
            elif equipacion == "NO":
                print("Tu equipacion es la Primera Sin Nombre")
        elif equipacion == "B":
            print("Tu equipacion es la Segunda")
            equipacion = input("¿Quieres poner un nombre a su equipacion?: (SI/NO)\n"
                               "SI - Pon un nombre\n"
                               "NO - No pon nombre\n")
            if equipacion == "SI":
                nombre = input("Introduce tu nombre: \n")
                print("Tu equipacion es la Segunda con el nombre {}".format(nombre))
            elif equipacion == "NO":
                print("Tu equipacion es la Segunda Sin Nombre")
    if talla == "C":
        print("Tu talla de equipacion es la L")
        equipacion = input("¿Que equipacion quieres?: \n"
                           "A - Primera Equipacion\n"
                           "B - Segunda Equipacion\n")
        if equipacion == "A":
            print("Tu equipacion es la Primera")
            equipacion = input("¿Quieres poner un nombre a su equipacion?: (SI/NO)\n"
                                 "SI - Pon un nombre\n"
                                 "NO - No pon nombre\n")
            if equipacion == "SI":
                nombre = input("Introduce tu nombre: \n")
                print("Tu equipacion es la Primera con el nombre {}".format(nombre))
            elif equipacion == "NO":
                print("Tu equipacion es la Primera Sin Nombre")
        elif equipacion == "B":
            print("Tu equipacion es la Segunda")
            equipacion = input("¿Quieres poner un nombre a su equipacion?: (SI/NO)\n"
                               "SI - Pon un nombre\n"
                               "NO - No pon nombre\n")
            if equipacion == "SI":
                nombre = input("Introduce tu nombre: \n")
                print("Tu equipacion es la Segunda con el nombre {}".format(nombre))
            elif equipacion == "NO":
                print("Tu equipacion es la Segunda Sin Nombre")
elif articulo == "C":
    articulo = input("¿En que tipo de articulo de merchandising le interesa?\n"
                     "A - Bufanda\n"
                     "B - Banderin"
                     "C - Merchandising Variado")
    if articulo == "A":
        print("El articulo de merchandising que vas adquirir es una bufanda")
    if articulo == "B":
        print("El articulo de merchandising que vas adquirir es un banderin")
    if articulo == "C":
        print("El articulo de merchandising que vas adquirir es un merchandising variado")

else:
    print("No has seleccionado ninguna opcion correcta")

print("Gracias por su visita, espero que haya sido de su agrado")