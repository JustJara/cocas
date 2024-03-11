def cifrar_mensaje(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            nueva_letra = chr((ord(letra) - ord('a' if letra.islower() else 'A') + desplazamiento) % 26 + ord('a' if letra.islower() else 'A'))
            mensaje_cifrado += nueva_letra
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

# Ejemplo de uso
mensaje_original = "Hola, este es un mensaje secreto"
desplazamiento = 3
mensaje_cifrado = cifrar_mensaje(mensaje_original, desplazamiento)

print("Mensaje original:", mensaje_original)
print("Mensaje cifrado:", mensaje_cifrado)
