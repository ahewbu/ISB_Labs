import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


def encrypt(txt, symmetrical_key):
    """
    :param txt: Plain text
    :param symmetrical_key: Symmetric key
    """
    nonce = os.urandom(16)
    algorithm = algorithms.ChaCha20(symmetrical_key, nonce)
    cipher = Cipher(algorithm, mode=None)
    encrypted = cipher.encryptor()
    cipher_txt = encrypted.update(bytes(txt, 'utf-8'))
    res = {'ciphertxt': cipher_txt, 'nonce': nonce}

    return res


def decrypt(cipher_txt, symmetrical_key, nonce):
    """
    :param cipher_txt: encrypted text
    :param symmetrical_key: Symmetric key
    :param nonce: Nonce for decrypt
    """
    algorithm = algorithms.ChaCha20(symmetrical_key, nonce)
    cipher = Cipher(algorithm, mode=None)
    decrypted = cipher.decryptor()
    dec_txt = decrypted.update(cipher_txt) + decrypted.finalize()

    return dec_txt
