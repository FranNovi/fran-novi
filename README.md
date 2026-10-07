# Portafolio de Fotografía

Proyecto web en Python para un portafolio personal de fotografía, desarrollado con Flask.

## Características
- Página principal elegante y moderna
- Galería con imágenes de ejemplo
- Sección de servicios
- Sobre mí
- Contacto
- Diseño responsive

## Requisitos
- Python 3.10+
- pip

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

La aplicación estará disponible en:
http://127.0.0.1:5000

## Estructura
- `app.py` - aplicación Flask
- `templates/` - vistas HTML
- `static/` - archivos CSS y JS

## Personalización
Puedes cambiar:
- Nombre del fotógrafo
- Descripción
- Galería de imágenes
- Datos de contacto
- Colores y estilo

Todo desde `app.py` y `templates/index.html`.
