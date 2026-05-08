# 🚀 Quick Kubernetes Setup

This guide provides the fastest path to get your ECommerce application running in Kubernetes.

## 📋 Prerequisites

- Docker Desktop installed and running
- Your ECommerce Docker image: `nayanarasse25/ecommerce-docker`
- kubectl CLI tool

## 🐳 Step 1: Enable Kubernetes in Docker Desktop

### Desktop Instructions
1. **Open Docker Desktop**
2. **Go to Settings** (gear icon ⚙️)
3. **Select Kubernetes** from left menu
4. **Enable Kubernetes**
   - Check "Enable Kubernetes"
   - Select "Kubernetes"
   - Click "Apply & Restart"
5. **Wait for Kubernetes to start** (2-3 minutes)

### Verify Kubernetes is Running
```bash
# Check if Kubernetes is available
kubectl cluster-info

# Should show:
# Kubernetes control plane is running at localhost:6443
# CoreDNS is running at https://localhost:6443/api/v1/namespaces/kube-system
```

## 🚀 Step 2: Create Kubernetes Namespace

```bash
# Create namespace for your application
kubectl create namespace ecommerce

# Verify namespace created
kubectl get namespace ecommerce
```

## 🚀 Step 3: Deploy Your ECommerce Application

### Create Deployment Manifest
```yaml
# ecommerce-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ecommerce-deployment
  namespace: ecommerce
  labels:
    app: ecommerce
    version: v1.0
spec:
  replicas: 2
  selector:
    matchLabels:
      app: ecommerce
  template:
    metadata:
      labels:
        app: ecommerce
        version: v1.0
    spec:
      containers:
      - name: ecommerce-app
        image: nayanarasse25/ecommerce-docker:latest
        ports:
        - containerPort: 80
        name: http
        env:
          - name: NODE_ENV
            value: "production"
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

### Create Service Manifest
```yaml
# ecommerce-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: ecommerce-service
  namespace: ecommerce
spec:
  selector:
    app: ecommerce
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

### Deploy to Kubernetes
```bash
# Apply all manifests
kubectl apply -f ecommerce-deployment.yaml
kubectl apply -f ecommerce-service.yaml

# Check deployment status
kubectl get deployment ecommerce-deployment -n ecommerce
kubectl get pods -n ecommerce
kubectl get services -n ecommerce

# Wait for pods to be ready
kubectl wait --for=condition=Ready pod --all -n ecommerce --timeout=300s
```

## 🌐 Step 4: Access Your Application

### Option A: Port Forwarding (Local Access)
```bash
# Forward service to local port
kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce

# Access your application
# Open: http://localhost:8080
```

### Option B: LoadBalancer (External Access)
```bash
# Get external IP
kubectl get service ecommerce-service -n ecommerce

# Access via external IP
# Open: http://<EXTERNAL-IP>
```

## 📊 Step 5: Monitor Your Application

### Check Pod Status
```bash
# List all pods with details
kubectl get pods -n ecommerce -o wide

# Get pod logs
kubectl logs -f deployment/ecommerce-deployment -n ecommerce

# Describe pod for troubleshooting
kubectl describe pod <pod-name> -n ecommerce
```

### Scale Your Application
```bash
# Scale to 3 replicas
kubectl scale deployment ecommerce-deployment --replicas=3 -n ecommerce

# Scale down to 1 replica
kubectl scale deployment ecommerce-deployment --replicas=1 -n ecommerce

# Check scaling status
kubectl get pods -n ecommerce
```

## 🔄 Step 6: Update Your Application

### Update Docker Image
```yaml
# Update deployment with new image version
kubectl set image deployment/ecommerce-deployment \
  nayanarasse25/ecommerce-docker:v2.0 \
  -n ecommerce

# Watch rollout status
kubectl rollout status deployment/ecommerce-deployment -n ecommerce
```

### Rollback if Needed
```bash
# Rollback to previous version
kubectl rollout undo deployment/ecommerce-deployment -n ecommerce

# Check rollback status
kubectl rollout status deployment/ecommerce-deployment -n ecommerce
```

## 🎯 Success Verification

### Your Application is Running When:
- ✅ Pods are in `Running` status
- ✅ Service has external IP or port forwarding works
- ✅ Application responds to HTTP requests
- ✅ Kubernetes shows desired replica count

### Troubleshooting Common Issues:
```bash
# If pods won't start
kubectl describe pod <pod-name> -n ecommerce

# If service has no external IP
kubectl get service ecommerce-service -n ecommerce -o wide

# If application not accessible
kubectl get events -n ecommerce --sort-by='.lastTimestamp'

# Delete and redeploy if needed
kubectl delete deployment ecommerce-deployment -n ecommerce
kubectl delete service ecommerce-service -n ecommerce
# Then apply manifests again
```

## 🎉 Kubernetes Success!

You now have:
- ✅ **Local Kubernetes Cluster**: Running in Docker Desktop
- ✅ **Application Deployed**: ECommerce running in pods
- ✅ **Service Exposed**: Accessible via port forwarding or LoadBalancer
- ✅ **Scalable**: Can scale replicas up/down
- ✅ **Monitoring**: Full visibility into application status

This completes your advanced DevSecOps journey with practical Kubernetes experience!
