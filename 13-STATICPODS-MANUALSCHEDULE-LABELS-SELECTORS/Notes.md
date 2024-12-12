**Static Pods**

Static Pods are special types of pods managed directly by the kubelet on each node rather than through the Kubernetes API server.

**Key Characteristics of Static Pods:**
*   Not Managed by the Scheduler: Unlike deployments or replicasets, the Kubernetes scheduler does not manage static pods.
  *   Defined on the Node: Configuration files for static pods are placed directly on the node's file system, and the kubelet watches these files.
  *   Some examples of static pods are: ApiServer, Kube-scheduler, controller-manager, ETCD etc
  
**Managing Static Pods:**
  * SSH into the Node: You will gain access to the node where the static pod is defined.(Mostly the control plane node)
    * Modify the YAML File: Edit or create the YAML configuration file for the static pod.
    *   Remove the Scheduler YAML: To stop the pod, you must remove or modify the corresponding file directly on the node.
      * Default location": is usually /etc/kubernetes/manifests/; you can place the pod YAML in the directory, and Kubelet will pick it for scheduling.

Since we are using kind cluster it acts containers nodes so login to control plain component

```
01:43:28 manojkrishnappa@Manojs-MacBook-Pro CKA-Series ±|main ✗|→ docker ps | grep manoj-cka-
0c3a5c156442   kindest/node:v1.29.10   "/usr/local/bin/entr…"   2 hours ago   Up 2 hours                                                   manoj-cka-cluster-worker
a3f8f944a2ee   kindest/node:v1.29.10   "/usr/local/bin/entr…"   2 hours ago   Up 2 hours   0.0.0.0:80->80/udp, 127.0.0.1:59920->6443/tcp   manoj-cka-cluster-control-plane
2769dde1bb33   kindest/node:v1.29.10   "/usr/local/bin/entr…"   2 hours ago   Up 2 hours                                                   manoj-cka-cluster-worker2
a95642b4966a   kindest/node:v1.29.10   "/usr/local/bin/entr…"   2 hours ago   Up 2 hours                                                   manoj-cka-cluster-worker3

```

```commandline
01:43:51 manojkrishnappa@Manojs-MacBook-Pro CKA-Series ±|main ✗|→ docker exec -it manoj-cka-cluster-control-plane bash
root@manoj-cka-cluster-control-plane:/# cd /etc/kube
kubelet     kubernetes/ 
root@manoj-cka-cluster-control-plane:/# cd /etc/kubernetes/manifests/
root@manoj-cka-cluster-control-plane:/etc/kubernetes/manifests# ls
etcd.yaml  kube-apiserver.yaml  kube-controller-manager.yaml  kube-scheduler.yaml
```
if you remove this and scheuler and if you deploy it in the pod it wont scheudule

```commandline
root@manoj-cka-cluster-control-plane:/etc/kubernetes/manifests# ls
etcd.yaml  kube-apiserver.yaml  kube-controller-manager.yaml  kube-scheduler.yaml
root@manoj-cka-cluster-control-plane:/etc/kubernetes/manifests# mv kube-scheduler.yaml /tmp
```

We have removed the scheduler file here 
```commandline
(N/A:N/A)   ~/ kubectl get pods -n kube-system
kubectl --context kind-manoj-cka-cluster get pods -n kube-system
NAME                                                      READY   STATUS    RESTARTS   AGE
coredns-76f75df574-72fqc                                  1/1     Running   0          122m
coredns-76f75df574-gffgj                                  1/1     Running   0          122m
etcd-manoj-cka-cluster-control-plane                      1/1     Running   0          122m
kindnet-4xrcv                                             1/1     Running   0          122m
kindnet-6rwx8                                             1/1     Running   0          122m
kindnet-lffrm                                             1/1     Running   0          122m
kindnet-x69v6                                             1/1     Running   0          122m
kube-apiserver-manoj-cka-cluster-control-plane            1/1     Running   0          122m
kube-controller-manager-manoj-cka-cluster-control-plane   1/1     Running   0          122m
kube-proxy-82cvj                                          1/1     Running   0          122m
kube-proxy-9mfbd                                          1/1     Running   0          122m
kube-proxy-gdg9z                                          1/1     Running   0          122m
kube-proxy-p7wvx                                          1/1     Running   0          122m
```

Deploying the Pod without that 
```commandline
kubectl run nginx --image=nginx
kubectl --context kind-manoj-cka-cluster -n default run nginx --image=nginx
pod/nginx created

Here it wont shecule now it will be in pending state only

kubectl --context kind-manoj-cka-cluster -n default get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   0/1     Pending   0          49s

Now lets move back the kube-scheuler and try

root@manoj-cka-cluster-control-plane:/etc/kubernetes/manifests# mv /tmp/kube-scheduler.yaml .


kubectl --context kind-manoj-cka-cluster -n default get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          2m55s

```

**Manual Pod Scheduling**

Manual scheduling in Kubernetes involves assigning a pod to a specific node rather than letting the scheduler decide.

**Key Points:**
*   nodeName Field: Use this field in the pod specification to specify the node where the pod should run.
*   No Scheduler Involvement: When nodeName is specified, the scheduler bypasses the pod, and it’s directly assigned to the given node.


**Example Configuration:**
```commandline
apiVersion: v1
kind: Pod
metadata:
  name: manual-scheduled-pod
spec:
  nodeName: manoj-cka-cluster-worker2
  containers:
  - name: nginx
    image: nginx
```

````commandline
01:54:53 manojkrishnappa@Manojs-MacBook-Pro 13-STATICPODS-MANUALSCHEDULE-LABELS-SELECTORS ±|main ✗|→ kubectl apply -f manual-scheduled-pod.yml 
pod/manual-scheduled-pod created

01:55:11 manojkrishnappa@Manojs-MacBook-Pro 13-STATICPODS-MANUALSCHEDULE-LABELS-SELECTORS ±|main ✗|→ kubectl get pods -o wide
NAME                   READY   STATUS    RESTARTS   AGE     IP           NODE                        NOMINATED NODE   READINESS GATES
manual-scheduled-pod   1/1     Running   0          13s     10.244.2.5   manoj-cka-cluster-worker2   <none>           <none>
nginx                  1/1     Running   0          6m32s   10.244.1.6   manoj-cka-cluster-worker    <none>           <none>

````

## 📌 Labels and Selectors in Kubernetes

### Labels 🏷️
Labels are key-value pairs attached to Kubernetes objects like pods, services, and deployments. They help organize and group resources based on criteria that make sense to you.

**Examples of Labels:**
- `environment: production`
- `type: backend`
- `tier: frontend`
- `application: my-app`

### Selectors 🔍
Selectors filter Kubernetes objects based on their labels. This is incredibly useful for querying and managing a subset of objects that meet specific criteria.

**Common Usage:**
- **Pods**: `kubectl get pods --selector app=my-app`
- **Deployments**: Used to filter the pods managed by the deployment.
- **Services**: Filter the pods to which the service routes traffic.

### Labels vs. Namespaces 🌍
- **Labels**: Organize resources within the same or across namespaces.
- **Namespaces**: Provide a way to isolate resources from each other within a cluster.

### Annotations 📝
Annotations are similar to labels but attach non-identifying metadata to objects. For example, recording the release version of an application for information purposes or last applied configuration details etc.

---