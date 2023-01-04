import random
from math import sqrt

'''
Jingtao Scott Hong
jh4ctf

reference repo : https://gist.github.com/djego/97db0d1bc3d16a9dcb9bab0930d277ff
'''



#to find the greatest common divisor of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#to find the the multiplicative inverse of e when moduled by phi.
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi

#to generate a key pair using given p and q
def generate_key_pair(p, q):
    if not (check_prime(p) and check_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private key_pair
    return ((e, n), (d, n))

# To unpack and encrypt the message 
def encrypt(pk, m):
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in m]
    # Return the array of bytes
    return cipher

# To unpack and decrypt the message 
def decrypt(pk, m):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    base = [str(pow(char, key, n)) for char in m]
    # Return the array of bytes as a string
    plain = [chr(int(a)) for a in base]
    return ''.join(plain)

#generate random pq so that pq are not equal and pq are prime
def p_q_gen():
    p = random.randrange(1,8000)
    q = random.randrange(1,80000)
    while(not check_prime(p)):
        p = random.randrange(1,8000)
    while(not check_prime(q) or p==q):
        q = random.randrange(1,8000)
    return p,q

# help funciton to check if the number is prime number
def check_prime(num):
    prime_flag = 0
    
    if(num > 1):
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    p,q = p_q_gen()
    e, d = generate_key_pair(p, q)
    print("p = ", p)
    print("q = ", q)
    print("e = ", e[0])
    print("d = ", d[0])
    message = input("Enter message: ")
    encrypted_msg = encrypt(e, message)
    print("Encrypted message =", ''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypted message =", decrypt(d, encrypted_msg))