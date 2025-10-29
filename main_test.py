# test_inventario.py
import inventario  # your main file should be named inventario.py

def run_tests():
    print("=== INICIO DE PRUEBAS DE INVENTARIO ===\n")

    # Simular varias operaciones de agregar inventario (opción 1)
    inventario.agregar_inventario(10.0, 50)   # 50 unidades a $10 c/u
    inventario.agregar_inventario(12.0, 30)   # 30 unidades a $12 c/u
    inventario.agregar_inventario(15.0, 20)   # 20 unidades a $15 c/u

    # Simular varias operaciones de venta (opción 2)
    inventario.realizar_pedido(40, 0.25)  # vender 40 unidades con margen 25%
    inventario.realizar_pedido(30, 10)    # vender 30 unidades con margen 10% (porcentaje)
    inventario.realizar_pedido(10, 0.50)  # vender 10 unidades con margen 50%

    # Mostrar resultado final
    print("\n=== RESULTADOS FINALES ===")
    print(f"Producto total inicial: {inventario.producto_total}")
    print(f"Producto restante actual: {inventario.producto_actual}")
    print(f"Gasto total: {inventario.gasto_total:.2f}")
    print(f"Ingresos totales: {inventario.ingresos:.2f}")
    print(f"Ganancia neta: {inventario.ingresos - inventario.gasto_total:.2f}")

if __name__ == "__main__":
    run_tests()
