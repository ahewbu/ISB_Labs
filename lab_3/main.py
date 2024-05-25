import argparse
import os
import pickle
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from work_files import *


# Loading settings from the files

json_data = read_json("settings.json")

path_initial_file = json_data["text"]
path_encrypted_file = json_data["encrypted_text"]
path_decrypted_file = json_data["decrypted_text"]
path_symmetric_key = json_data["symmetric_key"]
path_public_key = json_data["public_key"]
path_secret_key = json_data["secret_key"]


def key_generation(path_to_symmetric_key: str, path_to_public_key: str, path_to_secret_key: str) -> None:
    """
    :param path_to_symmetric_key: Path to symmetric key
    :param path_to_public_key: Path to public key
    :param path_to_secret_key: Path to secret key
    """
    symmetric_key = ChaCha20Poly1305.generate_key()

    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    privat_k = keys

    privat_pem = privat_k.private_bytes(encoding=serialization.Encoding.PEM,
                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                        encryption_algorithm=serialization.NoEncryption())
    write_binary(path_to_secret_key, privat_pem)

    public_k = keys.public_key()
    public_pem = public_k.public_bytes(encoding=serialization.Encoding.PEM,
                                       format=serialization.PublicFormat.SubjectPublicKeyInfo)
    write_binary(path_to_public_key, public_pem)

    enc_symmetrical_key = public_k.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                       algorithm=hashes.SHA256(), label=None))
    write_binary(path_to_symmetric_key, enc_symmetrical_key)


def main():
    parser = argparse.ArgumentParser(description='main.py')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', type=str, help='Call function to generate keys', dest='generation')
    group.add_argument('-enc', '--encryption', type=str, help='Call function to encrypt', dest='encryption')
    group.add_argument('-dec', '--decryption', type=str, help='Call function to decrypt', dest='decryption')
    args = parser.parse_args()

    if args.generation is not None:
        key_generation(path_symmetric_key, path_public_key, path_secret_key)
        print('keys created')
    if args.encryption is not None:
        encrypt_file(path_initial_file, path_secret_key, path_symmetric_key, path_encrypted_file)
        print('file encrypted')
    if args.decryption is not None:
        decrypt_file(path_encrypted_file, path_secret_key, path_symmetric_key, path_decrypted_file)
        print('file decrypted')


if __name__ == "__main__":
    main()
