valor = input("¿Ver el historial [1] o poner un precio[pulsa una tecla]? ") # PREGUTA AL USUARIO QUE QUIERE HACER
Yago = [10,24,34] # HISTORIAL DE USUARIOS
Maider = [89,6,78] # HISTORIAL DE USUARIOS
historico = ["Yago",Yago, "Maider",Maider] # VALORES HISTORICOS
iva = [0, 0.04, 0.1, 0.21] # TIPOS DE IVA

if valor == "1": # MUESTRA EL HISTORIAL 
    for j in historico:
        if isinstance(j,str):
            print(f"Historial de {j} :")
        else:
            for i in j:
                print(f"Precio sin IVA : {i}€")
                print(f"IVA : {(i*0.21):.2f}€")
                print(f"Precio con IVA : {i + (i*0.21):.2f}€")
else:

    # PREGUNTA QUE PRECIO QUIERE PONER CON IVA Y EL TIPO DE IVA QUE QUIERE USAR.
    while valor != "1":

        precio = int(input("Pon un precio : "))
        tipo_de_iva = input("¿Cual es el iva : 0, 4, 10 o 21? ")

        if tipo_de_iva == "0":
            precio_iva = precio * iva[0]
            total_mas_iva = precio + precio_iva
            print(f"Precio sin IVA : {precio}")
            print(f"IVA : {precio_iva}€")
            print(f"Precio con IVA : {total_mas_iva}€")
            valor = input("¿Quieres salir[1], para meter mas precios pulsa una tecla?")

        if tipo_de_iva == "4":
            precio_iva = precio * iva[1]
            total_mas_iva = precio + precio_iva
            print(f"Precio sin IVA : {precio}")
            print(f"IVA : {precio_iva}€")
            print(f"Precio con IVA : {total_mas_iva}€")
            valor = input("¿Quieres salir[1], para meter mas precios pulsa una tecla?")

        if tipo_de_iva == "10":
            precio_iva = precio * iva[2]
            total_mas_iva = precio + precio_iva
            print(f"Precio sin IVA : {precio}")
            print(f"IVA : {precio_iva}€")
            print(f"Precio con IVA : {total_mas_iva}€")
            valor = input("¿Quieres salir[1], para meter mas precios pulsa una tecla?")

        if tipo_de_iva == "21":
            precio_iva = precio * iva[3]
            total_mas_iva = precio + precio_iva
            print(f"Precio sin IVA : {precio}")
            print(f"IVA : {precio_iva}€")
            print(f"Precio con IVA : {total_mas_iva}€")
            valor = input("¿Quieres salir[1], para meter mas precios pulsa una tecla?")