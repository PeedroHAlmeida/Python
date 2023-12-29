import tkinter as tk

def on_button_click():
    label.config(text="Olá, " + entry.get())

# Cria a janela principal
root = tk.Tk()
root.title("Minha Interface Gráfica")

# Cria um rótulo
label = tk.Label(root, text="Digite seu nome:")
label.pack(pady=10)

# Cria uma caixa de entrada
entry = tk.Entry(root)
entry.pack(pady=10)

# Cria um botão
button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
