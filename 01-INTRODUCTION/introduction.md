# KUBERNETES

Kubernetes is a powerful container orchestration platform, and it’s crucial for modern application deployment, management, and scaling in cloud-native environments. Here's why we need Kubernetes:

### 1. Container Management at Scale
Automation: Kubernetes automates the deployment, scaling, and management of containerized applications. Without Kubernetes, managing large numbers of containers across multiple machines would be complex and error-prone.
Orchestration: It handles the scheduling and running of containers on clusters of machines, ensuring that they’re distributed, replicated, and running as expected.
### 2. Scalability
Horizontal Scaling: Kubernetes makes it easy to scale applications up and down based on demand. It automatically adjusts the number of running instances of a containerized application based on CPU or memory usage, or custom metrics.
Auto-scaling: Kubernetes supports both horizontal pod autoscaling (scaling the number of pods based on load) and vertical pod autoscaling (adjusting resources per pod).
### 3. Fault Tolerance & Self-Healing
High Availability: Kubernetes monitors the health of containers and nodes. If a container or node fails, Kubernetes can automatically reschedule workloads to healthy nodes, ensuring minimal downtime.

Self-Healing: Kubernetes can restart failed containers, replace containers, or reschedule them on different nodes without human intervention.
### 4. Declarative Configuration
Kubernetes uses declarative configuration to define the desired state of applications. You specify what you want (e.g., how many replicas of a pod), and Kubernetes ensures that the system matches this state. If something changes or goes wrong, Kubernetes works to bring the system back to the desired state automatically.
### 5. Environment Consistency
Kubernetes abstracts away underlying infrastructure details, meaning your application can run consistently across different environments—whether it's on-premises, in a public cloud, or a hybrid setup.
Developers and operators can define applications in YAML files, ensuring that the same configurations work across different environments without needing manual tweaks.
### 6. Infrastructure Abstraction
Kubernetes decouples application development from the underlying hardware or cloud infrastructure. This makes it easier to switch between cloud providers or data centers without a major impact on how applications are deployed and managed.
Multi-cloud & Hybrid-cloud Support: It allows you to run applications across different cloud environments and even on-premise systems without vendor lock-in.
### 7. Microservices & Distributed Systems
Kubernetes is designed to manage applications composed of multiple loosely coupled services (microservices). It facilitates communication between microservices, such as load balancing and service discovery, while also allowing them to scale independently.
Networking and Load Balancing: Kubernetes handles networking between services and load balancing traffic automatically. It ensures services can discover each other through a built-in DNS system.
### 8. Efficient Resource Utilization
Kubernetes optimizes resource usage by dynamically allocating CPU and memory resources. It allows you to run workloads on bare metal or virtualized infrastructure while ensuring that resources are distributed efficiently.
### 9. Version Control & Rollbacks
Kubernetes supports rolling updates and rollbacks. This allows for seamless deployment of new versions of applications without downtime. If a new version of the application fails, Kubernetes can automatically roll back to the previous stable version.
### 10. CI/CD Integration
Kubernetes integrates well with continuous integration and continuous delivery (CI/CD) pipelines. You can automate the deployment of new code, run tests, and deploy updates in a consistent and repeatable manner.
### 11. Security
Kubernetes provides mechanisms like Role-Based Access Control (RBAC) to secure access to resources and control what users can do within a cluster.
It also supports network policies for controlling communication between services and can run containerized applications with specific security profiles to limit risks.
### 12. Ecosystem and Extensibility
Kubernetes has a vibrant ecosystem and a wide array of open-source tools built around it, such as Helm for package management, Istio for service meshes, and Prometheus for monitoring.
Kubernetes supports custom resource definitions (CRDs), which allow you to extend its functionality to suit your specific use cases.
## In Summary:
Kubernetes is essential because it automates and optimizes the complex tasks involved in deploying and managing containerized applications at scale. It helps with scaling, failover, monitoring, resource management, and simplifying application deployment, making it a cornerstone of modern DevOps, CI/CD, and cloud-native architectures. Without Kubernetes or a similar orchestrator, managing large, complex containerized environments would be a logistical nightmare.


