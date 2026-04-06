# Traductor de Aprendizaje en Segundo Plano (Jarvis Translator)

## Visión General y Origen del Proyecto

Este proyecto nace de una necesidad específica: facilitar el aprendizaje del idioma inglés de una manera fluida, rápida y sin interrupciones. El objetivo principal es proporcionar al usuario una herramienta que opere de forma invisible en el sistema (en segundo plano) y que se active instantáneamente mediante atajos de teclado para traducir texto previamente seleccionado.

**Nota de Autoría y Desarrollo:** La conceptualización, la estructura arquitectónica del software, la definición de las funcionalidades (atajos de teclado, guardado de historial) y el diseño lógico fueron ideados íntegramente por el creador del proyecto. La inteligencia artificial fue utilizada como una herramienta de desarrollo para materializar la visión del creador, redactando el código funcional basado en estas directrices arquitectónicas.

## Flujo de Uso

La aplicación está diseñada para minimizar la fricción cognitiva durante la lectura. Su uso consta de dos pasos:
1. El usuario selecciona un texto en cualquier aplicación y lo copia al portapapeles (`Ctrl + C`).
2. El usuario ejecuta un atajo de teclado global:
   - `Ctrl + Alt + T`: Traduce el texto del portapapeles (de cualquier idioma) al Español.
   - `Ctrl + Alt + E`: Traduce el texto del portapapeles (de cualquier idioma) al Inglés.

Inmediatamente, se muestra una interfaz emergente con el resultado y, de manera asíncrona, la transacción se registra en un archivo de historial.

## Arquitectura de Software y Diseño Orientado a Objetos (POO)

Como estudiante de ingenieria de sistemas de segundo semestre, el enfoque para este proyecto fue garantizar un código limpio, modular y mantenible. Para ello, se aplicó el paradigma de Programación Orientada a Objetos (POO), implementando una estricta separación de responsabilidades (Separation of Concerns).

A continuación, se detalla la estructura del proyecto y la función de cada módulo:

### 1. `main.py` (Punto de Entrada)
Este es el orquestador del sistema. Su única responsabilidad es inicializar los componentes, inyectar las dependencias necesarias y mantener el hilo principal de ejecución activo. En este archivo se instancian los objetos principales y se utiliza una estructura de cola (`Queue`) para manejar la comunicación segura entre los hilos de fondo (que escuchan el teclado) y el hilo principal de la interfaz gráfica (Tkinter), evitando bloqueos y errores de concurrencia.

### 2. Directorio `core/` (Lógica de Negocio)
Contiene el núcleo del comportamiento de la aplicación, independiente de la interfaz o de cómo se capturan las teclas.
* **`translator.py` (`Translator`):** Clase encargada exclusivamente de la lógica de traducción. Encapsula las peticiones al motor de traducción. Si en el futuro se decide cambiar el proveedor de traducción, solo este archivo deberá ser modificado, protegiendo el resto del sistema.
* **`history.py` (`TranslationHistory`):** Clase responsable de la persistencia de datos. Recibe las cadenas originales y traducidas y las anexa al archivo `history.json`. Maneja las operaciones de entrada/salida (I/O) de manera segura para evitar corrupción de datos.

### 3. Directorio `ui/` (Capa de Presentación)
Aísla todo el código relacionado con la interfaz gráfica de usuario.
* **`popup.py` (`TranslatorPopup`):** Clase que gestiona la ventana emergente generada con Tkinter. Se encarga de recibir los datos de la cola de mensajes (`ui_queue`) y renderizarlos en pantalla, ajustando dimensiones y gestionando su ciclo de vida (aparición y desaparición) sin interrumpir el flujo del usuario.

### 4. Directorio `input/` (Capa de Captura de Eventos)
Maneja las interacciones a nivel de hardware/sistema operativo.
* **`hotkeys.py` (`HotkeyManager`):** Esta clase opera en un hilo separado (Thread). Se encarga de suscribirse a los eventos del teclado del sistema operativo. Al detectar las combinaciones exactas (`Ctrl+Alt+T` o `Ctrl+Alt+E`), lee el portapapeles, invoca a las clases del `core` para traducir y guardar, y finalmente envía el resultado a la clase de UI a través de la cola.

## Archivos de Datos y Distribución

Para garantizar que la aplicación sea portable y utilizable por cualquier usuario sin necesidad de tener un entorno de desarrollo configurado, el proyecto incluye archivos para su empaquetado:

* **`history.json`**: Archivo de base de datos local en formato JSON. Estructura un arreglo de objetos que contienen la marca de tiempo, el texto original, la traducción y el idioma de destino. Sirve como material de repaso y estudio para el usuario.
* **`MiTraductorV2.spec` / `TraductorFinal.spec`**: Archivos de especificación de PyInstaller. Contienen las instrucciones exactas sobre cómo compilar el script de Python, sus dependencias y recursos estáticos en un único archivo ejecutable aislado. Define qué módulos ocultos incluir y cómo optimizar el binario.
* **`TraductorFinal.exe`**: El artefacto final de despliegue. Un ejecutable independiente que contiene el intérprete de Python, las librerías estándar y el código de la aplicación comprimidos. Permite que la aplicación funcione de manera nativa en sistemas Windows simplemente haciendo doble clic, operando de manera silenciosa en segundo plano.

## Requisitos y Despliegue

Si se desea ejecutar desde el código fuente:
1. Clonar el repositorio.
2. Crear un entorno virtual (recomendado para aislar dependencias).
3. Instalar las dependencias necesarias.
4. Ejecutar `python main.py`.

Para usuarios finales, basta con ejecutar el archivo `TraductorFinal.exe` y comenzar a utilizar los atajos de teclado mientras se lee cualquier documento o sitio web.
