"""
Programa: Manejo de inventarios
Autor: Nicolás López
Fecha: 2025-10-29

Descripción:
Este programa maneja el inventario de una empresa

Funciones principales:
- pedido(costo_unidad, cantidad_producto): calcula las ganancias obtenidas.
"""

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

def main():
	ejecutando = True

	while ejecutando:

		rta_usuario = int(input("""
			Que deseas realizar?
			1. Agregar inventario
			2. Realizar pedido
			3. Revisar información general
			4. Salir
			"""))

		if rta_usuario == 4:
			print("Hasta luego")
			ejecutando = False

		elif rta_usuario == 3:
			print(f"""
				Cantidad de producto actual: {producto_actual}
				Ganancias: {ingresos - gasto_total}
				""")

		elif rta_usuario == 2:
			cantidad_producto = int(input("¿Cuántas unidades del producto quieres vender?\n"))
			margen = float(input("¿Cuál es el margen que quieres obtener?\n"))
			
			realizar_pedido(cantidad_producto, margen)

		elif rta_usuario == 1:
			cantidad_producto = int(input("¿Cuántas unidades del producto quieres comprar?\n"))
			costo_unidad = float(input("¿Cuál es el costo por unidad del producto?\n"))
			agregar_inventario(costo_unidad, cantidad_producto)
		
		else:
			print("No se reconoce el comando")

if __name__ == "__main__":
    main()