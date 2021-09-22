import os
import re
 
dirname = input("Enter the path of the file: ")
if not os.path.exists(dirname):
    print('\031[1;35;0m Error, the path doesnt exist \031[0m')
    exit(-1)
level = int(input("Enter the completion level(1-4): "))

C_KEYWORDS = ('auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
              'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
              'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
              'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while',
              )
C_AREA_SEPARATOR = (';', '{', '}', 'switch', 'case', 'if', 'else')


def remove_string(str):
    str = re.sub(r'\\\n', ' ', str)
    str = re.sub(r'".*?"(?<!\\")', r'""', str)  # Multiline characters within double quotation marks
    # without escape
    str = re.sub(r"('.*?')(?<!\\')", r'""', str)
    return str


def remove_annotation(str):
    str = re.sub(r'/\*((.|\n)*?)\*/(\n| )*', '\n', str)  # block comment
    str = re.sub(r'/\*((.|\n)*?)$', '\n', str)  # first half of block comment
    str = re.sub(r'//(.*?)(\n|$)', '\n', str)  # line comment
    str = re.sub(r'#(.*?)(\n|$)', '\n', str)  # macro definition
    # print(str)
    return str

 
def remove_newline(str):
    str = re.sub(r'\t', ' ', str)
    str = re.sub(r';', " ;\n", str)
    str = re.sub(r'((\t| )*\n+){2,}', "\n", str)
    str = re.sub(r'{', " { ", str)
    str = re.sub(r'}', " } ", str)
    return str


def remove_symbol(str):
    str = re.sub(r'[^\u4E00-\u9FA5A-Za-z0-9_{};\s]', ' ', str)
    str = re.sub(r' +', ' ', str)
    return str


