# Letras
Programa que resuelve la prueba de "letras" del programa de televisión "Cifras y Letras".


## Uso
Para ejecutar el programa es necesario usar [Python 3.13](https://www.python.org/)[^1].

Cuenta con una dependencia, [tqdm](https://pypi.org/project/tqdm/)[^2], y se usa el gestor de paquetes [uv](https://docs.astral.sh/uv).

[^1]: Es probable que versiones posteriores (y algunas anteriores) de Python funcionen, pero éste programa está probado exclusivamente en esta versión.
[^2]: Ésta dependencia es para un tema meramente visual (barra de carga mientras se generan los árboles), y se puede modificar ligeramente el código para evitar tener que usarla.

El programa cuenta con dos partes: [`generate_trees.py`](generate_trees.py) obtiene un listado de palabras válidas (una por línea), y genera los árboles de búsqueda en la carpeta [`trees/`](trees/). Éste listado se puede obtener de [JorgeDuenasLerin/diccionario-espanol-txt](https://github.com/JorgeDuenasLerin/diccionario-espanol-txt). Se ignoran palabras compuestas o mayores de 10 letras, y las tildes.

Primero es necesario generar los árboles a partir del listado de palabras:
```
uv run generate_trees.py 0_palabras_todas.txt
```

Para ejecutar el programa en sí, el cual obtiene una serie de letras y retorna la palabra más larga posible:
```
uv run letras.py abcdefghi
```
