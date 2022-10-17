from primos_grandes import BigPrimeLV, BigPrimeMC
from Crypto.Util import number
import time



# Crivos??

for n in range(4,32,2):
    print(n)
    t0 = time.time()

    # Primos grandes Las Vegas
    a = BigPrimeLV(n)
    t1 = time.time()
    print("Las Vegas (ms):", 1000*(t1-t0))

    # Primo grande Monte Carlo
    b = BigPrimeMC(n)
    t2 = time.time()
    print("Monte Carlo (ms):", 1000*(t2-t1))

    # Primos grandes PyCrypto
    c = number.getPrime(n)
    t3 = time.time()
    print("PyCrypto (ms):", 1000*(t3-t2))

# Plotar para diferentes N