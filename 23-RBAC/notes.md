Previous class we have created the user and we have set him autherisation and authentication

Now how can we see the weather i can access pod

```commandline
(N/A:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/ [main+*] kubectl  auth can-i get pod
kubectl --context kind-manoj-cka-cluster -n default auth can-i get pod
yes

```
```commandline
(N/A:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/ [main+*] kubectl auth whoami
kubectl --context kind-manoj-cka-cluster -n default auth whoami
ATTRIBUTE   VALUE
Username    kubernetes-admin
Groups      [kubeadm:cluster-admins system:authenticated]
```
Since we have already created the uday user lets see weather he can access pods or not
```commandline
(N/A:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/ [main+*] kubectl auth can-i get pod --as uday
kubectl --context kind-manoj-cka-cluster -n default auth can-i get pod --as vinoth
no
```
in order access pod as uday he need role access 


Two types of apis
**core groups:**
if it looks like apps/v1 or any deployment pod any object you create that will be core group 

**name groups:**
apiVersion: rbac.authorization.k8s.io/v1

role.yml
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods"]
  verbs: ["get", "watch", "list"] ## this is type of access this only provide read only access
```

```commandline
(N/A:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl apply -f role.yml 
kubectl --context kind-manoj-cka-cluster -n default apply -f role.yml
role.rbac.authorization.k8s.io/pod-reader created

(N/A:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl get role
kubectl --context kind-manoj-cka-cluster -n default get role
NAME         CREATED AT
pod-reader   2025-02-14T13:15:16Z
```
```commandline
(N/A:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl describe role pod-reader
kubectl --context kind-manoj-cka-cluster -n default describe role pod-reader
Name:         pod-reader
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  ---------  -----------------  --------------  -----
  pods       []                 []              [get watch list]

```
## Sample YAML for role binding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
# This role binding allows "jane" to read pods in the "default" namespace.
# You need to already have a Role named "pod-reader" in that namespace.
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
# You can specify more than one "subject"
- kind: User
  name: vinoth # "name" is case sensitive
  apiGroup: rbac.authorization.k8s.io
roleRef:
  # "roleRef" specifies the binding to a Role / ClusterRole
  kind: Role #this must be Role or ClusterRole
  name: pod-reader # this must match the name of the Role or ClusterRole you wish to bind to
  apiGroup: rbac.authorization.k8s.io
```

```commandline
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl apply -f role-binding.yml 
kubectl apply -f role-binding.yml
rolebinding.rbac.authorization.k8s.io/read-pods configured
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl auth can-i get pods --as vinoth
kubectl auth can-i get pods --as vinoth
yes

```
```commandline
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl apply -f role-binding.yml 
kubectl apply -f role-binding.yml
rolebinding.rbac.authorization.k8s.io/read-pods configured
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl auth can-i get pods --as adam
kubectl auth can-i get pods --as adam
yes
```

Now setting authersation:

```commandline
kubectl config set-credentials adam \
  --client-key=../22-Authentication/adam.key \
  --client-certificate=../22-Authentication/adam.crt \
  --certificate-authority=../22-Authentication/ca.crt
```
```commandline
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl config set-context adam --cluster=kind-manoj-cka-cluster \  
> --user=adam
kubectl config set-context adam --cluster=kind-manoj-cka-cluster --user=adam
Context "adam" created.
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl config use-context adam
kubectl config use-context adam
Switched to context "adam".

```


```commandline
(adam:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/ [main+*] kubectl auth whoami            
kubectl auth whoami
ATTRIBUTE   VALUE
Username    adam
Groups      [system:authenticated]

```





kubectl config set-context adam-context \
>   --cluster=kind-manoj-cka-cluster \
>   --user=adam
