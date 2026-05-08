#!/bin/bash

# Simple ECommerce Kubernetes Access Script
# This script provides direct access to your ECommerce application

echo "🚀 ECommerce Kubernetes Access"
echo ""

# Check if Kubernetes is available
if ! kubectl cluster-info &> /dev/null; then
    echo "❌ Kubernetes not accessible. Please check Docker Desktop."
    exit 1
fi

echo "✅ Kubernetes is ready. Choose access method:"
echo ""
echo "1. Port Forwarding (Local)"
echo "2. External IP (Production)"
echo "3. Check Status"
echo ""
echo "Enter your choice (1-3):"

read -p "Enter your choice: " choice

case $choice in
    1)
        echo "🔄 Starting port forwarding..."
        kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce &
        echo "✅ Port forwarding active!"
        echo "🌐 Access your application at: http://localhost:8080"
        echo ""
        echo "Press Enter to stop port forwarding..."
        read -r
        pkill -f "kubectl port-forward"
        echo "🛑 Port forwarding stopped!"
        ;;
    2)
        echo "🌐 Getting external IP..."
        EXTERNAL_IP=$(kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
        
        if [ -z "$EXTERNAL_IP" ]; then
            echo "⏳ Waiting for external IP..."
            sleep 5
            EXTERNAL_IP=$(kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
        fi
        
        echo "✅ External IP: $EXTERNAL_IP"
        echo "🌐 Access your application at: http://$EXTERNAL_IP"
        ;;
    3)
        echo "📊 Checking deployment status..."
        kubectl get pods -n ecommerce
        kubectl get services -n ecommerce
        kubectl get deployment ecommerce-simple -n ecommerce
        ;;
    *)
        echo "❌ Invalid choice. Please select 1, 2, or 3."
        ;;
esac

echo ""
echo "🎉 Access complete!"
