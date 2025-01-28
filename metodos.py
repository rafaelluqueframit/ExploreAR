import cv2
import numpy as np 
import os
import face_recognition
from gtts import gTTS
import tempfile
import speech_recognition as sr
import glob
import random
from pydub.playback import play
import pygame
from pygame import mixer
from PIL import ImageFont, ImageDraw, Image
from pyzbar.pyzbar import decode
import io
import time
import json
from usuario import Usuario

ventana_ancho = 1100
ventana_alto = 900

def calcular_descriptores():
    # Crear el objeto SIFT
    sift = cv2.SIFT_create()

    # Obtener la lista de archivos .jpg en la carpeta "./img/"
    lista_archivos = glob.glob("./img/*.jpg")

    # Inicializar lista para almacenar los descriptores
    descriptores = []

    # Procesar cada imagen y calcular sus descriptores
    for archivo in lista_archivos:
        # Leer la imagen
        imagen_referencia = cv2.imread(archivo)
        gris_referencia = cv2.cvtColor(imagen_referencia, cv2.COLOR_BGR2GRAY)

        # Calcular keypoints y descriptores
        kp_referencia, des_referencia = sift.detectAndCompute(gris_referencia, None)

        # Agregar descriptores a la lista
        descriptores.append(des_referencia)

    return descriptores


