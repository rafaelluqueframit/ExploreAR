import metodos
import usuario as user
import monumento
import sys
import numpy as np

# descriptores = metodos.calcular_descriptores()

# # Crear un nuevo Monumento
# nuevo_monumento = monumento.Monumento(nombre="Alcazaba", info="La alcazaba de Málaga es una fortificación palaciega de la época islámica, construida sobre una anterior fortificación de origen fenicio-púnico. Se encuentra en las faldas del monte Gibralfaro, en una posición elevada pero unida al centro histórico de la ciudad, lo que constituía la antigua madina de Mālaqa, y en cuya cumbre se halla el Castillo de Gibralfaro. Ocupaba el extremo oriental del recinto amurallado de la ciudad. Su superficie actual de 15.000 metros cuadrados no alcanza ni siquiera la mitad del tamaño que poseía en su época de esplendor. Este palacio-fortaleza es uno de los monumentos históricos más visitados de la ciudad por su historia y belleza. La Alcazaba actualmente es el resultado de un largo proceso histórico que podría dividirse en cuatro etapas: el periodo andalusí; la Reconquista; el del abandono de su estructura militar y deterioro; y el de su recuperación como Monumento Histórico Artístico desde la década de 1930 hasta nuestros días.", ruta="Para llegar a la Alcazaba desde la plaza de la Constitución debes dirigirte al este por el Pasaje Chinitas 41 metros. Gira a la izquierda y camina 26 metros. Luego, gira a la derecha hacia la Calle Santa María y continúa 170 metros. Continúa por la Calle Císter durante 180 metros. Gira a la izquierda hacia la Plaza de la Aduana y avanza 22 metros. Gira a la derecha hacia el Paseo Don Juan Temboury y camina 88 metros. Gira ligeramente a la izquierda y continua 43 metros. Gira a la derecha durante 220 metros. Por último, gira a la izquierda y avanza 130 metros para llegar a la Alcazaba de Málaga.", ruta_imagen="./img/alcazaba01.jpg", ruta_ruta="./img_rutas/alcazaba.jpg", caracteristicas_monu=descriptores[0])
# # Guardar los datos del Monumento en un archivo JSON
# nuevo_monumento.guardar_datos("./monumentos/alcazaba.json")

# # Crear un nuevo Monumento
# nuevo_monumento = monumento.Monumento(nombre="catedral", info="La Santa Iglesia Catedral Basílica de la Encarnación es la catedral de Málaga. Situada enfrente de la plaza del Obispo, el templo es una de las joyas renacentistas más valiosas de Andalucía. Se encuentra dentro de los límites que marcaba la desaparecida muralla árabe la primitiva mezquita aljama, el lugar donde los Reyes Católicos Isabel y Fernando ordenaron erigir un templo cristiano en 1487. Su proceso constructivo comenzó en 1525 y finalizó en 1782. Las originarias trazas, de estilo gótico, derivaron en un proyecto renacentista donde participaron Diego de Siloé y Andrés de Vandelvira. La catedral es una síntesis de estilos arquitectónicos entre los que prevalece el Renacimiento, junto con el Barroco y el Gótico. Hasta el 2012, fue el segundo edificio más alto de Andalucía. La altura de sus bóvedas solo es superada por la Catedral de Palma, siendo uno de los quince templos europeos con mayor altura en sus naves.", ruta="Para llegar a la catedral desde la plaza de la Constitución debes dirigirte al este por el Pasaje Chinitas 41 metros. Gira a la izquierda y camina 26 metros. Después, gira a la derecha hacia la Calle Santa María y continúa 100 metros. Gira a la derecha hacia la Calle Molina Lario y avanza 60 metros. El destino, la Catedral de Málaga, estará a tu izquierda.", ruta_imagen="./img/catedral01.jpg", ruta_ruta="./img_rutas/catedral.jpg", caracteristicas_monu=descriptores[1])
# # Guardar los datos del Monumento en un archivo JSON
# nuevo_monumento.guardar_datos("./monumentos/catedral.json")

# # Crear un nuevo Monumento
# nuevo_monumento = monumento.Monumento(nombre="plaza_toros", info="La Malagueta es la plaza de toros de Málaga. Se encuentra situada en la zona que le da su nombre, La Malagueta, en el Distrito Este de Málaga, junto al Paseo de Reding. La plaza de toros de La Malagueta es obra de Joaquín Rucoba. Se comenzó a construir el 16 de junio de 1874, finalmente, fue inaugurada el 11 de junio de 1876 con una corrida de toros de la ganadería de Murube. Parte de los planos de construcción creados para el proyecto, del arquitecto Rucoba, se encuentran en la Real Cátedra Gaudí de la Escuela Técnica Superior de Arquitectura de Barcelona; en concreto, los que corresponden a la estructura del edificio, pilares y balconadas. En 1976 fue declarada Conjunto Histórico-Artístico, coincidiendo con el centenario de su inauguración, y, en 1981, Bien de Interés Cultural.", ruta="Para llegar a la plaza de toros desde la plaza de la Constitución debes dirigirte al norte hacia la Calle Santa María 21 metros. Continúa hacia la derecha por calle Granada 380 metros. Gira ligeramente a la izquierda y continua 110 metros. Gira a la derecha hacia la Plaza María Guerrero y avanza 43 metros. Continúa por la Calle Santa Ana o la Plaza Jesús el Rico durante 450 metros. Luego, continúa por el Paseo Reding durante 170 metros. El destino, la Plaza de Toros de Málaga, estará a tu derecha.", ruta_imagen="./img/plaza_toros01.jpg", ruta_ruta="./img_rutas/plaza_toros.jpg", caracteristicas_monu=descriptores[2])
# # Guardar los datos del Monumento en un archivo JSON
# nuevo_monumento.guardar_datos("./monumentos/plaza_toros.json")

