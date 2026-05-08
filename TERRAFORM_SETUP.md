# 🏗️ Terraform Infrastructure as Code

This guide will help you learn Terraform for advanced DevSecOps practices after completing Kubernetes fundamentals.

## 📋 Prerequisites

- Completed Kubernetes fundamentals
- Basic understanding of cloud infrastructure
- Your ECommerce application containerized
- Cloud account access (Azure, AWS, or GCP)
- Terraform CLI installed

## 🎯 Terraform Learning Objectives

### What is Terraform?
- **Infrastructure as Code**: Declarative infrastructure management
- **Multi-Cloud**: Works with Azure, AWS, GCP
- **State Management**: Tracks infrastructure changes
- **Version Control**: Infrastructure changes in Git
- **Automation**: Programmatic resource creation

### Key Concepts
- **Providers**: Cloud service integrations (Azure, AWS, GCP)
- **Resources**: Infrastructure components (VMs, networks, storage)
- **Variables**: Parameterization for reusability
- **Modules**: Reusable infrastructure components
- **State**: Remote and local state management
- **Workspaces**: Environment separation

## 🚀 Terraform Setup

### 1. Install Terraform
```bash
# Download Terraform
# Visit: https://developer.hashicorp.com/terraform/downloads

# Windows (chocolatey)
choco install terraform

# Verify installation
terraform --version
```

### 2. Configure Azure Provider
```bash
# Initialize Terraform
terraform init

# Create provider configuration
# main.tf
provider "azurerm" {
  features {}
}

# Configure Azure credentials
# Set environment variables
$env:ARM_CLIENT_ID = "your-client-id"
$env:ARM_CLIENT_SECRET = "your-client-secret"
$env:ARM_SUBSCRIPTION_ID = "your-subscription-id"
$env:ARM_TENANT_ID = "your-tenant-id"
```

## 🏗️ Infrastructure as Code Examples

### 1. Azure Resource Group
```hcl
# resource-group.tf
resource "azurerm_resource_group" "ecommerce" {
  name     = "ecommerce-rg"
  location = "East US"
  tags = {
    Environment = "Production"
    Project     = "ECommerce"
    Owner       = "DevOps"
  }
}
```

### 2. Azure Kubernetes Cluster
```hcl
# aks-cluster.tf
resource "azurerm_kubernetes_cluster" "ecommerce" {
  name                = "ecommerce-cluster"
  location            = "East US"
  resource_group_name = azurerm_resource_group.ecommerce.name
  dns_prefix          = "ecommerce"
  
  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_B2s"
  }
  
  identity {
    type = "SystemAssigned"
  }
  
  tags = {
    Environment = "Production"
    Project     = "ECommerce"
  }
}
```

### 3. Azure Container Registry
```hcl
# container-registry.tf
resource "azurerm_container_registry" "ecommerce" {
  name                = "nayanarasse25registry"
  resource_group_name = azurerm_resource_group.ecommerce.name
  location            = "East US"
  sku                 = "Basic"
  admin_enabled        = true
  
  tags = {
    Environment = "Production"
    Project     = "ECommerce"
  }
}
```

### 4. Application Deployment
```hcl
# kubernetes-deployment.tf
resource "kubernetes_deployment" "ecommerce" {
  metadata {
    name = "ecommerce-app"
    namespace = "ecommerce"
  }
  
  spec {
    replicas = 3
    
    selector {
      match_labels = {
        app = "ecommerce"
      }
    }
    
    template {
      metadata {
        labels = {
          app = "ecommerce"
        }
      }
      
      spec {
        container {
          image = "${azurerm_container_registry.ecommerce.login_server}/ecommerce:latest"
          name  = "ecommerce-app"
          port {
            container_port = 80
          }
          
          resources {
            limits = {
              cpu    = "200m"
              memory = "256Mi"
            }
            requests = {
              cpu    = "100m"
              memory = "128Mi"
            }
          }
        }
      }
    }
  }
}
```

### 5. Variables and Outputs
```hcl
# variables.tf
variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "East US"
}

variable "node_count" {
  description = "Number of nodes in AKS cluster"
  type        = number
  default     = 2
}

variable "app_replicas" {
  description = "Number of application replicas"
  type        = number
  default     = 3
}

# outputs.tf
output "cluster_name" {
  value = azurerm_kubernetes_cluster.ecommerce.name
}

output "registry_url" {
  value = azurerm_container_registry.ecommerce.login_server
}
```

## 🚀 Terraform Commands

### Basic Workflow
```bash
# Initialize directory
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy infrastructure
terraform destroy
```

### Advanced Commands
```bash
# Validate syntax
terraform validate

# Format code
terraform fmt

# Show state
terraform show

# Import existing resources
terraform import azurerm_resource_group.ecommerce /subscriptions/xxx/resourceGroups/ecommerce-rg
```

