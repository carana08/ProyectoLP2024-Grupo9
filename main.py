import datetime
import os
import tkinter as tk
from tkinter import scrolledtext
from analizadorLexico.analizadorLexico import lexer
from analizadorSintactico.analizadorSintactico import parser
import subprocess
import errorList as errorList

def get_git_user():
    try:
        result = subprocess.run(['git', 'config', 'user.name'], stdout=subprocess.PIPE)
        username = result.stdout.decode('utf-8').strip()
        return username
    except Exception as e:
        print(f"Error al obtener el usuario de Git: {e}")
        return None

def analyze_expression():
    errorList.erroresLexicos = []
    errorList.erroresSintacticos = []
    
    
    user_input = input_text.get('1.0', tk.END).strip()
    console_text.delete('1.0', tk.END)
    errors_text.delete('1.0', tk.END)
    result = ""
    time = datetime.datetime.now().strftime('%d-%m-%Y-%H_%M_%S')
    
    
    if not user_input:
        console_text.insert(tk.END, "No se ingresó ninguna expresión")
        return
    
    logs_dirs = {
            "lexicos": os.path.abspath("logsLexicos"),
            "sintacticos": os.path.abspath("logsSintacticos")
    }
    for dir_path in logs_dirs.values():
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    try:
        # Analisis Lexico
        tokens = ""
        lexer.input(user_input)
        for token in lexer:
            tokens += f"{token}\n"

        console_text.insert(tk.END, "Tokens reconocidos: \n")
        console_text.insert(tk.END, tokens)

        lexicos_log_file = os.path.join(logs_dirs["lexicos"], f"lexico-{get_git_user()}-{time}.txt")
        with open(lexicos_log_file, 'w') as file:
            file.write("Analizador lexico:\n" + tokens)
            if errorList.erroresLexicos:
                console_text.insert(tk.END, "\nErrores:\n")
                file.write("\nErrores:\n")
                for error in errorList.erroresLexicos:
                    console_text.insert(tk.END, error + "\n")
                    file.write(error + "\n")
    except Exception as e:
        errors_text.insert(tk.END, f"Error en el análisis léxico: {str(e)}")
        file.write(f"Error en el análisis léxico: {str(e)}")
    try:
    # Analisis Sintactico
        result = parser.parse(user_input)
        print("Result: ", result);
        sintactico_log_file = os.path.join(logs_dirs["sintacticos"], f"sintactico-{get_git_user()}-{time}.txt")
        with open(sintactico_log_file, 'w') as file:
            if result:
                console_text.insert(tk.END, "\nAnalizador sintáctico:\n" + str(result) + "\n")
                file.write("Analizador sintactico:\n" + str(result) + "\n")
            else:
                console_text.insert(tk.END, "\nError en el análisis sintáctico.\n")
                file.write("Error en el análisis sintáctico.\n")
            if errorList.erroresSintacticos:
                errors_text.insert(tk.END, "Errores:\n")
                file.write("\nErrores:\n")
                for error in errorList.erroresSintacticos:
                    errors_text.insert(tk.END, error + "\n")
                    file.write(error + "\n")
    except Exception as e:
        errors_text.insert(tk.END, f"Error en el análisis sintáctico: {str(e)}")
        file.write(f"Error en el análisis sintáctico: {str(e)}")
    
    finally:
        errorList.erroresLexicos = []
        errorList.erroresSintacticos = []

        
root = tk.Tk()
root.title("Analizador de ruby")
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
root.geometry(f"{ancho_pantalla-30}x{alto_pantalla-50}")

# Configuración del marco principal
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Configuración de expansión de columnas y filas
main_frame.grid_columnconfigure(0, weight=2, uniform="equal")
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=0)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=0)
main_frame.grid_rowconfigure(3, weight=0)  # Ajustar esta fila para mover la consola más arriba
main_frame.grid_rowconfigure(4, weight=2)

# Entrada de expresión (más larga)
input_label = tk.Label(main_frame, text="Ingresa una expresión:")
input_label.grid(row=0, column=0, sticky="w")
input_text = scrolledtext.ScrolledText(main_frame, width=50, height=10, bg="black", fg="white", font=("Courier", 12), insertbackground="white")
input_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Botón para analizar (debajo del área de entrada, columna 0)
analyze_button = tk.Button(main_frame, text="Analizar", command=analyze_expression)
analyze_button.grid(row=2, column=0, padx=5, pady=5)

# Área de errores
errors_label = tk.Label(main_frame, text="Errores")
errors_label.grid(row=0, column=1, sticky="w")
errors_text = scrolledtext.ScrolledText(main_frame, width=30, height=5, bg="black", fg="white", font=("Courier", 12))
errors_text.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
errors_text.insert(tk.END, "No hay errores.\n")

# Consola de resultado (colocada más cerca del área de errores)
console_label = tk.Label(main_frame, text="Consola")
console_label.grid(row=3, column=1, sticky="w", padx=5, pady=5)
console_text = scrolledtext.ScrolledText(main_frame, width=80, height=10, bg="black", fg="white", font=("Courier", 12))
console_text.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
console_text.insert(tk.END, "Bienvenido a la aplicación.\n")

root.mainloop()
