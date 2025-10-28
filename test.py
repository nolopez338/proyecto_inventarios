


def pedido(costo_unidad, cantidad_producto):
	costo_venta = costo_unidad*1.3
	return (costo_venta - costo_unidad)  * cantidad_producto


cantidad_producto = int(input("Cuanto producto quieres"))


print(f"Las ganancias son:{pedido(5000, cantidad_producto)}")