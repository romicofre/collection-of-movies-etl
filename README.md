# Modo de uso

Las siguientes son instrucciones para poder ejecutar este repositorio

## Requerimientos
### Necesarios
- Python3
- Una base de datos MySQL
- pip
- Librerías Python: Pandas, PyMySQL, SQLAlchemy 
### Opcionales
- Jupyter
- virtualenv o conda

## Opcional: Usando un entorno virtual con conda 
Installation: https://docs.conda.io/projects/conda/en/latest/user-guide/install/

Usar en la consola:

`conda create -n collection-of-movies-etl`

`conda activate collection-of-movies-etl`

## Instalar requirements

En la consola, si es necesario dentro del entorno virtual creado anteriormente:

`pip intall -r requiremts.txt`

## Ejecutar programa
Setear variables de la base de datos, reemplazar user, pass, host, port y db
```
export MYSQL_USER=user
export MYSQL_PASS=pass
export MYSQL_HOST=host
export MYSQL_PORT=port
export MYSQL_DB_NAME=db
```
Correr script
`python main.py ` 

## Pruebas
Usar archivo `db/test_result.sql` para revisar contenido de la o las nuevas tablas creadas.

`notebook\movie_analysis.ipynb` es un archivo utilizado para explorar el archivo csv, 
descargado a un dataframe de pandas. 

# Data: collection-of-movies-etl
Data source: https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney/data

