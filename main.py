import tkinter as tk

class DibujoCuadrado:
    def __init__(self, lado: int):
        self.lado = lado

    def dibujar(self, canvas: tk.Canvas):
        canvas.delete("all")  # Limpiar el canvas antes de dibujar
        x0, y0 = 50, 50  # Coordenadas de la esquina superior izquierda
        x1, y1 = x0 + self.lado, y0 + self.lado  # Coordenadas de la esquina inferior derecha
        canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="blue")

# Función para manejar la lógica de la interfaz
def dibujar_cuadrado():
    try:
        lado = int(entry_lado.get())
        if lado <= 0:
            raise ValueError("La longitud del lado debe ser un número positivo.")
        dibujo = DibujoCuadrado(lado)
        dibujo.dibujar(canvas)
    except ValueError as e:
        tk.messagebox.showerror("Entrada inválida", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Dibujo de un Cuadrado")

# Crear y colocar los widgets
label_lado = tk.Label(root, text="Longitud del lado:")
label_lado.grid(row=0, column=0, padx=10, pady=10)

entry_lado = tk.Entry(root)
entry_lado.grid(row=0, column=1, padx=10, pady=10)

button_dibujar = tk.Button(root, text="Dibujar Cuadrado", command=dibujar_cuadrado)
button_dibujar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Crear un canvas donde se dibujará el cuadrado
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()

