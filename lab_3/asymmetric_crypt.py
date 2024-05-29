import os
from typing import Any

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


def encrypt(txt: str, symmetrical_key: Any) -> dict:
    """Function sequentially calls a set of functions to encrypt the text
    :param txt: string of text that needed to be encrypted.
    :param symmetrical_key: symmetric key required for encryption
    Returns:
        dictionary containing the ciphertext and a random number of nonce
    """
    nonce = os.urandom(16)
    algorithm = algorithms.ChaCha20(symmetrical_key, nonce)
    cipher = Cipher(algorithm, mode=None)
    encrypted = cipher.encryptor()
    cipher_txt = encrypted.update(bytes(txt, 'utf-8'))
    res = {'ciphertxt': cipher_txt, 'nonce': nonce}

    return res


def decrypt(cipher_txt: Any, symmetrical_key: Any, nonce: Any) -> bytes:
    """Function sequentially calls a set of functions to decrypt the text
    :param cipher_txt: encrypted bytes of plain text
    :param symmetrical_key: symmetric key required for decryption
    :param nonce: random number of nonce needed to decrypt the text
    Returns:
        decrypted text as a set of bytes
    """
    algorithm = algorithms.ChaCha20(symmetrical_key, nonce)
    cipher = Cipher(algorithm, mode=None)
    decrypted = cipher.decryptor()
    dec_txt = decrypted.update(cipher_txt) + decrypted.finalize()

    return dec_txt
