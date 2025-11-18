"""
Programa: Manejo de inventarios
Autor: Nicolás López
Fecha: 2025-10-29

Descripción:
Este programa maneja el inventario de una empresa

Funciones principales:
- pedido(costo_unidad, cantidad_producto): calcula las ganancias obtenidas.
"""

import random

producto_total = 0 
gasto_total = 0

producto_actual = 0

ingresos = 0

def agregar_inventario(costo_unidad, cantidad_producto):
	global producto_total, producto_actual, gasto_total

	# Actualizar información
	producto_total += cantidad_producto
	producto_actual += cantidad_producto
	gasto_total += costo_unidad * cantidad_producto
	print(f"Se agregaron {cantidad_producto} unidades a un costo unitario de {costo_unidad:.2f}")

def realizar_pedido(cantidad_producto, margen):
	global ingresos, producto_actual, gasto_total, producto_total

	if margen > 1: margen = margen / 100

	if cantidad_producto > producto_actual:
		print("No hay suficiente producto para realizar este pedido")
	else:
		costo_venta = (gasto_total/producto_total)*(1 + margen)

		# Actualizar información
		ingresos += cantidad_producto * costo_venta
		producto_actual -= cantidad_producto

		print(f"Se realiza un pedido de {cantidad_producto} productos a un precio de {costo_venta} por unidad")

# def mes():
	

	
def evento_compra(precio_fijo=None, cantidad_fija=None, input_func=input):
    """Evento de compra con parámetros controlables para pruebas."""
    global producto_actual, producto_total, gasto_total

    print("\n--- EVENTO DE COMPRA ---")

    # Usar parámetros fijos si existen (tests), o random si no
    precio_producto = precio_fijo if precio_fijo is not None else round(random.uniform(5, 30), 2)
    cantidad_disponible = cantidad_fija if cantidad_fija is not None else random.randint(5, 20)

    print(f"Producto disponible por {precio_producto:.2f} la unidad. Cantidad disponible: {cantidad_disponible}")

    cantidad_a_comprar = int(input_func("¿Cuántas unidades deseas comprar? (0 para no comprar)\n"))

    if cantidad_a_comprar > cantidad_disponible:
        print("No puedes comprar más de la cantidad disponible.")
        return

    if cantidad_a_comprar > 0:
        agregar_inventario(precio_producto, cantidad_a_comprar)
    else:
        print("Decidiste no comprar.")


def evento_venta(cant_fija=None, precio_max_fijo=None, input_func=input):
    """Evento de venta con parámetros controlables para pruebas."""
    global ingresos, producto_actual

    print("\n--- EVENTO DE VENTA ---")

    cantidad_deseada = cant_fija if cant_fija is not None else random.randint(5, 20)
    precio_maximo = precio_max_fijo if precio_max_fijo is not None else round(random.uniform(10, 50), 2)

    print(f"Un comprador desea comprar hasta {cantidad_deseada} unidades.")

    cantidad_ofrecida = int(input_func("¿Cuántas unidades deseas ofrecer?\n"))
    if cantidad_ofrecida > cantidad_deseada:
        print("El comprador no quiere tantas unidades.")
        return

    precio_ofrecido = float(input_func("¿A qué precio por unidad las ofreces?\n"))

    if precio_ofrecido <= precio_maximo:
        if cantidad_ofrecida <= producto_actual:
            ingresos += cantidad_ofrecida * precio_ofrecido
            producto_actual -= cantidad_ofrecida
            print(f"Venta realizada. El comprador aceptó tu oferta a {precio_ofrecido:.2f} por unidad.")
        else:
            print("No tienes suficientes productos para completar la venta.")
    else:
        print("El comprador rechazó tu oferta. Precio demasiado alto.")


def ejecutar_evento():
    """Selecciona y ejecuta al azar un evento de compra o venta"""
    tipo_evento = random.choice(["compra", "venta"])
    if tipo_evento == "compra":
        evento_compra()
    else:
        evento_venta()

def main():
	ejecutando = True
	print("\nBienvenido al sistema de inventarios.\n")

	while ejecutando:
		ejecutar_evento()

		rta_usuario = int(input("""
			Que deseas realizar?
			1. Revisar información general
			0. Salir
			"""))

		if rta_usuario == 0:
			print("Hasta luego")
			ejecutando = False

		elif rta_usuario == 1:
			print(f"""
				Cantidad de producto actual: {producto_actual}
				Ganancias: {ingresos - gasto_total}
				""")
		elif rta_usuario == 2:
			continue
		else:
			print("No se reconoce el comando")

if __name__ == "__main__":
    main()