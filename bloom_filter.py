# !pip install bitarray
from typing import Optional
from bitarray import bitarray
from bitarray.util import serialize, deserialize


class BloomFilter:
    # Primes less than 2**32
    # primes = [4294967189, 4294967197, 4294967231, 4294967279, 4294967291]
    primes = [257, 263, 269, 271, 277]


    def __init__(self, ba: Optional[bitarray] = None, size: int = 2**32 + 5):
        if ba is None:
            self.bloom = bitarray(size)
            self.bloom.setall(0)
        else:
            self.bloom = ba


    def exists(self, input: str) -> bool:
        input = input.lower()
        for p in self.primes:
            hash = self.__hash_str(input, p)
            if not self.bloom[hash]:
                return False
        return True


    def store(self, input: str):
        input = input.lower()
        for p in self.primes:
            hash = self.__hash_str(input, p)
            self.bloom[hash] = 1


    def save_to_file(self, path: str):
        with open(path, 'wb') as f:
            f.write(serialize(self.bloom))


    @staticmethod
    def from_file(path: str) -> "BloomFilter":
        with open(path, 'rb') as f:
            return BloomFilter(ba=deserialize(f.read()))


    def __hash_str(self, input: str, p: int, mod: int = int(2**32)) -> int:
        hash = 0
        p_pow = 1
        s = bytes(input, encoding="utf-8")

        for x in s:
            hash = ((hash + (x * p_pow)) % mod)
            p_pow = p_pow * p

        return hash