# # Crear un nuevo Monumento
# nuevo_monumento = monumento.Monumento(nombre="teatro_romano", info="El teatro romano de Málaga son los restos arqueológicos del teatro de la Malaca antigua y el principal vestigio conservado de la presencia romana en Málaga. Está situado en el centro histórico de la ciudad. Obra de los primeros años del Imperio, su diseño corresponde a una construcción mixta que combina el aprovechamiento de la ladera del cerro para el graderío. Se trata de un teatro de medianas dimensiones que conserva gran parte de la cavea o graderío, la orchestra decorada con grandes losas de mármol, y la scaena, en la que hoy se ha reproducido su pavimento con un entarimado de madera como el que tendría en su momento de uso. El aparato escénico cerraría al fondo con una fachada ornamental decorada con vanos, columnas y esculturas, de las que se han recuperado varios ejemplares. Se tomó la decisión de derribar la casa de la cultura, excavar todo el solar y, posteriormente, restaurarlo y consolidarlo para su puesta en valor.", ruta="Para llegar al teatro romano desde la plaza de la Constitución debes dirigirte al este por el Pasaje Chinitas 41 metros. Gira a la izquierda y avanza 26 metros más. Luego, gira a la derecha hacia la Calle Santa María y continúa por 170 metros. Continúa por la Calle Císter durante 180 metros. Gira a la izquierda hacia la Plaza de la Aduana. Después, gira ligeramente a la izquierda hacia la Calle Alcazabilla y camina 90 metros. El destino, el Teatro Romano de Málaga, estará a tu derecha.", ruta_imagen="./img/teatro_romano01.jpg", ruta_ruta="./img_rutas/teatro_romano.jpg", caracteristicas_monu=descriptores[3])
# # Guardar los datos del Monumento en un archivo JSON
# nuevo_monumento.guardar_datos("./monumentos/teatro_romano.json")

    
estado, nombre = metodos.ComprobarRegistro()

cliente = user.Usuario()

if estado == False:
    print("No estas registrado, ¿Quieres registrate?")
    metodos.ReproducirVoz("No estás registrado. ¿Quieres registrarte?")
    respuesta = metodos.ReconocerVoz()
    if respuesta == "sí":
        print("Comienzo del registro")
        metodos.ReproducirVoz("Comienzo del registro")
        print("¿Como te llamas?")
        metodos.ReproducirVoz("¿Como te llamas?")
        nombre = metodos.ReconocerVoz()
        metodos.ReproducirVoz("¿Qué edad tienes?")
        edad = metodos.ReconocerVoz()
        print("Hola " + nombre)
        metodos.ReproducirVoz("Hola " + nombre)
        ruta_foto, vector_cara = metodos.RegistroFacial(nombre)
        print(ruta_foto)
        # Crear una instancia de la clase Persona
        usuario = user.Usuario(nombre, edad, ruta_foto, vector_cara)
        # Guardar los datos de la persona en un archivo
        usuario.registarse("./datos/datos_"+nombre+".json")

    else:
        print("Hasta luego")
        metodos.ReproducirVoz("Hasta luego.")
        sys.exit()
else:
    print("Bienvenido " + nombre)
    metodos.ReproducirVoz("Bienvenido " + nombre)
    # Cargar los datos de una persona desde el archivo
    usuario = user.Usuario.cargar_datos("./datos/datos_"+nombre+".json")

while True:
    print("Ahora puedes elegir: ruta a monumento, reconocer monumento, ayuda o salir. ¿Qué deseas hacer?")
    metodos.ReproducirVoz("Ahora puedes elegir: ruta a monumento, reconocer monumento, ayuda o salir. ¿Qué deseas hacer?")
    respuesta = metodos.ReconocerVoz()

    entra = False
    if respuesta == "ruta a monumento":
        while entra == False:
            print("¿A qué monumento quieres llegar? Opciones: Alcazaba, catedral, plaza de toros, teatro romano.")
            metodos.ReproducirVoz("¿A qué monumento quieres llegar? Opciones: Alcazaba, catedral, plaza de toros, teatro romano.")
            respuesta_info = metodos.ReconocerVoz()
            if respuesta_info in ["Alcazaba", "catedral", "plaza de toros", "teatro romano"]:
                entra = True
        metodos.ObtenerMapa(respuesta_info)
                                                                                            
    if respuesta == "reconocer monumento":
        monumento = metodos.ReconocimientoMonumento()
        if monumento != "":
            print("¿Quieres información sobre este monumento?")
            metodos.ReproducirVoz("¿Quieres información sobre este monumento?")
            respuesta_info = metodos.ReconocerVoz()
            if respuesta_info == "sí":
                info = metodos.ObtenerInformacion(monumento)

    if respuesta == "ayuda":
        info = """Los comandos de voz son los siguientes:
        ruta a monumento: Si quieres ver una ruta hacia un monumento
        reconocer monumento: Si quiere reconocer y obtener informacion de un monumento de la ciudad a traves de una imagen.
        salir: salir de la aplicación."""
        print(info)
        metodos.ReproducirVoz(info)

    if respuesta == "salir":
        print("Muchas gracias, hasta pronto.")
        metodos.ReproducirVoz("Muchas gracias, hasta pronto.")
        break

