
# ENTREGA FINAL DE PRÁCTICAS CUIA

@image [arucoMarcador2.pdf](https://github.com/user-attachments/files/18575886/arucoMarcador2.pdf)

## ExploreAR – Aplicación Turística

- **Autor**: Rafael Luque Framit  
- **Título**: ExploreAR – Aplicación turística  
- **Asignatura**: Computación Ubicua e Inteligencia Ambiental  

---

## Índice
- [Descripción General](#descripción-general)
- [Interés del problema a resolver](#interés-del-problema-a-resolver)
- [Funcionalidades y Tecnologías involucradas](#funcionalidades-y-tecnologías-involucradas)
  - [Reconocimiento facial](#reconocimiento-facial)
  - [Reconocimiento de voz](#reconocimiento-de-voz)
  - [Reproducción de voz](#reproducción-de-voz)
  - [Realidad aumentada](#realidad-aumentada)
  - [Reconocimiento e identificación de imágenes](#reconocimiento-e-identificación-de-imágenes)
  - [Requirements.txt](#requirementstxt)
- [Manual de Usuario](#manual-de-usuario)
  - [Instalación y ejecución de la aplicación](#instalación-y-ejecución-de-la-aplicación)
  - [Uso de la aplicación](#uso-de-la-aplicación)

---

## Descripción General

ExploreAR es un proyecto que consiste en la realización de una aplicación enfocada al turismo en la ciudad de Málaga, España. Esta aplicación es apta para todos los públicos de todas las edades y adaptada para las personas que sean ciegas o sordas gracias a sus funcionalidades.

La aplicación realiza **Interacción Hombre-Máquina implícita** y **Conciencia de contexto** mediante funcionalidades como:  
- Reconocimiento de voz.  
- Procesado de lenguaje natural.  
- Realidad Aumentada (OpenCV).  
- Reconocimiento e identificación de imágenes (OpenCV).  

Está escrita íntegramente en Python y utiliza varias librerías que se mencionan más adelante.

Por un lado, la aplicación tiene identificación y registro de usuarios mediante reconocimiento facial, almacenando datos y fotos de los usuarios. La interacción se realiza mediante **comandos de voz**. Una de las funcionalidades es que el usuario puede elegir que el programa le planifique una ruta hacia un monumento específico.

A través de una marca ArUco, el usuario puede escanearla en tiempo real mediante la cámara de su dispositivo y observar un mapa del centro de Málaga con la ruta desde su ubicación actual al monumento seleccionado. La aplicación también describe la ruta mediante comandos de voz.

Por otro lado, al estar frente a un monumento, el usuario puede enfocar su cámara para que el sistema lo reconozca y le proporcione información tanto escrita como hablada.

---

## Interés del problema a resolver

Esta aplicación turística es útil porque fomenta la exploración y descubrimiento de Málaga, facilitando al usuario su experiencia turística. Además:  
- Mejora la interacción usuario-máquina mediante reconocimiento facial, voz y reproducción de voz.  
- Es inclusiva, diseñada para personas ciegas y sordas.  
- Es apta para todas las edades.

---

## Funcionalidades y Tecnologías involucradas

### Reconocimiento facial
La aplicación identifica y registra usuarios mediante la librería `face_recognition`. Si el usuario no está registrado, aparece un cuadro rojo con “Desconocido”. Si lo desea, puede registrarse, proporcionando su nombre y edad. Los datos se almacenan en un archivo JSON junto con un vector de características faciales. Los usuarios registrados son identificados con un cuadro verde.

### Reconocimiento de voz
Se utiliza la librería `speech_recognition` para capturar comandos de voz. En caso de error, se muestra un mensaje indicando que no se pudo reconocer el comando.

### Reproducción de voz
La aplicación comunica información mediante comandos de voz (librería `gtts`) y reproduce mensajes de información usando `pygame.mixer`. Los audios se generan en formato MP3.

### Realidad aumentada
Mediante un marcador ArUco y la librería `cv2` (OpenCV), se proyecta un mapa del centro de Málaga con la ruta al monumento seleccionado. Las funciones utilizadas incluyen:  
- `detectMarkers`  
- `drawDetectedMarkers`  
- `findHomography`  
- `warpPerspective`

### Reconocimiento e identificación de imágenes
La cámara identifica monumentos usando el algoritmo `sift` de OpenCV. Si hay coincidencias con los descriptores almacenados, el sistema proporciona información escrita y hablada.

### Requirements.txt
Dependencias necesarias:
```plaintext
numpy==1.26.4
requests==2.32.2
deepface==0.0.87
mediapipe==0.10.11
face-recognition==1.3.0
gTTS==2.5.1
SpeechRecognition==3.10.1
folium==0.16.0
opencv-contrib-python==4.9.0.80
opencv-python==4.9.0.80
pygame==2.5.2
```

En primer lugar, una vez tengamos el proyecto descompilado debemos instalarnos todas las
dependencias necesarias para que la aplicación funcione. Para ello debemos ejecutar en la
terminal el siguiente comando:
```pip install -r requirements.txt```

Tras esto podemos ejecutar la aplicación, para ello ejecutamos en la terminal el comando:
```python main.py```

### Uso de la aplicación
En primer lugar, una vez iniciada la aplicación, se abrirá la cámara del dispositivo y nos
reconocerá la cara. En el caso de que no estemos registrados el sistema nos preguntará si
queremos registrarnos, en el caso de que queramos registrarnos nos preguntará nuestro
nombre y nuestra edad y por último abrirá de nuevo la cámara del dispositivo para tomar
captura de un frame y guardarlo como imagen de la cara del usuario. Tras esto podremos
hacer uso de las siguientes funcionalidades de la aplicación. Para salir de esa ventana deberá
presionar la letra “q”.
En el caso de que el usuario si esté registrado el sistema lo reconocerá mostrando un recuadro
en verde con el nombre del usuario y seguidamente podrá hacer uso de las siguientes
funcionalidades de la aplicación. Para salir de esa ventana deberá presionar la letra “q”.
El usuario podrá hacer uso de la aplicación con los siguientes comandos de voz:
- ruta a monumento: si el usuario dice este comando se le va a proporcionar una ruta hacia
el monumento que el desee. En primer lugar, el sistema preguntará que monumento
quiere visitar (Alcazaba, catedral, plaza de toros, teatro romano), el usuario responderá y
a continuación se abrirá la cámara del dispositivo. Si la cámara detecta el marcador ArUco
se sobrepondrá el mapa con la ruta hacia ese monumento y pulsando la tecla “a” podrá
obtener la información de la ruta mediante reproducción de audio. Para salir de esta
ventana deberá presionar la letra “q”.
- reconocer monumento: si el usuario dice este comando se abrirá la cámara del
dispositivo, el sistema identificará el monumento al que se está enfocando. Para salir de
esa ventana deberá presionar la letra “q”. A continuación, el sistema preguntará si desea
obtener información sobre ese monumento, en el caso de que el usuario si quiera
comenzará a reproducirse por audio la información y además se mostrará por cámara
dicha información escrita.
ayuda: si el usuario dice este comando el sistema mostrará y reproducirá la lista de
comandos de voz que el usuario puede realizar aportando también una breve descripción
de lo que realiza cada uno de ellos, entre los que se encuentran: “ruta a monumento,
reconocer monumento, ayuda o salir”.
- salir: si el usuario dice este comando la aplicación se cerrará mostrando y reproduciendo
un mensaje “Muchas gracias, hasta pronto.”.
