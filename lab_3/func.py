from asymmetric_crypt import *
from keys_functions import *


def encrypt_file(path_to_initial_file: str, path_to_secret_key: str, path_to_symmetric_key: str,
                 path_to_encrypt_file: str) -> None:
    """
    :param path_to_initial_file: Path to text
    :param path_to_secret_key: Path to secret key
    :param path_to_symmetric_key: Path to symmetric key
    :param path_to_encrypt_file: Path to encrypted file
    """
    symmetrical_key = decrypt_symmetric_key(path_to_symmetric_key, path_to_secret_key)
    txt = read_text(path_to_initial_file)
    res = encrypt(txt, symmetrical_key)
    write_encrypt(path_to_encrypt_file, res)


def decrypt_file(path_to_encrypt_file: str, path_to_secret_key: str, path_to_symmetric_key: str,
                 path_to_decrypted_file: str) -> None:
    """
    :param path_to_encrypt_file: Path to encrypted file
    :param path_to_secret_key: Path to secret key
    :param path_to_symmetric_key: Path to symmetric key
    :param path_to_decrypted_file: Path to decrypted file
    """
    symmetrical_key = decrypt_symmetric_key(path_to_symmetric_key, path_to_secret_key)
    cipher_tmp = read_encrypt(path_to_encrypt_file)
    cipher_txt = cipher_tmp['ciphertxt']
    nonce = cipher_tmp['nonce']
    dec_txt = decrypt(cipher_txt, symmetrical_key, nonce)
    write_decrypt(path_to_decrypted_file, dec_txt)
