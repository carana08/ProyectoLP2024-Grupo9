import ply.lex as lex
import errorList as errorList

#reserved words
reserved = {
    #Aporte de César Arana
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'end': 'END',
    'def': 'DEF',
    'class': 'CLASS',
    # Aporte de Johann Ramírez
    'unless': 'UNLESS',  
    'until': 'UNTIL',   

    # Apórte de Luis Inga
    'nil': 'NIL',
    'while': 'WHILE',
    'when': 'WHEN'

}

tokens = (
    #Aporte de César Arana
    'LOCAL_VAR',        # Variables locales (minúsculas o _ al inicio)
    'GLOBAL_VAR',       # Variables globales ($var)
    'INSTANCE_VAR',     # Variables de instancia (@var)
    'CLASS_VAR',        # Variables de clase (@@var)
    'CONSTANT',         # Constantes (inician con mayúscula)
    'INTEGER',          # Números enteros
    'FLOAT',            # Números de punto flotante
    'STRING',           # Cadenas de texto
    'PLUS', 'MINUS',    # Operadores aritméticos
    'GREATER',          # Operador de comparación '>'
    'EQUAL',            # Operador de asignación o comparación '='

    # Aporte de Luis Inga
    'COMMA',
    'L_PAREN',
    'R_PAREN',
    'L_MAYUS_PAREN',
    'R_MAYUS_PAREN',
    'L_ULTRA_PAREN',
    'R_ULTRA_PAREN',
    'TWO_POINTS',
    'HASHARROW',
)+tuple(reserved.values())

#Tokens para expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_GREATER = r'>'
t_EQUAL = r'='
t_COMMA = r','
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_L_MAYUS_PAREN = r'\{'
t_R_MAYUS_PAREN = r'}'
t_L_ULTRA_PAREN = r'\['
t_R_ULTRA_PAREN = r']'
t_TWO_POINTS = r':'
t_HASHARROW = r'=>'

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

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remover las comillas de la cadena
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
    line = t.lineno
    position = t.lexpos - t.lexer.lexdata.rfind("\n", 0, t.lexpos)
    errorList.errores.append(f"Illegal character ('{t.value[0]}',{line},{position})")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex();



