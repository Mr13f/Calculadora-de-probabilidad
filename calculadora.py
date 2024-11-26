import tkinter as tk
from tkinter import messagebox

def calcular_probabilidad():
    try:
        c1 = int(entry_c1.get()) #8
        c2 = int(entry_c2.get())
        c3 = int(entry_c3.get())
        k1 = int(entry_k1.get())
        k2 = int(entry_k2.get())
        k3 = int(entry_k3.get())
        
        Total = c1 + c2 + c3

        # Calcular combinaciones para el primer conjunto
        k01 = 1
        for i in range(k1): 
            k01 *= (c1 - i)#8 #2
        for i in range(1, k1 + 1):
            k01 //= i

        # Calcular combinaciones para el segundo conjunto
        k02 = 1
        for i in range(k2):
            k02 *= (c2 - i)
        for i in range(1, k2 + 1):
            k02 //= i

        # Calcular combinaciones para el tercer conjunto
        k03 = 1
        for i in range(k3):
            k03 *= (c3 - i)
        for i in range(1, k3 + 1):
            k03 //= i

        # Calcular combinaciones totales
        combinacionest = 1
        for i in range(k1 + k2 + k3):
            combinacionest *= (Total - i)
        for i in range(1, k1 + k2 + k3 + 1):
            combinacionest //= i

        # Calcular la probabilidad
        probabilidad = (k01 * k02 * k03) / combinacionest

        # Mostrar el resultado
        messagebox.showinfo("Resultado", f"La probabilidad de extraer {k1} {n1.get()}, {k2}  {n2.get()} y {k3} {n3.get()} es: {probabilidad * 100:.2f}%")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Probabilidad")

# Crear y colocar los widgets
tk.Label(root, text="Característica del primer conjunto:").grid(row=0, column=0)
n1 = tk.Entry(root)
n1.grid(row=0, column=1)

tk.Label(root, text="Número de elementos del primer conjunto:").grid(row=1, column=0)
entry_c1 = tk.Entry(root)
entry_c1.grid(row=1, column=1)

tk.Label(root, text="Característica del segundo conjunto:").grid(row=2, column=0)
n2 = tk.Entry(root)
n2.grid(row=2, column=1)

tk.Label(root, text="Número de elementos del segundo conjunto:").grid(row=3, column=0)
entry_c2 = tk.Entry(root)
entry_c2.grid(row=3, column=1)

tk.Label(root, text="Característica del tercer conjunto:").grid(row=4, column=0)
n3 = tk.Entry(root)
n3.grid(row=4, column=1)

tk.Label(root, text="Número de elementos del tercer conjunto:").grid(row=5, column=0)
entry_c3 = tk.Entry(root)
entry_c3.grid(row=5, column=1)

tk.Label(root, text="Número de elementos a extraer del primer conjunto:").grid(row=6, column=0)
entry_k1 = tk.Entry(root)
entry_k1.grid(row=6, column=1)

tk.Label(root, text="Número de elementos a extraer del segundo conjunto:").grid(row=7, column=0)
entry_k2 = tk.Entry(root)
entry_k2.grid(row=7, column=1)

tk.Label(root, text="Número de elementos a extraer del tercer conjunto:").grid(row=8, column=0)
entry_k3 = tk.Entry(root)
entry_k3.grid(row=8, column=1)

tk.Button(root, text="Calcular Probabilidad", command=calcular_probabilidad).grid(row=9, columnspan=2)

# Iniciar el bucle principal de la interfaz gráfica
roo t.mainloop()
