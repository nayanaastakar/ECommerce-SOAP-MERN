# 🚀 ECommerce Website - Run and Test Commands

## 📋 **Complete Terminal Commands**

### **Step 1: Navigate to Project Directory**
```bash
cd "c:\Users\HP\OneDrive\Desktop\CNA pro\ECommerce-SOAP-MERN"
```

### **Step 2: Check Kubernetes Status**
```bash
# Check if Kubernetes is running
kubectl cluster-info

# Check nodes
kubectl get nodes

# Check pods in ecommerce namespace
kubectl get pods -n ecommerce
```

### **Step 3: Check Services**
```bash
# Check services in ecommerce namespace
kubectl get services -n ecommerce

# Check service details
kubectl describe service ecommerce-final -n ecommerce
```

### **Step 4: Start Website (Port Forwarding)**
```bash
# Option 1: Port forward to specific pod
kubectl port-forward pod/ecommerce-simple-86f66774d6-6sg2q 8080:80 -n ecommerce

# Option 2: Port forward to service
kubectl port-forward service/ecommerce-final 8080:80 -n ecommerce
```

### **Step 5: Test Website Access**
```bash
# Test website locally
curl http://localhost:8080

# Test with verbose output
curl -v http://localhost:8080

# Check HTTP status
curl -I http://localhost:8080
```

### **Step 6: Check Application Logs**
```bash
# Check pod logs
kubectl logs -f deployment/ecommerce-simple -n ecommerce

# Check specific pod logs
kubectl logs -f pod/ecommerce-simple-86f66774d6-6sg2q -n ecommerce
```

### **Step 7: Troubleshooting Commands**
```bash
# Check pod events
kubectl get events -n ecommerce --sort-by='.lastTimestamp'

# Describe pod for issues
kubectl describe pod ecommerce-simple-86f66774d6-6sg2q -n ecommerce

# Check resource usage
kubectl top pods -n ecommerce

# Restart deployment
kubectl rollout restart deployment/ecommerce-simple -n ecommerce
```

### **Step 8: Scale Application (if needed)**
```bash
# Scale to 3 replicas
kubectl scale deployment ecommerce-simple --replicas=3 -n ecommerce

# Scale to 5 replicas
kubectl scale deployment ecommerce-simple --replicas=5 -n ecommerce
```

### **Step 9: Stop Port Forwarding**
```bash
# Stop port forwarding
pkill -f "kubectl port-forward"

# Or press Ctrl+C in the port forwarding terminal
```

## 🔧 **Alternative: Docker Method**

If Kubernetes has issues, you can run with Docker:

```bash
# Build Docker image
docker build -t ecommerce-app .

# Run Docker container
docker run -p 8080:80 --name ecommerce-container ecommerce-app

# Test Docker application
curl http://localhost:8080

# Stop Docker container
docker stop ecommerce-container
docker rm ecommerce-container
```

## 📊 **Expected Results**

### **Successful Run Should Show:**
- ✅ Kubernetes cluster info
- ✅ 2-3 pods in Running state
- ✅ Service with NodePort type
- ✅ Port forwarding active
- ✅ Website accessible at http://localhost:8080
- ✅ HTTP 200 OK response
- ✅ Nginx welcome page or ECommerce content

### **Common Issues and Fixes:**

#### **Issue 1: Port Forwarding Fails**
```bash
# Check if port 8080 is in use
netstat -ano | findstr :8080

# Kill existing port forwarding
pkill -f "kubectl port-forward"

# Try different port
kubectl port-forward pod/ecommerce-simple-86f66774d6-6sg2q 8081:80 -n ecommerce
```

#### **Issue 2: Pods Not Running**
```bash
# Check pod status
kubectl get pods -n ecommerce -o wide

# Describe pod for errors
kubectl describe pod <pod-name> -n ecommerce

# Restart deployment
kubectl rollout restart deployment/ecommerce-simple -n ecommerce
```

#### **Issue 3: Service Not Accessible**
```bash
# Check service endpoints
kubectl get endpoints -n ecommerce

# Recreate service
kubectl delete service ecommerce-final -n ecommerce
kubectl apply -f k8s-service-final.yaml
```

## 🎯 **Quick Test Commands**

```bash
# One-liner to check everything
cd "c:\Users\HP\OneDrive\Desktop\CNA pro\ECommerce-SOAP-MERN" && kubectl get pods -n ecommerce && kubectl port-forward pod/ecommerce-simple-86f66774d6-6sg2q 8080:80 -n ecommerce &

# Test website
curl http://localhost:8080

# Check logs
kubectl logs -f deployment/ecommerce-simple -n ecommerce
```

## 📱 **Browser Access**

After running port forwarding:
- Open browser and go to: http://localhost:8080
- Should see ECommerce website or Nginx welcome page

## 🎉 **Success Indicators**

Your website is running successfully when:
- ✅ Port forwarding starts without errors
- ✅ curl http://localhost:8080 returns HTTP 200
- ✅ Browser shows website content
- ✅ No error messages in pod logs
- ✅ Pods remain in Running state
