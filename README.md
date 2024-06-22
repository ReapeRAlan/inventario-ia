# Sistema de Inventario con IA

Este proyecto es un sistema de gestión de inventario con capacidades de análisis y predicción basadas en inteligencia artificial.

## Características

- Gestión de inventario
- Análisis de datos de ventas
- Predicción de necesidades de inventario

## Instalación

1. Clona el repositorio
2. Instala las dependencias del backend y frontend
3. Ejecuta el servidor

```bash
git clone https://github.com/ReapeRAlan/inventario-ia.git
cd inventario-ia
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
flask db upgrade
flask run
# Frontend
cd ../frontend
npm install
npm start