# KUBERNETES ARCHITECTURE

![img.png](img.png)

```commandline
07:16:00 manojkrishnappa@Manojs-MacBook-Pro uday → kubectl get pods -n kube-system -o wide
NAME                                                        READY   STATUS    RESTARTS   AGE   IP           NODE                                NOMINATED NODE   READINESS GATES
coredns-7c65d6cfc9-g6xl4                                    1/1     Running   0          38m   10.244.0.2   manoj-cka-cluster-1-control-plane   <none>           <none>
coredns-7c65d6cfc9-g7g8r                                    1/1     Running   0          38m   10.244.0.3   manoj-cka-cluster-1-control-plane   <none>           <none>
etcd-manoj-cka-cluster-1-control-plane                      1/1     Running   0          38m   172.18.0.5   manoj-cka-cluster-1-control-plane   <none>           <none>
kindnet-48dd6                                               1/1     Running   0          38m   172.18.0.4   manoj-cka-cluster-1-worker          <none>           <none>
kindnet-ppgk8                                               1/1     Running   0          38m   172.18.0.5   manoj-cka-cluster-1-control-plane   <none>           <none>
kindnet-sdxp9                                               1/1     Running   0          38m   172.18.0.3   manoj-cka-cluster-1-worker2         <none>           <none>
kindnet-zz6hk                                               1/1     Running   0          38m   172.18.0.2   manoj-cka-cluster-1-worker3         <none>           <none>
kube-apiserver-manoj-cka-cluster-1-control-plane            1/1     Running   0          38m   172.18.0.5   manoj-cka-cluster-1-control-plane   <none>           <none>
kube-controller-manager-manoj-cka-cluster-1-control-plane   1/1     Running   0          38m   172.18.0.5   manoj-cka-cluster-1-control-plane   <none>           <none>
kube-proxy-lkpss                                            1/1     Running   0          38m   172.18.0.5   manoj-cka-cluster-1-control-plane   <none>           <none>
kube-proxy-qcph4                                            1/1     Running   0          38m   172.18.0.2   manoj-cka-cluster-1-worker3         <none>           <none>
kube-proxy-qkmjw                                            1/1     Running   0          38m   172.18.0.3   manoj-cka-cluster-1-worker2         <none>           <none>
kube-proxy-w486t                                            1/1     Running   0          38m   172.18.0.4   manoj-cka-cluster-1-worker          <none>           <none>
kube-scheduler-manoj-cka-cluster-1-control-plane            1/1     Running   0          38m   172.18.0.5   manoj-cka-cluster-1-control-plane   <none>           <none>

```

## Kubernetes Architecture Overview
Kubernetes is a container orchestration platform designed to automate the deployment, scaling, and operation of application containers. It has a complex yet well-defined architecture that is composed of several key components that work together to provide a scalable, reliable, and flexible platform for managing containerized applications.
Let’s break down the Kubernetes architecture into its key components:
### 1. Cluster Components
A Kubernetes cluster consists of two main parts: the control plane (responsible for managing the cluster) and the worker nodes (where your applications run).
### Control Plane
The control plane is responsible for the overall management of the Kubernetes cluster, making global decisions about scheduling, managing the state of the cluster, and responding to events (e.g., starting or stopping containers).
Key Components of the Control Plane:
### API Server (kube-apiserver):
•	The API server is the central management entity of Kubernetes, and it serves as the gateway to communicate with the cluster. It exposes the Kubernetes API, which is the interface that administrators and clients use to interact with Kubernetes (e.g., using kubectl, other Kubernetes services, or applications).
•	It is responsible for validating and processing REST requests, making decisions (such as scheduling) and updating resources in the etcd database.
•	All Kubernetes components communicate with each other via the API server.

### etcd:
•	etcd is a distributed key-value store used to store all cluster data, including configuration data, the state of the cluster, and metadata about the applications running in the cluster.
•	It ensures that the cluster is highly available and can quickly recover its state in case of failure. etcd is crucial for maintaining the consistency of the cluster.
•	For example, if you deploy a new pod or update a service, the state of the change is saved in etcd.
	
