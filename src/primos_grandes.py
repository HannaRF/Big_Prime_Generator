from random import random
from crivos import crivo_de_eratostenes

class BigPrime:
    def __init__(self, bitSize):
        self.bitSize = bitSize

    def nBitRandom(bitSize):
        """
        Dado N bits, retorna um número aleatório de N bits
        """
        return(random.randrange(2**(bitSize-1)+1, 2**bitSize-1))

    
    def lowLevelPrime(prime_candidate, primesUntil=1000):
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

    