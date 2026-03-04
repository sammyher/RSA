import math 
from math_utils import generate_prime, mod_inverse

def generate_keys(min, max):
    p = generate_prime(min, max)
    q = generate_prime(min, max)
    
    while q == p:
        q = generate_prime(min, max)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randint(3, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(3, phi - 1)

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key


