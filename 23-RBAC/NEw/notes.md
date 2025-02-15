checking the certificate validatity
```commandline
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] openssl x509 -noout -dates -in ../../22-Authentication/adam.crt 
notBefore=Feb 15 03:55:55 2025 GMT
notAfter=Feb 16 03:55:55 2025 GMT

```

getting ca.crt 

```commandline
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl get nodes
kubectl get nodes
NAME                              STATUS   ROLES           AGE   VERSION
manoj-cka-cluster-control-plane   Ready    control-plane   40d   v1.31.2
manoj-cka-cluster-worker          Ready    <none>          40d   v1.31.2
manoj-cka-cluster-worker2         Ready    <none>          40d   v1.31.2
manoj-cka-cluster-worker3         Ready    <none>          40d   v1.31.2
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] docker exec -it manoj-cka-cluster-control-plane bash
root@manoj-cka-cluster-control-plane:/# cd /etc/kubernetes/pki/
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# ls
apiserver-etcd-client.crt     apiserver.crt  etcd                    front-proxy-client.key
apiserver-etcd-client.key     apiserver.key  front-proxy-ca.crt      sa.key
apiserver-kubelet-client.crt  ca.crt         front-proxy-ca.key      sa.pub
apiserver-kubelet-client.key  ca.key         front-proxy-client.crt
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# 

```
```commandline
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl get nodes
kubectl get nodes
NAME                              STATUS   ROLES           AGE   VERSION
manoj-cka-cluster-control-plane   Ready    control-plane   40d   v1.31.2
manoj-cka-cluster-worker          Ready    <none>          40d   v1.31.2
manoj-cka-cluster-worker2         Ready    <none>          40d   v1.31.2
manoj-cka-cluster-worker3         Ready    <none>          40d   v1.31.2
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] docker exec -it manoj-cka-cluster-control-plane bash
root@manoj-cka-cluster-control-plane:/# cd /etc/kubernetes/pki/
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# ls
apiserver-etcd-client.crt     apiserver.crt  etcd                    front-proxy-client.key
apiserver-etcd-client.key     apiserver.key  front-proxy-ca.crt      sa.key
apiserver-kubelet-client.crt  ca.crt         front-proxy-ca.key      sa.pub
apiserver-kubelet-client.key  ca.key         front-proxy-client.crt
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# 
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# ls
apiserver-etcd-client.crt     apiserver.crt  etcd                    front-proxy-client.key
apiserver-etcd-client.key     apiserver.key  front-proxy-ca.crt      sa.key
apiserver-kubelet-client.crt  ca.crt         front-proxy-ca.key      sa.pub
apiserver-kubelet-client.key  ca.key         front-proxy-client.crt
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# cat ca.crt 
-----BEGIN CERTIFICATE-----
MIIDBTCCAe2gAwIBAgIIdyZZ4sxpLy4wDQYJKoZIhvcNAQELBQAwFTETMBEGA1UE
AxMKa3ViZXJuZXRlczAeFw0yNTAxMDUwNTM5MzRaFw0zNTAxMDMwNTQ0MzRaMBUx
EzARBgNVBAMTCmt1YmVybmV0ZXMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQDQvJgZ7S/wrB1LURMO/HHTH/tV5alIK8Topm89d9sxgagPFE6y0oA2hk2y
TP3YUcOoxYGdsXFl40G5h5lMD170ouNsaUmqMZoEvIdlEdlWDEApioRRcNLcGVOv
FPtjlYQ4tAMB3Rm2oKjsCxsw0aiNSxzFcX4V2usQcxlS088ebktnccFIx54bq6lK
HyknA+QDRzZUpsnMn2kvmp+5vyvRGW2yBAxHFinn1Tei6cMbbqIv+zz1zY61fIT8
lSW9dhxiZDd4qHCt1kZ7pFn4BaMCmcOU0cvx9q811OxbZaxVhGkJUTMBO34/4YIy
DD9cMumdATVCdxQT6yyPkLmSyJkxAgMBAAGjWTBXMA4GA1UdDwEB/wQEAwICpDAP
BgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBSNBsK8FC+PShXQ3oI1NQWdLERQdTAV
BgNVHREEDjAMggprdWJlcm5ldGVzMA0GCSqGSIb3DQEBCwUAA4IBAQDPWk3TS2qF
jYNm0WdnD1eUuwu/lobpX0XC81T0gSfxSGtUoLjL8ZbDtnIh6kEOKJfyygpGp3jN
wKi2BYKK0RdqgI1ut9u/zznm7/0NixvmzenSeLETrMAyr5b4ACn4AHd2oTXGbeAn
Nq1uqb3HbaZym9aytG9eCLEZBElRjAAPvoOAQQaR539mmG4G/QlS2gWyE0yFkAwu
JfsN7FNwckHEQ/4ZWv1K6CFl0QeiwXzeVcGxbgVAOqqNZqFihSRem51VBa4tXqUv
diigC4dW+5iHGIzam1kfaXuQqWuwplHnN6LcRzgDCkLipSNm0aBR6gdd8O+F0+i7
oniP6qaxNTsm
-----END CERTIFICATE-----
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# 
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# ls
apiserver-etcd-client.crt     apiserver.crt  etcd                    front-proxy-client.key
apiserver-etcd-client.key     apiserver.key  front-proxy-ca.crt      sa.key
apiserver-kubelet-client.crt  ca.crt         front-proxy-ca.key      sa.pub
apiserver-kubelet-client.key  ca.key         front-proxy-client.crt
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# cat ca.key
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA0LyYGe0v8KwdS1ETDvxx0x/7VeWpSCvE6KZvPXfbMYGoDxRO
stKANoZNskz92FHDqMWBnbFxZeNBuYeZTA9e9KLjbGlJqjGaBLyHZRHZVgxAKYqE
UXDS3BlTrxT7Y5WEOLQDAd0ZtqCo7AsbMNGojUscxXF+FdrrEHMZUtPPHm5LZ3HB
SMeeG6upSh8pJwPkA0c2VKbJzJ9pL5qfub8r0RltsgQMRxYp59U3ounDG26iL/s8
9c2OtXyE/JUlvXYcYmQ3eKhwrdZGe6RZ+AWjApnDlNHL8favNdTsW2WsVYRpCVEz
ATt+P+GCMgw/XDLpnQE1QncUE+ssj5C5ksiZMQIDAQABAoIBAEgHfFkd/vgG/Ijb
7j6yoDihhaJrgNHVwLojjKlibbIUssCZWlrcxr+J8s+/P61g8aqQlRyseZwWIrz5
7M1RVIwIlX/4iSIAwcw2nmYjFaNa0N1E3koYK7slxjnZfLItixXiEFOZT2E06XWi
k3xyLL6tF72OX1r9UzY28ZsiWgt+ld0Iu8Qxtbs9VZMZItqkLhmtIQ9S4FnJcbeN
zNb/TYKMcxfkUQQwtTF1GbOEaD3iJbZOtBZwnvIZYRX2jNM4TgFDKm1QfiinVczb
VdQpQVxNuopgHMdaoNfYmitOoZpE7xJcmuV8kz2xQcC3V05HigSdLgKdY4jh70TF
bOoLPJECgYEA+lTrMCCVW1GoXytxX5i0vpf6TTiQTiYJvI0XYi/PHAkIBg3oPPw5
t7IQT5n7TZbXS4myfTyWYBQcmeGctRcJE0RAY6t7TPuV70+g8IiNqbrlMd5lgQmM
D+bWXJSmqAHGgCLaedEZ7lzxDzR02NrSNUwt2Ol9KXsBLT78XPmsRN0CgYEA1XaQ
eWW29xUBrygT4dnYuz1rDvslx6gO/tzcag0Q6uoKHm5m/IKAbBKg+aRGBXhWrwTe
ZM/EpJCBGzYNRWY3xdktVAoW+DzKTXUPKl3UzXFrEhoZTfV/ai3G1V9LsMmH5ghw
Qb06g6WIzIgOPJeOI59tzXsuNnXZ15LoCsihRmUCgYAdrtIQa9yp7l3ToxgXaMkN
zIGOhIV/7ry60dQS/W5Geb+s0BtYl+PUJ1YNykllIty2hUZX2UZPcDMQABOP2YJm
+XHVH7FIKJDXxo5j1x1NIe8pYaCRk2s7O3jxk2LLiyJZcUiMp0G25OhkkCjGyfOh
BD5veQgxUfeKwOw1rhlCNQKBgHLr8R4aX6WoPo7hQcr+8IrlpwSau51A4knd+CB0
Rl5if+4gO/vH+oG0icu84CHDxs9VDLIzlUePsKJIuF5biL1QjfHHuNQOTk/jLLX/
bDjqzd0iBeuNtvogCQMI2gQki7CRbHZH/P+xF/Qdb6S5Z0HQbFoK7jdNvWks4xYj
K4htAoGAUEoYEPReIBRJQrDgrSGnGSlQ2Uso2lFh+NEElqIZgOSwi5Gk2XpDOQCS
0oXsXKVMoCEceB4vNgUcaJ0it0HhPn9LpZR7pRcKY2Zf79yWmTnqJLazGEgea9hM
lnOBF4Km/9BeezacWo2XG5L5Vff8LTbDuxvn82tURR4CFrW8+3Q=
-----END RSA PRIVATE KEY-----
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# 
root@manoj-cka-cluster-control-plane:/etc/kubernetes/pki# exit
exit
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] openssl genrsa -out manoj.key 2048

Generating RSA private key, 2048 bit long modulus
..........................................................................................................+++++
................................................+++++
e is 65537 (0x10001)
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] openssl req -new -key manoj.key -out manoj.csr -subj "/CN=manoj"

(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] ls
ca.crt    ca.key    manoj.csr manoj.key notes.md
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] 
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] ls
ca.crt    ca.key    csr.yml   manoj.csr manoj.key notes.md
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl apply -f csr.yml 
kubectl apply -f csr.yml
certificatesigningrequest.certificates.k8s.io/manoj created
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] cat manoj.csr| base64 | tr -d "\n"

LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZUQ0NBVDBDQVFBd0VERU9NQXdHQTFVRUF3d0ZiV0Z1YjJvd2dnRWlNQTBHQ1NxR1NJYjNEUUVCQVFVQQpBNElCRHdBd2dnRUtBb0lCQVFDempiOUYxY0NmTUtDRmlxS25ucmpJSjVyZHFBOFdaeXJpbnovNEkwQkt5T0NaCnBHbXgrcS9aSlcrNS9oTG5uSmRLK3RtQmtkeTZna0VzMWo3SXArSElmS3JuT3NtenZUS3JvdkROWStrelUxOHgKTHZRZTZ3bWlyQlhGSEJhaFlLRGZDdUVpZTBTMTBqN0pPaFZBVytaTEkxakovWGo2amNQUXRXbEppbStHOS80NwpEbTh0bklyWWYwYTNQcUhrZWNLZDZBSjYzM1lGa2p0SE9BTHJsTjBSZHNjcDRTSVdkV1AzL0tvU0FTZFFNZFZZClBSM3NvUUQzWWI3OFFFeDF1VGdCYXJCa201ZzU0TEhGeHJSOHp4VGNVOXcwSG5ibzMzMlVLRFRsc25nbkVXcnIKR1NHZ05hckpxZXlJb1U4bmRXYSs5WlBJV2VKZVF5cU8vdFpLaWhyeEFnTUJBQUdnQURBTkJna3Foa2lHOXcwQgpBUXNGQUFPQ0FRRUFPVXdRWE96THB4b3cxSmdLdkN1cWk4bmtuaURua01Jdk45VmxtMVMzY2RoeTZMRStWMGdxClhWQkZMeDBYeVFzSno1T3ArREU5MllFL0FnSWhBd0hxcTQ0WXdDY000Tk9mRUlITnQ5OEZSeXVwTUw2czh3bkwKaEhMVnN0d0l0dGxYSlFhV0JuK1BjNzNVbUp1RDgvemhkQnhUV2h1bmRTZU9FdDlJWlA5V1lsNi9XY1k5MmlLTgpvb3pXbmZsTmNRdXZDUTRrZnFDakZTMGNFNHV2cFZSL3RISDZ1UG1EY3FPMTR1VlFOOU5BcUtnblpacTc0bzdlCitPTk90SjY4OXdIZ0F3Uks4bEtIdGRzc2xENEFBajJUVU1POGwvZXRubHBtM2IyZXdMZUlFVVlsT2M0Ym9pT3oKV3BscVJWeTgxSTUzd1duOEtHYWNQSXo5Z0kwZm9DYXppZz09Ci0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLQo=%                                                                           (kind-manoj-cka-cluster:N/A)   ~/Desktop/CL
```
```commandline
kubectl apply -f csr.yml
kubectl apply -f csr.yml
certificatesigningrequest.certificates.k8s.io/manoj configured
```

