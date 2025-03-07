import json 
import funciones
carta = {} 
def leer_txt(menu):
    try:
        with open(menu, "r", encoding='utf-8') as archivo:
            contenido = menu.json()
        print(f"contenido del archivo {menu}: /n {contenido}")
    except FileExistsError:
        print(f"error !!! el archivo {menu} no fue encontrado")
    except IOError as e:
        print(f"ocurrio un erros inesperado en la lectura de {menu}: {e}")

def ver_menu(menu, mensaje):
    try:
        with open(menu, "w", encoding= 'utf-8') as archivo:
            archivo.write(mensaje)
        print("texto fue guardado en el archivo{nombre_archivo}")
    except IOError as e:
        print("ocurrio un error al escribir el archivo: {e}")
menu = [{
    "categoria" :  "entrada", 
    "nombre": "empanadas mini", 
    "precio":9000
},
{ 
    "categoria" :  "entrada", 
    "nombre": "aros de cebolla", 
    "precio":8000
},
{
    "categoria" :  "entrada", 
    "nombre": "papas fritas", 
    "precio":10000
},
{
    "categoria" :  "platos fuertes", 
    "nombre": "mondongo", 
    "precio":16000
},
{
    "categoria" :  "patos fuertes", 
    "nombre": "ajiaco", 
    "precio":18000
},
{
    "categoria" :  "platos fuertes", 
    "nombre": "carne asada", 
    "precio":18000
},
{
    "categoria" :  "bebida", 
    "nombre": "jugo de coco", 
    "precio":9000
},
{
    "categoria" :  "debida", 
    "nombre": "limonada", 
    "precio":9000
},
{
    "categoria" :  "debida", 
    "nombre": "juego de mango", 
    "precio":9000
}
]
while True:
    print("Bienvenido al restaurante Molipollo ")
    print("Ingrese\n1. ver carta \n2.seleccionar pedido \n3.estado del pedido \n4.total a pagar \n0. Para salir")
    opc = input("Ingrese la opción que necesita ")
    if opc == "1":
        ver_menu = (menu)
        print(ver_menu)  

    elif opc == "4":
        print("***Sus productos son***")
        total = 0
        for llave, valor in carta.items():
            print(llave, " - cantidad: ", valor, " - precio: ", menu.get(llave))
            total  += valor * menu.get(llave)
        print("El total a pagar es: ", total)

    elif opc == "0":
        print("Saliendo...")
        break
