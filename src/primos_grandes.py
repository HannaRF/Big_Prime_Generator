import random
from crivos import crivo_de_eratostenes

class BigNumber:
    def nBitRandom(self, bitSize):
        """
        Dado N bits, retorna um número aleatório de N bits
        """
        return(random.randrange(2**(bitSize-1)+1, 2**bitSize-1))

    def __str__(self): return str(self.valor)


class BigPrimeLV(BigNumber):
    def __init__(self, bitSize):
        self.bitSize = bitSize
        while True:
            self.valor = self.nBitRandom(self.bitSize)
            if self.is_prime(self.valor): break

    def is_prime(self, n):
        if not(n%2): return False
        for i in range(3, int(n**(1/2)), 2):
            if not(n%i): return False
        return True


class BigPrimeMC(BigNumber):
    def __init__(self, bitSize, primesUntil=1000, trials=20):
        self.bitSize = bitSize
        while True:
            self.valor = self.nBitRandom(self.bitSize)
            if self.lowLevelPrime(self.valor, primesUntil):
                if self.isMillerRabin(self.valor, trials): break

    def lowLevelPrime(self, prime_candidate, primesUntil=1000):
        """"
        Dado um candidato a primo, retorna booleano indicando primalidade
        de baixo nível (com primos até 'primesUntil')
        """
        first_primes_list = crivo_de_eratostenes(primesUntil)
        first_primes_list = filter(lambda x: x**2 <= prime_candidate,
                                   first_primes_list)
        for divisor in first_primes_list:
            if not (prime_candidate % divisor): return False
        return True

    def trialComposite(self, prime_candidate, round_tester,
                       evenComponent, maxDivisionsByTwo):
        if pow(round_tester, evenComponent, prime_candidate) == 1: return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * evenComponent,
                   prime_candidate)== prime_candidate-1: return False
        return True 

    def isMillerRabin(self, prime_candidate, trials=20):
        maxDivisionsByTwo = 0
        evenComponent = prime_candidate-1
        while evenComponent % 2 == 0:
            evenComponent >>= 1
            maxDivisionsByTwo += 1
        assert(2**maxDivisionsByTwo * evenComponent == prime_candidate-1)
        for _ in range(trials):
            round_tester = random.randrange(2, prime_candidate)
            if self.trialComposite(prime_candidate, round_tester,
                evenComponent, maxDivisionsByTwo): return False
        return True
