// #include<stdio.h>
// void main()
// {
    // int a, b;
    // a=10;
   // b=20;
 //   printf("This is my first C Program");
//}


import re

# Open C program file
with open("cprogram.c", "r") as file:
    lines = file.readlines()

# Token definitions
keywords = ['void', 'int', 'float', 'return']
symbols = ['(', ')', ',', ';', '{', '}', '<', '>', '#']
system_identifiers = ['main', 'printf', 'scanf']

# Regex patterns
identifier_pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
number_pattern = r'^\d+$'
string_pattern = r'"[^"]*"'

print("\n--- LEXICAL ANALYSIS OUTPUT ---\n")

for line in lines:
    line = line.strip()

    # Handle preprocessor directive
    if line.startswith('#'):
        print("# - Symbol")

        header = re.findall(r'<(.+?)>', line)
        lib = re.findall(r'#include', line)

        if lib:
            print("include - Keyword")
        if header:
            print(header[0], "- Identifier")

    # Handle printf separately
    elif line.startswith('printf'):
        print("printf - Identifier")

        start = line.find('(')
        end = line.find(')')

        print("( - Symbol")

        string_match = re.findall(string_pattern, line)
        if string_match:
            print(string_match[0], "- String Constant")

        print(") - Symbol")

        if line.endswith(';'):
            print("; - Symbol")

    else:
        # Split line into tokens
        tokens = re.split(r'(\W)', line)

        for token in tokens:
            token = token.strip()

            if token == '':
                continue

            elif token in keywords:
                print(token, "- Keyword")

            elif token in symbols:
                print(token, "- Symbol")

            elif token in system_identifiers:
                print(token, "- System Identifier")

            elif re.match(number_pattern, token):
                print(token, "- Literal")

            elif re.match(identifier_pattern, token):
                print(token, "- Identifier")

            elif re.match(string_pattern, token):
                print(token, "- String Constant")

            elif token == '=':
                print("= - Assignment Operator")

            elif token in ['+', '-', '*', '/']:
                print(token, "- Arithmetic Operator")

            else:
                print(token, "- Unknown")