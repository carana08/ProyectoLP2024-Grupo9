import datetime
import os
import tkinter as tk
from tkinter import scrolledtext
from analizadorLexico.analizadorLexico import lexer
import subprocess

def get_git_user():
    try:
        result = subprocess.run(['git', 'config', 'user.name'], stdout=subprocess.PIPE)
        username = result.stdout.decode('utf-8').strip()
        return username
    except Exception as e:
        print(f"Error al obtener el usuario de Git: {e}")
        return None

def analyze_expression():
    user_input = input_text.get('1.0', tk.END) 
    result_text.delete('1.0', tk.END)
    
    result = ""
    time = datetime.datetime.now().strftime('%d-%m-%Y-%H_%M_%S')

    lexer.input(user_input)
    for token in lexer:
        result += f"{token}\n"
        result_text.insert(tk.END, result)
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    log_file = os.path.join("logs","lexico-"+get_git_user()+"-"+time+".txt")
    with open(log_file, 'w') as file:
        file.write("Analizador lexico:\n" + result)

root = tk.Tk()
root.title("Analizador Léxico de Ruby")

input_label = tk.Label(root, text="Ingresa una expresión:")
input_label.pack()

input_text = scrolledtext.ScrolledText(root, width=50, height=5, bg="black", fg="white")
input_text.pack()

analyze_button = tk.Button(root, text="Analizar", command=analyze_expression)
analyze_button.pack()

result_label = tk.Label(root, text="Resultado del analizador léxico:")
result_label.pack()

result_text = scrolledtext.ScrolledText(root, width=50, height=10, bg="black", fg="white")
result_text.pack()

root.mainloop()
