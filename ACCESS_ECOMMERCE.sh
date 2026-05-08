#!/bin/bash

# ECommerce Kubernetes Access Script
# This script provides multiple ways to access your ECommerce application

echo "🚀 ECommerce Kubernetes Access Options:"
echo ""
echo "1. Port Forwarding (Local Access)"
echo "2. External IP (Production Access)"
echo "3. Background Port Forwarding"
echo "4. Stop Port Forwarding"
echo ""

# Option 1: Port Forwarding (Recommended for development)
echo "📦 Starting port forwarding..."
kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce &
echo "✅ Port forwarding active!"
echo "🌐 Access your application at: http://localhost:8080"
echo ""
echo "Press Enter to stop port forwarding..."
read -r

# Stop port forwarding when user presses Enter
echo "🛑 Stopping port forwarding..."
pkill -f "kubectl port-forward"
echo "✅ Port forwarding stopped!"

# Option 2: External IP (Production access)
echo "🌐 Getting external IP..."
EXTERNAL_IP=$(kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

if [ -z "$EXTERNAL_IP" ]; then
    echo "⏳ Waiting for external IP..."
    sleep 5
    EXTERNAL_IP=$(kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
fi

echo "✅ External IP: $EXTERNAL_IP"
echo "🌐 Access your application at: http://$EXTERNAL_IP"
echo ""

# Option 3: Background Port Forwarding
echo "🔄 Starting background port forwarding..."
nohup kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce &
echo "✅ Background port forwarding started!"
echo "📊 Use 'curl http://localhost:8080' to test"
echo ""
echo "To stop: pkill -f 'kubectl port-forward'"

# Option 4: Stop All Forwarding
echo "🛑 Stopping all port forwarding..."
pkill -f "kubectl port-forward"
echo "✅ All port forwarding stopped!"

# Option 5: Check Status
echo "📊 Checking deployment status..."
kubectl get pods -n ecommerce
kubectl get services -n ecommerce
kubectl get deployment ecommerce-simple -n ecommerce

echo ""
echo "🎯 Management Commands:"
echo "View logs: kubectl logs -f deployment/ecommerce-simple -n ecommerce"
echo "Scale deployment: kubectl scale deployment ecommerce-simple --replicas=<number> -n ecommerce"
echo "Restart deployment: kubectl rollout restart deployment ecommerce-simple -n ecommerce"