### Controller Manager (kube-controller-manager):
•	The controller manager runs a set of controllers, which are responsible for regulating the state of the cluster. Each controller is a process that watches the state of the cluster (through the API server) and ensures that the actual state matches the desired state.
•	For example, the Replication Controller ensures that the desired number of replicas for a pod is maintained. If a pod fails, the controller will create a new one.
•	There are various controllers for managing different Kubernetes resources, such as nodes, namespaces, deployments, and more.
### Scheduler (kube-scheduler):
•	The scheduler is responsible for selecting which node in the cluster will run a newly created pod. The decision is based on resource requirements (CPU, memory), policies (affinity/anti-affinity), constraints, and available resources in the cluster.
•	Once the scheduler decides on a node, it binds the pod to the selected node. The scheduler’s role is crucial for optimizing the performance and resource utilization of the cluster.

## Worker Nodes
Worker nodes are the machines (virtual or physical) where the actual applications (in the form of containers) run. A Kubernetes cluster can have many worker nodes, depending on the scale of the application.
### Key Components of a Worker Node:
###	Kubelet:
•	The kubelet is an agent that runs on each worker node. It ensures that the containers described in Kubernetes pod specifications are running and healthy on the node.
•	The kubelet constantly checks the status of the containers and reports back to the API server. It also interacts with container runtimes to start, stop, and maintain containers as per the pod specifications.
•	If a pod is not running or healthy, the kubelet will try to restart it based on the defined policies (e.g., restart policies).
### Kube Proxy:
•	The kube-proxy is responsible for maintaining network rules on nodes. These rules allow for communication between pods within the cluster and external clients.
•	It can manage services (load balancing), providing a stable IP address for a set of pods that might change over time due to scaling operations.
•	Kube Proxy uses either iptables or ipvs to forward traffic to the appropriate backend pods, ensuring that services remain accessible even as pods come and go.
###	Container Runtime:
•	The container runtime is the software responsible for running containers on a node. Kubernetes supports multiple container runtimes, such as Docker, containerd, and CRI-O.
•	The container runtime interacts with the kubelet to start and stop containers and manage the container lifecycle.


## KUBERNETES OBJECTS:
----

1) POD
2) REPLICASET
3) REPLICATION CONTROLLER
4) DEPLOYMENT
5) NAMESPACE
6) SERVICES
7) CONFIGMAP AND SECRET
8) STATEFULL SET
9) DEMONSET
10) PV AND PVC
11) PROBES


# POD

A pod is the smallest and simplest unit of deployment in kuberenets
it represents the single instance of the running process in the clsuter

**We can create a pod in two different ways** 

![img_1.png](img_1.png)


## Imperative 

```commandline
07:17:12 manojkrishnappa@Manojs-MacBook-Pro uday → kubectl get pods
No resources found in default namespace.

07:35:32 manojkrishnappa@Manojs-MacBook-Pro uday → kubectl run nginx --image=nginx
pod/nginx created

07:35:47 manojkrishnappa@Manojs-MacBook-Pro uday → kubectl get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          44s

```

## Declarative 

### pod.yml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-test-decl
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
    - containerPort: 80
```


```commandline
07:37:44 manojkrishnappa@Manojs-MacBook-Pro 01-INTRODUCTION → ls
img.png         img_1.png       introduction.md pod.yml
07:38:01 manojkrishnappa@Manojs-MacBook-Pro 01-INTRODUCTION → kubectl get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          2m18s
07:38:05 manojkrishnappa@Manojs-MacBook-Pro 01-INTRODUCTION → kubectl apply -f pod.yml 
pod/nginx-test-decl created
07:38:09 manojkrishnappa@Manojs-MacBook-Pro 01-INTRODUCTION → kubectl get pods
NAME              READY   STATUS              RESTARTS   AGE
nginx             1/1     Running             0          2m24s
nginx-test-decl   0/1     ContainerCreating   0          2s

07:38:21 manojkrishnappa@Manojs-MacBook-Pro 01-INTRODUCTION → kubectl get pods
NAME              READY   STATUS    RESTARTS   AGE
nginx             1/1     Running   0          3m23s
nginx-test-decl   1/1     Running   0          61s
```


