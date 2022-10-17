from primos_grandes import BigPrimeLV, BigPrimeMC
from Crypto.Util import number

# Crivos??



n = 128

# Primos grandes Las Vegas
a = BigPrimeLV(n)

# Primo grande Monte Carlo
b = BigPrimeMC(n)

# Primos grandes PyCrypto
c = number.getPrime(n)