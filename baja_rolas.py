#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
from convierte import convierte
import sys
from pathlib import Path

def limpiar_url(url):
    """Elimina espacios en blanco y saltos de línea de una URL"""
    return url.strip()

def leer_enlaces(archivo_enlaces):
    """Lee el archivo y devuelve una lista de URLs válidas"""
    enlaces = []
    try:
        with open(archivo_enlaces, 'r', encoding='utf-8') as f:
            for linea in f:
                url = limpiar_url(linea)
                # Ignorar líneas vacías o que no sean de YouTube
                if url and ('youtube.com' in url or 'youtu.be' in url):
                    enlaces.append(url)
                    print(f" Enlace cargado: {url}")
                elif url:
                    print(f"⚠️Enlace ignorado (no parece ser de YouTube): {url}")
        
        if not enlaces:
            print(" No se encontraron enlaces válidos de YouTube en el archivo.")
            return None
        return enlaces
    except FileNotFoundError:
        print(f" No se encontró el archivo: {archivo_enlaces}")
        return None
    except Exception as e:
        print(f" Error al leer el archivo: {e}")
        return None


def descargar_audio(url, carpeta_destino, archivo_cookies="www.youtube.com.cookies.txt"):
    """Descarga el audio de una URL usando yt-dlp"""
    
    # Comando base de yt-dlp
    cmd = [
       "yt-dlp",
        "-x",  # Extraer audio
        "--cookies", archivo_cookies,
      #  "--remote-components", "ejs:github",
        "-o", f"{carpeta_destino}/%(title)s.%(ext)s",  # Formato de salida
        url
    ]

    
        
    try:
        print(f"\n🎵 Descargando: {url}")
        print(f" Destino: {carpeta_destino}")
        
        # Ejecutar el comando
        resultado = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if resultado.returncode == 0:
            print(f" Descarga completada exitosamente")
            return True
        else:
            print(f" Error en la descarga:")
            print(resultado.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ No se encontró 'yt-dlp'. ¿Está instalado?")
        print("   Instálalo con: pip install yt-dlp")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def main():
    """Función principal del script"""
    
    print("🍄🍄🍄 === DESCARGA DE ROLAS DEL CLUB CATÁSTROFE === 🍄🍄🍄\n")
    
    # 1. Pedir la carpeta de destino
    while True:
        carpeta = input("📁 Nombre de la carpeta para guardar los audios: ").strip()
        if carpeta:
            break
        print("⚠️ Por favor, ingresa un nombre de carpeta válido.")
    
    # Crear la carpeta si no existe
    Path(carpeta).mkdir(parents=True, exist_ok=True)
    print(f"✅ Carpeta creada/verificada: {carpeta}\n")
    
    # 2. Pedir el archivo de enlaces
    while True:
        archivo_enlaces = input("📄 Nombre del archivo con los enlaces (ej: enlaces.txt): ").strip()
        if archivo_enlaces:
            break
        print("⚠️ Por favor, ingresa un nombre de archivo válido.")
    
    # 3. Leer los enlaces
    print(f"\n📖 Leyendo archivo: {archivo_enlaces}")
    enlaces = leer_enlaces(archivo_enlaces)
    
    if not enlaces:
        print("❌ No se pudieron cargar los enlaces. Saliendo...")
        sys.exit(1)
    
    # 4. Confirmar la descarga
    print(f"\n📊 Se encontraron {len(enlaces)} enlaces válidos para descargar.")
    respuesta = input("¿Deseas continuar con la descarga? (s/n): ").strip().lower()
    
    if respuesta != 's':
        print("❌ Descarga cancelada por el usuario.")
        sys.exit(0)

    # 5. Descargar cada enlace
    print("\n🎬 INICIANDO DESCARGAS...\n")
    exitosos = 0
    fallidos = []
    
    for i, url in enumerate(enlaces, 1):
        print(f"\n{'='*60}")
        print(f"📥 Procesando {i} de {len(enlaces)}")
        print(f"{'='*60}")
        
        if descargar_audio(url, carpeta):
            exitosos += 1
        else:
            fallidos.append(url)

    # 5.5 Preguntar si convertir los audios a mp3:
    print("\n" + "="*60)
    convertir = input("📊 ¿CONVERTIR A MP3? (s/n)").strip().lower()
    
    if convertir == 's':
        print("Convirtiendo archivos a mp3...\n")
        convierte(carpeta)
        
    print("="*60)
    # 6. Mostrar resumen final
    print("\n" + "="*60)
    print("📊 RESUMEN FINAL")
    print("="*60)
    print(f"✅ Descargas exitosas: {exitosos}/{len(enlaces)}")
    
    if fallidos:
        print(f"❌ Descargas fallidas: {len(fallidos)}")
        print("\nEnlaces con problemas:")
        for url in fallidos:
            print(f"  - {url}")
    else:
        print("🎉 ¡Todas las descargas fueron exitosas!")
    
    print(f"\n📁 Los audios se guardaron en: {os.path.abspath(carpeta)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Proceso interrumpido por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
