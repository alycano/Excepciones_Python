class StockInsuficienteError(Exception):
    pass

def vender_producto(cantidad):
    stock_actual = 5
    if cantidad > stock_actual:
        raise StockInsuficienteError(f"Intento de venta: {cantidad}. Stock disponible: {stock_actual}")
    print("Venta realizada con éxito.")

try:
    vender_producto(10)
except StockInsuficienteError as e:
    print(f"Error de inventario: {e}")