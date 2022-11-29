from primos_grandes import BigPrimeLV, BigPrimeMC
from crivos import crivo_de_eratostenes, crivo_de_sandaram
import matplotlib.pyplot as plt
from Crypto.Util import number
import time

tam = list(range(1,100000, 100))
l1, l2, l3 = [], [], []

for n in tam:

    t0 = time.time()

    # Crivo de Erastotenes
    _ = crivo_de_eratostenes(n)
    t1 = time.time()
    l1.append(1000*(t1-t0))

    # Crivo de Sandaram
    _ = crivo_de_sandaram(n)
    t2 = time.time()
    l2.append(1000*(t2-t1))

plt.plot(tam, l1, label="Erasatotenes")
plt.plot(tam, l2, label="Sandaram")
plt.title("Tempo de geração de primos com crivos")
plt.ylabel("Tempo (ms)")
plt.xlabel("Primos até n")
plt.legend()
plt.show()


tam = list(range(4,44,2))
l1, l2, l3 = [], [], []
start=time.time()

for n in tam:

    t0 = time.time()

    # Primos grandes Las Vegas
    a = BigPrimeLV(n)
    t1 = time.time()
    l1.append(1000*(t1-t0))

    # Primo grande Monte Carlo
    b = BigPrimeMC(n)
    t2 = time.time()
    l2.append(1000*(t2-t1))

    # Primos grandes PyCrypto
    c = number.getPrime(n)
    t3 = time.time()
    l3.append(1000*(t3-t2))

print("Números gerados em:", (time.time()-start), "s")

plt.plot(tam[1:], l1[1:], label="Las Vegas")
plt.plot(tam[1:], l2[1:], label="Monte Carlo")
plt.plot(tam[1:], l3[1:], label="PyCripto")
plt.title("Tempo de geração dos números por método")
plt.ylabel("Tempo (ms)")
plt.xlabel("Tamanho do número (bits)")
plt.legend()
plt.show()
