#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from pathlib import Path

def convierte (carpeta_destino):

    # Generamos un arreglo con los archivos en la carpeta
    archivos = [a for a in Path(carpeta_destino).iterdir() if a.is_file()]

    #Recorremos el arreglo convirtiendo los archivos que no son mp3 a mp3
    #Para esto, obtenemos la extensión del archivo como una cadena
    for nombre_archivo in archivos:
        extension = str(nombre_archivo.suffix)
        if extension != ".mp3":
            nuevo_nombre = str(nombre_archivo.with_suffix(".mp3"))
            cmd = ["ffmpeg", "-i", str(nombre_archivo), "-b:a", "320k", nuevo_nombre]
            print(f"LOG: Ejecutaremos el comando {cmd}")
            try:
                print(f"cnvirtiendo {str(nombre_archivo)} en mp3")
                resultado = subprocess.run(cmd, capture_output=True, text=True, check=False)
                if resultado.returncode != 0:
                    print(f"Error al convertir {str(nombre_archivo)}")
                          
            except Exception as e:
                print(f" Error inesperado: {e}")
                return False
    print("Conversión exitosa")

    eliminar = input("¿Eliminamos los archivos que no son mp3?(s/n)").strip().lower()
    if eliminar == 's':
        comando = f"find {carpeta_destino}/ -maxdepth 1 -type f ! -name *.mp3"
        print(f"LOG: Ejecutamos el comando {comando}")
    try:
        print("Eliminaremos los siguientes archivos:")
        resultado2 = subprocess.run(comando.split(), capture_output = True, text = True)
        if resultado2.returncode == 0:
            print(resultado2.stdout)
        else:
            print("Error inesperado al enlistar los archivos")
        respuesta = input("Confirmar? (s/n)").strip().lower()
        if respuesta == 's':
            resultado3 = subprocess.run(comando.split()+["-delete"], capture_output = True, text = True)
            
            if resultado3.returncode == 0:
                print("Limpieza exitosa")
            else:
                print(f"Error inesperado al eliminar archivos: {resultado3.stderr}")
        else:
            print("Vale, no eliminaremos nada")
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False
    return True

def main():
    while True:
        carpeta = input("¿Qué carpeta de archivos vamos a convertir?")
        if carpeta:
            break
        else:
            print("Escribe un nombre de carpeta válido.")
    convierte(carpeta)
    print("Gracias por usar este software")                         
                
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️Proceso interrumpido por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n Error inesperado: {e}")
        sys.exit(1)
