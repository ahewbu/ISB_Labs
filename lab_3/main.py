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

