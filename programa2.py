import re

# Inicialização da tabela de símbolos com palavras-chave
keyword_table = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    # adicione mais palavras-chave aqui, se necessário
}

# Expressões regulares para reconhecer tokens
decimal_pattern = r'\d+(\.\d+)?'
operator_pattern = r'[+\-*/]'
relational_operator_pattern = r'[<>]=?'
identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
resto = ['(', ')', '{', '}']
igual = ['=']


# Função para remover comentários da linguagem C
def remove_comments(line):
    # Remove comentários de bloco /* ... */
    line = re.sub(r'/\*.*?\*/', '', line)

    # Remove comentários de linha // ...
    line = re.sub(r'//.*', '', line)

    return line


# Função para realizar a análise léxica
def lex(input_string):
    tokens = []
    lines = input_string.split('\n')
    line_number = 1

    for line in lines:
        line = remove_comments(line)
        line = line.strip()  # Remove espaços em branco no início e no fim

        position = 0
        while position < len(line):
            token = None
            if line[position].isspace():
                position += 1
                continue

            if line[position] == ';':
                token = line[position]
                tokens.append(('SEMICOLON', token, line_number))
                position += 1
                continue

            if line[position] == '=':
                token = line[position]
                tokens.append(('Equal', token, line_number))

                position += 1
                continue

            # Reconhecimento de números decimais
            match = re.match(decimal_pattern, line[position:])
            if match:
                token = match.group(0)
                tokens.append(('NUM', token, line_number))
                position += len(token)
                continue

            # Reconhecimento de operadores aritméticos
            if line[position] in '+-*/':
                token = line[position]
                tokens.append(('OP_ARIT', token, line_number))
                position += 1
                continue

            # Reconhecimento de operadores relacionais
            match = re.match(relational_operator_pattern, line[position:])
            if match:
                token = match.group(0)
                tokens.append(('OP_REL', token, line_number))
                position += len(token)
                continue

            # Reconhecimento de identificadores
            match = re.match(identifier_pattern, line[position:])
            if match:
                token = match.group(0)

                # Verifica se é uma palavra-chave
                if token in keyword_table:
                    tokens.append((keyword_table[token], token, line_number))
                else:
                    tokens.append(('ID', token, line_number))

                position += len(token)
                continue

            # Se chegou até aqui, é um caractere inválido
            token = line[position]
            print(f"Erro: Caractere inválido '{token}' na linha {line_number}")
            position += 1

        line_number += 1

    return tokens


# Exemplo de uso
program = '''
int x = 10;
float y = 3.14; // teste
if x > y  /* aaaaaa */
    printf("x > y");
 else 
    printf("x <= a y");

'''
tokens = lex(program)
for token in tokens:
    print(token)