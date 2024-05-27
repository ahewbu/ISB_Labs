from func import *


def main():
    # Loading settings from the files
    json_data = read_json("settings.json")

    parser = argparse.ArgumentParser(description='main.py')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', type=str, help='Call function to generate keys', dest='generation')
    group.add_argument('-enc', '--encryption', type=str, help='Call function to encrypt', dest='encryption')
    group.add_argument('-dec', '--decryption', type=str, help='Call function to decrypt', dest='decryption')
    parser.add_argument("-isec", "--input_secret_key", dest="secret_key", required=False, type=validate_file,
                        help="input path to secret key", metavar="FILE")
    parser.add_argument("-ipk", "--input_public_key", dest="public_key", required=False, type=validate_file,
                        help="input path to public key", metavar="FILE")
    parser.add_argument("-isym", "--input_symmetric_key", dest="symmetric_key", required=False, type=validate_file,
                        help="input path to symmetric key", metavar="FILE")
    parser.add_argument("-ipl", "--input_plain_text", dest="plain_text", required=False, type=validate_file,
                        help="input path to plain text", metavar="FILE")
    parser.add_argument("-ienc", "--input_encrypted_text", dest="encrypted_text", required=False, type=validate_file,
                        help="input path to encrypted text", metavar="FILE")
    parser.add_argument("-idec", "--input_decrypted_text", dest="decrypted_text", required=False, type=validate_file,
                        help="input path to decrypted text", metavar="FILE")
    args = parser.parse_args()

    value = ''

    if args.generation is not None:
        value = 'generation'
        if args.symmetric_key is not None:
            path_symmetric_key = args.symmetric_key
        else:
            path_symmetric_key = json_data["symmetric_key"]
        if args.public_key is not None:
            path_public_key = args.public_key
        else:
            path_public_key = json_data["public_key"]
        if args.secret_key is not None:
            path_secret_key = args.secret_key
        else:
            path_secret_key = json_data["secret_key"]
    elif args.encryption is not None:
        value = 'encryption'
        if args.symmetric_key is not None:
            path_symmetric_key = args.symmetric_key
        else:
            path_symmetric_key = json_data["symmetric_key"]
        if args.public_key is not None:
            path_public_key = args.public_key
        else:
            path_public_key = json_data["public_key"]
        if args.secret_key is not None:
            path_secret_key = args.secret_key
        else:
            path_secret_key = json_data["secret_key"]
        if args.plain_text is not None:
            path_initial_file = args.plain_text
        else:
            path_initial_file = json_data["text"]
        if args.encrypted_text is not None:
            path_encrypted_file = args.encrypted_text
        else:
            path_encrypted_file = json_data["encrypted_text"]
    elif args.decryption is not None:
        value = 'decryption'
        if args.symmetric_key is not None:
            path_symmetric_key = args.symmetric_key
        else:
            path_symmetric_key = json_data["symmetric_key"]
        if args.public_key is not None:
            path_public_key = args.public_key
        else:
            path_public_key = json_data["public_key"]
        if args.secret_key is not None:
            path_secret_key = args.secret_key
        else:
            path_secret_key = json_data["secret_key"]
        if args.encrypted_text is not None:
            path_encrypted_file = args.encrypted_text
        else:
            path_encrypted_file = json_data["encrypted_text"]
        if args.decrypted_text is not None:
            path_decrypted_file = args.decrypted_text
        else:
            path_decrypted_file = json_data["decrypted_text"]

    match value:
        case 'generation':
            key_generation(path_symmetric_key, path_public_key, path_secret_key)
            print('keys created')
        case 'encryption':
            encrypt_file(path_initial_file, path_secret_key, path_symmetric_key, path_encrypted_file)
            print('file encrypted')
        case 'decryption':
            decrypt_file(path_encrypted_file, path_secret_key, path_symmetric_key, path_decrypted_file)
            print('file decrypted')
        case _:
            print(f"Args '{args}' not understood")


if __name__ == "__main__":
    main()
