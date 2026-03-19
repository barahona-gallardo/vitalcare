# Deploy de Django en Railway

Este proyecto fue desplegado utilizando Django, PostgreSQL y Railway.

A continuación se describe el proceso para desplegar una aplicación Django en producción usando Railway.

---

## 1. Requisitos

* Repositorio en GitHub
* Cuenta en Railway

---

## 2. Estructura del proyecto

El proyecto debe tener manage.py (lanzador de Django) y requirements.txt (archivo de dependencias dependencias) en la raíz:

```
manage.py
requirements.txt
```

---

## 3. Dependencias

Instalar dependencias:

```bash
pip install django psycopg gunicorn whitenoise django_bootstrap5
```

Generar archivo:

```bash
pip freeze > requirements.txt
```

---

## 4. Configuración de Django (settings.py)

### Importaciones

```python
import os
from pathlib import Path
```

### Configuración base

```python
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-key")
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [host for host in os.environ.get("ALLOWED_HOSTS", "").split(",") if host]
CSRF_TRUSTED_ORIGINS = [origin for origin in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if origin]
```

### Middleware

```python
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### Base de datos (PostgreSQL)

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGDATABASE"),
        "USER": os.environ.get("PGUSER"),
        "PASSWORD": os.environ.get("PGPASSWORD"),
        "HOST": os.environ.get("PGHOST"),
        "PORT": os.environ.get("PGPORT", "5432"),
    }
}
```

### Archivos estáticos

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
```

---

## 5. Subir a GitHub

```bash
git add .
git commit -m "Preparar deploy en Railway"
git push origin main
```

---

## 6. Crear proyecto en Railway

1. Crear nuevo proyecto
2. Seleccionar "Deploy from GitHub Repo"
3. Elegir el repositorio

---

## 7. Agregar PostgreSQL

* Add Service → PostgreSQL

---

## 8. Conectar base de datos

En el servicio web (deploy → Variables):

```
PGDATABASE=${{Postgres.PGDATABASE}}
PGUSER=${{Postgres.PGUSER}}
PGPASSWORD=${{Postgres.PGPASSWORD}}
PGHOST=${{Postgres.PGHOST}}
PGPORT=${{Postgres.PGPORT}}
```

---

## 9. Variables de entorno

```
SECRET_KEY=tu_clave_segura
DEBUG=False
ALLOWED_HOSTS=tu-app.up.railway.app
CSRF_TRUSTED_ORIGINS=https://tu-app.up.railway.app
```

---

## 10. Generar dominio

* Settings → Networking
* Generate Domain

---

## 11. Start Command

```bash
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

---

## 12. Crear superusuario

Instalar CLI:

```bash
npm i -g @railway/cli
```

Login:

```bash
railway login
```

Conectar proyecto:

```bash
railway link
```

Entrar al contenedor:

```bash
railway ssh
```

Crear usuario:

```bash
python manage.py createsuperuser
```

---

## 13. Acceso

Aplicación:

```
https://tu-app.up.railway.app/
```

Admin:

```
https://tu-app.up.railway.app/admin/
```

---

## Resumen

El flujo de despliegue consiste en:

1. Preparar proyecto Django
2. Configurar variables de entorno
3. Conectar PostgreSQL
4. Generar dominio
5. Ejecutar migraciones y levantar servidor

---

## Estado

* Aplicación desplegada
* Base de datos conectada
* Autenticación funcional
* Panel de administración operativo

---

## Documentación

https://docs.railway.com/guides/django

https://docs.railway.com/cli
