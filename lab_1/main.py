import json

def read_text(path: str):
    """The function of reading text from file
    Args:
      path: the path to the file
    Returns:
      text from the file
    """
    with open(path, 'r', encoding='UTF-8') as f:
        text = f.read().lower()
    return text


def write_text(path: str, text: str):
    """The function of writing information to file
    Args:
      path: the path to the file
    """
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(text)


def decrypt(text, decryption_mapping):
    """The function of transposition by key
    Args:
      text: encrypted message
      decryption_mapping: dictionary list with key transposition
    Returns:
      decrypted text
    """
    decrypted_text = ''
    for char in text:
        decrypted_text += decryption_mapping.get(char, char)

    return decrypted_text


def task_1(plain_text: str, key: str, encrypted: str):
    """Encryption by a simple transposition cipher
    Args:
      plain_text: encrypted text
      key: required key string
      encrypted: string where the resulting cipher is written
    """
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
    """The function for decryption by 
    Args:
      plain_text: encrypted text
      key: required key string
      decrypted: string where the resulting deciphering is written
    """
    crypt_alphabet = read_text(key)
    normal_alphabet = " ОИЕНШЧЬПРЭТЙКЯМСЛДЗАЖЦУВГБФХЮ,ЩЫ."

    decryption_mapping = dict(zip(crypt_alphabet, normal_alphabet))

    data = read_text(plain_text)

    decrypted_text = decrypt(data, decryption_mapping)

    write_text(decrypted, decrypted_text)


def read_json(file: str):
    """The function of reading data from a json file
    Args:
      path: the path to the file
    Returns:
      parameters from json file
    """
    with open("D:\SHALAN REP\\ISB_Labs\\lab_1\\paths.json", "r", encoding="utf-8") as f:
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
