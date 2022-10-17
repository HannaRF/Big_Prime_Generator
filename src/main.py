from primos_grandes import BigPrime
from Crypto.Util import number

# Crivos??



n = 128

# Primo grande
a = BigPrime(n)

# Primos grandes PyCrypto
b = number.getPrime(n)