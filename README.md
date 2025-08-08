# Conway's Game of Life

#### Description:

Este proyecto implementa el famoso "Juego de la Vida" de Conway usando Python y una arquitectura Model-View-Controller (MVC). El Juego de la Vida es un autómata celular creado por el matemático John Conway que simula la evolución de células en una cuadrícula bidimensional basada en reglas simples.

## Características

- **Interfaz gráfica** desarrollada con Tkinter
- **Arquitectura MVC** bien estructurada
- **Patrones predefinidos** (glider, blinker, block, toad, beacon)
- **Carga y guardado** de estados desde/hacia archivos de texto
- **Control de velocidad** de simulación en tiempo real
- **Pausa y reanudación** de la simulación
- **Generación aleatoria** de estados iniciales
- **Argumentos de línea de comandos** para configuración flexible

## Estructura del Proyecto

```
game_of_life/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py                 # Punto de entrada principal
│   ├── controllers/
│   │   ├── game_controller.py  # Controlador de la simulación
│   │   └── file_controller.py  # Controlador de archivos
│   ├── models/
│   │   ├── game_of_life.py     # Lógica del juego
│   │   └── file_manager.py     # Manejo de archivos
│   └── views/
│       └── view_tkinter.py     # Interfaz gráfica
├── tests/
│   ├── test_game_of_life.py
│   └── test_file_controller.py
└── hola.txt                    # Archivo de ejemplo
```

### Descripción de Archivos

- **`src/main.py`**: Punto de entrada que maneja argumentos de línea de comandos y coordina la inicialización de los componentes MVC.
- **`src/models/game_of_life.py`**: Implementa la lógica central del autómata celular, incluyendo las reglas de Conway y la gestión del estado de la cuadrícula.
- **`src/models/file_manager.py`**: Proporciona funciones estáticas para cargar y guardar estados del juego desde/hacia archivos de texto.
- **`src/views/view_tkinter.py`**: Implementa la interfaz gráfica usando Tkinter, mostrando la cuadrícula y proporcionando controles para el usuario.
- **`src/controllers/game_controller.py`**: Maneja el flujo de la simulación, incluyendo pausa, velocidad e iteraciones.
- **`src/controllers/file_controller.py`**: Gestiona las operaciones de exportación de archivos a través de la interfaz gráfica.

## Instalación y Configuración

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**:
```bash
git clone https://github.com/RaulCasado/python-gameoflife.git
cd python-gameoflife
```

2. **Crear un entorno virtual** (recomendado):
```bash
python3 -m venv venv
```

3. **Activar el entorno virtual**:
   - En Linux/macOS:
   ```bash
   source venv/bin/activate
   ```
   - En Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

5. **Verificar instalación de Tkinter** (normalmente viene con Python):
```bash
python3 -c "import tkinter; print('Tkinter disponible')"
```
   
   Si Tkinter no está disponible, instalarlo según tu sistema operativo:
   - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
   - **CentOS/RHEL**: `sudo yum install tkinter`
   - **macOS**: Normalmente incluido con Python
   - **Windows**: Normalmente incluido con Python

## Uso

### Ejecución Básica

```bash
python3 src/main.py --random --rows 20 --cols 20 --speed 100
```

### Opciones de Línea de Comandos

- `--rows`: Número de filas de la cuadrícula (por defecto: 20)
- `--cols`: Número de columnas de la cuadrícula (por defecto: 20)
- `--speed`: Velocidad de simulación en milisegundos (por defecto: 100)
- `--iterations`: Número máximo de iteraciones (por defecto: 200)
- `--name`: Nombre de la ventana (por defecto: "World")
- `--load ARCHIVO`: Cargar estado inicial desde un archivo
- `--pattern PATRON`: Usar un patrón predefinido
- `--random`: Generar estado inicial aleatorio

### Ejemplos de Uso

1. **Patrón Glider**:
```bash
python3 src/main.py --pattern glider --rows 30 --cols 30 --speed 300
```

2. **Cargar desde archivo**:
```bash
python3 src/main.py --load hola.txt --speed 400
```

3. **Estado aleatorio personalizado**:
```bash
python3 src/main.py --random --rows 50 --cols 50 --speed 200 --iterations 500
```

### Patrones Disponibles

- **glider**: Patrón que se mueve diagonalmente
- **blinker**: Oscilador simple de período 2
- **block**: Patrón estático (naturaleza muerta)
- **toad**: Oscilador de período 2
- **beacon**: Oscilador de período 2

### Controles de la Interfaz

- **Botón Pause/Resume**: Pausa o reanuda la simulación
- **Botones +/-**: Ajusta la velocidad de simulación
- **Botón Export**: Guarda el estado actual en un archivo de texto
- **Display de velocidad**: Muestra la velocidad actual en milisegundos

## Formato de Archivos

Los archivos de estado utilizan un formato de texto simple donde:
- `1` representa una célula viva
- `0` representa una célula muerta
- Cada fila está en una línea separada
- Los valores están separados por espacios

Ejemplo (`hola.txt`):
```
0 0 0 1 0
0 1 0 1 0
1 1 1 1 0
0 0 0 0 0
```

## Ejecutar Tests

```bash
pytest tests/
```

O para un archivo específico:
```bash
pytest tests/test_game_of_life.py -v
```

## Decisiones de Diseño

### Arquitectura MVC

Elegí implementar una arquitectura Model-View-Controller por las siguientes razones:

1. **Separación de responsabilidades**: Cada componente tiene una función clara y específica.
2. **Mantenibilidad**: Es fácil modificar la lógica del juego sin afectar la interfaz, y viceversa.
3. **Escalabilidad**: Se pueden agregar nuevas vistas (como una versión de consola) sin modificar el modelo.
4. **Testabilidad**: La lógica de negocio está aislada y es fácil de probar.

### Uso de NumPy

Decidí usar NumPy para la manipulación de la cuadrícula porque:
- Proporciona operaciones eficientes en arrays multidimensionales
- Simplifica la lectura/escritura de archivos con `loadtxt` y `savetxt`
- Mejora el rendimiento en comparación con listas de Python puras

### Gestión de Estado

El controlador mantiene el estado de la simulación (corriendo/pausado, velocidad, iteración actual) separado del modelo, lo que permite un control fino sobre la ejecución sin contaminar la lógica del juego.
