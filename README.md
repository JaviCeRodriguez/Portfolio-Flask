# Desafios / Página web
Web App hecho con **Flask + HTML + Tailwind CSS + Firebase**. Este repositorio surge a partir de una serie de ejercicios propuestos en el grupo de estudio de Python, alojado en [FrontendCafé](https://frontend.cafe/).

## Instalación de virtualenv
1) Instalamos la librería: `pip install virtualenv`
2) Creamos el entorno virtual: `virtualenv env`
3) Lo activamos: `env\Scripts\activate`
4) Para desactivar: `deactivate`

## Instalacion de librerías
Si tenemos preparado un archivo `requeriments.txt`, instalamos las versiones de ahí: `pip install -r requirements.txt`.
Caso contrario, instalaremos a mano:
`pip install flask`
ó `pip install flask==1.0.1`
Si necesitamos actualizar una librería: `pip install flask -U`

## requeriments.txt
Podemos crear este archivo y actualizarlo con `pip freeze > requirements.txt`

## Ejecución de la app
Debemos escribir lo siguiente en consola:
```cmd
> set FLASK_APP=main.py
> set FLASK_ENV=DEVELOPMENT
> set FLASK_DEBUG=1
> flask run
```
Luego, Flask nos dará una dirección para entrar que suele ser: `http://127.0.0.1:5000/`.

