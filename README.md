# RSA 

A command-line tool for RSA key generation, encryption, and decryption.

## Commands

### 1. Generate Keys
Generates a new public and private key pair.

```bash
python -m src.rsa keygen
```

### 2. Encrypt
Encrypts a text message using a public key (`-e` and `-n`). Wrap your message in quotes.

```bash
python -m src.rsa encrypt "Your message here" -e <public_e> -n <modulus>
```
**Example:**
```bash
python -m src.rsa encrypt "Top Secret" -e 17 -n 3233
```

### 3. Decrypt
Decrypts a space-separated string of ciphertext integers using a private key (`-d` and `-n`). Wrap the ciphertext in quotes.

```bash
python -m src.rsa decrypt "cipher text numbers" -d <private_d> -n <modulus>
```
**Example:**
```bash
python -m src.rsa decrypt "2034 2100 1205" -d 2753 -n 3233
```
