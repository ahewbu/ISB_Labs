from work_files import *


alphabet = "abcdefghijklmnopqrstuvwxyz"


def task_1(plain_text: str, key: str, encrypted: str):
    """Encryption by a simple transposition cipher
    Args:
      plain_text: encrypted text
      key: required key string
      encrypted: string where the resulting cipher is written
    """
    text = read_text(plain_text)
    alphabet_replacement = read_text(key)

    print(alphabet_replacement)

    result_string = ''
    for letter in text:
        try:
            index = alphabet.index(letter)
            result_string = result_string + alphabet_replacement[index]
        except ValueError:
            print("That was no valid number!")
            result_string = result_string + letter      

    print(result_string)

    write_text(encrypted, result_string)

    for i in range(0, len(alphabet)):
        print(alphabet[i] + ' -> ' + alphabet_replacement[i])


def task_2(plain_text: str, key: str, decrypted: str, normal_alphabet: str):
    """The function for decryption by 
    Args:
      plain_text: encrypted text
      key: required key string
      decrypted: string where the resulting deciphering is written
      normal_alphabet: alphabet to decrypt
    """
    crypt_alphabet = read_text(key)
    normal_alphabet = read_text(normal_alphabet)

    decryption_mapping = dict(zip(crypt_alphabet, normal_alphabet))

    data = read_text(plain_text)

    decrypted_text = decrypt(data, decryption_mapping)

    write_text(decrypted, decrypted_text)


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


def main():
    text_1, key_1, encrypted, text_2, key_2, \
        decrypted, normal_alphabet = read_json("paths.json")
    task_1(text_1, key_1, encrypted)
    task_2(text_2, key_2, decrypted, normal_alphabet)


if __name__ == '__main__':
    main()
