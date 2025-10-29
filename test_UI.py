import tkinter as tk
from tkinter import messagebox

# Variables globales
producto_total = 0
producto_actual = 0
gasto_total = 0
ingresos = 0

# Funciones lógicas
def agregar_inventario():
    global producto_total, producto_actual, gasto_total
    try:
        costo_unidad = float(entry_costo.get())
        cantidad = int(entry_cantidad.get())

        producto_total += cantidad
        producto_actual += cantidad
        gasto_total += costo_unidad * cantidad

        messagebox.showinfo("Inventario actualizado", 
                            f"Se agregaron {cantidad} unidades a un costo unitario de {costo_unidad:.2f}")
        actualizar_info()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")

def realizar_pedido():
    global ingresos, producto_actual, gasto_total, producto_total
    try:
        cantidad = int(entry_cantidad.get())
        margen = float(entry_margen.get())

        if margen > 1:
            margen = margen / 100

        if cantidad > producto_actual:
            messagebox.showwarning("Sin stock", "No hay suficiente producto para realizar este pedido")
        else:
            costo_venta = (gasto_total / producto_total) * (1 + margen)
            ingresos += cantidad * costo_venta
            producto_actual -= cantidad
            messagebox.showinfo("Pedido realizado", 
                                f"Se vendieron {cantidad} unidades a {costo_venta:.2f} por unidad")
            actualizar_info()
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No hay inventario inicial para calcular el costo de venta")

def actualizar_info():
    label_info.config(text=f"""
Cantidad de producto actual: {producto_actual}
Ganancias: {ingresos - gasto_total:.2f}
""")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Manejo de Inventarios")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Título
tk.Label(ventana, text="Gestión de Inventario", font=("Arial", 16, "bold")).pack(pady=10)

# Entradas
frame_inputs = tk.Frame(ventana)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Cantidad de producto:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_cantidad = tk.Entry(frame_inputs)
entry_cantidad.grid(row=0, column=1)

tk.Label(frame_inputs, text="Costo por unidad:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_costo = tk.Entry(frame_inputs)
entry_costo.grid(row=1, column=1)

tk.Label(frame_inputs, text="Margen (% o decimal):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_margen = tk.Entry(frame_inputs)
entry_margen.grid(row=2, column=1)

# Botones de acción
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Agregar Inventario", command=agregar_inventario, width=18, bg="#b3e6b3").grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="Realizar Pedido", command=realizar_pedido, width=18, bg="#add8e6").grid(row=0, column=1, padx=5, pady=5)

# Información general
label_info = tk.Label(ventana, text="", font=("Courier", 10), justify="left")
label_info.pack(pady=15)
actualizar_info()

# Botón de salida
tk.Button(ventana, text="Salir", command=ventana.destroy, width=15, bg="#ff9999").pack(pady=5)

ventana.mainloop()
