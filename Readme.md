# API REST para le consulta de paises

## Arquitectura
- Python 12 o superior
- Fastapi
- Mysql 8: utilizar pymyql para la conexión desde python
- Kubernetes

## Especificación

El servicio va a exponer el siguiente endpoint:
GET /demo/api/country

Retornara el siguiente JSON con el código HTTP 200:

```json
{
    "environment": [
        {
            "key": "key_name",
            "value": "value_content"
        },
        {
            "key": "key_name",
            "value": "value_content"
        },
    ],
    "secrets": [
        {
            "key": "key_name",
            "value": "value_content"
        },
        {
            "key": "key_name",
            "value": "value_content"
        },
    ],
    "contries": [
        {
            "code": "contry_code",
            "name": "contry_name"
        },
        {
            "code": "contry_code",
            "name": "contry_name"
        },

    ]
}
```

environment: contiene un listado con las variables de entorno del contenedor y sus valores.
secrets: contiene un listado con los secret del pod y sus valores.
contries: contiene un listado con los paises. Esta listado de paises se obtiene de la tabla country que se encuentra en mysql.

El API también tiene los endpoint de liveness y de readiness para poder desplegarlo en kubernetes.

## Configuraciones
La url de conexión, puerto, nombre de base de datos y usuario de base de datos se manejan como configmaps de kubernetes y la clave de conexión a la base de datos se maneja como un secret de kubernetes.

## Despliegue
Los archivos de kubernetes para exponer el servicio se encuentran en la carpeta deploy/kubernetes/api, el servicio se expone utilizan un ingress bajo el dominio "demo.com" y se crear 2 instancias del servicio como mínimo y como máximo 3 instancias.
Dentro de la carpeta deploy/kubernetes/mysql se encuentran los archivos de kubernetes para ejecutar mysql en el cluster de kubernetes.

## Ejecución local

### Usando Python directamente

1. Crear y activar entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno (crear archivo .env):
```bash
MYSQL_USER=root
MYSQL_PASSWORD=example
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=country_db
```

4. Iniciar la aplicación:
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Usando Docker Compose

1. Construir e iniciar los contenedores:
```bash
docker compose up --build
```

Esto iniciará:
- La API en http://localhost:8000
- MySQL en el puerto 3306
- La base de datos será inicializada automáticamente con datos de ejemplo

Para detener los contenedores:
```bash
docker compose down
```

### Endpoints disponibles

- API: http://localhost:8000/demo/api/country
- Documentación de la API: http://localhost:8000/docs
- Health check: http://localhost:8000/health/liveness
- Readiness check: http://localhost:8000/health/readiness