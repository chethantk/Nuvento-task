GitHub Repositories
Scenario
Description
GitHub Repository Link

1. Pokémon API Scanner Python script
GitHub - Scenario 1 (https://github.com/chethantk/pokemon-api-scanner)
2. Dockerized version of the scanner using Alpine Linux
GitHub - Scenario 2 (https://github.com/chethantk/Nuvento-task/blob/master/Dockerfile)
3. Helm chart to deploy scanner on Minikube
GitHub - Scenario 3 (https://github.com/chethantk/Nuvento-task/tree/master/pokemon-api-chart)


🐳 Docker Hub Link
Docker Image:
https://hub.docker.com/repository/docker/chethantk/pokemon-scanner-alpine


📄 Documentation
✅ Scenario 1: Pokémon API Scanner
pip install -r requirements.txt
python pokemon_scanner.py pikachu

 Output(JSON)
{
  "name": "pikachu",
  "base_experience": 112,
  "height": 4,
  "weight": 60,
  "abilities": [
    "static",
    "lightning-rod"
  ]
}

=======================

✅ Scenario 2: Containerization

Build Docker Image:

docker build -t chethantk/pokemon-scanner .

Run Container:

docker run chethantk/pokemon-scanner pikachu

==================

✅ Scenario 3: Helm Deployment on Minikube

Start Minikube:

minikube start

Install Helm chart:

helm install pokemon-scanner ./pokemon-scanner-chart

Manually run the pod:

kubectl get pods
kubectl exec -it <pod-name> -- python pokemon_scanner.py pikachu
eg: kubectl exec -it pokemon-api-release-pokemon-api-chart-7cdc86fd79-gh92q -- /bin/sh

root@IN5782-01:/home/dish/task/Nuvento-task# kubectl exec -it pokemon-api-release-pokemon-api-chart-7cdc86fd79-gh92q -- /bin/sh
/app # python pokemon_scanner.py pikachu
{
    "name": "pikachu",
    "base_experience": 112,
    "height": 4,
    "weight": 60,
    "abilities": [
        "static",
        "lightning-rod"
    ]
}