def ComprobarRegistro():
     
    resultado = False
    nombre = ''

    # Cargar las características de las caras de los usuarios desde los archivos JSON
    caracteristicas_caras = []
    nombres_clientes = []

    for nombre_archivo in os.listdir('datos/'):
        ruta = os.path.join('datos/', nombre_archivo)
        if nombre_archivo.endswith('.json'):
            usuario = Usuario.cargar_datos(ruta)
            caracteristicas_cara = usuario.caracteristicas_cara
            if caracteristicas_cara:
                caracteristicas_caras.append(np.array(caracteristicas_cara))
                nombres_clientes.append(usuario.nombre)

    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    # Configurar el tamaño de la ventana de la cámara
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        # Leemos fotogramas
        ret, frame = cap.read()
        if ret == False: break
        
        face_locations = face_recognition.face_locations(frame)
        if face_locations != []:
            for face_location in face_locations:
                    face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
                    for i in range(len(caracteristicas_caras)):
                        result = face_recognition.compare_faces([face_frame_encodings], caracteristicas_caras[i])

                        if result[0] == True:
                            resultado = True
                            nombre = nombres_clientes[i]
                            color = (0, 255, 0)  # Cambiar color a verde
                            break
                        else:
                            resultado = False
                            nombre = "Desconocido"
                            color = (0, 0, 255)  # Cambiar color a rojo

                    # Dibujar recuadro con sombra
                    shadow_offset = 5  # Desplazamiento para la sombra
                    shadow_color = (0, 0, 0)  # Color de la sombra
                    cv2.rectangle(frame, (face_location[3] + shadow_offset, face_location[2] + shadow_offset), (face_location[1] + shadow_offset, face_location[2] + 30 + shadow_offset), shadow_color, -1)
                    cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2]+30), color, -1)
                    cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
                    cv2.putText(frame, nombre, (face_location[3]+2, face_location[2]+22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, shadow_color, 2, cv2.LINE_AA)  # Añadir sombra al texto
                    cv2.putText(frame, nombre, (face_location[3], face_location[2]+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 1, cv2.LINE_AA)

        # Agregar mensaje de presionar 'q' para salir
        cv2.putText(frame, "Presiona 'q' para salir", (50, frame.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Comprobacion Registro Facial", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    # Liberar los recursos
    cap.release()
    cv2.destroyAllWindows()

    return resultado, nombre

# Comprobar Registro Facial (Cada 150 frames o 7 segundos, va fluido pero no aparece recuadro rojo o verde)
# def ComprobarRegistro():
#     resultado = False
#     nombre = ''

#     # Cargar las imágenes almacenadas en el programa
#     imagenes_almacenadas = []
#     nombres_clientes = []
#     face_image_encodings = []

#     for nombre_archivo in os.listdir('registrados/'):
#         ruta = os.path.join('registrados/', nombre_archivo)
#         imagen = cv2.imread(ruta)
#         if imagen is not None:
#             face_loc = face_recognition.face_locations(imagen)[0]
#             face_image_encodings.append(face_recognition.face_encodings(imagen, known_face_locations=[face_loc])[0])
#             imagenes_almacenadas.append(imagen)
#             nombres_clientes.append(nombre_archivo[:-5])


#     # Inicializar la cámara
#     cap = cv2.VideoCapture(0)

#     # Configurar el tamaño de la ventana de la cámara
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#     frame_count = 0
#     last_comparison_time = time.time()
#     while True:
#         # Leemos fotogramas
#         ret, frame = cap.read()
#         if ret == False:
#             break

#         # Incrementar el contador de fotogramas
#         frame_count += 1

#         # Comparar solo después de un cierto número de fotogramas o un cierto intervalo de tiempo
#         if frame_count >= 150 or time.time() - last_comparison_time >= 6:
#             face_locations = face_recognition.face_locations(frame)
#             if face_locations != []:
#                 for face_location in face_locations:
#                     face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
#                     for i in range(len(imagenes_almacenadas)):
#                         result = face_recognition.compare_faces([face_frame_encodings], face_image_encodings[i])

#                         if result[0] == True:
#                             resultado = True
#                             nombre = nombres_clientes[i]
#                             color = (0, 255, 0)  # Cambiar color a verde
#                             break
#                         else:
#                             nombre = "Desconocido"
#                             resultado = False
#                             color = (0, 0, 255)  # Cambiar color a rojo

#                     # Dibujar recuadro con sombra
#                     shadow_offset = 5  # Desplazamiento para la sombra
#                     shadow_color = (0, 0, 0)  # Color de la sombra
#                     shadow_thickness = 2  # Grosor de la sombra
#                     cv2.rectangle(frame, (face_location[3] + shadow_offset, face_location[2] + shadow_offset), (face_location[1] + shadow_offset, face_location[2] + 30 + shadow_offset), shadow_color, -1)
#                     cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2]+30), color, -1)
#                     cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
#                     cv2.putText(frame, nombre, (face_location[3]+2, face_location[2]+22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, shadow_color, 2, cv2.LINE_AA)  # Añadir sombra al texto
#                     cv2.putText(frame, nombre, (face_location[3], face_location[2]+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 1, cv2.LINE_AA)

#             # Restablecer el contador de fotogramas y actualizar el tiempo de la última comparación
#             frame_count = 0
#             last_comparison_time = time.time()

#         # Agregar mensaje de presionar 'q' para salir
#         cv2.putText(frame, "Presiona 'q' para salir", (50, frame.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
#         cv2.imshow("Comprobacion Registro Facial", frame)

#         # Salir si se presiona 'q'
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
            
#     # Liberar los recursos
#     cap.release()
#     cv2.destroyAllWindows()

#     return resultado, nombre


# Reproducir cadena de caracteres
######################## CON NUMERO RANDOM ######################
def ReproducirVoz(texto):
    # Generar un número aleatorio del 0 al 3000
    numero_aleatorio = random.randint(0, 3000)
    
    # Crear un objeto gTTS con el texto proporcionado
    tts = gTTS(text=texto, lang='es')

    # Crear un archivo temporal para almacenar el audio
    nombre_archivo = "audio_temporal_{}.mp3".format(numero_aleatorio)
    ruta_temporal = os.path.join(tempfile.gettempdir(), nombre_archivo)
    with open(ruta_temporal, "wb") as archivo_temporal:
        tts.write_to_fp(archivo_temporal)

    # Inicializar pygame
    pygame.init()

    # Reproducir el audio utilizando pygame
    pygame.mixer.music.load(ruta_temporal)
    pygame.mixer.music.play()

    # Esperar a que termine de reproducirse
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# Reconocimiento de voz
def ReconocerVoz():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source, timeout=8)

    texto = ""
    try:
        texto = r.recognize_google(audio, language="es-ES")
        print("Texto reconocido:", texto)
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError as e:
        print("Error en la solicitud del reconocimiento de voz:", e)

    return texto

################################################################################

# Registro con Reconocimiento Facial
def RegistroFacial(nombre):
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)
    # Configurar el tamaño de la ventana de la cámara
    ventana_ancho = 640
    ventana_alto = 480
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ventana_ancho)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ventana_alto)

    ruta_foto = ''
    face_encodings = None  # Vector para almacenar las características de la cara

    # Ruta de la carpeta para guardar las imágenes
    carpeta_registrados = "./registrados/"
    # Crear la carpeta si no existe
    if not os.path.exists(carpeta_registrados):
        os.makedirs(carpeta_registrados)

    while True:
        # Leemos fotogramas
        ret, frame = cap.read()
        if not ret:
            break

        # Corregimos el color
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detectamos rostros en la imagen
        face_locations = face_recognition.face_locations(rgb)
        
        # Si se detecta al menos un rostro, calculamos sus características
        if face_locations:
            face_encodings = face_recognition.face_encodings(rgb, face_locations)[0]

        #Dibujar rectángulos alrededor de los rostros detectados
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Agregar mensaje de presionar 'q' para salir
        cv2.putText(frame, "Presiona 'q' para salir", (50, frame.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Reconocimiento Facial", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Guardar la imagen de la cara detectada
            ruta_imagen = os.path.join(carpeta_registrados, nombre + ".webp")
            cv2.imwrite(ruta_imagen, frame)
            ruta_foto = ruta_imagen
            break

    cap.release()
    cv2.destroyAllWindows()
    
    return ruta_foto, face_encodings



####################################################################
def ReconocimientoMonumento():
    # Crear el objeto SIFT
    sift = cv2.SIFT_create()
    bf_matcher = cv2.BFMatcher()

    # Obtener la lista de archivos .json en la carpeta "./monumentos/"
    lista_json = glob.glob("./monumentos/*.json")

    # Leer los descriptores de los archivos JSON
    descriptores_referencia = []
    for archivo_json in lista_json:
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
        descriptores_referencia.append(datos["caracteristicas_monu"])

    # Inicializar la cámara
    cap = cv2.VideoCapture(0)
    # Configurar el tamaño de la ventana de la cámara
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ventana_ancho)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ventana_alto)

    font = cv2.FONT_HERSHEY_SIMPLEX
    threshold = 0.01

    nombre_monumento = ''

    while True:
        # Leer el siguiente frame de la cámara
        ret, frame = cap.read()

        # Convertir el frame a escala de grises
        gris_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar keypoints y calcular descriptores del frame actual
        kp_frame, des_frame = sift.detectAndCompute(gris_frame, None)

        max_coincidencias = 0
        indice_coincidente = None
        des_coincidente = None

        if des_frame is not None:
            # Realizar la comparación entre descriptores con todas las imágenes de referencia
            for i, des_referencia in enumerate(descriptores_referencia):
                des_referencia = np.array(des_referencia)
                if des_referencia is not None:
                    des_referencia = des_referencia.astype(des_frame.dtype)  # Asegurar el mismo tipo de datos
                    coincidencias = bf_matcher.knnMatch(des_referencia, des_frame, k=2)

                    good = []
                    for m, n in coincidencias:
                        if m.distance < 0.7 * n.distance:
                            good.append(m)

                    # Obtener la máxima cantidad de coincidencias
                    if len(good) > max_coincidencias:
                        max_coincidencias = len(good)
                        indice_coincidente = i
                        des_coincidente = des_referencia

        # Calcular el porcentaje de coincidencia
        if des_coincidente is not None:
            coincidencia_pct = max_coincidencias / len(des_coincidente)
        else:
            coincidencia_pct = 0

        # Mostrar el nombre de la imagen de referencia si se supera el umbral de coincidencia
        if coincidencia_pct > threshold:
            nombre_monumento = os.path.basename(lista_json[indice_coincidente])[:-5]  # Eliminar la extensión .json
            cv2.putText(frame, nombre_monumento, (65, 50), font, 1, (0, 255, 0), 2)

        # Agregar mensaje de presionar 'q' para salir
        cv2.putText(frame, "Presiona 'q' para salir", (50, frame.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        # Mostrar el frame con las coincidencias
        cv2.imshow("Reconocimiento de Imagen", frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar los recursos
    cap.release()
    cv2.destroyAllWindows()

    return nombre_monumento



# Reconocimiento de Monumentos cada 30 frames (no aparece el nombre del monumento)
# def ReconocimientoMonumento():

#     nombre_imagen_referencia = ""
#     contador_frames = 0  # Contador para llevar el seguimiento de los frames procesados

#     # Crear el objeto SIFT
#     sift = cv2.SIFT.create()
#     bf_matcher = cv2.BFMatcher()

#     # Obtener la lista de archivos .jpg en la carpeta "img/"
#     lista_archivos = glob.glob("img/*.jpg")

#     # Leer las imágenes de referencia y calcular sus descriptores
#     imagenes_referencia = []
#     descriptores_referencia = []
#     for archivo in lista_archivos:
#         imagen_referencia = cv2.imread(archivo)
#         gris_referencia = cv2.cvtColor(imagen_referencia, cv2.COLOR_BGR2GRAY)
#         kp_referencia, des_referencia = sift.detectAndCompute(gris_referencia, None)
#         imagenes_referencia.append(imagen_referencia)
#         descriptores_referencia.append(des_referencia)

#     # Inicializar la cámara
#     cap = cv2.VideoCapture(0)
#     # Configurar el tamaño de la ventana de la cámara
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, ventana_ancho)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ventana_alto)

#     font = cv2.FONT_HERSHEY_SIMPLEX
#     threshold = 0.01

#     while True:
#         # Leer el siguiente frame de la cámara
#         ret, frame = cap.read()

#         # Incrementar el contador de frames
#         contador_frames += 1

#         # Realizar la comparación cada 20 frames
#         if contador_frames % 30 == 0:
#             # Resetear el contador de frames
#             contador_frames = 0

#             # Convertir el frame a escala de grises
#             gris_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#             # Detectar keypoints y calcular descriptores del frame actual
#             kp_frame, des_frame = sift.detectAndCompute(gris_frame, None)

#             max_coincidencias = 0
#             indice_coincidente = None
#             des_coincidente = None

#             if des_frame is not None:
#                 # Realizar la comparación entre descriptores con todas las imágenes de referencia
#                 for i in range(len(imagenes_referencia)):
#                     des_referencia = descriptores_referencia[i]
#                     if des_referencia is not None:
#                         des_referencia = des_referencia.astype(des_frame.dtype)  # Asegurar el mismo tipo de datos
#                         coincidencias = bf_matcher.knnMatch(des_referencia, des_frame, k=2)
#                         good = []
#                         for m, n in coincidencias:
#                             if m.distance < 0.7 * n.distance:
#                                 good.append(m)

#                         # Obtener la máxima cantidad de coincidencias
#                         if len(good) > max_coincidencias:
#                             max_coincidencias = len(good)
#                             indice_coincidente = i
#                             des_coincidente = des_referencia

#             # Calcular el porcentaje de coincidencia
#             if des_coincidente is not None:
#                 coincidencia_pct = max_coincidencias / len(des_coincidente)
#             else:
#                 coincidencia_pct = 0

#             # Mostrar el nombre de la imagen de referencia si se supera el umbral de coincidencia
#             if coincidencia_pct > threshold:
#                 nombre_archivo_referencia = os.path.basename(lista_archivos[indice_coincidente])
#                 nombre_imagen_referencia = nombre_archivo_referencia[:-6]  # Eliminar los últimos 6 caracteres (los dos dígitos y el .jpg)
#                 cv2.putText(frame, nombre_imagen_referencia, (65, 50), font, 1, (0, 255, 0), 2)

#         # Agregar mensaje de presionar 'q' para salir
#         cv2.putText(frame, "Presiona 'q' para salir", (50, frame.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
#         # Mostrar el frame con las coincidencias
#         cv2.imshow("Reconocimiento de Imagen", frame)

#         # Salir del bucle si se presiona la tecla 'q'
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Liberar los recursos
#     cap.release()
#     cv2.destroyAllWindows()

#     return nombre_imagen_referencia

# Devuelve informacion sobre el monumento identificado""
def ObtenerInformacion(monumento):
    informacion = ""

    # Ruta al archivo JSON del monumento
    ruta_json = f"./monumentos/{monumento}.json"

    # Verificar si el archivo JSON existe
    if os.path.exists(ruta_json):
        # Leer la información del archivo JSON
        with open(ruta_json, 'r') as file:
            datos = json.load(file)
            informacion = datos.get("info")
    else:
        informacion = "Lo siento, no se encontró información para este monumento."

    print(informacion)
    MostrarInformacionEnCamara(informacion)

    return informacion
    
    
# Función para mostrar información en la cámara
def MostrarInformacionEnCamara(informacion):
    # Reproducir el audio una vez al inicio
    ReproducirVozMonumentos1(informacion)

    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    # Configurar el tamaño del texto y otros parámetros
    fuente_path = "./Georgia.ttf"  # Ruta al archivo de fuente TrueType (puedes cambiarla según la fuente que desees)
    fuente_tamano = 20
    fuente = ImageFont.truetype(fuente_path, fuente_tamano)
    color_texto_blanco = (255, 255, 255)  # Color blanco
    color_texto_negro = (0, 0, 0)  # Color negro

    # Dividir el texto en líneas para ajustarlo en la pantalla
    lineas_texto = [informacion[i:i+70] for i in range(0, len(informacion), 70)]

    # Inicializar índice para rastrear la línea actual
    indice_linea = 0

    # Configurar el tamaño de la ventana de la cámara
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ventana_ancho)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ventana_alto)

    while True:
        # Leer el siguiente frame de la cámara
        ret, frame = cap.read()

        # Convertir el frame a formato RGB (Pillow utiliza este formato)
        frame_pillow = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imagen_pillow = Image.fromarray(frame_pillow)

        # Crear un objeto ImageDraw para dibujar el texto
        draw = ImageDraw.Draw(imagen_pillow)

        # Mostrar el texto en el frame
        if indice_linea < len(lineas_texto):
            y = 40 + indice_linea * 30
            # Dibujar el texto en negro ligeramente desplazado hacia abajo y a la derecha
            draw.text((21, y + 1), lineas_texto[indice_linea], font=fuente, fill=color_texto_negro)
            # Dibujar el texto en blanco ligeramente desplazado hacia arriba y a la izquierda
            draw.text((20, y), lineas_texto[indice_linea], font=fuente, fill=color_texto_blanco)

        # Convertir la imagen de nuevo a formato BGR (OpenCV)
        frame_pillow = cv2.cvtColor(np.array(imagen_pillow), cv2.COLOR_RGB2BGR)

        # Mostrar el frame con la información del monumento
        cv2.imshow("Informacion Monumento", frame_pillow)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q') or indice_linea >= len(lineas_texto):
            break
        
        # Incrementar el índice de la línea después de un retraso
        time.sleep(5.0)  # Ajusta el valor de retraso según lo desees
        indice_linea += 1

    # Liberar los recursos
    cap.release()
    cv2.destroyAllWindows()

    # Detener la reproducción de voz
    mixer.music.stop()


