"""
RESTAURANTE MOLIPOLLO - PROGRAMA PRINCIPAL
===========================================
Este es un programa que simula un restaurante.
Aquí el usuario puede ver el menú, hacer pedidos y pagar.
"""

import funciones

print("\n")
print("=" * 50)
print("   ¡BIENVENIDO AL RESTAURANTE MOLIPOLLO!")
print("=" * 50)

# Cargamos el menú del restaurante
menu = funciones.cargar_menu()

# Creamos un carrito vacío para el cliente
carrito = []

# ============================================================
# BUCLE PRINCIPAL - El programa se repite hasta que el usuario salga
# ============================================================

while True:
    
    # Mostramos el menú principal
    print("\n" + "-" * 50)
    print("            MENÚ PRINCIPAL")
    print("-" * 50)
    print("1. Ver el menú del restaurante")
    print("2. Agregar un plato al carrito")
    print("3. Ver mi carrito")
    print("4. Ver total a pagar")
    print("5. Finalizar y guardar pedido")
    print("6. Pagar")
    print("7. Vaciar carrito")
    print("0. Salir")
    print("-" * 50)
    
    opcion = input("\nEscribe el número de tu elección: ")
    
    
    # --------------------------------------------------------
    # OPCIÓN 1: Ver el menú
    # --------------------------------------------------------
    if opcion == "1":
        funciones.mostrar_menu(menu)
        input("Presiona Enter para continuar...")
    
    
    # --------------------------------------------------------
    # OPCIÓN 2: Agregar plato al carrito
    # --------------------------------------------------------
    elif opcion == "2":
        carrito = funciones.agregar_al_carrito(menu, carrito)
        
        continuar = input("\n¿Deseas agregar otro plato? (s/n): ")
        
        while continuar == "s" or continuar == "S":
            carrito = funciones.agregar_al_carrito(menu, carrito)
            continuar = input("\n¿Deseas agregar otro plato? (s/n): ")
    
    
    # --------------------------------------------------------
    # OPCIÓN 3: Ver el carrito
    # --------------------------------------------------------
    elif opcion == "3":
        funciones.mostrar_carrito(carrito)
        input("Presiona Enter para continuar...")
    
    
    # --------------------------------------------------------
    # OPCIÓN 4: Ver total a pagar
    # --------------------------------------------------------
    elif opcion == "4":
        if len(carrito) == 0:
            print("\n¡Tu carrito está vacío!")
        else:
            total = funciones.mostrar_carrito(carrito)
            
            print(f"Total a pagar: ${total :,.0f}")
        
        input("\nPresiona Enter para continuar...")
    
    
    # --------------------------------------------------------
    # OPCIÓN 5: Finalizar y guardar pedido
    # --------------------------------------------------------
    elif opcion == "5":
        if len(carrito) == 0:
            print("\n¡Tu carrito está vacío! No hay nada que guardar.")
        else:
            funciones.mostrar_carrito(carrito)
            
            confirmar = input("¿Confirmas este pedido? (s/n): ")
            
            if confirmar == "s" or confirmar == "S":
                nombre = input("Escribe tu nombre: ")
                funciones.guardar_pedido(nombre, carrito)
            else:
                print("\nPedido no guardado")
        
        input("\nPresiona Enter para continuar...")
    
    
    # --------------------------------------------------------
    # OPCIÓN 6: Pagar
    # --------------------------------------------------------
    elif opcion == "6":
        if len(carrito) == 0:
            print("\n¡Tu carrito está vacío! No hay nada que pagar.")
        else:
            # Calculamos el total
            total = funciones.calcular_total(carrito)
            
            # Mostramos resumen
            print("\n" + "=" * 50)
            print("           RESUMEN DE PAGO")
            print("=" * 50)
            funciones.mostrar_carrito(carrito)
            
            # Pedimos confirmación
            confirmar = input("¿Proceder con el pago? (s/n): ")
            
            if confirmar == "s" or confirmar == "S":
                nombre = input("Escribe tu nombre: ")
                funciones.guardar_pago(nombre, total)
                
                print("\n¡Gracias por tu compra!")
                
                vaciar = input("¿Deseas vaciar el carrito? (s/n): ")
                if vaciar == "s" or vaciar == "S":
                    carrito = funciones.vaciar_carrito()
            else:
                print("\nPago cancelado")
        
        input("\nPresiona Enter para continuar...")
    
    
    # --------------------------------------------------------
    # OPCIÓN 7: Vaciar carrito
    # --------------------------------------------------------
    elif opcion == "7":
        if len(carrito) == 0:
            print("\n¡El carrito ya está vacío!")
        else:
            funciones.mostrar_carrito(carrito)
            
            confirmar = input("¿Seguro que quieres vaciar el carrito? (s/n): ")
            
            if confirmar == "s" or confirmar == "S":
                carrito = funciones.vaciar_carrito()
            else:
                print("\nOperación cancelada")
        
        input("\nPresiona Enter para continuar...")
    
    
    # --------------------------------------------------------
    # OPCIÓN 0: Salir del programa
    # --------------------------------------------------------
    elif opcion == "0":
        # Si hay cosas en el carrito, advertimos
        if len(carrito) > 0:
            print("\n¡ATENCIÓN! Tienes platos en tu carrito.")
            funciones.mostrar_carrito(carrito)
            
            confirmar = input("¿Seguro que quieres salir sin completar el pedido? (s/n): ")
            
            if confirmar != "s" and confirmar != "S":
                continue  # Vuelve al inicio del bucle
        
        # Mensaje de despedida
        print("\n" + "=" * 50)
        print("   ¡Gracias por visitar Molipollo!")
        print("   ¡Vuelve pronto!")
        print("=" * 50 + "\n")
        break  # Sale del bucle y termina el programa
    
    
    # Si el usuario escribió algo que no es una opción válida
    else:
        print("\n Opción no válida. Por favor elige un número del 0 al 7.")
        input("Presiona Enter para continuar...")
