# Image de base légère
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier uniquement les fichiers nécessaires
COPY app/requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copier le reste du code de l'application
COPY app/ .

# Exposer le port
EXPOSE 8000

# Démarrer le serveur FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
