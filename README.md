# sentiment-analyzer

Sentiment Analyzer un microservice conteneurisé pour l’analyse de sentiment basé sur **FastAPI**, **Hugging Face Transformers** et **PyTorch**, intégrant un **pipeline CI/CD GitLab** pour automatiser le **build**, les **tests** et la **livraison de l’image Docker** sur **Docker Hub**.

## Architecture :

```mermaid
flowchart TD
    A1[Client] -->|POST /analyze| B1[FastAPI - Sentiment Analyzer Service]
    B1 -->|Utilise le pipeline Transformers| C1[(Hugging Face Model)]
    C1 -->|Prédit le sentiment| B1
    B1 -->|Return JSON response| A1
```

## Fonctionnalités

- Analyse le sentiment d’un texte en anglais (positif / négatif).
- Basé sur le modèle léger `distilbert-base-uncased-finetuned-sst-2-english`.
- API REST simple construite avec **FastAPI**.
- Framework PyTorch (CPU)
- Déployable facilement via **Docker**.
- Integration continue et déploiment automatique avec **GitLab CI/CD**

---

## Tech Stack

- **Python**
- **FastAPI**
- **Transformers**
- **PyTorch**
- **PyTest**
- **Docker**
- **GitLab CI/CD**
- **Docker Hub**

---

## Lancement avec Docker :

Assurez-vous d’avoir Docker installé, puis :

### Image Docker

- **Lien direct vers l’image sur Docker Hub :** [sentiment-analyzer](https://hub.docker.com/r/mess09/sentiment-analyzer)

- **Taille** : 1.55 GB


### Pull de l’image à partir de Docker Hub

```bash
  docker pull mess09/sentiment-analyzer
```

## Ou cloner le dépôt

**Cloner le dépôt**

```bash
  git clone https://github.com/messaoudRm/sentiment-analyzer.git
  cd sentiment-analyzer
```

**Build l'image Docker**

```bash
  docker build -t sentiment-analyzer .
```

**Lancer le conteneur**:
```bash
  docker run -d -p 8000:8000 sentiment-analyzer
```

---

### Pipeline GitLab CI/CD  :

Le **pipeline GitLab CI/CD** automatise entièrement le cycle de vie de l’application : **tests**, **build**, et **livraison continue** sur **Docker Hub**.

Il se déclenche automatiquement à chaque **commit** ou **merge request** sur le dépôt **GitLab**.

![img.png](img/imgPipeline.png)

#### 1. Test

- Utilise une image légère : `python:3.10-slim`
- Exécute les **tests unitaires** avec `pytest` pour garantir :
    - Le bon fonctionnement des **endpoints**
    - La validité des **dépendances**


#### 2. Build & Delivery (Docker Hub)

- Construit l’image **Docker** à partir du `Dockerfile`
- Se connecte automatiquement à **Docker Hub**
- **Pousse** la nouvelle image sur le dépôt distant pour un déploiement continu

---

### Tester l’API :
Accède à la documentation interactive : http://localhost:8000/docs

#### Exemple de text positive
![img.png](img/img.png)
![img_1.png](img/img_1.png)

#### Exemple de text negative
![img_2.png](img/img_2.png)
![img_3.png](img/img_3.png)









