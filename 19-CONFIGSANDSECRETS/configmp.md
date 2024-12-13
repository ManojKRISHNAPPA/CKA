# kubernetes configmap and secret

### What is a config map in Kubernetes?
- When your manifest grows it becomes difficult to manage multiple env vars
- You can take this out of the manifest and store as a config map object in the key-value pair
- Then you can inject that config map into the pod
- You can reuse the same config map into multiple pods

#### Sample command to create a config map

```
- kubectl create cm <configmapname> --from-literal=color=blue \
--from-literal=color=red
```
Where color=clue is the key and value of the config map

#### Secrets

Follow the doc: https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data


```yaml
apiVersion: v1
data:
  firstname: Manoj
  lastname: Krishnappa
kind: ConfigMap
metadata:
  name: app-cm
```
```commandline
01:03:35 manojkrishnappa@Manojs-MacBook-Pro 19-CONFIGSANDSECRETS ±|main ✗|→ kubectl apply -f config.yml 
configmap/app-cm created

01:03:46 manojkrishnappa@Manojs-MacBook-Pro 19-CONFIGSANDSECRETS ±|main ✗|→ kubectl get cm
NAME               DATA   AGE
app-cm             2      9s
kube-root-ca.crt   1      25h

```

pod.yml
```commandline
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app.kubernetes.io/name: MyApp
spec:
  containers:
  - name: myapp-container
    image: busybox:1.28
    env:
    - name: FIRSTNAME
      valueFrom:
        configMapKeyRef:
          name: app-cm
          key: firstname
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
```

```commandline
01:05:17 manojkrishnappa@Manojs-MacBook-Pro 19-CONFIGSANDSECRETS ±|main ✗|→ kubectl describe pod myapp-pod
Name:             myapp-pod
Namespace:        default
Priority:         0
Service Account:  default
Node:             manoj-cka-cluster-worker/172.18.0.2
Start Time:       Fri, 13 Dec 2024 13:05:10 +0530
Labels:           app.kubernetes.io/name=MyApp
Annotations:      <none>
Status:           Running
IP:               10.244.1.22
IPs:
  IP:  10.244.1.22
Containers:
  myapp-container:
    Container ID:  containerd://ad62b0a03152963ed1662e4dfa0caba8e36eed2e2f362610b945fd7ebe2cdb4b
    Image:         busybox:1.28
    Image ID:      docker.io/library/busybox@sha256:141c253bc4c3fd0a201d32dc1f493bcf3fff003b6df416dea4f41046e0f37d47
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
      echo The app is running! && sleep 3600
    State:          Running
      Started:      Fri, 13 Dec 2024 13:05:11 +0530
    Ready:          True
    Restart Count:  0
    Environment:
      FIRSTNAME:  <set to the key 'firstname' of config map 'app-cm'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-c6pnq (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-c6pnq:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  49s   default-scheduler  Successfully assigned default/myapp-pod to manoj-cka-cluster-worker
  Normal  Pulled     48s   kubelet            Container image "busybox:1.28" already present on machine
  Normal  Created    48s   kubelet            Created container myapp-container
  Normal  Started    48s   kubelet            Started container myapp-container
01:05:59 manojkrishnappa@Manojs-MacBook-Pro 19-CONFIGSANDSECRETS ±|main ✗|→ 

```

```commandline
    Environment:
      FIRSTNAME:  <set to the key 'firstname' of config map 'app-cm'>  Optional: false
```

```commandline
01:07:53 manojkrishnappa@Manojs-MacBook-Pro 19-CONFIGSANDSECRETS ±|main ✗|→ kubectl exec -it myapp-pod -- printenv
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=myapp-pod
FIRSTNAME=Manoj
PHP_APACHE_PORT_80_TCP_PORT=80
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
MYSERVICE_PORT_80_TCP=tcp://10.96.96.227:80
MYDB_PORT=tcp://10.96.139.180:80
PHP_APACHE_PORT_80_TCP=tcp://10.96.201.88:80
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
MYSERVICE_PORT_80_TCP_PROTO=tcp
PHP_APACHE_SERVICE_HOST=10.96.201.88
MYSERVICE_PORT_80_TCP_ADDR=10.96.96.227
MYDB_SERVICE_HOST=10.96.139.180
KUBERNETES_SERVICE_HOST=10.96.0.1
MYSERVICE_PORT=tcp://10.96.96.227:80
MYDB_SERVICE_PORT=80
MYDB_PORT_80_TCP=tcp://10.96.139.180:80
MYDB_PORT_80_TCP_PORT=80
PHP_APACHE_PORT_80_TCP_ADDR=10.96.201.88
PHP_APACHE_PORT_80_TCP_PROTO=tcp
MYSERVICE_SERVICE_PORT=80
PHP_APACHE_PORT=tcp://10.96.201.88:80
MYSERVICE_PORT_80_TCP_PORT=80
MYDB_PORT_80_TCP_PROTO=tcp
MYDB_PORT_80_TCP_ADDR=10.96.139.180
PHP_APACHE_SERVICE_PORT=80
MYSERVICE_SERVICE_HOST=10.96.96.227
KUBERNETES_SERVICE_PORT=443
TERM=xterm
HOME=/root

```