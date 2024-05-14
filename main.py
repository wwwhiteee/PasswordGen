import random
import string

longitud = int(input("Ingrese el digito: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(longitud))
print("Cadena aleatoria:", cadena_aleatoria)