def ReproducirVozMonumentos1(informacion):
    # Configurar texto a voz
    tts = gTTS(text=informacion, lang='es')
    tts.save("informacion.mp3")

    # Reproducir audio
    mixer.init()
    mixer.music.load("informacion.mp3")
    mixer.music.play()

# Variable para controlar si se está reproduciendo audio
reproduciendo_audio = False

def ReproducirVozMonumentos(informacion):
    global reproduciendo_audio
    # Inicializar Pygame Mixer si no se ha inicializado
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Generar el audio en memoria
    with io.BytesIO() as f:
        tts = gTTS(text=informacion, lang='es')
        tts.write_to_fp(f)
        f.seek(0)

        # Reproducir el audio desde la memoria
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()

        # Marcar que se está reproduciendo audio
        reproduciendo_audio = True

        # Esperar hasta que termine la reproducción del audio
        while pygame.mixer.music.get_busy():
            pass

        # Marcar que la reproducción del audio ha terminado
        reproduciendo_audio = False

######################################################################################


# Superpone un mapa de Málaga sobre un marcador de Aruco
def ObtenerMapa(respuesta):
    global reproduciendo_audio

    # Crear un objeto de parámetros del detector
    parametros = cv2.aruco.DetectorParameters()

    # Ajustar los parámetros para mejorar la detección en diferentes condiciones de iluminación
    parametros.adaptiveThreshWinSizeMin = 3
    parametros.adaptiveThreshWinSizeMax = 30

    # Definir el diccionario de ArUco
    diccionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_100)

    cap = cv2.VideoCapture(0)
    # Configurar el tamaño de la ventana de la cámara
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, ventana_ancho)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ventana_alto)

    informacion = ""

    if respuesta == "Alcazaba":
        aux = "alcazaba"
    elif respuesta == "catedral":
        aux = "catedral"
    elif respuesta == "plaza de toros":
        aux = "plaza_toros"
    elif respuesta == "teatro romano":
        aux = "teatro_romano"

    with open("./monumentos/" + aux + ".json", 'r') as file:
        data = json.load(file)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar los marcadores ArUco con los parámetros ajustados
        esquinas, ids, candidatos_malos = cv2.aruco.detectMarkers(gray, diccionario, parameters=parametros)

        if np.all(ids != None):
            aruco = cv2.aruco.drawDetectedMarkers(frame, esquinas)

            c1 = (esquinas[0][0][0][0], esquinas[0][0][0][1])
            c2 = (esquinas[0][0][1][0], esquinas[0][0][1][1])
            c3 = (esquinas[0][0][2][0], esquinas[0][0][2][1])
            c4 = (esquinas[0][0][3][0], esquinas[0][0][3][1])

            copy = frame.copy()

            imagen = cv2.imread(data.get("ruta_ruta"))
            informacion = data.get("ruta")

            tamaño = imagen.shape
            puntos_aruco = np.array([c1,c2,c3,c4])
            puntos_imagen = np.array([
                [0,0],
                [tamaño[1] - 1, 0],
                [tamaño[1] - 1, tamaño[0] - 1],
                [0, tamaño[0] - 1]
            ], dtype=float)

            h, estado = cv2.findHomography(puntos_imagen, puntos_aruco)

            perspectiva = cv2.warpPerspective(imagen, h, (copy.shape[1], copy.shape[0]))
            cv2.fillConvexPoly(copy, puntos_aruco.astype(int), 0, 16)
            copy = copy + perspectiva

            # Agregar mensaje de presionar 'a' para escuchar indicaciones
            cv2.putText(copy, "Presiona 'a' para escuchar indicaciones", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow("Realidad Aumentada", copy)

            if cv2.waitKey(1) & 0xFF == ord('a'):
                ReproducirVozMonumentos(informacion)

        else:
            # Agregar mensaje de presionar 'q' para salir
            cv2.putText(frame, "Presiona 'q' para salir", (50, frame.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("Realidad Aumentada", frame)
            

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    # Detener la reproducción de voz
    pygame.mixer.music.stop()


#######################################################################3
