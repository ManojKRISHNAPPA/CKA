# HELM CHARTS
1. What is helm chart.?
    A Helm Chart is a package format for Kubernetes applications. It consists of a set of YAML files that define Kubernetes resources like Deployments, Services, ConfigMaps, and more. It essentially bundles all the Kubernetes manifests needed to deploy an application or service into a single package. Helm charts make it easier to deploy and manage applications on Kubernetes clusters.
    Helm itself is a package manager for Kubernetes, similar to how apt or yum is used for managing packages in Linux-based systems.    
![img.png](img.png)
![img_1.png](img_1.png)

2. Why we need in kubernetes..?
Without Helm, you would have to manually define Kubernetes resources for each application, and managing these resources can become quite complex, especially as your app grows or as you deploy multiple apps with similar configurations. 
**Here’s why Helm is useful:**
**Simplifies Deployment:** You can deploy complex applications with just a single command (helm install).
**Version Control:** Helm charts allow you to version-control the deployments, which is important when you need to upgrade or roll back releases.
**Reuse:** Helm charts are reusable and shareable. You can either use pre-existing charts from repositories like Helm Hub or create your own.
**Configuration Management:** Helm provides easy ways to manage configuration changes by using values files (values.yaml), so you don’t need to modify your Kubernetes resource definitions directly.

3. How helm chart will help us to manage k8s
Helm provides a streamlined approach to managing Kubernetes applications by:
**Packaging:** Helm allows you to package your Kubernetes applications and manage them as a unit. This reduces duplication and simplifies deployment.
**Dependency Management:** Helm charts can declare dependencies on other charts, making it easy to deploy multi-component applications (e.g., a web application with a backend database).
**Release Management:** Helm allows you to track different "releases" of an application. Each release has its own configuration, and Helm can roll back to a previous version if something goes wrong.
**Templating:** Helm uses templates to dynamically generate Kubernetes manifests. You can use variables in your chart’s YAML files and provide values at the time of deployment to customize the setup.
**Upgrade and Rollback:** Helm supports easy upgrades and rollbacks. You can roll back to any previous release version with a simple command if the current deployment fails.
![img_2.png](img_2.png)

4. How to install helm chart.?
   1. Install Helm on your local machine:
   You can install Helm using a package manager like Homebrew (macOS) or download it directly for your operating system.

**For macOS (with Homebrew):**
```commandline
brew install helm
```
**For Linux (using a script):**
```commandline
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```
**For Windows, you can use Chocolatey:**
```commandline
choco install kubernetes-helm
```
**2. Initialize Helm (if needed):**
```commandline
helm repo add stable https://charts.helm.sh/stable
helm repo update
```
**3. Install a Chart:**
```commandline
helm install nginx-ingress stable/nginx-ingress
```
**4. Use Custom Values:**
```commandline
helm install my-app stable/my-chart -f custom-values.yaml
```
**5.Upgrade an Existing Release:**
```commandline
helm upgrade my-app stable/my-chart
```
6. Uninstall a Helm Release:
```commandline
helm uninstall my-app
```
---
## hands on
```commandline
root@ip-172-31-17-47:~# curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11903  100 11903    0     0   276k      0 --:--:-- --:--:-- --:--:--  276k
Downloading https://get.helm.sh/helm-v3.17.0-linux-amd64.tar.gz
Verifying checksum... Done.
Preparing to install helm into /usr/local/bin
helm installed into /usr/local/bin/helm
root@ip-172-31-17-47:~#
```
![img_3.png](img_3.png)

