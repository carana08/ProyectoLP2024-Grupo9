import ply.lex as lex

#reserved words
reserved = {
    #César Arana
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'end': 'END',
    'def': 'DEF',
    'class': 'CLASS',
}

tokens = (
    #César Arana
    'LOCAL_VAR',        # Variables locales (minúsculas o _ al inicio)
    'GLOBAL_VAR',       # Variables globales ($var)
    'INSTANCE_VAR',     # Variables de instancia (@var)
    'CLASS_VAR',        # Variables de clase (@@var)
    'CONSTANT',         # Constantes (inician con mayúscula)
    'INTEGER',          # Números enteros
    'FLOAT',            # Números de punto flotante
    'STRING',           # Cadenas de texto
    'PLUS', 'MINUS',    # Operadores aritméticos
)+tuple(reserved.values())

#Tokens para expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'

# Definición de expresiones regulares para tokens complejos
def t_GLOBAL_VAR(t):
    r'\$[a-zA-Z_]\w*'
    return t

def t_INSTANCE_VAR(t):
    r'@[a-zA-Z_]\w*'
    return t

def t_CLASS_VAR(t):
    r'@@[a-zA-Z_]\w*'
    return t

def t_CONSTANT(t):
    r'[A-Z][a-zA-Z_]\w*'
    return t

def t_LOCAL_VAR(t):
    r'[a-z_][a-zA-Z_0-9]*'   # Empieza con minúscula o _
    t.type = reserved.get(t.value, 'LOCAL_VAR')  # Verifica si es una palabra reservada
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Definición de comentarios
def t_comment(t):
    r'\#.*'
    pass  # Ignorar comentarios

# Definición de salto de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()



