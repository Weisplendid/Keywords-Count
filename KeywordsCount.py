import re


dirname = input("Enter the path of the file(absolute path): ")


C_KEYWORDS = ('auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
              'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
              'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
              'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while',
              )


def remove_string(str):
    str = re.sub(r'("(.*?(\\n\\\n)?)+?")(?<!\\")', r'""',str)   # Multiline characters within double quotation marks
    # without escape
    str = re.sub(r"('.*?')(?<!\\')", r'""', str)
    return str

def remove_annotation(str):
    str = re.sub(r'/\*((.|\n)*?)$', '\n', str)  # first half of block comment
    str = re.sub(r'/\*((.|\n)*?)\*/(\n| )*', '\n', str)    # block comment
    str = re.sub(r'//(.*?)(\n|$)', '\n', str)   # line comment
    str = re.sub(r'#(.*?)(\n|$)', '\n',str)  # macro definition
    # print(str)
    return str
def remove_newline(str):
    str = re.sub(r'((\t| )*\n+){2,}',"\n",str)
    return str
def remove_symbol(str):
    str = re.sub(r'\W',' ',str)
    str = re.sub(r' +',' ',str)
    return str

def main():

    keyword_count = 0

    with open(dirname, encoding='utf8') as file:
        full_text = file.read()
    full_text = remove_string(full_text)
    full_text = remove_annotation(full_text)
    full_text = remove_newline(full_text)
    full_text = remove_symbol(full_text)
    # print(full_text)
    lines = full_text.split('\n')
    for line in lines:
        tup = line.split(' ')
        for word in tup:
            if word in C_KEYWORDS:
                # print(word)
                keyword_count = keyword_count + 1

    print("total num: ", keyword_count)


if __name__ == '__main__':
    main()
