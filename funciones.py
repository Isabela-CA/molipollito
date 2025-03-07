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

        

