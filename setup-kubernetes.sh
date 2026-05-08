#!/bin/bash

# Kubernetes Cluster Setup Script for DevSecOps
# This script sets up a local Kubernetes cluster for your ECommerce application

echo "🚀 Setting up Kubernetes cluster for ECommerce deployment..."

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl not found. Please install kubectl first."
    echo "📋 Install kubectl:"
    echo "curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.24.0/bin/linux/amd64/kubectl"
    echo "chmod +x kubectl"
    echo "sudo mv kubectl /usr/local/bin/"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker not running. Please start Docker Desktop first."
    exit 1
fi

echo "✅ Prerequisites checked. Setting up Kubernetes cluster..."

# Option 1: Minikube (Recommended for beginners)
setup_minikube() {
    echo "🔧 Setting up Minikube..."
    
    # Check if Minikube is installed
    if ! command -v minikube &> /dev/null; then
        echo "📥 Installing Minikube..."
        curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
        sudo install minikube-linux-amd64
        sudo chmod +x /usr/local/bin/minikube
    fi
    
    # Start Minikube
    minikube start --driver=docker --cpus=2 --memory=4096 --disk-size=20g
    
    # Configure kubectl to use Minikube
    kubectl config use-context minikube
    
    echo "✅ Minikube cluster started!"
    echo "🌐 Access: Minikube will configure access"
}

# Option 2: Docker Desktop Kubernetes (Easiest setup)
setup_docker_k8s() {
    echo "🐳 Setting up Docker Desktop Kubernetes..."
    
    # Check if Docker Desktop is running
    if ! docker info &> /dev/null; then
        echo "❌ Docker Desktop not running. Please start Docker Desktop."
        exit 1
    fi
    
    # Enable Kubernetes in Docker Desktop
    echo "⏳ Enabling Kubernetes in Docker Desktop..."
    echo "Please enable Kubernetes in Docker Desktop settings:"
    echo "1. Open Docker Desktop"
    echo "2. Go to Settings → Kubernetes"
    echo "3. Enable Kubernetes"
    echo "4. Apply & Restart"
    
    # Wait for user to enable Kubernetes
    echo "⏸ Waiting for Kubernetes to be enabled..."
    echo "Press Enter when Kubernetes is enabled in Docker Desktop..."
    read -r
    
    # Verify Kubernetes is available
    kubectl cluster-info &> /dev/null
    if [ $? -eq 0 ]; then
        echo "✅ Docker Desktop Kubernetes is ready!"
        echo "🌐 Access: kubectl is configured for Docker Desktop"
    else
        echo "❌ Kubernetes not available. Please check Docker Desktop settings."
        exit 1
    fi
}

# Option 3: Azure Kubernetes Service (AKS)
setup_aks() {
    echo "☁️ Setting up Azure Kubernetes Service (AKS)..."
    
    # Check if Azure CLI is installed
    if ! command -v az &> /dev/null; then
        echo "❌ Azure CLI not found. Please install Azure CLI first."
        echo "📋 Install Azure CLI:"
        echo "curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash"
        exit 1
    fi
    
    # Login to Azure
    echo "🔐 Please login to Azure:"
    az login
    
    # Create resource group if it doesn't exist
    echo "📦 Creating resource group..."
    az group create --name "ecommerce-rg" --location "East US" --output none
    
    # Create AKS cluster
    echo "☸️ Creating AKS cluster..."
    az aks create \
        --resource-group "ecommerce-rg" \
        --name "ecommerce-cluster" \
        --node-count 2 \
        --node-vm-size "Standard_B2s" \
        --generate-ssh-keys \
        --output none
    
    # Get cluster credentials
    echo "🔑 Getting cluster credentials..."
    az aks get-credentials \
        --resource-group "ecommerce-rg" \
        --name "ecommerce-cluster" \
        --file ~/.kube/config \
        --overwrite-existing
    
    # Verify connection
    kubectl get nodes
    if [ $? -eq 0 ]; then
        echo "✅ AKS cluster created and configured!"
        echo "🌐 Access: kubectl is configured for AKS"
        echo "📊 Cluster info:"
        kubectl cluster-info
    else
        echo "❌ Failed to connect to AKS cluster."
        exit 1
    fi
}

# Interactive setup menu
echo "🎯 Kubernetes Setup Options:"
echo "1. Minikube (Local development)"
echo "2. Docker Desktop Kubernetes (Easiest)"
echo "3. Azure Kubernetes Service (AKS - Production)"
echo ""
echo "Please choose an option (1-3):"

read -p "Enter your choice: " choice

case $choice in
    1)
        setup_minikube
        ;;
    2)
        setup_docker_k8s
        ;;
    3)
        setup_aks
        ;;
    *)
        echo "❌ Invalid choice. Please select 1, 2, or 3."
        exit 1
        ;;
esac

echo ""
echo "🎉 Kubernetes setup complete!"
echo "📋 Next steps:"
echo "1. Deploy your ECommerce application:"
echo "   kubectl apply -f k8s/"
echo "2. Check deployment:"
echo "   kubectl get pods -n ecommerce"
echo "3. Access your application:"
echo "   kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce"
echo ""
echo "📚 Documentation available in KUBERNETES_SETUP.md"
