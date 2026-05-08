# ☁️ Microsoft Azure Setup Guide

This guide will help you complete Level 5 of your DevSecOps roadmap: Microsoft Azure Overview and cloud deployment.

## 📋 Prerequisites

- Microsoft Azure account (free tier available)
- Your Docker image: `nayanarasse25/ecommerce-docker`
- Basic understanding of cloud concepts
- Completed DevSecOps Levels 1-4

## 🚀 Quick Start: Azure Account Creation

### 1. Access Your Azure Account
1. **Visit**: https://portal.azure.com
2. **Login**: Use your Microsoft account `nayanara@iservce.onmicrosoft.com`
3. **Dashboard**: Overview of your Azure resources
4. **Subscription**: Check your available services and limits

### 2. Azure Portal Access
1. **Login**: https://portal.azure.com
2. **Dashboard**: Overview of your Azure resources
3. **Search bar**: Top of portal for quick resource access

## 🏗️ Core Azure Services to Learn

### 1. Azure Virtual Machines (IaaS)
- **Purpose**: Virtual servers in the cloud
- **Use Case**: Running Jenkins, databases, custom applications
- **Pricing**: Pay-as-you-go, free tier available
- **Command**: `az vm create`

### 2. Azure Storage (PaaS)
- **Purpose**: Object storage for files, images, backups
- **Types**: Blob storage, File storage, Disk storage
- **Use Case**: Storing Docker images, application data
- **Command**: `az storage account create`

### 3. Azure App Service (PaaS)
- **Purpose**: Web application hosting
- **Use Case**: Deploying containerized applications
- **Features**: Auto-scaling, load balancing, SSL
- **Command**: `az webapp create`

### 4. Azure Container Registry
- **Purpose**: Private Docker image repository
- **Use Case**: Storing and managing Docker images
- **Integration**: Works with Azure Container Instances
- **Command**: `az acr create`

## 🔧 Step-by-Step Azure Deployment

### Step 1: Create Resource Group
```bash
# Install Azure CLI (if not installed)
# Download from: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

# Login to Azure
az login

# Create resource group
az group create \
  --name "ecommerce-rg" \
  --location "eastus"
```

### Step 2: Create Container Registry
```bash
# Create Azure Container Registry
az acr create \
  --resource-group "ecommerce-rg" \
  --name "nayanarasse25registry" \
  --sku "Basic"

# Get registry credentials
az acr credential show \
  --name "nayanarasse25registry" \
  --resource-group "ecommerce-rg"
```

### Step 3: Push Docker Image to Azure
```bash
# Tag your image for Azure
docker tag lushlather-ecommerce:latest nayanarasse25registry.azurecr.io/ecommerce:latest

# Login to Azure Container Registry
az acr login --name "nayanarasse25registry"

# Push image to Azure
docker push nayanarasse25registry.azurecr.io/ecommerce:latest
```

### Step 4: Deploy Container Instance
```bash
# Deploy container from Azure registry
az container create \
  --resource-group "ecommerce-rg" \
  --name "ecommerce-app" \
  --image "nayanarasse25registry.azurecr.io/ecommerce:latest" \
  --cpu 1 \
  --memory 1 \
  --ports 80 \
  --dns-name-label "ecommerce-nayanarasse25"
```

## 🌐 Access Your Deployed Application

### After Deployment
- **URL**: `http://ecommerce-nayanarasse25.eastus.azurecontainer.io`
- **Status**: Available globally
- **SSL**: Automatically configured
- **Scaling**: Can scale CPU/memory as needed

## 📊 Azure Pricing (Free Tier Limits)

| Service | Free Tier | Paid Tiers |
|---------|------------|------------|
| VM | 750 hours/month | $0.008/hour+ |
| Storage | 5 GB | $0.018/GB+ |
| App Service | 10 web apps | $0.10/hour+ |
| Container Registry | 1 registry | $0.007/day+ |
| Bandwidth | 100 GB/month | $0.087/GB+ |

## 🎯 DevSecOps Level 5 Objectives

### ✅ Azure Cloud Concepts to Master

#### **Cloud Service Models**
- **IaaS**: Infrastructure as a Service (Virtual Machines)
- **PaaS**: Platform as a Service (App Service, Storage)
- **SaaS**: Software as a Service (Office 365, Dynamics 365)

#### **Core Azure Services**
- **Azure VM**: Virtual machines for compute
- **Azure Storage**: Scalable object storage
- **Azure App Service**: Managed web hosting
- **Azure Container Registry**: Private Docker registry

