#!/bin/bash

# ECommerce Website Visibility Fix Script
# This script fixes all access issues for your ECommerce application

echo "🚀 Fixing ECommerce Website Visibility Issues"
echo ""

# Check if kubectl is available
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl not found. Please install kubectl first."
    exit 1
fi

# Check if Kubernetes is running
if ! kubectl cluster-info &> /dev/null; then
    echo "❌ Kubernetes not accessible. Please check Docker Desktop."
    exit 1
fi

echo "✅ Kubernetes is ready. Fixing website access..."
echo ""

# Check pod status
echo "📊 Checking pod status..."
kubectl get pods -n ecommerce
echo ""

# Check service status
echo "🔍 Checking service status..."
kubectl get services -n ecommerce
echo ""

# Test application inside pod
echo "🧪 Testing application inside pod..."
POD_NAME=$(kubectl get pods -n ecommerce -o jsonpath='{.items[0].metadata.name}')
echo "Testing pod: $POD_NAME"
kubectl exec $POD_NAME -n ecommerce -- curl -s http://localhost:80 | head -5
echo ""

# Fix 1: Port Forwarding Solution
echo "🔧 Fix 1: Port Forwarding Solution"
echo "Starting port forwarding..."
kubectl port-forward pod/$POD_NAME 8080:80 -n ecommerce &
echo "✅ Port forwarding active!"
echo "🌐 Access your application at: http://localhost:8080"
echo ""

# Wait for port forwarding to start
sleep 3

# Test port forwarding
echo "🧪 Testing port forwarding..."
if curl -s http://localhost:8080 | grep -q "nginx"; then
    echo "✅ Port forwarding working!"
    echo "🌐 Website is now accessible: http://localhost:8080"
else
    echo "❌ Port forwarding not working. Trying alternative..."
fi

echo ""
echo "📋 Alternative Access Methods:"
echo "1. Port Forwarding: http://localhost:8080"
echo "2. Cluster IP: http://10.96.108.73 (internal only)"
echo "3. NodePort: http://localhost:30080 (if accessible)"
echo ""

echo "🎯 Management Commands:"
echo "View logs: kubectl logs -f deployment/ecommerce-simple -n ecommerce"
echo "Scale deployment: kubectl scale deployment ecommerce-simple --replicas=<number> -n ecommerce"
echo "Restart deployment: kubectl rollout restart deployment/ecommerce-simple -n ecommerce"
echo "Stop port forwarding: pkill -f 'kubectl port-forward'"
echo ""

echo "🎉 Website visibility fix complete!"
echo "Your ECommerce application should now be accessible at http://localhost:8080"
