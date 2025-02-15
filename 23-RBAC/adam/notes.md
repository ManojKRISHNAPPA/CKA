Step 1: Create the adam User
Generate a private key and certificate for the adam user: This will allow adam to authenticate with the Kubernetes API server. You can use OpenSSL to generate a key and self-signed certificate.

bash
Copy
# Generate private key for 'adam'
openssl genpkey -algorithm RSA -out adam.key

# Create a Certificate Signing Request (CSR) for 'adam'
openssl req -new -key adam.key -out adam.csr -subj "/CN=adam"

# Create the certificate (self-signed for simplicity)
openssl x509 -req -in adam.csr -signkey adam.key -out adam.crt
You now have adam.key (private key) and adam.crt (certificate).

Step 2: Set up kubeconfig for the adam user
You need to set up a kubeconfig file for adam so they can interact with the cluster.

Add the user credentials (adam.key and adam.crt):

You can create a kubeconfig for adam by adding the user credentials. Assuming your Kubernetes context is kubernetes-admin:

bash
Copy
kubectl config set-credentials adam \
  --client-certificate=./adam.crt \
  --client-key=./adam.key
Set the context for adam:

Now that the user is set, you need to create a context for adam to use in the kubeconfig.

bash
Copy
kubectl config set-context adam-context \
  --cluster=your-cluster-name \
  --user=adam
Switch to the adam context:

bash
Copy
kubectl config use-context adam-context
Step 3: Create Role and RoleBinding for adam
To allow adam to read pods, you need to assign the appropriate role to them.

Create a Role (or ClusterRole if you need cluster-wide access):

You can create a Role that grants read access to Pods in the default namespace. Here’s a sample role.yml:

yaml
Copy
# pod-reader-role.yml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
Apply the role:

bash
Copy
kubectl apply -f pod-reader-role.yml
Create a RoleBinding to bind the pod-reader Role to adam:

Now, bind the role to the adam user using a RoleBinding.

yaml
Copy
# pod-reader-binding.yml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
  namespace: default
subjects:
- kind: User
  name: adam
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
Apply the RoleBinding:

bash
Copy
kubectl apply -f pod-reader-binding.yml
Step 4: Test the Permissions
Verify that adam can list the pods:

Switch to the adam context:

bash
Copy
kubectl config use-context adam-context
Run the following command to verify that adam has the required permissions to read pods:

bash
Copy
kubectl get pods
If the setup is correct, adam should be able to list pods in the default namespace.

Step 5: Delete the User (Optional)
If you need to delete the user (adam), you can delete the RoleBinding and user credentials.

Delete the RoleBinding for adam:

bash
Copy
kubectl delete rolebinding pod-reader-binding -n default
Delete the Role:

bash
Copy
kubectl delete role pod-reader -n default
Delete the adam credentials from the kubeconfig:

You can delete adam's credentials using:

bash
Copy
kubectl config delete-user adam
Delete the context for adam:

If you created a specific context for adam:

bash
Copy
kubectl config delete-context adam-context
(Optional) Delete adam.key and adam.crt files:

If you're done with these files, you can delete them:

bash
Copy
rm adam.key adam.crt
Summary of Key Files:
Role (pod-reader-role.yml): Grants the necessary permissions to read pods.
RoleBinding (pod-reader-binding.yml): Binds the pod-reader role to the adam user.
Kubeconfig for adam: Configures adam with the necessary credentials to interact with Kubernetes.