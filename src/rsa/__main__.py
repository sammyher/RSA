import argparse
from .keygen import generate_keys
from .cipher import encrypt_text, decrypt_text

def main():
    parser = argparse.ArgumentParser(description="RSA Encryption/Decryption")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # command 1: keygen
    keygen_parser = subparsers.add_parser("keygen", help="Generate RSA keys")
    keygen_parser.add_argument("--min", type=int, default=100, help="Minimum prime number")
    keygen_parser.add_argument("--max", type=int, default=1000, help="Maximum prime number")

    # comaand 2: encrypt
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a message")
    engrypt_parser.add_argument("message", type=str, help="Message to encrypt")
    encrypt_parser.add_argument("-e", type=int, required=True, help="Public exponent")
    encrypt_parser.add_argument("-n", type=int, required=True, help="Modulus")

    # command 3: decrypt
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a message")
    decrypt_parser.add_argument("encrypted", type=int, nargs="+", help="Encrypted message (list of integers)")
    decrypt_parser.add_argument("-d", type=int, required=True, help="Private exponent")
    decrypt_parser.add_argument("-n", type=int, required=True, help="Modulus")

    args = parser.parse_args()

    if args.command == "keygen":
        public_key, private_key = generate_keys(args.min, args.max)
        print(f"[+] Public Key: {public_key}")
        print(f"[+] Private Key: {private_key}")
        print(f"[+] n: {public_key[1]}")
        print("\nSave these numbers! You need them to encrypt and decrypt.")
    elif args.command == "encrypt":
        public_key = (args.e, args.n)
        encrypted = encrypt_text(args.message, public_key)
        print(f"[+] Encrypted message: {encrypted}")

    elif args.command == "decrypt":
        private_key = (args.d, args.n)
        try:
            cipher_list = [int(x) for x in args.ciphertext.split()]
        except ValueError:
            print("\nError: Ciphertext must be space-separated numbers.")
            return
        decrypted = decrypt_text(args.encrypted, private_key)
        print(f"[+] Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()



