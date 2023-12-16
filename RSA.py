import random
import math
import time

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

#Генерируем простое число указанной длины
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# TODO: Функция нахождения НОД
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# TODO: Реализация расширенного алгоритма Евклида
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

# TODO: Функция нахождения обратного элемента по модулю
def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Обратного элемента не существует')
    else:
        return x % m

# TODO: Генерация пары ключей (закрытого/открытого)
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return '\n'.join(map(str, ciphertext))  # Объединяем числа в столбец

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(int(char), d, n)) for char in ciphertext.split()])
    return plaintext

def RSA_chiper(key_bits, message):
    start_time = time.time()
    # Генерация ключей
    public_key, private_key = generate_keypair(key_bits)

    print(f'\nPublic key: {public_key}')
    print(f'Private key: {private_key}')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal elapsed time: {elapsed_time:.6f} seconds")

    # Шифрование
    encrypted_message = encrypt(public_key, message)
    print(f'__________________')
    print(f'Encrypted message: \n{encrypted_message}')

    # Дешифрование
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f'\nDecrypted message: {decrypted_message}')