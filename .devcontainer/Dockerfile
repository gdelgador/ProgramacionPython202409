FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Instalar PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib libpq-dev

# Configurar PostgreSQL
USER postgres
RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER vscode WITH SUPERUSER PASSWORD 'password';" &&\
    createdb -O vscode vscode

# Crear directorio para el volumen de datos
RUN mkdir -p /var/lib/postgresql/data
VOLUME /var/lib/postgresql/data
# Exponer el puerto 5432
EXPOSE 5432

USER vscode
