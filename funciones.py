import json
from datetime import datetime

def cargar_menu():
    
    archivo = open("menu.json", "r", encoding='utf-8')
    menu = json.load(archivo)
    archivo.close()
    return menu


def guardar_pedido(nombre_cliente, items_pedido):
 
    # Primero lee los pedidos que ya existen
    archivo = open("pedidos.json", "r", encoding='utf-8')
    pedidos_anteriores = json.load(archivo)
    archivo.close()
    
    # Creamos el nuevo pedido
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for item in items_pedido:
        pedido_nuevo = {
            "cliente": nombre_cliente,
            "items": item["nombre"],
            "cantidad": item["cantidad"],
            "precio": item["precio"],
            "fecha": fecha_actual
        }
        pedidos_anteriores.append(pedido_nuevo)
    
    # se guarda todo de nuevo en el archivo
    archivo = open("pedidos.json", "w", encoding='utf-8')
    json.dump(pedidos_anteriores, archivo, indent=4, ensure_ascii=False)
    archivo.close()
    
    print(f"\n✓ Pedido guardado exitosamente para {nombre_cliente}")


def guardar_pago(nombre_cliente, total):
    """
    Esta función guarda un pago en el archivo pagos.json
    
    Parámetros:
        nombre_cliente: El nombre de quien paga
        total: La cantidad de dinero que pagó
    """
    # Lee los pagos anteriores
    archivo = open("pagos.json", "r", encoding='utf-8')
    pagos_anteriores = json.load(archivo)
    archivo.close()
    
    # Crea el nuevo pago
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    pago_nuevo = {
        "cliente": nombre_cliente,
        "total": total,
        "fecha de pago": fecha_actual
    }
    
    pagos_anteriores.append(pago_nuevo)
    
    # Guarda todo de nuevo
    archivo = open("pagos.json", "w", encoding='utf-8')
    json.dump(pagos_anteriores, archivo, indent=4, ensure_ascii=False)
    archivo.close()
    
    print(f"\n✓ Pago registrado: ${total:,}")


# ============================================================
# FUNCIONES PARA MOSTRAR INFORMACIÓN EN PANTALLA
# ============================================================

def mostrar_menu(menu):

    print("\n" + "=" * 50)
    print("        MENÚ DEL RESTAURANTE MOLIPOLLO  ")
    print("=" * 50)
    
    # Muestra cada plato con su número
    for i in range(len(menu)):
        plato = menu[i]
        numero = i + 1
        nombre = plato["nombre"]
        precio = plato["precio"]
        categoria = plato["categoria"]
        
        print(f"{numero}. {nombre.title():<30} ${precio:>10,}  ({categoria})")
    
    print("=" * 50 + "\n")


def mostrar_carrito(carrito):
    
    print("\n" + "=" * 50)
    print("            TU CARRITO DE COMPRAS")
    print("=" * 50)
    
    # Si el carrito está vacío
    if len(carrito) == 0:
        print("\n¡Tu carrito está vacío!")
        print("Agrega platos desde el menú.\n")
        return
    
    # Muestra cada item del carrito
    total_general = 0
    
    print(f"\n{'PLATO':<25} {'CANTIDAD':>10} {'PRECIO':>12} {'TOTAL':>12}")
    print("-" * 60)
    
    for item in carrito:
        nombre = item["nombre"]
        cantidad = item["cantidad"]
        precio = item["precio"]
        total = cantidad * precio
        total_general = total_general + total
        
        print(f"{nombre.title():<25} {cantidad:>10} ${precio:>11,} ${total:>11,}")
    
    print("-" * 60)
    print(f"{'TOTAL A PAGAR':<25} {' ':>10} {' ':>12} ${total_general:>11,}")
    print("=" * 50 + "\n")
    
    return total_general


# ============================================================
# FUNCIONES PARA AGREGAR PLATOS AL CARRITO
# ============================================================

def agregar_al_carrito(menu, carrito):
   
    mostrar_menu(menu)
    
    # Pedimos al usuario que elija un plato
    print("¿Qué plato deseas ordenar?")
    numero = int(input("Escribe el número del plato: "))
    
    # Verificamos que el número sea válido
    if numero < 1 or numero > len(menu):
        print("\n Ese número no existe en el menú. Intenta de nuevo.")
        return carrito
    
    # Obtenemos el plato elegido
    plato_elegido = menu[numero - 1]
    
    # Pedimos la cantidad
    cantidad = int(input("¿Cuántos deseas?: "))
    
    if cantidad <= 0:
        print("\n La cantidad debe ser mayor a 0.")
        return carrito
    
    # Creamos el item para el carrito
    item_nuevo = {
        "nombre": plato_elegido["nombre"],
        "precio": plato_elegido["precio"],
        "cantidad": cantidad,
        "categoria": plato_elegido["categoria"]
    }
    
    # Agregamos al carrito
    carrito.append(item_nuevo)
    
    print(f"\n✓ {cantidad} x {plato_elegido['nombre'].title()} agregado al carrito")
    
    return carrito


# ============================================================
# FUNCIÓN PARA VACIAR EL CARRITO
# ============================================================

def vaciar_carrito():
    print("\n✓ Carrito vaciado")
    return []


# ============================================================
# FUNCIÓN PARA CALCULAR EL TOTAL
# ============================================================

def calcular_total(carrito):
    
    total = 0
    
    for item in carrito:
        precio = item["precio"]
        cantidad = item["cantidad"]
        total = total + (precio * cantidad)
    
    return total