import math


def crivo_de_eratostenes(n):
    """
    Recebe um inteiro N e retorna a lista dos primos menores ou iguais a N
    """
    numeros = [False, False] + [True] * (n - 1)
    primos = []
    for numero, primo in enumerate(numeros):
        if primo:
            primos.append(numero)
            for i in range(numero * 2, n + 1, numero):
                numeros[i] = False
    return primos

def crivo_de_sandaram(n):
    """
    Recebe um inteiro N e retorna a lista dos primos menores ou iguais a N
    """
    primos=[2] if n>=2 else []
    k = int((n - 2) / 2)
    a = [0] * (k + 1)
    for i in range(1, k + 1):
        j = i 
        while((i + j + 2 * i * j) <= k):
            a[i + j + 2 * i * j] = 1
            j += 1
    for i in range(1, k + 1):
        if (a[i] == 0):
            primos.append(2 * i + 1)
    return primos

def crivo_de_atkin(nmax):
    """
    Recebe um inteiro N e retorna a lista dos primos menores ou iguais a N
    """
    is_prime = dict([(i, False) for i in range(5, nmax+1)])
    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= nmax):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes
