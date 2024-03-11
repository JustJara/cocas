def verificador_palindromo(palabra):

    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return verificador_palindromo(palabra[1:-1])
    else:
        return False

palabra = "osos"

print(verificador_palindromo(palabra))