## CREATING A FIRST HELM CHART
```commandline
root@ip-172-31-17-47:~# curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11903  100 11903    0     0   276k      0 --:--:-- --:--:-- --:--:--  276k
Downloading https://get.helm.sh/helm-v3.17.0-linux-amd64.tar.gz
Verifying checksum... Done.
Preparing to install helm into /usr/local/bin
helm installed into /usr/local/bin/helm
root@ip-172-31-17-47:~#
root@ip-172-31-17-47:~#
root@ip-172-31-17-47:~# helm create helloworld
Creating helloworld
root@ip-172-31-17-47:~# ls -lart | grep helloworld
drwxr-xr-x  4 root root 4096 Jan 27 14:14 helloworld
root@ip-172-31-17-47:~# cd helloworld/
root@ip-172-31-17-47:~/helloworld# ls
Chart.yaml  charts  templates  values.yaml
root@ip-172-31-17-47:~/helloworld# ls charts/
root@ip-172-31-17-47:~/helloworld# ls
Chart.yaml  charts  templates  values.yaml
root@ip-172-31-17-47:~/helloworld# cd charts/
root@ip-172-31-17-47:~/helloworld/charts# ls
root@ip-172-31-17-47:~/helloworld/charts# cd ../templates/
root@ip-172-31-17-47:~/helloworld/templates# ls
NOTES.txt  _helpers.tpl  deployment.yaml  hpa.yaml  ingress.yaml  service.yaml  serviceaccount.yaml  tests
root@ip-172-31-17-47:~/helloworld/templates# tree
Command 'tree' not found, but can be installed with:
snap install tree  # version 2.1.3+pkg-5852, or
apt  install tree  # version 2.1.1-2
See 'snap info tree' for additional versions.
root@ip-172-31-17-47:~/helloworld/templates# snap install tree
tree 2.1.3+pkg-5852 from 林博仁(Buo-ren Lin) (brlin) installed
root@ip-172-31-17-47:~/helloworld/templates# tree
.
├── NOTES.txt
├── _helpers.tpl
├── deployment.yaml
├── hpa.yaml
├── ingress.yaml
├── service.yaml
├── serviceaccount.yaml
└── tests
    └── test-connection.yaml

2 directories, 8 files
root@ip-172-31-17-47:~/helloworld/templates# cd ..
root@ip-172-31-17-47:~/helloworld# ks
Command 'ks' not found, but can be installed with:
apt install qdl
root@ip-172-31-17-47:~/helloworld# ls
Chart.yaml  charts  templates  values.yaml
root@ip-172-31-17-47:~/helloworld# tree
.
├── Chart.yaml
├── charts
├── templates
│   ├── NOTES.txt
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   ├── serviceaccount.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml

4 directories, 10 files
```
2.2: Update the service.type from ClusterIP to NodePort inside the values.yml
Before you run your helloworld Helm Chart we need to update the service.type from ClusterIP to NodePort.

The reason for this change is - After installing/running the helloworld Helm Chart we should be able to access the service outside of the kubernetes cluster. And if you do not change the service.type then you will only be able to access the service withing kubernetes cluster.

To update the values.yml, first go inside the directory helloworld

change in values.yml
```commandline
service:
  # This sets the service type more information can be found here: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types
  type: NodePort
  # This sets the ports more information can be found here: https://kubernetes.io/docs/concepts/services-networking/service/#field-spec-ports
  port: 80

```
```commandline
root@ip-172-31-17-47:~# helm install myhelloworld helloworld
NAME: myhelloworld
LAST DEPLOYED: Mon Jan 27 14:26:38 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services myhelloworld)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
root@ip-172-31-17-47:~# helm list -a
NAME        	NAMESPACE	REVISION	UPDATED                               	STATUS  	CHART           	APP VERSION
myhelloworld	default  	1       	2025-01-27 14:26:38.80614407 +0000 UTC	deployed	helloworld-0.1.0	1.16.0
root@ip-172-31-17-47:~# kubectl get svc
NAME           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
kubernetes     ClusterIP   10.152.183.1     <none>        443/TCP        18m
myhelloworld   NodePort    10.152.183.209   <none>        80:32648/TCP   37s
```

![img_5.png](img_5.png)

To view dashboard status
```commandline
microk8s dashboard-proxy
Checking if Dashboard is running.
Infer repository core for addon dashboard
Infer repository core for addon metrics-server
Waiting for Dashboard to come up.
Trying to get token from microk8s-dashboard-token
Waiting for secret token (attempt 0)
Dashboard will be available at https://127.0.0.1:10443
Use the following token to login:
eyJhbGciOiJSUzI1NiIsImtpZCI6Ik1hS0lrbU45bXEzNzQzblgyV1RfQWtTOHFLTEZWbzQtbElmYURPVC1rX1EifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJtaWNyb2s4cy1kYXNoYm9hcmQtdG9rZW4iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjA1MTQ3YTA1LWEyM2UtNDU0My04NWRmLWU0OGEwMGUzNzk5ZiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlLXN5c3RlbTpkZWZhdWx0In0.SafUeDkI_vnRiTfCg5lgGPkjlimS01nAnJNCvCAOwQXVHcWH40OH6yCMAZgYNFKOxG50fWrBgoVHCEh4OOoh663WK5_XWmdBZPNFciAzDZFis9i1BZ8te7240VVro-m_tD7pO-xM9D_O5aYLyRJ3_n4EimVi9AcfNLLLt0qsbIFwEH3yZB5mO3UBQdfWbjcNyVk7vVFMufzQQxc6JJIdzCbA5lG3bv5NgiWWtxGzrsfiHHt73mboFFroI9op5WmZHNFfw7-yRjzkclg-IfK-Zjm4T1at8k35hagYHZr4xrHi90rBna4RhD09XDh1BVpZF5bNxuqbKFyCApLRpPawcg
```

