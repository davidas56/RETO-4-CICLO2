unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
diez_a_diecinueve = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
decenas = ['', '', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']

def convertir_a_palabras(numero):
    if numero < 0 or numero > 999:
        return "Fuera de rango"
    
    if numero == 0:
        return "cero"
    elif numero < 10:
        return unidades[numero]
    elif numero < 20:
        return diez_a_diecinueve[numero - 10]
    elif numero < 100:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return decenas[decena]
        else:
            return decenas[decena] + " y " + unidades[unidad]
    else:
        centena = numero // 100
        resto = numero % 100
        if resto == 0:
            return centenas[centena]
        else:
            return centenas[centena] + " " + convertir_a_palabras(resto)

numero = int(input("Ingrese un número entre 0 y 999: "))
numero_en_palabras = convertir_a_palabras(numero)
print(numero_en_palabras)
