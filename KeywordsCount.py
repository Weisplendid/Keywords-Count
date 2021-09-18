import re


def remove_symbol(str):
    match = re.match(r'^([a-z]*)\(.*\).*$', str)
    if match:
        return match.group(1)
    match = re.match(r'^([a-z]*).*$', str)
    if match:
        return match.group(1)
    return str


C_KEYWORDS = ('auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
              'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
              'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
              'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while',
              )
keyword_count = 0

dirname = input("Enter the path of the file (absolute path): ")
with open(dirname, encoding='utf8') as file:
    lines = file.readlines()

for line in lines:
    tup = line.split(' ')
    for word in tup:
        word = remove_symbol(word)
        if word in C_KEYWORDS:
            # print(word)
            keyword_count = keyword_count + 1

print("total num: ", keyword_count)