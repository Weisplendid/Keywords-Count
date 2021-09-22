dirname = input("Enter the path of the file: ")

C_KEYWORDS = ('auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
              'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
              'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
              'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while',
              )

def main():

    keyword_count = 0

    with open(dirname, encoding='utf8') as file:
        full_text = file.read()

    # print(full_text)
    lines = full_text.split('\n')
    for line in lines:
        tup = line.split(' ')
        # print(tup)
        for word in tup:
            if word in C_KEYWORDS:
                # print(word)
                keyword_count = keyword_count + 1

    print("total num: ", keyword_count)


if __name__ == '__main__':
    main()