class Count(object):

    def __init__(self):
        self.keyword_count = 0
        self.switch_count = 0
        self.case_count = []
        self.if_else_count = 0
        self.if_elif_else_count = 0
        self.stack = []
        self.switch_stack = []
        self.if_state = 0  # if: 0, if-else: 1, if-elif-else: 2

    def pop_semicolon(self):  # 分号
        self.stack.pop()
        if len(self.stack) > 0:
            if self.stack[-1] == 'switch':
                pass  # error
            elif self.stack[-1] == 'case':
                self.pop_case()
            elif self.stack[-1] == 'if':
                self.stack[-1] = 'can_pop_if'
            elif self.stack[-1] == 'can_pop_if':
                self.pop_if()
            elif self.stack[-1] == 'elif':
                self.stack[-1] = 'can_pop_elif'
            elif self.stack[-1] == 'can_pop_elif':
                self.pop_elif()
            elif self.stack[-1] == 'else':
                self.stack[-1] = 'can_pop_else'
            elif self.stack[-1] == 'can_pop_else':
                self.pop_else()

    def pop_switch(self):
        self.stack.pop()
        self.switch_count += 1
        self.case_count.append(self.switch_stack.pop())
        if len(self.stack) > 0:
            if self.stack[-1] == 'switch':
                self.pop_switch()
            elif self.stack[-1] == 'case':
                self.pop_case()
            elif self.stack[-1] == 'if':
                self.stack[-1] = 'can_pop_if'
            elif self.stack[-1] == 'can_pop_if':
                self.pop_if()
            elif self.stack[-1] == 'elif':
                self.stack[-1] = 'can_pop_elif'
            elif self.stack[-1] == 'can_pop_elif':
                self.pop_elif()
            elif self.stack[-1] == 'else':
                self.stack[-1] = 'can_pop_else'
            elif self.stack[-1] == 'can_pop_else':
                self.pop_else()

    def pop_case(self):
        self.stack.pop()
        if len(self.stack) > 0:
            if self.stack[-1] == 'switch':
                self.pop_switch()
            elif self.stack[-1] == 'case':
                self.pop_case()
            elif self.stack[-1] == 'if':
                self.stack[-1] = 'can_pop_if'
            elif self.stack[-1] == 'can_pop_if':
                self.pop_if()
            elif self.stack[-1] == 'elif':
                self.stack[-1] = 'can_pop_elif'
            elif self.stack[-1] == 'can_pop_elif':
                self.pop_elif()
            elif self.stack[-1] == 'else':
                self.stack[-1] = 'can_pop_else'
            elif self.stack[-1] == 'can_pop_else':
                self.pop_else()
        else:
            pass  # error

    def pop_if(self):
        self.stack.pop()
        if self.if_state == 1:
            self.if_else_count += 1
            self.if_state = 0
        elif self.if_state == 2:
            self.if_elif_else_count += 1
            self.if_state = 0

        if len(self.stack) > 0:
            if self.stack[-1] == 'switch':
                self.pop_switch()
            elif self.stack[-1] == 'case':
                self.pop_case()
            elif self.stack[-1] == 'if':
                self.stack[-1] = 'can_pop_if'
            elif self.stack[-1] == 'can_pop_if':
                self.pop_if()
            elif self.stack[-1] == 'elif':
                self.stack[-1] = 'can_pop_elif'
            elif self.stack[-1] == 'can_pop_elif':
                self.pop_elif()
            elif self.stack[-1] == 'else':
                self.stack[-1] = 'can_pop_else'
            elif self.stack[-1] == 'can_pop_else':
                self.pop_else()

    def pop_elif(self):
        self.stack.pop()
        while self.stack[-1] != 'can_pop_if':
            temp = self.stack[-1]
            if temp == 'switch':
                self.pop_switch()
            elif temp == 'case':
                self.pop_case()
            elif temp == 'if':
                pass  # error
            elif temp == 'elif':
                pass  # error
            elif temp == 'can_pop_elif':
                self.stack.pop()
            elif temp == 'else':
                pass  # error
            elif temp == 'can_pop_else':
                self.pop_else()

        if self.if_state == 1:
            self.if_state = 2

        self.pop_if()

    def pop_else(self):
        self.stack.pop()
        while (self.stack[-1] != 'can_pop_if') and (self.stack[-1] != 'can_pop_elif'):
            temp = self.stack[-1]
            if temp == 'switch':
                self.pop_switch()
            elif temp == 'case':
                self.pop_case()
            elif temp == 'if':
                pass  # error
            elif temp == 'elif':
                pass  # error
            elif temp == 'else':
                pass  # error
            elif temp == 'can_pop_else':
                self.pop_else()

        self.if_state = 1

        if self.stack[-1] == 'can_pop_if':
            self.pop_if()
        else:
            self.pop_elif()

    def pop_brace(self):  # 大括号
        self.stack.pop()

        temp = ''
        while temp != '{':
            temp = self.stack[-1]
            if temp == 'switch':
                self.pop_switch()
            elif temp == 'case':
                self.pop_case()
            elif temp == 'if':
                pass  # error
            elif temp == 'can_pop_if':
                self.pop_if()
            elif temp == 'elif':
                pass  # error
            elif temp == 'can_pop_elif':
                self.pop_elif()
            elif temp == 'else':
                pass  # error
            elif temp == 'can_pop_else':
                self.pop_else()
        self.stack.pop()

        if len(self.stack) > 0:
            if self.stack[-1] == 'switch':
                self.pop_switch()
            elif self.stack[-1] == 'case':
                self.pop_case()
            elif self.stack[-1] == 'if':
                self.stack[-1] = 'can_pop_if'
            elif self.stack[-1] == 'can_pop_if':
                self.pop_if()
            elif self.stack[-1] == 'elif':
                self.stack[-1] = 'can_pop_elif'
            elif self.stack[-1] == 'can_pop_elif':
                self.pop_elif()
            elif self.stack[-1] == 'else':
                self.stack[-1] = 'can_pop_else'
            elif self.stack[-1] == 'can_pop_else':
                self.pop_else()

    def readfile(self):
        with open(dirname, encoding='utf8') as file:
            full_text = file.read()
        full_text = remove_string(full_text)
        full_text = remove_annotation(full_text)
        full_text = remove_symbol(full_text)
        full_text = remove_newline(full_text)
        # print(full_text)
        lines = full_text.split('\n')
        for line in lines:
            tup = line.split(' ')
            # print(tup)
            for word in tup:
                if word in C_KEYWORDS:
                    # print(word)
                    self.keyword_count += 1
                if word in C_AREA_SEPARATOR:
                    self.stack.append(word)
                    if word == 'switch':
                        self.switch_stack.append(0)
                    elif word == 'case':
                        self.switch_stack[-1] += 1
                    elif word == ';':
                        self.pop_semicolon()
                    elif word == '}':
                        self.pop_brace()
                    elif word == 'if' and len(self.stack) > 1:
                        if self.stack[-2] == 'else':
                            self.stack[-2] = 'elif'
                            self.stack.pop()

        while len(self.stack) > 0:
            temp = self.stack[-1]
            if temp == 'can_pop_else':
                self.pop_else()
            elif temp == 'can_pop_elif':
                self.pop_elif()
            elif temp == 'can_pop_if':
                self.pop_if()

        if level >= 1:
            print("total num:", self.keyword_count)
        if level >= 2:
            print('switch num:', self.switch_count)
            print('case num:', end=' ')
            for case_num in self.case_count:
                print(case_num, end=' ')
            print()
        if level >= 3:
            print('if-else num:', self.if_else_count)
        if level >= 4:
            print('if-elseif-else num:', self.if_elif_else_count)


def main():
    c = Count()
    c.readfile()


if __name__ == '__main__':
    main()
