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
    encrypt_parser.add_argument("message", type=str, help="Message to encrypt")
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
        print(f"\n[+] Public Key (e, n): ({public_key[0]}, {public_key[1]})")
        print(f"[+] Private Key (d, n): ({private_key[0]}, {private_key[1]})")
        print("\nSave these pairs! You need the Public Key to encrypt and the Private Key to decrypt.")
    elif args.command == "encrypt":
        public_key = (args.e, args.n)
        encrypted = encrypt_text(args.message, public_key)
        encrypted_str = " ".join(str(num) for num in encrypted)
        print(f"\n[+] Encrypted message: {encrypted_str}\n")

    elif args.command == "decrypt":
        private_key = (args.d, args.n)
        decrypted = decrypt_text(args.encrypted, private_key)
        print(f"\n[+] Decrypted message: {decrypted}\n")

if __name__ == "__main__":
    main()



