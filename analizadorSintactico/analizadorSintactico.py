import ply.yacc as yacc
from analizadorLexico.analizadorLexico import tokens
import errorList as errorList

# Regla para el programa principal
def p_program(p):
    '''program : statement_list'''
    pass

# Regla para la lista de sentencias
def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    pass

# Regla general para las sentencias
def p_statement(p):
    '''statement : print_statement
                 | puts_statement
                 | input_statement
                 | assignment_statement
                 | data_structure
                 | control_structure
                 | function_definition'''
    pass

# Regla para la asignación
def p_assignment_statement(p):
    '''assignment_statement : LOCAL_VAR ASSIGN expression'''
    pass

# Regla para la sentencia de impresión
def p_print_statement(p):
    '''print_statement : PRINT L_PAREN argument_list R_PAREN
                       | PRINT L_PAREN R_PAREN 
                       | PRINT argument_list
                       | PRINT'''
    pass

# Regla para la sentencia de impresión (puts)
def p_puts_statement(p):
    '''puts_statement : PUTS L_PAREN argument_list R_PAREN
                     | PUTS L_PAREN R_PAREN 
                     | PUTS argument_list
                     | PUTS'''
    pass

# Regla para la lista de argumentos (en la sentencia print)
def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    pass

# Regla para la sentencia de entrada
def p_input_statement(p):
    '''input_statement : LOCAL_VAR ASSIGN GETS
                        | LOCAL_VAR ASSIGN GETS DOT CHOMP'''
    pass

# Definición de estructura de datos
def p_data_structure(p):
    '''data_structure : array_definition'''
    pass

# Definición de arreglo
def p_array_definition(p):
    '''array_definition : LOCAL_VAR ASSIGN L_ULTRA_PAREN element_list R_ULTRA_PAREN'''
    pass

# Lista de elementos en el arreglo
def p_element_list(p):
    '''element_list : expression
                    | element_list COMMA expression'''
    pass

# Definición de estructuras de control
def p_control_structure(p):
    '''control_structure : if_statement
                         | until_statement
                         | unless_statement'''
    pass

# Estructura condicional if-else
def p_if_statement(p):
    '''if_statement : IF condition statement_list END
                    | IF condition statement_list ELSE statement_list END'''
    pass

def p_unless_statement(p):
    '''unless_statement : UNLESS condition statement_list END
                        | UNLESS condition statement_list ELSE statement_list END'''
    pass

# Estructura de control until
def p_until_statement(p):
    '''until_statement : UNTIL condition statement_list END'''
    pass

# Definición de la condición (expresión booleana)
def p_condition(p):
    '''condition : expression comparison_operator expression'''
    pass

# Definición de funciones (creación y llamada)
def p_function_definition(p):
    '''function_definition : DEF LOCAL_VAR L_PAREN parameter_list R_PAREN statement_list END'''
    pass

# Lista de parámetros de las funciones
def p_parameter_list(p):
    '''parameter_list : LOCAL_VAR
                      | parameter_list COMMA LOCAL_VAR
                      | empty'''
    pass

# Expresiones generales
def p_expression(p):
    '''expression : INTEGER
                  | FLOAT
                  | STRING
                  | LOCAL_VAR
                  | array_access
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MODULE expression
                  | expression comparison_operator expression'''
    pass

# Definición de acceso a elementos de arreglo
def p_array_access(p):
    '''array_access : LOCAL_VAR L_ULTRA_PAREN expression R_ULTRA_PAREN'''
    pass

# Operadores de comparación
def p_comparison_operator(p):
    '''comparison_operator : EQUALS
                           | DIFFERENT
                           | LESS
                           | LESS_EQUAL
                           | GREATER
                           | GREATER_EQUAL'''
    pass

# Regla para manejar producciones vacías (para listas de parámetros)
def p_empty(p):
    '''empty :'''
    pass

# Manejo de errores
def p_error(p):
    if p:
        errorList.erroresSintacticos.append(f"Syntax error at token '{p.value}'")
    else:
        print("Syntax error: unexpected end of input")
        errorList.erroresSintacticos.append("Syntax error: unexpected end of input")
    
# Construcción del analizador
parser = yacc.yacc()

def parse_input(input_data):
    result = parser.parse(input_data)
    return result
