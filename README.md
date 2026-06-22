
#herramientas

baja_rolas.py

convierte.py

## Prerequisitos:

- Instala python3 y con el gestor pip descarga:

`pip install yt-mp3`

- Extensión para descargar cookies, recomiendo:

Get cookies.txt LOCALLY

que es una extensión de chrome.

- Guarda los scripts baja_rolas.py y convierte.py en una
carpeta que identifiques facilmente (o has clone del proyecto)

##Preparando el entorno:

1. Crea una cuenta de google que no sea la personal
2. Abre el navegador con esa cuenta, e instala la extensión Get cookies.txt LOCALLY
3. Abre youtube
4. Con la extensión para descargar cookies, descárgalas en formato netscape en un texto
plano y guárdalo en la carpeta donde hayas descargado los scripts de los programas, de
preferencia con el nombre www.youtube.com.cookies.txt
5. Prepara un documento de texto plano y guarda en él varios enlaces de youtube cuyos
audios quieras descargar. Puedes hacerlo en la terminal con los siguientes comandos:
(presiona ENTER después de cada línea)

`touch mis_enlaces.txt`
`echo https://www.youtube.com/watch?v=Yv6_JMxt7wo >> mis_enlaces.txt`
`echo https://www.youtube.com/watch?v=7wfmcLxaNBo >> mis_enlaces.txt`
`echo https://www.youtube.com/watch?v=KrJAolWk0nQ >> mis_enlaces.txt`
`echo https://www.youtube.com/watch?v=fcSJ8G4f_Wo >> mis_enlaces.txt`

De este modo tendrías un archivo llamado mis_enlaces.txt con cuatro enlaces listos para
descargar. Puedes comprobarlo con el comando:

`cat mis_enlaces.txt`

Que imprimirá en pantalla los enlaces que a penas escribimos en el documento. 

##Ejecución

0. Abre una terminal linux (de preferencia Ubuntu)

1. Ejecuta el comando

`python3 baja_rolas.py`

2. El programa se abre y te pide el nombre de una carpeta
📁 Nombre de la carpeta para guardar los audios:

Si la carpeta no existe el programa la genera automáticamente.
Tras escribir el nombre de tu carpeta presiona ENTER:

Ejemplo:
📁 Nombre de la carpeta para guardar los audios: musica_nueva
ENTER

3. Ahora el programa pide que le pases el archivo con los enlaces
que creamos previamente (mira el punto 5 en la sección Preparando el entorno):

📄 Nombre del archivo con los enlaces (ej: enlaces.txt):

Ejemplo:
📄 Nombre del archivo con los enlaces (ej: enlaces.txt): mis_enlaces.txt
ENTER

4. Ahora el programa pide que confirmes la descarga:

📊 Se encontraron 5 enlaces válidos para descargar.
¿Deseas continuar con la descarga? (s/n):

Simplemente escribe  "s" y presiona ENTER.

Ejemplo:
¿Deseas continuar con la descarga? (s/n): s
ENTER

5.Una vez descargados, el programa nos pregunta si queremos convertirlos
a mp3:

📊 ¿CONVERTIR A MP3? (s/n)

Si presionas "s" el programa los conveirte a mp3. Si presionas "n" el programa termina. 

6. Finalmente el programa te pregunta si gustas eliminar los archivos con formato mka u opus:

¿Eliminamos los archivos que no son mp3?(s/n)

Nuevamente "s" confirma la limpieza de archivos duplicados con formato dstinto a mp3 y "n"
termina la ejecución del programa.

7. ¡Listo! 
