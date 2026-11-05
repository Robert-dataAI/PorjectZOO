from pathlib import Path

# Nombre del proyecto
nombre_proyecto = "Project_ZOO"

# Estructura de carpetas y archivos
estructura = {
    "main.py": "",
    "README.md": "# Mi proyecto POO\n",
    "requirements.txt": "",
    ".gitignore": "__pycache__/\n.venv/\n*.pyc\n.env\n",

    "src": {
        nombre_proyecto: {
            "__init__.py": "",
            "modeles": {
                "__init__.py": "",
                "persona.py": "",
            },
            "services": {
                "__init__.py": "",
                "gestion_personas.py": "",
            },
            "utilites": {
                "__init__.py": "",
                "funciones.py": "",
            },
        }
    },

    "tests": {
        "__init__.py": "",
        "test_persona.py": "",
    },

    "docs": {}
}


def crear_estructura(ruta, contenido):

    for nombre, elemento in contenido.items():

        nueva_ruta = ruta / nombre

        if isinstance(elemento, dict):
            nueva_ruta.mkdir(parents=True, exist_ok=True)

            crear_estructura(nueva_ruta, elemento)

        else:
            nueva_ruta.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            nueva_ruta.write_text(
                elemento,
                encoding="utf-8"
            )


# Crear proyecto
ruta_proyecto = Path(nombre_proyecto)

ruta_proyecto.mkdir(exist_ok=True)

crear_estructura(ruta_proyecto, estructura)

print("Proyecto creado correctamente.")
print(f"Ubicación: {ruta_proyecto.resolve()}")
