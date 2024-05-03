import json


def read_text(path: str):
    with open(path, 'r', encoding='UTF-8') as f:
        text = f.read().lower()
    return text


def write_text(path: str, text: str):
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(text)


def decrypt(text, decryption_mapping):
    decrypted_text = ''
    for char in text:
        decrypted_text += decryption_mapping.get(char, char)

    return decrypted_text


def task_1(plain_text: str, key: str, encrypted: str):
    text = read_text(plain_text)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_replacement = read_text(key)

    print(alphabet_replacement)

    result_string = ''
    for letter in text:
        try:
            index = alphabet.index(letter)
        except ValueError:
            result_string = result_string + letter
            continue
        result_string = result_string + alphabet_replacement[index]

    print(result_string)

    write_text(encrypted, result_string)

    for i in range(0, len(alphabet)):
        print(alphabet[i] + ' -> ' + alphabet_replacement[i])


def task_2(plain_text: str, key: str, decrypted: str):
    crypt_alphabet = read_text(key)
    normal_alphabet = " ОИЕНШЧЬПРЭТЙКЯМСЛДЗАЖЦУВГБФХЮ,ЩЫ."

    decryption_mapping = dict(zip(crypt_alphabet, normal_alphabet))

    data = read_text(plain_text)

    decrypted_text = decrypt(data, decryption_mapping)

    write_text(decrypted, decrypted_text)


def read_json(file: str):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    text_1 = data.get("path_to_text_1")
    key_1 = data.get("path_to_key_1")
    encrypted = data.get("path_to_encryption_1")

    text_2 = data.get("path_to_text_2")
    key_2 = data.get("path_to_key_2")
    decrypted = data.get("path_to_decrypt_2")

    return text_1, key_1, encrypted, text_2, key_2, decrypted


def main():
    text_1, key_1, encrypted, text_2, key_2, decrypted = read_json("paths.json")
    task_1(text_1, key_1, encrypted)
    task_2(text_2, key_2, decrypted)


if __name__ == '__main__':
    main()