Unistalling the hello-world
```commandline
root@ip-172-31-17-47:~# helm list -a
NAME        	NAMESPACE	REVISION	UPDATED                               	STATUS  	CHART           	APP VERSION
myhelloworld	default  	1       	2025-01-27 14:26:38.80614407 +0000 UTC	deployed	helloworld-0.1.0	1.16.0
root@ip-172-31-17-47:~# helm uninstall myhelloworld
release "myhelloworld" uninstalled
root@ip-172-31-17-47:~# helm uninstall helloworld
Error: uninstall: Release not loaded: helloworld: release: not found
root@ip-172-31-17-47:~#
```

# CHAPTER 3 
## HELM CLI COMMANDS

![img_6.png](img_6.png)

![img_7.png](img_7.png)
```commandline
root@ip-172-31-17-47:~# helm create helloworld
Creating helloworld
root@ip-172-31-17-47:~# ls
helloworld  snap
root@ip-172-31-17-47:~# cd helloworld/
root@ip-172-31-17-47:~/helloworld# tree
.
├── Chart.yaml
├── charts
├── templates
│   ├── NOTES.txt
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   ├── serviceaccount.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml

4 directories, 10 files
```


```commandline
root@ip-172-31-17-47:~# helm install myhelloworld helloworld
NAME: myhelloworld
LAST DEPLOYED: Mon Jan 27 14:39:40 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=helloworld,app.kubernetes.io/instance=myhelloworld" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

here is the first revision

```commandline
root@ip-172-31-17-47:~# helm list -a
NAME        	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART           	APP VERSION
myhelloworld	default  	1       	2025-01-27 14:39:40.364554311 +0000 UTC	deployed	helloworld-0.1.0	1.16.0
```

![img_8.png](img_8.png)

here my just for demo am changing replicas count values.yml is 2

```commandline
root@ip-172-31-17-47:~/helloworld# ls
Chart.yaml  charts  templates  values.yaml
root@ip-172-31-17-47:~/helloworld# vi values.yaml
root@ip-172-31-17-47:~/helloworld#
```
```commandline
root@ip-172-31-17-47:~# helm upgrade myhelloworldrelease helloworld/
Error: UPGRADE FAILED: "myhelloworldrelease" has no deployed releases
root@ip-172-31-17-47:~# helm upgrade myhelloworld helloworld/
Release "myhelloworld" has been upgraded. Happy Helming!
NAME: myhelloworld
LAST DEPLOYED: Mon Jan 27 14:42:55 2025
NAMESPACE: default
STATUS: deployed
REVISION: 2
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=helloworld,app.kubernetes.io/instance=myhelloworld" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
root@ip-172-31-17-47:~# helm ls -a
NAME        	NAMESPACE	REVISION	UPDATED                               	STATUS  	CHART           	APP VERSION
myhelloworld	default  	2       	2025-01-27 14:42:55.66008303 +0000 UTC	deployed	helloworld-0.1.0	1.16.0
```
# how to rollback 
```commandline
root@ip-172-31-17-47:~# helm rollback myhelloworld 1
Rollback was a success! Happy Helming!
root@ip-172-31-17-47:~# helm ls -a
NAME        	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART           	APP VERSION
myhelloworld	default  	3       	2025-01-27 14:44:12.622364522 +0000 UTC	deployed	helloworld-0.1.0	1.16.0
```

![img_9.png](img_9.png)

```commandline
root@ip-172-31-17-47:~# ls
helloworld  snap
root@ip-172-31-17-47:~# helm install test --debug  --dry-run helloworld
install.go:225: 2025-01-27 14:45:35.927226646 +0000 UTC m=+0.043787702 [debug] Original chart version: ""
install.go:242: 2025-01-27 14:45:35.927280082 +0000 UTC m=+0.043840945 [debug] CHART PATH: /root/helloworld

NAME: test
LAST DEPLOYED: Mon Jan 27 14:45:35 2025
NAMESPACE: default
STATUS: pending-install
REVISION: 1
USER-SUPPLIED VALUES:
{}

