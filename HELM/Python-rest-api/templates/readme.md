# 1. Build Docker image
```commandline
docker build -t manojkrishnapa/helm-python-rest-api .
```
# 2. Run Docker image
```commandline
docker run -p 9001:9001 manojkrishnapa/helm-python-rest-api
```
# 3 Docker Push
```commandline
docker push manojkrishnapa/helm-python-rest-api
```