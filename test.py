"""
Programa: Manejo de inventarios
Autor: Nicolás López
Fecha: 2025-10-29

Descripción:
Este programa maneja el inventario de una empresa

Funciones principales:
- pedido(costo_unidad, cantidad_producto): calcula las ganancias obtenidas.
"""


def pedido(costo_unidad, cantidad_producto, margen):
	costo_venta = costo_unidad*(1 + margen)
	return (costo_venta - costo_unidad)  * cantidad_producto

margen = 0.3
cantidad_producto = int(input("¿Cuántas unidades del producto quieres vender?\n"))
costo_unidad = float(input("¿Cuál es el costo por unidad del producto?\n"))

ganancias = pedido(costo_unidad, cantidad_producto, margen)

print(f"Las ganancias son:{ganancias:.2f}")