```commandline
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl get csr
kubectl get csr
NAME    AGE     SIGNERNAME                            REQUESTOR          REQUESTEDDURATION   CONDITION
adam    86m     kubernetes.io/kube-apiserver-client   kubernetes-admin   24h                 Approved,Issued
manoj   3m13s   kubernetes.io/kube-apiserver-client   kubernetes-admin   24h                 Pending
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl delete csr adam
kubectl delete csr adam
certificatesigningrequest.certificates.k8s.io "adam" deleted
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl certificate approve manoj
kubectl certificate approve manoj
certificatesigningrequest.certificates.k8s.io/manoj approved
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl auth can-i get pods --as manoj
kubectl auth can-i get pods --as manoj
no
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] 
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] ls
ca.crt    ca.key    csr.yml   manoj.csr manoj.key notes.md
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] 
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] ls
ca.crt           csr.yml          manoj.key        role-binding.yml
ca.key           manoj.csr        notes.md         role.yml
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl apply -f role.yml
kubectl apply -f role.yml
role.rbac.authorization.k8s.io/pod-reader unchanged
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl apply -f role-binding.yml
kubectl apply -f role-binding.yml
rolebinding.rbac.authorization.k8s.io/read-pods configured
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl config set-credentials manoj --client-key=manoj.key --client-certificate=manoj.crt --embed-certs=true
kubectl config set-credentials manoj --client-key=manoj.key --client-certificate=manoj.crt --embed-certs=true
error: could not stat client-certificate file manoj.crt: stat manoj.crt: no such file or directory
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl get csr -o yaml > manoj.crt
kubectl get csr -o yaml
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] echo "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM5akNDQWQ2Z0F3SUJBZ0lRTitDd1FWK1NOcXJHY1JnQjZTSWorVEFOQmdrcWhraUc5dzBCQVFzRkFEQVYKTVJNd0VRWURWUVFERXdwcmRXSmxjbTVsZEdWek1CNFhEVEkxTURJeE5UQTFNakV4TVZvWERUSTFNREl4TmpBMQpNakV4TVZvd0VURVBNQTBHQTFVRUF4TUdkbWx1YjNSb01JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBCk1JSUJDZ0tDQVFFQXZ2azE4cEJKUkgvc2ppOXEzWlRRNXIzVDl5VWVqeHpRWFMyalQwM3o3cVZ3MzROR0J3ZUEKZmE3TzhFbHRYN3BHNkR4NHcrNXlxczZYSm9Ddzhxc1BnR1JwQVpXU1VnKzEzSFcvMVNrUXZuYlhUemk3Nk5MbQpSUjJJRU5uOGc2VzJaRWVTNlFDRk5KTG1scE8zK0RNSnpTb1UvcFgvL21RaFJ4S0xWa0RFdlJ2VWJFdlA1N0xZClV6ODRvS3diRXVkbG1iUVYxUGhSaXZxWURRT2Zkbi9Pc3F0Vm5tUlg3Z2FGSndtMHpVeUdGak9reGRKSVRkbUEKYmYzYjZtQkg3Ukc1bnlwR3oxNm15Qm5KSFpNdEtzeXRVNmc1azhJMU9xSkp1UHFURm80MSs1ZFNNVW10dkVBTwpvTGpGK0NYZkV1alhQRzRNU3hUSVBnZFRIMlNpblZZSDd3SURBUUFCbzBZd1JEQVRCZ05WSFNVRUREQUtCZ2dyCkJnRUZCUWNEQWpBTUJnTlZIUk1CQWY4RUFqQUFNQjhHQTFVZEl3UVlNQmFBRkkwR3dyd1VMNDlLRmREZWdqVTEKQlowc1JGQjFNQTBHQ1NxR1NJYjNEUUVCQ3dVQUE0SUJBUUNqRFk1U0huZEpuWURnZTYyTkVnUER6eVZteEp6OApTamdCdS9IL2R6VlpkU3o3QU9jZTM4WVdCRkdXQWNTVHhGT3BuT2FwTEZtd0ZZSXowZVlCWTV0ZGtRb2JFZUgrCklpZGdCam9LL3JzZHduRjkxSzNVNHlneXJ5alRib2ltTUxwbVRtK3l2V1g1LzdnUFBBU2pmckhQdDZScFRmUmcKcXRMRGE4WU1KaGYxWjNRM1BYKzR1VVV1SlZBZURlcVdmR0U3ZTZYT3I1aURPS0tDVnUzT2s5MmZuQzNmMXNwagowM3JUSkNORmxiMkJJaGpuMHVubnFZUjR6MzBoWTRxbXAxQlNPQmNHNzkzWVpQNjZ5TXhBZjhmSkEyc0FwZUg5CmFxMVpDVStUeTNaK212OS8wSDJwdzdLR2JGeG5vejliUTlFcUVLYjEvUm94SWZpWUVsZG8yZHkwCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K" | base64 -d | tr -d "/n" > manoj.crt
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl config set-credentials manoj --client-key=manoj.key --client-certificate=manoj.crt --embed-certs=true
kubectl config set-credentials manoj --client-key=manoj.key --client-certificate=manoj.crt --embed-certs=true
User "manoj" set.
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl auth can-i get pods
kubectl auth can-i get pods
yes
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl config use-context manoj
kubectl config use-context manoj
error: no context exists with the name: "manoj"
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl config use-context manoj-context
kubectl config use-context manoj-context
error: no context exists with the name: "manoj-context"
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl config set-context manoj     
kubectl config set-context manoj
Context "manoj" created.
(kind-manoj-cka-cluster:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl config use-context manoj        
kubectl config use-context manoj
Switched to context "manoj".
(manoj:N/A)   ~/Desktop/CLASS/KUBERNETES/CKA-Series/23-RBAC/new/ [main+*] kubectl get pods                        
kubectl get pods
```