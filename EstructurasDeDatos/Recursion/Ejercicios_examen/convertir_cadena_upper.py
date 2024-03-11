def convertir_cadena_a_uppercase(cadena,indice):
    if indice == len(cadena):
        return ''
    if indice < len(cadena):
        letra_upper = cadena[indice].upper()
        return letra_upper + convertir_cadena_a_uppercase(cadena,indice+1)

palabra_original = "La profsora es mera firma la plena"
print(f"Palabra original: {palabra_original}")
print(f"Palabra en upper: {convertir_cadena_a_uppercase(palabra_original,0)}")