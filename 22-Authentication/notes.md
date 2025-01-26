# Kubernetes Authentication and Authorization

## Authentication: Verifying Who You Are
Imagine your cluster is a fortress. 
Authentication is like checking IDs at the gate. Kubeconfig is your keycard containing certificates that identify you to the Kubernetes API server.

![img.png](img.png)

**Making API Calls:**
bashnst a cluster, you can use the below command

kubectl get pods -- kubeconfig config


