# API de Santé avec FastAPI

Une API simple avec un endpoint de santé, construite avec FastAPI.

## Prérequis

- Python 3.7+
- pip (gestionnaire de paquets Python)

## Installation

1. Cloner le dépôt
2. Créer un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Linux/Mac
   # ou
   .\venv\Scripts\activate  # Sur Windows
   ```
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Démarrage

Pour lancer le serveur de développement :

```bash
uvicorn main:app --reload
```

L'API sera disponible à l'adresse : http://localhost:5010

## Documentation

- Documentation interactive : http://localhost:5010/swagger
- Documentation alternative : http://localhost:5010/redoc

## Endpoints

### Vérification de l'état de santé

- **URL** : `/sante`
- **Méthode** : `GET`
- **Réponse** :
  ```json
  {
    "status": "ok",
    "message": "L'API fonctionne correctement",
    "version": "1.0.0"
  }
  ```

## Développement

Pour installer les dépendances de développement :

```bash
pip install -r requirements-dev.txt
```

## Licence

MIT
