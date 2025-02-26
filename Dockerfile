# Utilisation d'une image Python
FROM python:3.9

# répertoire de travail
WORKDIR /app

# Copie les fichiers dans le conteneur
COPY addition.py test_addition.py /app/

# Installation de  pytest 
RUN pip install pytest

# point d'entrée
ENTRYPOINT ["python", "addition.py"]
