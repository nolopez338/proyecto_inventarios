# test_inventario.py
import random
from unittest.mock import Mock
import inventario


def reset_globals():
    inventario.producto_total = 0
    inventario.producto_actual = 0
    inventario.gasto_total = 0
    inventario.ingresos = 0


def run_tests():
    print("\n=== PRUEBAS CONTROLADAS DE EVENTOS ===\n")

    reset_globals()

    # Reproducibilidad
    random.seed(123)

    print("--- PRUEBA EVENTO DE COMPRA CON PARÁMETROS FIJOS ---")
    # Input simulado: comprar 3 unidades
    fake_input = Mock(side_effect=["3"])
    inventario.evento_compra(
        precio_fijo=10.0,
        cantidad_fija=8,
        input_func=fake_input
    )

    print("\n--- PRUEBA EVENTO DE VENTA CON PARÁMETROS FIJOS ---")
    # Inputs simulados: ofrecer 2 unidades, precio = 9
    fake_input = Mock(side_effect=["2", "9"])
    inventario.evento_venta(
        cant_fija=5,        # comprador desea hasta 5 unidades
        precio_max_fijo=12,  # comprador acepta hasta 12
        input_func=fake_input
    )

    print("\n--- PRUEBA SECUENCIA COMPLETA CONTROLADA ---")
    fake_input = Mock(side_effect=[
        "0",   # compra: no comprar
        "4",   # venta: ofrecer 4
        "11"   # venta: precio ofrecido
    ])

    inventario.evento_compra(
        precio_fijo=7,
        cantidad_fija=5,
        input_func=fake_input
    )

    inventario.evento_venta(
        cant_fija=10,
        precio_max_fijo=15,
        input_func=fake_input
    )

    # Resumen final
    print("\n=== RESULTADOS ===")
    print(f"Total producto: {inventario.producto_total}")
    print(f"Producto actual: {inventario.producto_actual}")
    print(f"Gasto total: {inventario.gasto_total}")
    print(f"Ingresos totales: {inventario.ingresos}")
    print(f"Ganancia neta: {inventario.ingresos - inventario.gasto_total}")


if __name__ == "__main__":
    run_tests()
