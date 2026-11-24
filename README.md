<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# Démonstration DevOps Modulaire : FastAPI, Nginx, Kubernetes & CI/CD
=======
# ad_devops_demo1
>>>>>>> 0f20356 (Initial commit)

Ce dépôt contient le code source, les manifestes Kubernetes et les pipelines CI/CD permettant de démontrer **le découplage applicatif et le déploiement indépendant de modules** sur un cluster Kubernetes.

L'architecture repose sur deux microservices autonomes déployés dans le namespace `demo-app` :
- **`api-backend`** : API REST développée avec **FastAPI** (Python), exposée en interne via un service `ClusterIP` sur le port `8000`.
- **`frontend`** : Interface web statique servie par **Nginx**, exposée à l'extérieur via un service `NodePort` (`30080`) et faisant office de reverse-proxy vers le backend.

---

## Architecture et Arborescence

```text
.
├── backend/
│   ├── Dockerfile          # Image Python/Uvicorn pour FastAPI
│   ├── main.py             # Code source de l'API (/api/info)
│   └── backend.yaml        # Manifestes Deployment & Service (ClusterIP)
├── frontend/
│   ├── Dockerfile          # Image Nginx pour le frontend
│   ├── entrypoint.sh       # Script d'initialisation au démarrage du conteneur
│   ├── index.html          # Interface utilisateur web
│   └── frontend.yaml       # Manifestes Deployment & Service (NodePort 30080)
├── .gitlab-ci.yml          # Pipeline CI/CD GitLab avec règles de détection par dossier
└── README.md               # Documentation du projet
```

---

## Prérequis de l'infrastructure

Cette démonstration s'exécute sur une machine virtuelle Ubuntu ( son adrese ip est `192.168.126.131`) disposant des composants suivants :
- **Kubernetes** (avec `containerd` comme runtime, namespace `k8s.io`)
- **Docker** (pour la construction des images locales)
- **Terraform** (pour l'initialisation de l'infrastructure et des namespaces)
- **GitLab Runner** et/ou **Jenkins** (exécutés en conteneurs avec accès au `kubeconfig`)

---

## Déploiement Manuel Initial

Si vous déployez l'application pour la première fois sans passer par le pipeline CI/CD :

### 1. Construire les images Docker locales
```bash
docker build -t demo-backend:v1.0 ./backend
docker build -t demo-frontend:v1.0 ./frontend
```

### 2. Importer les images dans `containerd` (namespace `k8s.io`)
Kubernetes utilisant `containerd` directement en local sans registre externe, il est nécessaire d'importer les archives d'images :
```bash
docker save -o /tmp/demo-backend-v1.0.tar demo-backend:v1.0
docker save -o /tmp/demo-frontend-v1.0.tar demo-frontend:v1.0

sudo ctr -n k8s.io images import /tmp/demo-backend-v1.0.tar
sudo ctr -n k8s.io images import /tmp/demo-frontend-v1.0.tar
```

### 3. Appliquer les manifestes Kubernetes
```bash
kubectl get ns demo-app || kubectl create ns demo-app
kubectl apply -f ./backend/backend.yaml
kubectl apply -f ./frontend/frontend.yaml
```

### 4. Vérifier le déploiement
```bash
kubectl get pods,svc -n demo-app -o wide
curl -s http://127.0.0.1:30080/api/info
```
L'interface web est accessible depuis votre navigateur à l'adresse de votre machine : `http://192.168.126.131:30080`.

---

## Workflow de Mise à Jour Isolée via VS Code et GitLab CI

L'objectif principal de ce dépôt est de prouver qu'une modification sur un module n'entraîne aucun redémarrage ni interruption de service sur l'autre module.

### Principe de fonctionnement
Le fichier `.gitlab-ci.yml` utilise le mot-clé `rules:changes` :
- Une modification dans `backend/**/*` déclenche uniquement le job `deploy_backend`.
- Une modification dans `frontend/**/*` déclenche uniquement le job `deploy_frontend`.

### Étapes pour tester une mise à jour depuis VS Code
1. **Modifier un seul module** : Ouvrez le projet dans VS Code et éditez uniquement `backend/main.py` (par exemple, changez la valeur de `APP_VERSION` ou ajoutez un champ dans `/api/info`).
2. **Commiter et pousser vers GitLab** :
   ```bash
   git add backend/main.py
   git commit -m "feat(backend): mise à jour isolée de l'API"
   git push origin main
   ```
3. **Observer l'isolation sur Kubernetes** :
   ```bash
   kubectl get pods -n demo-app -w
   ```
   Vous constaterez que **seul le pod `api-backend` est recréé**, tandis que l'ancienneté (`AGE`) du pod `frontend` reste strictement inchangée.

