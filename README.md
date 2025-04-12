# Letras
Programa que resuelve la prueba de "letras" del programa de televisión "Cifras y Letras".


## Uso
Para ejecutar el programa es necesario usar [Python 3.13](https://www.python.org/)[^1].

Cuenta con una dependencia, [tqdm](https://pypi.org/project/tqdm/).

Para instalarla con [uv](https://docs.astral.sh/uv):
```
uv sync
```

Y luego activar el _Virtual Environment_:
- Windows Powershell:
  ```
  .\.venv\bin\activate.ps1
  ```
- Linux Bash/ZSH:
  ```
  source .venv/bin/activate
  ```


[^1]: Es probable que versiones posteriores (y algunas anteriores) de Python funcionen, pero éste programa está probado exclusivamente en esta versión.

El programa cuenta con dos partes: [`generate_trees.py`](generate_trees.py) obtiene un listado de palabras válidas (una por línea), y genera los árboles de búsqueda en la carpeta [`trees/`](trees/). Éste listado se puede obtener de [JorgeDuenasLerin/diccionario-espanol-txt](https://github.com/JorgeDuenasLerin/diccionario-espanol-txt). Se ignoran palabras compuestas o mayores de 10 letras, y las tildes.

Para ejecutarlo:
```
python3 generate_trees.py 0_palabras_todas.txt
```

La segunda parte es el programa en sí, la cual obtiene una serie de letras y retorna la palabra más larga posible:
```
python3 letras.py abcdefghi
```
