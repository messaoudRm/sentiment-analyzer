# Image de base légère
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt
COPY app/requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir torch==2.4.1+cpu --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY app/ .

# Exposer le port
EXPOSE 8000

# Lancer l’application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
