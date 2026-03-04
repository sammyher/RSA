# encrypts message using the public key
# formula: c = (m^e) mod n
def encrypt(message, public_key):
    e, n = public_key

    if message < 0 or message >= n:
        raise ValueError("Message must be in the range [0, n-1]")

    cipher = pow(message, e, n)
        
    return cipher

# decrypts cipher using the private key
# formula: m = (c^d) mod n
def decrypt(ciphertext, private_key):
    d, n = private_key

    message = pow(ciphertext, d, n)

    return message

def encrypt_text(text: str, public_key: tuple) -> list:
    encrypted = []
    
    for char in text:
        char_int = ord(char)
        encrypted_int = encrypt(char_int, public_key)
        encrypted.append(encrypted_int)
    
    return encrypted

def decrypt_text(encrypted: list, private_key: tuple) -> str:
    decrypted = []

    for encrypted_int in encrypted:
        decrypted_int = decrypt(encrypted_int, private_key)
        decrypted_char = chr(decrypted_int)
        decrypted.append(decrypted_char)

    return "".join(decrypted)

