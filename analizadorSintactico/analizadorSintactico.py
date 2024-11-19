import ply.yacc as yacc
from analizadorLexico.analizadorLexico import tokens
import errorList as errorList

precedence = (
    ('right', 'NOT'),
    ('left', 'AND'),
    ('left', 'OR'),
    ('nonassoc', 'LESS', 'GREATER', 'LESS_EQUAL', 'GREATER_EQUAL', 'EQUALS', 'DIFFERENT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULE'),
)

# Regla para el programa principal
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])  # El programa es una lista de sentencias

# Regla para la lista de sentencias
def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]  # Lista con una sola sentencia
    else:
        p[0] = p[1] + [p[2]]  # Concatenamos las sentencias

# Regla general para las sentencias
def p_statement(p):
    '''statement : print_statement
                 | puts_statement
                 | input_statement
                 | assignment_statement
                 | data_structure
                 | control_structure
                 | function_definition
                 | return_statement'''
    p[0] = p[1]  # La sentencia es el resultado de la subregla

# Regla para el retorno
def p_return_statement(p):
    '''return_statement : RETURN expression'''
    p[0] = ('return', p[2])  # Representamos el retorno como una tupla

# Regla para la asignación
def p_assignment_statement(p):
    '''assignment_statement : LOCAL_VAR ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])  # Representamos la asignación

# Regla para la sentencia de impresión
def p_print_statement(p):
    '''print_statement : PRINT L_PAREN argument_list R_PAREN
                       | PRINT L_PAREN R_PAREN 
                       | PRINT argument_list
                       | PRINT'''
    if len(p) == 5:
        p[0] = ('print', p[3])  # print(argumentos)
    elif len(p) == 4:
        p[0] = ('print', [])  # print()
    elif len(p) == 3:
        p[0] = ('print', p[2])  # print argumentos
    else:
        p[0] = ('print', [])  # print

# Regla para la sentencia de impresión (puts)
def p_puts_statement(p):
    '''puts_statement : PUTS L_PAREN argument_list R_PAREN
                      | PUTS L_PAREN R_PAREN 
                      | PUTS argument_list
                      | PUTS'''
    if len(p) == 5:
        p[0] = ('puts', p[3])  # puts(argumentos)
    elif len(p) == 4:
        p[0] = ('puts', [])  # puts()
    elif len(p) == 3:
        p[0] = ('puts', p[2])  # puts argumentos
    else:
        p[0] = ('puts', [])  # puts

# Regla para la lista de argumentos
def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]  # Lista con una expresión
    else:
        p[0] = p[1] + [p[3]]  # Concatenamos las expresiones

# Regla para la sentencia de entrada
def p_input_statement(p):
    '''input_statement : LOCAL_VAR ASSIGN GETS
                       | LOCAL_VAR ASSIGN GETS DOT CHOMP'''
    if len(p) == 4:
        p[0] = ('input', p[1])  # variable = gets
    else:
        p[0] = ('input_chomp', p[1])  # variable = gets.chomp

# Definición de estructura de datos
def p_data_structure(p):
    '''data_structure : array_definition
                      | hash_definition'''
    p[0] = p[1]  # La estructura de datos es el resultado de la subregla

# Definición de hashes (diccionarios)
def p_hash_definition(p):
    '''hash_definition : LOCAL_VAR ASSIGN L_MAYUS_PAREN hash_element_list R_MAYUS_PAREN'''
    p[0] = ('hash_assign', p[1], p[4])  # variable = { elementos }

# Lista de elementos del hash
def p_hash_element_list(p):
    '''hash_element_list : hash_element
                         | hash_element_list COMMA hash_element'''
    if len(p) == 2:
        p[0] = [p[1]]  # Lista con un elemento
    else:
        p[0] = p[1] + [p[3]]  # Concatenamos los elementos

# Elemento de un hash
def p_hash_element(p):
    '''hash_element : STRING HASHARROW expression'''
    p[0] = ('hash_element', p[1], p[3])  # "clave" => valor

# Operadores lógicos para condiciones complejas
def p_logical_operator(p):
    '''logical_operator : AND
                        | OR'''
    p[0] = p[1]  # Retornamos el operador

# Definición de arreglo
def p_array_definition(p):
    '''array_definition : LOCAL_VAR ASSIGN L_ULTRA_PAREN element_list R_ULTRA_PAREN'''
    p[0] = ('array_assign', p[1], p[4])  # variable = [ elementos ]

# Lista de elementos en el arreglo
def p_element_list(p):
    '''element_list : expression
                    | element_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]  # Lista con un elemento
    else:
        p[0] = p[1] + [p[3]]  # Concatenamos los elementos

# Definición de estructuras de control
def p_control_structure(p):
    '''control_structure : if_statement
                         | until_statement
                         | unless_statement
                         | while_statement'''
    p[0] = p[1]  # La estructura de control es el resultado de la subregla

# Estructura condicional if-else
def p_if_statement(p):
    '''if_statement : IF condition statement_list END
                    | IF condition statement_list ELSE statement_list END'''
    if len(p) == 5:
        p[0] = ('if', p[2], p[3])  # if condición then sentencias end
    else:
        p[0] = ('if_else', p[2], p[3], p[5])  # if condición then sentencias else sentencias end

