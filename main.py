from RSA import RSA_chiper

# рекомендуется значение, не превышающее 56 бит
key_bits = int(input('Enter key size: '))
# сообщение
msg = input('Enter your message: ')

RSA_chiper(key_bits, msg)