<<<<<<< HEAD
---
=======
## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
=======
=======
>>>>>>> 0c58f52 (Readme update)
# Démonstration DevOps Modulaire : FastAPI, Nginx, Kubernetes & CI/CD

Ce dépôt contient le code source, les manifestes Kubernetes et les pipelines CI/CD permettant de démontrer **le découplage applicatif et le déploiement indépendant de modules** sur un cluster Kubernetes.

L'architecture repose sur deux microservices autonomes déployés dans le namespace `demo-app` :
- **`api-backend`** : API REST développée avec **FastAPI** (Python), exposée en interne via un service `ClusterIP` sur le port `8000`.
- **`frontend`** : Interface web statique servie par **Nginx**, exposée à l'extérieur via un service `NodePort` (`30080`) et faisant office de reverse-proxy vers le backend.

---

## Architecture et Arborescence

```text
.
├── backend/
│   ├── Dockerfile          # Image Python/Uvicorn pour FastAPI
│   ├── main.py             # Code source de l'API (/api/info)
│   └── backend.yaml        # Manifestes Deployment & Service (ClusterIP)
├── frontend/
│   ├── Dockerfile          # Image Nginx pour le frontend
│   ├── entrypoint.sh       # Script d'initialisation au démarrage du conteneur
│   ├── index.html          # Interface utilisateur web
│   └── frontend.yaml       # Manifestes Deployment & Service (NodePort 30080)
├── .gitlab-ci.yml          # Pipeline CI/CD GitLab avec règles de détection par dossier
└── README.md               # Documentation du projet
```

---

## Prérequis de l'infrastructure

Cette démonstration s'exécute sur une machine virtuelle Ubuntu ( son adrese ip est `192.168.126.131`) disposant des composants suivants :
- **Kubernetes** (avec `containerd` comme runtime, namespace `k8s.io`)
- **Docker** (pour la construction des images locales)
- **Terraform** (pour l'initialisation de l'infrastructure et des namespaces)
- **GitLab Runner** et/ou **Jenkins** (exécutés en conteneurs avec accès au `kubeconfig`)

---

## Déploiement Manuel Initial

Si vous déployez l'application pour la première fois sans passer par le pipeline CI/CD :

### 1. Construire les images Docker locales
```bash
docker build -t demo-backend:v1.0 ./backend
docker build -t demo-frontend:v1.0 ./frontend
```

### 2. Importer les images dans `containerd` (namespace `k8s.io`)
Kubernetes utilisant `containerd` directement en local sans registre externe, il est nécessaire d'importer les archives d'images :
```bash
docker save -o /tmp/demo-backend-v1.0.tar demo-backend:v1.0
docker save -o /tmp/demo-frontend-v1.0.tar demo-frontend:v1.0

sudo ctr -n k8s.io images import /tmp/demo-backend-v1.0.tar
sudo ctr -n k8s.io images import /tmp/demo-frontend-v1.0.tar
```

### 3. Appliquer les manifestes Kubernetes
```bash
kubectl get ns demo-app || kubectl create ns demo-app
kubectl apply -f ./backend/backend.yaml
kubectl apply -f ./frontend/frontend.yaml
```

### 4. Vérifier le déploiement
```bash
kubectl get pods,svc -n demo-app -o wide
curl -s http://127.0.0.1:30080/api/info
```
L'interface web est accessible depuis votre navigateur à l'adresse de votre machine : `http://192.168.126.131:30080`.

---

## Workflow de Mise à Jour Isolée via VS Code et GitLab CI

L'objectif principal de ce dépôt est de prouver qu'une modification sur un module n'entraîne aucun redémarrage ni interruption de service sur l'autre module.

### Principe de fonctionnement
Le fichier `.gitlab-ci.yml` utilise le mot-clé `rules:changes` :
- Une modification dans `backend/**/*` déclenche uniquement le job `deploy_backend`.
- Une modification dans `frontend/**/*` déclenche uniquement le job `deploy_frontend`.

### Étapes pour tester une mise à jour depuis VS Code
1. **Modifier un seul module** : Ouvrez le projet dans VS Code et éditez uniquement `backend/main.py` (par exemple, changez la valeur de `APP_VERSION` ou ajoutez un champ dans `/api/info`).
2. **Commiter et pousser vers GitLab** :
   ```bash
   git add backend/main.py
   git commit -m "feat(backend): mise à jour isolée de l'API"
   git push origin main
   ```
3. **Observer l'isolation sur Kubernetes** :
   ```bash
   kubectl get pods -n demo-app -w
   ```
   Vous constaterez que **seul le pod `api-backend` est recréé**, tandis que l'ancienneté (`AGE`) du pod `frontend` reste strictement inchangée.

---
>>>>>>> 52484bc (Initial commit)
>>>>>>> 0f20356 (Initial commit)