### State Management
```bash
# Remote state (Azure Storage)
terraform backend "azurerm" {
  resource_group_name  = "terraform-state"
  storage_account_name = "terraformstatenayanarasse25"
  container_name    = "state"
  key               = "ecommerce.terraform.tfstate"
}

# Initialize remote backend
terraform init -migrate-state
```

## 🔄 Terraform + Kubernetes Integration

### 1. Deploy Infrastructure
```bash
# Deploy all infrastructure
terraform apply

# Get kubeconfig
az aks get-credentials \
  --resource-group ecommerce-rg \
  --name ecommerce-cluster \
  --file ~/.kube/config

# Set context
kubectl config use-context ecommerce-cluster
```

### 2. Deploy Application
```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/
```

## 📊 Terraform vs Manual

| Aspect | Manual | Terraform |
|--------|---------|------------|
| Speed | Slow, error-prone | Fast, automated |
| Consistency | Variable | Standardized |
| Version Control | Git repos | Infrastructure in Git |
| Reusability | Copy-paste | Modules, variables |
| Collaboration | Documentation | Code review |
| Cost Control | Manual tracking | State management |
| Auditing | Manual logs | Change tracking |

## 🛠️ Terraform Best Practices

### 1. Code Organization
```
project/
├── main.tf              # Main configuration
├── variables.tf           # Input variables
├── outputs.tf            # Output values
├── modules/              # Reusable components
│   ├── aks/
│   ├── networking/
│   └── storage/
├── environments/          # Environment-specific configs
│   ├── dev/
│   ├── staging/
│   └── prod/
└── terraform.tfstate     # State file (gitignore)
```

### 2. Security Practices
```hcl
# Use Azure Key Vault for secrets
resource "azurerm_key_vault_secret" "app_secret" {
  name         = "database-password"
  value        = var.db_password
  key_vault_id = azurerm_key_vault.ecommerce.id
}

# Network security
resource "azurerm_network_security_group" "ecommerce" {
  name                = "ecommerce-nsg"
  location            = var.location
  resource_group_name = azurerm_resource_group.ecommerce.name
  
  security_rule {
    name                       = "allow-https"
    priority                   = 100
    direction                  = "Inbound"
    access                    = "Allow"
    protocol                   = "Tcp"
    source_port_range           = "*"
    destination_port_range      = "443"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}
```

### 3. Cost Optimization
```hcl
# Use spot instances for non-production
resource "azurerm_kubernetes_cluster" "ecommerce" {
  # ... other config ...
  
  default_node_pool {
    vm_size    = "Standard_B2s"
    node_count = 2
    
    # Enable cluster autoscaler
    enable_auto_scaling = true
    min_count         = 1
    max_count         = 5
  }
}
```

## 🔄 CI/CD Integration

### GitHub Actions with Terraform
```yaml
# .github/workflows/infrastructure.yml
name: 'Deploy Infrastructure'

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Terraform
      uses: hashicorp/setup-terraform@v1
      
    - name: Terraform Init
      run: terraform init
      
    - name: Terraform Plan
      run: terraform plan -out=tfplan
      
    - name: Terraform Apply
      run: terraform apply -auto-approve
      env:
        ARM_CLIENT_ID: ${{ secrets.AZURE_CLIENT_ID }}
        ARM_CLIENT_SECRET: ${{ secrets.AZURE_CLIENT_SECRET }}
        ARM_SUBSCRIPTION_ID: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
```

## 🎯 Advanced DevSecOps Skills

### ✅ Infrastructure as Code Mastered
- **Declarative Configuration**: Infrastructure defined in code
- **Version Control**: Infrastructure changes tracked in Git
- **Multi-Cloud**: Provider-agnostic resource management
- **Automation**: Programmatic resource provisioning
- **State Management**: Reliable state tracking

### ✅ Terraform Skills
- **HCL Language**: Terraform configuration syntax
- **Providers**: Azure, AWS, GCP integrations
- **Modules**: Reusable infrastructure components
- **CI/CD Integration**: GitHub Actions automation
- **Best Practices**: Security, cost optimization

## 🔄 Next Advanced Topics

After mastering Terraform, you're ready for:

### Advanced DevSecOps
- **Multi-Environment Deployments**: Dev, staging, production
- **GitOps Workflows**: Automated infrastructure updates
- **Compliance as Code**: Automated policy enforcement
- **Cost Monitoring**: Real-time optimization

### Cloud Native Technologies
- **Service Mesh**: Istio, Linkerd
- **Serverless**: Functions, FaaS
- **Event Streaming**: Kafka, Event Hubs
- **Advanced Security**: Zero-trust architectures

## 🎉 Enterprise DevSecOps Engineer!

You now have complete mastery of:
- **Git & GitHub** (Levels 1-2)
- **Docker & Containerization** (Level 3)
- **Jenkins CI/CD** (Level 4)
- **Azure Cloud** (Level 5)
- **Kubernetes Orchestration** (Advanced)
- **Terraform IaC** (Advanced)

This represents a complete, enterprise-grade DevSecOps skillset ready for production environments!
