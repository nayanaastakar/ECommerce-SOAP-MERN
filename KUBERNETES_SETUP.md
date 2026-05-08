# ☸️ Kubernetes Setup Guide

This guide will help you learn Kubernetes for advanced DevSecOps practices after completing Levels 1-5.

## 📋 Prerequisites

- Completed DevSecOps Levels 1-5 (Git, Docker, Jenkins, Azure)
- Basic understanding of containers and orchestration
- Your Dockerized ECommerce application
- Kubernetes cluster access (local or cloud)
- kubectl CLI tool installed

## 🎯 Kubernetes Learning Objectives

### What is Kubernetes?
- **Container Orchestration**: Manages multiple containers at scale
- **Self-Healing**: Automatically restarts failed containers
- **Load Balancing**: Distributes traffic across containers
- **Scaling**: Auto-scales based on resource usage
- **Service Discovery**: Containers find and communicate with each other

### Key Concepts
- **Pods**: Smallest deployable unit in Kubernetes
- **Deployments**: Manages replica sets and updates
- **Services**: Network endpoints for pods
- **Namespaces**: Organizes resources logically
- **ConfigMaps**: Configuration data for applications
- **Secrets**: Sensitive data management

## 🚀 Quick Setup Options

### Option 1: Local Kubernetes (Minikube)
```bash
# Install Minikube for local development
# Download from: https://minikube.sigs.k8s.io/docs/start/

# Start local cluster
minikube start

# Verify cluster
kubectl cluster-info

# Set as default context
kubectl config use-context minikube
```

### Option 2: Azure Kubernetes Service (AKS)
```bash
# Install Azure CLI with Kubernetes extension
az extension add aks-preview
az extension add k8s-configuration

# Create AKS cluster
az aks create \
  --resource-group "ecommerce-rg" \
  --name "ecommerce-cluster" \
  --node-count 1 \
  --node-vm-size "Standard_B2s" \
  --generate-ssh-keys

# Get cluster credentials
az aks get-credentials \
  --resource-group "ecommerce-rg" \
  --name "ecommerce-cluster" \
  --file ~/.kube/config

# Verify connection
kubectl get nodes
```

### Option 3: Docker Desktop Kubernetes
```bash
# Enable Kubernetes in Docker Desktop
# Settings → Kubernetes → Enable Kubernetes
# Set as current context
kubectl config use-context docker-desktop
```

## 📝 Kubernetes Manifests for ECommerce

### 1. Deployment Manifest
```yaml
# ecommerce-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ecommerce-deployment
  namespace: ecommerce
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ecommerce
  template:
    metadata:
      labels:
        app: ecommerce
    spec:
      containers:
      - name: ecommerce-app
        image: nayanarasse25/ecommerce-docker:latest
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
        env:
          - name: NODE_ENV
            value: "production"
```

### 2. Service Manifest
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

### 3. Namespace Manifest
```yaml
# ecommerce-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ecommerce
  labels:
    name: ecommerce
    environment: production
```

### 4. ConfigMap for Environment
```yaml
# ecommerce-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: ecommerce-config
  namespace: ecommerce
data:
  NODE_ENV: "production"
  API_URL: "https://api.ecommerce.com"
  LOG_LEVEL: "info"
```

## 🚀 Deployment Commands

### Apply All Manifests
```bash
# Create namespace
kubectl apply -f ecommerce-namespace.yaml

# Apply configuration
kubectl apply -f ecommerce-config.yaml

# Deploy application
kubectl apply -f ecommerce-deployment.yaml

# Expose service
kubectl apply -f ecommerce-service.yaml

# Check deployment status
kubectl get pods -n ecommerce
kubectl get services -n ecommerce
```

### Scale Application
```bash
# Scale to 5 replicas
kubectl scale deployment ecommerce-deployment --replicas=5 -n ecommerce

# Scale down to 2 replicas
kubectl scale deployment ecommerce-deployment --replicas=2 -n ecommerce
```

### Update Application
```bash
# Update image version
kubectl set image deployment/ecommerce-deployment \
  nayanarasse25/ecommerce-docker:v2.0 \
  -n ecommerce

# Check rollout status
kubectl rollout status deployment/ecommerce-deployment -n ecommerce
```

## 📊 Monitoring and Debugging

### Check Pod Status
```bash
# List all pods
kubectl get pods -n ecommerce -o wide

# Get pod logs
kubectl logs <pod-name> -n ecommerce

# Describe pod
kubectl describe pod <pod-name> -n ecommerce

# Exec into pod
kubectl exec -it <pod-name> -n ecommerce -- /bin/sh
```

### Service Endpoints
```bash
# Get service URL
kubectl get service ecommerce-service -n ecommerce

# Port forward to local
kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce
```

## 🔧 Advanced Kubernetes Features

### Horizontal Pod Autoscaler
```yaml
# ecommerce-hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ecommerce-hpa
  namespace: ecommerce
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ecommerce-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### Ingress for External Access
```yaml
# ecommerce-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ecommerce-ingress
  namespace: ecommerce
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: ecommerce.nayanarasse25.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: ecommerce-service
                port:
                  number: 80
```

## 🛠️ Kubernetes vs Docker

| Feature | Docker | Kubernetes |
|---------|---------|------------|
| Scale | Single host | Multiple nodes/clusters |
| Networking | Bridge networks | Complex network policies |
| Storage | Volumes | Persistent volumes |
| Load Balancing | Manual port mapping | Automatic service discovery |
| Health Checks | Container restarts | Self-healing pods |
| Configuration | Environment variables | ConfigMaps/Secrets |
| Scaling | Manual orchestration | Auto-scaling with HPA |

## 🎯 Advanced DevSecOps Skills

### ✅ Kubernetes Concepts Mastered
- Container orchestration at scale
- Self-healing and load balancing
- Service discovery and networking
- Configuration management
- Auto-scaling capabilities

### ✅ Practical Implementation
- Multi-pod application deployment
- Service exposure and load balancing
- Configuration with ConfigMaps
- Monitoring and debugging
- Rolling updates and rollbacks

## 🔄 Next Advanced Topics

After Kubernetes mastery, you're ready for:

### Infrastructure as Code (Terraform)
- Declarative infrastructure
- Multi-cloud deployments
- State management
- Cost optimization

### DevSecOps Security
- Container security scanning
- Network policies
- RBAC implementation
- Secret management
- Compliance automation

### Advanced CI/CD
- GitOps workflows
- Multi-environment deployments
- Blue-green deployments
- Canary releases

## 🎉 Advanced DevSecOps Ready!

You now have enterprise-grade skills in:
- **Container Orchestration**: Kubernetes management
- **Cloud Native**: Microservices architecture
- **Scalable Infrastructure**: Auto-scaling and load balancing
- **Production Deployment**: Multi-replica applications
- **Advanced Monitoring**: Pod-level observability

This completes your journey from basic Git to advanced Kubernetes orchestration!