# Estructura de control while
def p_while_statement(p):
    '''while_statement : WHILE condition statement_list END'''
    p[0] = ('while', p[2], p[3])  # while condición do sentencias end

# Estructura de control unless
def p_unless_statement(p):
    '''unless_statement : UNLESS condition statement_list END
                        | UNLESS condition statement_list ELSE statement_list END'''
    if len(p) == 5:
        p[0] = ('unless', p[2], p[3])  # unless condición then sentencias end
    else:
        p[0] = ('unless_else', p[2], p[3], p[5])  # unless condición then sentencias else sentencias end

# Estructura de control until
def p_until_statement(p):
    '''until_statement : UNTIL condition statement_list END'''
    p[0] = ('until', p[2], p[3])  # until condición do sentencias end

# Definición de la condición (expresión booleana)
def p_condition(p):
    '''condition : expression comparison_operator expression
                 | condition logical_operator condition
                 | NOT condition
                 | L_PAREN condition R_PAREN'''
    if len(p) == 4 and p[1] == '(':
        p[0] = p[2]  # ( condición )
    elif len(p) == 3:
        p[0] = ('not', p[2])  # not condición
    elif len(p) == 4 and p.slice[2].type in ('AND', 'OR'):
        p[0] = ('logical_op', p[2], p[1], p[3])  # condición AND/OR condición
    else:
        p[0] = ('comparison', p[2], p[1], p[3])  # expresión operador expresión

# Definición de funciones (creación y llamada)
def p_function_definition(p):
    '''function_definition : DEF LOCAL_VAR parameter_list statement_list END
                           | DEF LOCAL_VAR statement_list END'''
    if len(p) == 6:
        p[0] = ('function_def', p[2], p[3], p[4])  # def nombre(parámetros) sentencias end
    else:
        p[0] = ('function_def', p[2], [], p[3])  # def nombre sentencias end

# Lista de parámetros de las funciones o vacío
def p_parameter_list(p):
    '''parameter_list : L_PAREN parameter_list_inner R_PAREN
                      | empty'''
    if len(p) == 4:
        p[0] = p[2]  # ( parámetros )
    else:
        p[0] = []  # Sin parámetros

# Parámetros
def p_parameter_list_inner(p):
    '''parameter_list_inner : LOCAL_VAR
                            | parameter_list_inner COMMA LOCAL_VAR'''
    if len(p) == 2:
        p[0] = [p[1]]  # Lista con un parámetro
    else:
        p[0] = p[1] + [p[3]]  # Concatenamos los parámetros

# Define las expresiones
def p_expression(p):
    '''expression : expression_binop
                  | expression_not
                  | expression_group
                  | expression_term'''
    p[0] = p[1]

# Expresiones generales
def p_expression_binop(p):
    '''expression_binop : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MODULE expression
                  | expression EQUALS expression
                  | expression DIFFERENT expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression GREATER_EQUAL expression
                  | expression LESS_EQUAL expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = ('bin_op', p[2], p[1], p[3])


def p_expression_not(p):
    '''expression_not : NOT expression'''
    p[0] = ('unary_op', p[1], p[2])

def p_expression_group(p):
    '''expression_group : L_PAREN expression R_PAREN'''
    p[0] = p[2]

def p_expression_term(p):
    '''expression_term : INTEGER
                  | FLOAT
                  | STRING
                  | LOCAL_VAR
                  | array_access
                  | function_call'''
    p[0] = p[1]


# Regla para las llamadas a función
def p_function_call(p):
    '''function_call : LOCAL_VAR L_PAREN argument_list R_PAREN
                     | LOCAL_VAR L_PAREN R_PAREN
                     | LOCAL_VAR argument_list
                     | LOCAL_VAR'''
    if len(p) == 5:
        p[0] = ('function_call', p[1], p[3])  # nombre_funcion(argumentos)
    elif len(p) == 4:
        p[0] = ('function_call', p[1], [])    # nombre_funcion()
    elif len(p) == 3:
        p[0] = ('function_call', p[1], p[2])  # nombre_funcion argumentos
    else:
        p[0] = ('function_call', p[1], []) 

# Definición de acceso a elementos de arreglo
def p_array_access(p):
    '''array_access : LOCAL_VAR L_ULTRA_PAREN expression R_ULTRA_PAREN'''
    p[0] = ('array_access', p[1], p[3])  # variable[índice]

# Operadores de comparación
def p_comparison_operator(p):
    '''comparison_operator : EQUALS
                           | DIFFERENT
                           | LESS
                           | LESS_EQUAL
                           | GREATER
                           | GREATER_EQUAL'''
    p[0] = p[1]  # Retornamos el operador

# Regla para manejar producciones vacías (para listas de parámetros)
def p_empty(p):
    '''empty :'''
    pass  # No hacemos nada

# Manejo de errores
def p_error(p):
    if p:
        errorList.erroresSintacticos.append(f"Syntax error at token '{p.value}', line {p.lineno}")
    else:
        errorList.erroresSintacticos.append("Syntax error: unexpected end of input")
        
# Construcción del analizador
parser = yacc.yacc()

def parse_input(input_data):
    result = parser.parse(input_data)
    return result