COMPUTED VALUES:
affinity: {}
autoscaling:
  enabled: false
  maxReplicas: 100
  minReplicas: 1
  targetCPUUtilizationPercentage: 80
fullnameOverride: ""
image:
  pullPolicy: IfNotPresent
  repository: nginx
  tag: ""
imagePullSecrets: []
ingress:
  annotations: {}
  className: ""
  enabled: false
  hosts:
  - host: chart-example.local
    paths:
    - path: /
      pathType: ImplementationSpecific
  tls: []
livenessProbe:
  httpGet:
    path: /
    port: http
nameOverride: ""
nodeSelector: {}
podAnnotations: {}
podLabels: {}
podSecurityContext: {}
readinessProbe:
  httpGet:
    path: /
    port: http
replicaCount: 2
resources: {}
securityContext: {}
service:
  port: 80
  type: ClusterIP
serviceAccount:
  annotations: {}
  automount: true
  create: true
  name: ""
tolerations: []
volumeMounts: []
volumes: []

HOOKS:
---
# Source: helloworld/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "test-helloworld-test-connection"
  labels:
    helm.sh/chart: helloworld-0.1.0
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: test
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['test-helloworld:80']
  restartPolicy: Never
MANIFEST:
---
# Source: helloworld/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: test-helloworld
  labels:
    helm.sh/chart: helloworld-0.1.0
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: test
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: helloworld/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: test-helloworld
  labels:
    helm.sh/chart: helloworld-0.1.0
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: test
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: test
---
# Source: helloworld/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-helloworld
  labels:
    helm.sh/chart: helloworld-0.1.0
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: test
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 2
  selector:
    matchLabels:
      app.kubernetes.io/name: helloworld
      app.kubernetes.io/instance: test
  template:
    metadata:
      labels:
        helm.sh/chart: helloworld-0.1.0
        app.kubernetes.io/name: helloworld
        app.kubernetes.io/instance: test
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: test-helloworld
      containers:
        - name: helloworld
          image: "nginx:1.16.0"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http

NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=helloworld,app.kubernetes.io/instance=test" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
![img_10.png](img_10.png)
```commandline
root@ip-172-31-17-47:~# helm template helloworld
---
# Source: helloworld/templates/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: release-name-helloworld
  labels:
    helm.sh/chart: helloworld-0.1.0
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
automountServiceAccountToken: true
---
# Source: helloworld/templates/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: release-name-helloworld
  labels:
    helm.sh/chart: helloworld-0.1.0
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: release-name
---
# Source: helloworld/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: release-name-helloworld
  labels:
    helm.sh/chart: helloworld-0.1.0
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
spec:
  replicas: 2
  selector:
    matchLabels:
      app.kubernetes.io/name: helloworld
      app.kubernetes.io/instance: release-name
  template:
    metadata:
      labels:
        helm.sh/chart: helloworld-0.1.0
        app.kubernetes.io/name: helloworld
        app.kubernetes.io/instance: release-name
        app.kubernetes.io/version: "1.16.0"
        app.kubernetes.io/managed-by: Helm
    spec:
      serviceAccountName: release-name-helloworld
      containers:
        - name: helloworld
          image: "nginx:1.16.0"
          imagePullPolicy: IfNotPresent
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /
              port: http
          readinessProbe:
            httpGet:
              path: /
              port: http
---
# Source: helloworld/templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "release-name-helloworld-test-connection"
  labels:
    helm.sh/chart: helloworld-0.1.0
    app.kubernetes.io/name: helloworld
    app.kubernetes.io/instance: release-name
    app.kubernetes.io/version: "1.16.0"
    app.kubernetes.io/managed-by: Helm
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['release-name-helloworld:80']
  restartPolicy: Never
```
![img_11.png](img_11.png)

```commandline
root@ip-172-31-17-47:~# helm lint helloworld
==> Linting helloworld
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
root@ip-172-31-17-47:~#
```
```commandline
root@ip-172-31-17-47:~# helm ls -a
NAME        	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART           	APP VERSION
myhelloworld	default  	3       	2025-01-27 14:44:12.622364522 +0000 UTC	deployed	helloworld-0.1.0	1.16.0
root@ip-172-31-17-47:~# helm unistall myhelloworld
Error: unknown command "unistall" for "helm"

Did you mean this?
	install
	uninstall

Run 'helm --help' for usage.
root@ip-172-31-17-47:~# helm uninstall myhelloworld
release "myhelloworld" uninstalled
```
![img_12.png](img_12.png)

