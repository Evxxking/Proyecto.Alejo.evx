import os
from moviepy import VideoFileClip

def menu():
    print("1: Cambiar extension de archivo mp3 a mp4")
    print("2: Cambiar extension de archivo mp4")
    print("3: Cambiar calidad de video")
    print("4: salir")

while True:
    menu()
    opcion = int(input("Elije una opcion: "))
    if opcion == 1:
        ruta_usuario = input("Seleccione la ruta del archivo mp3: ")
        if os.path.exists(ruta_usuario):
            nombre_base, extension = os.path.splitext(ruta_usuario)
            extension = extension.lower()
            ruta = os.path.dirname(ruta_usuario)
        else:
            print("Ruta no valida")
            continue
        if extension == ".mp3":
            nombre_nuevo = input("Seleccione el nombre para el archivo: ")
            os.rename(ruta_usuario, os.path.join(ruta, nombre_nuevo + ".mp4"))
    elif opcion == 2:
        ruta_usuario = input("Seleccione la ruta del archivo mp4: ")
        if os.path.exists(ruta_usuario):
            nombre_base, extension = os.path.splitext(ruta_usuario)
            extension = extension.lower()
            ruta = os.path.dirname(ruta_usuario)
            
            if extension == ".mp4":
                nombre_nuevo = input("Seleccione el nombre para el archivo de audio: ")
                ruta_salida = os.path.join(ruta, nombre_nuevo + ".mp3")
                
                print("Extrayendo audio... por favor espera.")
                video = VideoFileClip(ruta_usuario)
                video.audio.write_audiofile(ruta_salida)
                video.close()
                print("¡Convertido a MP3 real con éxito!")
            else:
                print("El archivo no es .mp4")
        else:
            print("Ruta no valida")
    elif opcion == 3:
        ruta_usuario = input("Seleccione la ruta del video: ")
        if os.path.exists(ruta_usuario):
            clip = VideoFileClip(ruta_usuario)
            ruta = os.path.dirname(ruta_usuario)
            
            print("\n--- Seleccione Calidad ---")
            print("1: 720p")
            print("2: 1080p")
            print("3: 2k")
            calidad = input("Elija resolución: ")
            
            nombre_nuevo = input("Nombre para el nuevo archivo: ")
            ruta_salida = os.path.join(ruta, nombre_nuevo + ".mp4")

            if calidad == "1":
                nuevo_clip = clip.resized(height=720)
            elif calidad == "2":
                nuevo_clip = clip.resized(height=1080)
            elif calidad == "3":
                nuevo_clip = clip.resized(height=1440)
            else:
                print("Opción no válida, usando original.")
                nuevo_clip = clip

            print("Procesando video... esto tardará dependiendo de tu PC.")
            nuevo_clip.write_videofile(ruta_salida, codec="libx264")
            
            clip.close()
            nuevo_clip.close()
            print("¡Video procesado con éxito!")

    elif opcion == 4:
        print("Fin del programa")
        break
    else:
        print("opcion no valida")