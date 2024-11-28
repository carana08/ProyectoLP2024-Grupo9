import ply.lex as lex
import errorList as errorList

#reserved words
reserved = {
    #Aporte de César Arana
    'print': 'PRINT',
    'gets': 'GETS',
    'then': 'THEN',
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'end': 'END',
    'def': 'DEF',
    'class': 'CLASS',
    'begin': 'BEGIN',
    'end': 'END',
    'puts': 'PUTS',
    'chomp': 'CHOMP',
    # Aporte de Johann Ramírez
    'unless': 'UNLESS',  
    'until': 'UNTIL',   
    'true': 'TRUE',   
    'false': 'FALSE', 

    # Apórte de Luis Inga
    'nil': 'NIL',
    'while': 'WHILE',
    'when': 'WHEN',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'return': 'RETURN',

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
    'LESS',             # Operador de comparación '<'
    'ASSIGN',           # Operador de asignación '='
    'EQUALS',           # Operador de comparación '=='
    'DIFFERENT',        # Operador de comparación '!='
    'GREATER_EQUAL',    # Operador de comparación '>='
    'LESS_EQUAL',       # Operador de comparación '<='
    'PLUS_EQUAL',        # Operador de incremento
    'DOT',              # Punto .
    'OR_OPERATOR',      # Operador OR '||'
    'APPEND',           # Operador de concatenación '<<'
    

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

    #Aporte Johann Ramírez

    'MODULE',          # Operador de módulo
    'DIVIDE',           # Operador '/'
    'MULTIPLY',         # Operador '*'
    'RANGE',            #RANGO
    'INCLUSIVE_RANGE',  #RANGO INCLUSIVO
    
)+tuple(reserved.values())

#Tokens para expresiones regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'         
t_DIVIDE = r'/'            
t_GREATER = r'>'
t_ASSIGN = r'='
t_COMMA = r','
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_L_MAYUS_PAREN = r'\{'
t_R_MAYUS_PAREN = r'}'
t_L_ULTRA_PAREN = r'\['
t_R_ULTRA_PAREN = r']'
t_TWO_POINTS = r':'
t_HASHARROW = r'=>'
t_EQUALS = r'=='
t_DIFFERENT = r'!='
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_PLUS_EQUAL = r'\+='
t_LESS = r'<'
t_DOT = r'\.'
t_MODULE = r'%'  
t_OR_OPERATOR = r'\|\|'
t_APPEND = r'<<'
t_RANGE = r'\.\.'  
t_INCLUSIVE_RANGE = r'\.\.\.'
# Definición de expresiones regulares para tokens complejos

def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PUTS(t):
    r'puts'
    return t

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

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'(\"(\\.|[^"\\])*\"|\'(\\.|[^\'\\])*\')'
    t.value = t.value[1:-1]  # Remover las comillas de la cadena
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Definición de comentarios
def t_comment(t):
    r'\#.*'
    pass  # Ignorar comentarios

# Comentarios multilínea delimitados por =begin y =end
def t_COMMENT_MULTILINE(t):
    r'=begin(\n|.)*?=end'
    pass # Ignorar el contenido del comentario multilínea

# Definición de salto de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    line = t.lineno
    position = t.lexpos - t.lexer.lexdata.rfind("\n", 0, t.lexpos)
    errorList.erroresLexicos.append(f"Illegal character ('{t.value[0]}',{line},{position})")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex();



