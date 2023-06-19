menu = {
    "1": "Ver saldo",
    "2": "Recargar saldo",
    "3": "Transferir saldo",
    "4": "Salir"
}

saldo = 1000  # Saldo inicial

while True:
    # Mostrar el menú
    print("----- Menú Telefónico USSD -----")
    for key, value in menu.items():
        print(f"{key}. {value}")
    
    # Obtener la opción seleccionada por el usuario
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        # Opción: Ver saldo
        print(f"Su saldo actual es de {saldo} pesos.")
    elif opcion == "2":
        # Opción: Recargar saldo
        recarga = float(input("Ingrese el monto de la recarga: "))
        saldo += recarga
        print("Recarga exitosa. Su saldo actual es de", saldo, "pesos.")
    elif opcion == "3":
        # Opción: Transferir saldo
        transferencia = float(input("Ingrese el monto a transferir: "))
        if transferencia <= saldo:
            saldo -= transferencia
            print("Transferencia exitosa. Su saldo actual es de", saldo, "pesos.")
        else:
            print("Saldo insuficiente para realizar la transferencia.")
    elif opcion == "4":
        # Opción: Salir
        print("Gracias por utilizar el Menú Telefónico USSD. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
