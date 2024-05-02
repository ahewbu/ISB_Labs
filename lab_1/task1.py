def read_text(path: str):
    with open(path, 'r') as f:
        text = f.read()
    return text


def write_text(path: str, text: str):
    with open(path, 'w') as f:
        f.write(text)


def task_1():
    text = read_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\text_task1.txt")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_replacement = \
        read_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\key.txt")


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

    write_text("D:\\SHALAN REP\\ISB_Labs\\lab_1\\texts\\encrypt.txt", \
               result_string)

    for i in range(0, len(alphabet)):
        print(alphabet[i] + ' -> ' + alphabet_replacement[i])


def main():
    task_1()


if __name__ == '__main__':
    main()