#### **Cloud Benefits**
- **Scalability**: Scale resources up/down as needed
- **Reliability**: 99.9% uptime SLA
- **Global Reach**: Deploy to multiple regions
- **Pay-as-you-go**: Only pay for what you use

## 🛠️ Azure CLI Commands Cheat Sheet

### Authentication
```bash
# Login
az login

# Set subscription
az account set --subscription "Your-Subscription-Name"

# List subscriptions
az account list
```

### Resource Management
```bash
# List resource groups
az group list

# Delete resource group
az group delete --name "ecommerce-rg" --yes --no-wait
```

### Container Operations
```bash
# List containers
az container list

# Show container logs
az container logs --resource-group "ecommerce-rg" --name "ecommerce-app"

# Stop container
az container stop --resource-group "ecommerce-rg" --name "ecommerce-app"

# Start container
az container start --resource-group "ecommerce-rg" --name "ecommerce-app"
```

### Registry Operations
```bash
# List repositories
az acr repository list --name "nayanarasse25registry"

# Show repository tags
az acr repository show-tags \
  --name "nayanarasse25registry" \
  --repository "ecommerce"
```

## 🔄 Azure + Jenkins Integration

### Update Jenkinsfile for Azure Deployment
```groovy
stage('Deploy to Azure') {
    steps {
        script {
            sh """
                az login --service-principal \
                    --username $AZURE_CLIENT_ID \
                    --password $AZURE_CLIENT_SECRET \
                    --tenant $AZURE_TENANT_ID
                
                az container create \
                    --resource-group "ecommerce-rg" \
                    --name "ecommerce-app-${BUILD_NUMBER}" \
                    --image "nayanarasse25registry.azurecr.io/ecommerce:${DOCKER_TAG}" \
                    --cpu 1 \
                    --memory 1
            """
        }
    }
}
```

## 📱 Azure Portal vs CLI

### Azure Portal (GUI)
- **Easy to use**: Visual interface
- **Good for beginners**: Drag-and-drop configuration
- **Monitoring**: Built-in dashboards and alerts
- **Access**: https://portal.azure.com

### Azure CLI (Command Line)
- **Automation**: Scriptable and repeatable
- **CI/CD Integration**: Perfect for Jenkins pipelines
- **Speed**: Faster for experienced users
- **Install**: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

## 🎯 Practice Tasks for Level 5

### Task 1: Create Resource Group
- Navigate to Azure Portal
- Create resource group "ecommerce-rg"
- Choose East US region

### Task 2: Set Up Container Registry
- Create Azure Container Registry
- Push your Docker image
- Verify image in registry

### Task 3: Deploy Container Instance
- Deploy your ECommerce application
- Configure DNS name
- Test public access

### Task 4: Monitor and Scale
- Set up monitoring alerts
- Test scaling capabilities
- Review cost optimization

## 🚨 Important Security Notes

### Azure Security Best Practices
1. **Use Resource Groups**: Organize and isolate resources
2. **Apply Tags**: For cost tracking and management
3. **Use RBAC**: Role-Based Access Control
4. **Enable Monitoring**: Set up alerts and logging
5. **Use Private Networks**: When possible for sensitive data

### Cost Management
1. **Set Budgets**: Prevent unexpected charges
2. **Monitor Usage**: Regular cost review
3. **Use Free Tier**: Maximize free benefits
4. **Right-size Resources**: Don't over-provision

## 🎉 Level 5 Complete!

Once you complete these tasks, you've mastered:

### ✅ Cloud Computing Concepts
- IaaS, PaaS, SaaS understanding
- Azure services familiarity
- Cloud deployment strategies

### ✅ Practical Azure Skills
- Resource group management
- Container registry usage
- Container instance deployment
- CLI and portal proficiency

### ✅ DevSecOps Foundation
- Complete CI/CD pipeline (Jenkins + Azure)
- Cloud deployment automation
- Infrastructure as code preparation
- Production-ready deployment

## 🔄 Next Steps: Advanced DevSecOps

After Level 5, you're ready for:
- **Kubernetes**: Container orchestration
- **Terraform**: Infrastructure as Code
- **DevSecOps**: Security in CI/CD
- **Advanced Cloud**: Multi-cloud strategies
- **Monitoring**: Advanced observability

This completes your foundational DevSecOps journey with enterprise-ready cloud deployment skills!
