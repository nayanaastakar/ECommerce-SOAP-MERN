#!/bin/bash

# ECommerce Kubernetes Deployment Script
# This script deploys your ECommerce application to Kubernetes

echo "🚀 Deploying ECommerce to Kubernetes..."

# Check if kubectl is available
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl not found. Please install kubectl first."
    echo "📋 Follow QUICK_K8S_SETUP.md for installation"
    exit 1
fi

# Check if Kubernetes is running
if ! kubectl cluster-info &> /dev/null; then
    echo "❌ Kubernetes cluster not accessible."
    echo "📋 Please ensure Docker Desktop Kubernetes is enabled"
    exit 1
fi

echo "✅ Kubernetes is ready. Starting deployment..."

# Create namespace
echo "📦 Creating namespace..."
kubectl apply -f k8s-namespace.yaml

# Wait for namespace to be created
kubectl wait --for=condition=Ready namespace/ecommerce --timeout=60s

# Deploy application
echo "🚀 Deploying ECommerce application..."
kubectl apply -f k8s-deployment.yaml

# Wait for deployment to be ready
kubectl wait --for=condition=Available deployment/ecommerce-deployment --timeout=120s

# Create service
echo "🌐 Creating service..."
kubectl apply -f k8s-service.yaml

# Wait for service to be ready
kubectl wait --for=condition=Ready service/ecommerce-service --timeout=60s

# Get deployment status
echo "📊 Checking deployment status..."
kubectl get deployment ecommerce-deployment -n ecommerce

# Get pod status
echo "📱 Checking pod status..."
kubectl get pods -n ecommerce -o wide

# Get service status
echo "🔍 Checking service status..."
kubectl get service ecommerce-service -n ecommerce

# Get external IP
EXTERNAL_IP=$(kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

if [ -z "$EXTERNAL_IP" ]; then
    echo "⏳ Waiting for external IP..."
    sleep 10
    EXTERNAL_IP=$(kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
fi

echo "✅ Deployment completed!"
echo ""
echo "🌐 Application Details:"
echo "📦 Namespace: ecommerce"
echo "🚀 Deployment: ecommerce-deployment"
echo "📱 Pods: $(kubectl get pods -n ecommerce --no-headers | wc -l)"
echo "🌐 Service: ecommerce-service"
echo ""
echo "🔗 Access Options:"
echo "1. Port Forwarding (Local):"
echo "   kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce"
echo "   Then open: http://localhost:8080"
echo ""
echo "2. External IP (Production):"
if [ ! -z "$EXTERNAL_IP" ]; then
    echo "   🌐 http://$EXTERNAL_IP"
else
    echo "   ⏳ External IP not yet available"
    echo "   🕐 Check again with: kubectl get service ecommerce-service -n ecommerce"
fi
echo ""
echo "🔧 Management Commands:"
echo "📊 View pods: kubectl get pods -n ecommerce"
echo "📝 View logs: kubectl logs -f deployment/ecommerce-deployment -n ecommerce"
echo "📈 Scale deployment: kubectl scale deployment ecommerce-deployment --replicas=<number> -n ecommerce"
echo "🗑️ Delete deployment: kubectl delete deployment ecommerce-deployment -n ecommerce"
echo ""
echo "📋 Troubleshooting:"
echo "❌ If pods not starting: kubectl describe pod <pod-name> -n ecommerce"
echo "🔄 Restart deployment: kubectl rollout restart deployment/ecommerce-deployment -n ecommerce"
echo "📱 Check events: kubectl get events -n ecommerce --sort-by='.lastTimestamp'"
