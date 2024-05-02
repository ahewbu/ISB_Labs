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


def task_1():
    text = \
        read_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\task1\\text.txt")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_replacement = \
        read_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\task1\\key.txt")

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

    write_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\task1\\encrypt.txt", \
               result_string)

    for i in range(0, len(alphabet)):
        print(alphabet[i] + ' -> ' + alphabet_replacement[i])


def task_2():
    crypt_alphabet = \
        read_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\task2\\key.txt")
    normal_alphabet = " ОИЕНШЧЬПРЭТЙКЯМСЛДЗАЖЦУВГБФХЮ,ЩЫ."

    decryption_mapping = dict(zip(crypt_alphabet, normal_alphabet))

    data = \
        read_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\task2\\text.txt")

    decrypted_text = decrypt(data, decryption_mapping)

    write_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\task2\\result.txt", \
               decrypted_text)

    
def main():
    task_1()
    task_2()

if __name__ == '__main__':
    main()
