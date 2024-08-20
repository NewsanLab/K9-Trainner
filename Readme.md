# K9 Trainner
Este proyecto ha sido diseñado como una solución innovadora para satisfacer las necesidades del servicio penitenciario de Ushuaia, enfocado en optimizar el adiestramiento de los perros K9 especializados en la detección de sustancias ilícitas.
El sistema integra un compartimiento donde se pueden colocar diversas muestras de estupefacientes, permitiendo al perro realizar un ejercicio de búsqueda y localización entre múltiples cajas similares. Al identificar correctamente la caja que contiene la muestra marcada, el agente encargado activa un mecanismo a través de una aplicación para dispositivos móviles, conectada mediante tecnología Bluetooth no solo al lanzador, sino también controlada a través de nuestra placa ARCHI.

ARCHI, actúa como el cerebro del sistema, gestionando la comunicación y el control del lanzador. Al recibir la señal de la aplicación móvil, ARCHI activa el mecanismo que permite expulsar de manera controlada la pelota, la cual cumple la función de refuerzo positivo, motivando al perro a asociar el éxito en la detección con una recompensa tangible. Este enfoque no solo mejora la eficacia del entrenamiento, sino que también promueve un método de aprendizaje interactivo y dinámico entre el perro y su manejador.
![Muestra final del lanzador.](https://github.com/NewsanLab/Lanzador-de-pelotas/blob/main/img/Dispositivo.png)

## Diseño y Estructura mecánica

El dispositivo prototípico se compone de una estructura cerrada, la cual incorpora un orificio superior destinado a la introducción de una pelota de tenis.
En su núcleo, el sistema incorpora un motor universal de limpia parabrisas de 12V, que proporciona la potencia necesaria para la operación mecánica del dispositivo.
El mecanismo cuenta con un piñón y una cremallera, las cuales han sido diseñadas utilizando Software CAD como SolidWorks y fabricadas en acrílico mediante corte láser. El piñón está firmemente anclado al motor y, al girar este último, arrastra la cremallera a lo largo de su trayectoria. La cremallera, por su parte, se encuentra conectada a dos varillas de 12 mm de diámetro, que actúan como guías para el movimiento lineal.
Dentro de este sistema, las varillas están equipadas con resortes que se comprimen durante el movimiento de arrastre de la cremallera. Al liberar la cremallera del piñón, la energía acumulada en los resortes se utiliza para lanzar la pelota con fuerza, aprovechando así la energía de compresión generada. 
La pelota está sostenida por una pieza diseñada y fabricada mediante impresión 3D, que permite una fácil inserción y extracción de la misma. Todos estos componentes, incluidos el porta pelotas, las varillas y el motor, están montados en una estructura base fabricada en acrílico, asegurando la rigidez y estabilidad del sistema, la cual fue diseñada en SolidWorks y cortada por láser para lograr un ajuste preciso y eficiente. Este diseño modular y funcional permite un correcto rendimiento del mecanismo, optimizando la experiencia de entrenamiento para los perros K9.

![Lanzador de pelotas por dentro.](https://github.com/NewsanLab/Lanzador-de-pelotas/blob/main/img/Dispositivo%20interior.png)
![Mecanismo del lanzador.](https://github.com/NewsanLab/Lanzador-de-pelotas/blob/main/img/Mecanismo.png)

## Hardware

En la sección de Hardware, se encuentra la placa Archi y un shield diseñado específicamente para el dispositivo. Estos componentes se alimentan mediante cuatro baterías recargables incorporadas en la caja, las cuales son extraíbles para facilitar su recarga. La caja incluye también un interruptor de encendido/apagado (on/off). 
Este mecanismo está equipado con un sensor que contabiliza los dientes del piñón, permitiendo determinar el momento preciso para detenerse. Además, el sistema está integrado con una aplicación móvil para su monitoreo y control.

![Imagen del Shield de frente.](https://github.com/NewsanLab/Lanzador-de-pelotas/blob/main/Hardware/ShielArchiK9Top.png)
![Imagen del Shield del dorso.](https://github.com/NewsanLab/Lanzador-de-pelotas/blob/main/Hardware/ShielArchiK9Bot.png)

## Software

En la sección de software, se desarrolló una aplicación móvil que permite ingresar y gestionar los datos de cada perro. La aplicación se conecta con el dispositivo K9 y cuenta con funcionalidades integradas, como un cronómetro y una base de datos. Esta base de datos registra el tiempo que tarda el perro en localizar la caja correcta. Al presionar un botón en la aplicación, se activa el mecanismo que dispara la pelota como recompensa.
El software gestiona el mecanismo de lanzamiento de la pelota con precisión. Al seleccionar la opción para lanzar la pelota, el programa activa el motor que hace girar el piñón. El sensor asociado cuenta los dientes de la cremallera, permitiendo que el mecanismo se detenga en la posición correcta y garantizando que siempre vuelva a comenzar desde el mismo punto.
