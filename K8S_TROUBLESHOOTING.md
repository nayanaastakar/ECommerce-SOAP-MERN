# 🔧 Kubernetes Troubleshooting Guide

This guide will help you fix common ECommerce application deployment issues in Kubernetes.

## 🚨 Common Kubernetes Issues

### 1. Pods Not Starting
#### **Symptoms**
- Pods stuck in `Pending` or `ContainerCreating` state
- Application not accessible
- Deployment shows 0/0 ready replicas

#### **Diagnosis Commands**
```bash
# Check pod status
kubectl get pods -n ecommerce -o wide

# Describe pod for details
kubectl describe pod <pod-name> -n ecommerce

# Check pod events
kubectl get events -n ecommerce --sort-by='.lastTimestamp'

# Check deployment status
kubectl get deployment ecommerce-deployment -n ecommerce -o yaml

# Check resource quotas
kubectl describe namespace ecommerce
```

#### **Common Fixes**
```bash
# Image pull issues
kubectl describe pod <pod-name> -n ecommerce | grep "ImagePullBackOff"

# Resource constraints
kubectl describe pod <pod-name> -n ecommerce | grep "Insufficient"

# Fix deployment
kubectl rollout restart deployment/ecommerce-deployment -n ecommerce

# Delete and recreate
kubectl delete deployment ecommerce-deployment -n ecommerce
kubectl apply -f k8s-deployment.yaml
```

### 2. Service Not Accessible
#### **Symptoms**
- Service shows `ClusterIP` instead of `LoadBalancer` IP
- External IP not accessible from browser
- Port forwarding doesn't work

#### **Diagnosis Commands**
```bash
# Check service status
kubectl get service ecommerce-service -n ecommerce -o wide

# Check service endpoints
kubectl get endpoints ecommerce-service -n ecommerce

# Check network policies
kubectl get networkpolicy -n ecommerce

# Test service connectivity
kubectl run -it --rm debug-pod --image=busybox -- wget -qO- http://ecommerce-service.ecommerce -n ecommerce
```

#### **Common Fixes**
```bash
# Fix service type
kubectl patch service ecommerce-service -p '{"spec":{"type":"LoadBalancer"}}' -n ecommerce

# Recreate service
kubectl delete service ecommerce-service -n ecommerce
kubectl apply -f k8s-service.yaml

# Check node port availability
kubectl get nodes -o wide

# Use NodePort instead of LoadBalancer (for testing)
kubectl patch service ecommerce-service -p '{"spec":{"type":"NodePort","ports":[{"port":80,"nodePort":30080}]}' -n ecommerce
```

### 3. Application Not Responding

#### **Symptoms**
- HTTP requests timeout
- 502/503 errors
- Application shows healthy but doesn't respond

#### **Diagnosis Commands**
```bash
# Test application health
kubectl exec -it <pod-name> -n ecommerce -- curl -f http://localhost:80/health

# Check container logs
kubectl logs -f deployment/ecommerce-deployment -n ecommerce --tail=50

# Port forward and test locally
kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce &
curl -v http://localhost:8080/

# Check resource usage
kubectl top pods -n ecommerce
kubectl top nodes
```

#### **Common Fixes**
```bash
# Fix health check path
kubectl patch deployment ecommerce-deployment -p '{"spec":{"template":{"spec":{"containers":[{"name":"ecommerce-app","livenessProbe":{"httpGet":{"path":"/health","port":80}}}]}}}' -n ecommerce

# Increase resource limits
kubectl patch deployment ecommerce-deployment -p '{"spec":{"template":{"spec":{"containers":[{"name":"ecommerce-app","resources":{"limits":{"memory":"1Gi","cpu":"1000m"}}}]}}}' -n ecommerce

# Add readiness probe
kubectl patch deployment ecommerce-deployment -p '{"spec":{"template":{"spec":{"containers":[{"name":"ecommerce-app","readinessProbe":{"httpGet":{"path":"/","port":80}}}]}}}' -n ecommerce
```

### 4. Persistent Storage Issues

#### **Symptoms**
- Data lost when pods restart
- Database connection errors
- File system permissions issues

#### **Diagnosis Commands**
```bash
# Check PVC status
kubectl get pvc -n ecommerce

# Check storage class
kubectl get storageclass

# Check pod mount points
kubectl exec -it <pod-name> -n ecommerce -- df -h

# Check volume mounts
kubectl describe pod <pod-name> -n ecommerce | grep -A5 -B5 "Mounts"
```

#### **Common Fixes**
```bash
# Fix volume permissions
kubectl patch deployment ecommerce-deployment -p '{"spec":{"template":{"spec":{"containers":[{"name":"ecommerce-app","securityContext":{"runAsUser":1000}]}}}' -n ecommerce

# Add persistent volume
kubectl apply -f ecommerce-pvc.yaml
kubectl apply -f ecommerce-storage.yaml
```

## 🛠️ Advanced Debugging Tools

### 1. Kubernetes Dashboard
```bash
# Enable dashboard
minikube addons enable dashboard

# Access dashboard
minikube dashboard
# Or for Docker Desktop
kubectl proxy
# Open: http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/#
```

### 2. Port Forwarding Debugging
```bash
# Forward multiple ports
kubectl port-forward service/ecommerce-service 8080:80 8443:443 -n ecommerce

# Background port forwarding
nohup kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce &

# Check what's using ports
netstat -tulpn | grep :8080
```

### 3. Resource Monitoring
```bash
# Real-time monitoring
watch kubectl get pods -n ecommerce

# Resource usage
kubectl top pods -n ecommerce --containers
kubectl top nodes

# Events monitoring
kubectl get events -n ecommerce --watch --only-show-events
```

## 📊 Performance Optimization

### 1. Resource Requests and Limits
```yaml
# Optimized deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ecommerce-deployment
  namespace: ecommerce
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: ecommerce-app
        image: nayanarasse25/ecommerce-docker:latest
        ports:
          - containerPort: 80
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        env:
          - name: NODE_ENV
            value: "production"
        livenessProbe:
          httpGet:
            path: /health
            port: 80
            initialDelaySeconds: 15
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /
            port: 80
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 3
```

### 2. Horizontal Pod Autoscaler
```yaml
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

## 🔄 Quick Fix Commands

### Reset Everything
```bash
# Delete namespace and all resources
kubectl delete namespace ecommerce --ignore-not-found=true

# Recreate everything
kubectl apply -f k8s-namespace.yaml
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
```

### Force Restart
```bash
# Restart all pods
kubectl rollout restart deployment/ecommerce-deployment -n ecommerce

# Force new rollout
kubectl rollout undo deployment/ecommerce-deployment -n ecommerce
kubectl rollout history deployment/ecommerce-deployment -n ecommerce
```

## 🎯 Success Indicators

### Your ECommerce is Working When:
- ✅ **Pods Running**: All pods in `Running` state
- ✅ **Service Accessible**: Application responds to HTTP requests
- ✅ **External IP Available**: LoadBalancer or NodePort accessible
- ✅ **Health Checks Passing**: Liveness and readiness probes succeed
- ✅ **Logs Clean**: No error messages in pod logs
- ✅ **Resource Usage Normal**: CPU and memory within limits

### Monitoring Dashboard
- **Pod Status**: Green checkmarks for running pods
- **Service Health**: Green indicators for accessible endpoints
- **Resource Usage**: Charts for CPU, memory, and network
- **Error Rate**: Low error rates and fast response times

This comprehensive troubleshooting guide should help you quickly identify and fix any Kubernetes deployment issues with your ECommerce application!
