# 🔐 DevSecOps Security Practices Guide

This guide will help you implement security practices for advanced DevSecOps workflows.

## 📋 Security Fundamentals

### DevSecOps Principles
- **Security Left**: Integrate security early in development
- **Automation**: Security checks in CI/CD pipelines
- **Continuous Monitoring**: Real-time security visibility
- **Compliance**: Regulatory and policy enforcement
- **Zero Trust**: Never trust, always verify

### Security in DevOps Pipeline
- **Static Analysis**: Code scanning for vulnerabilities
- **Dependency Scanning**: Check third-party packages
- **Container Security**: Image vulnerability scanning
- **Secrets Management**: Secure credential handling
- **Infrastructure Security**: Network and access controls

## 🛠️ Container Security

### 1. Docker Security Best Practices
```dockerfile
# Use minimal base images
FROM node:18-alpine

# Create non-root user
RUN addgroup -g appuser && adduser -D -G appuser appuser
USER appuser

# Remove unnecessary packages
RUN apk del --purge \
    gcc \
    musl-dev \
    python3 \
    make

# Set secure permissions
COPY --chown=appuser:appuser . /app
WORKDIR /app

# Use specific version tags
FROM node:18.17.0-alpine

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1
```

### 2. Kubernetes Security Policies
```yaml
# Pod Security Policy
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: ecommerce-psp
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
    - ALL
  volumes:
    - configMap
    - emptyDir
    - projected
  runAsUser:
    rule: 'MustRunAsNonRoot'
  fsGroup:
    rule: 'MustRunAs'
```

### 3. Network Security
```yaml
# Network Policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: ecommerce-netpol
spec:
  podSelector:
    matchLabels:
      app: ecommerce
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: ingress-nginx
      ports:
        - protocol: TCP
          port: 80
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              name: database
      ports:
        - protocol: TCP
          port: 5432
```

## 🔍 Security Scanning Tools

### 1. Container Image Scanning
```bash
# Trivy - Open source vulnerability scanner
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image nayanarasse25/ecommerce-docker

# Clair - Static analysis
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/clair:latest scan nayanarasse25/ecommerce-docker

# Docker Scout (Docker Hub)
docker scout cves nayanarasse25/ecommerce-docker
```

### 2. Static Code Analysis
```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    
    steps:
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        scan-ref: '.'
        format: 'sarif'
        
    - name: Upload SARIF file
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'
```

### 3. Dependency Scanning
```bash
# npm audit
npm audit --audit-level=high

# Snyk (dependency vulnerability scanner)
snyk test --json > snyk-report.json

# OWASP Dependency Check
dependency-check --audit .
```

## 🔐 Secrets Management

### 1. Kubernetes Secrets
```yaml
# Secret for database credentials
apiVersion: v1
kind: Secret
metadata:
  name: ecommerce-db-secret
  namespace: ecommerce
type: Opaque
data:
  username: <base64-encoded-username>
  password: <base64-encoded-password>
  connection-string: <base64-encoded-connection-string>
```

### 2. Azure Key Vault Integration
```hcl
# Terraform Azure Key Vault
resource "azurerm_key_vault" "ecommerce" {
  name                        = "ecommerce-kv"
  location                    = var.location
  resource_group_name         = azurerm_resource_group.ecommerce.name
  tenant_id                  = var.tenant_id
  soft_delete_retention_days  = 90
  
  sku_name = "standard"
  
  access_policy {
    tenant_id = var.tenant_id
    object_id = var.object_id
  }
}

resource "azurerm_key_vault_secret" "db_password" {
  name         = "database-password"
  value        = var.db_password
  key_vault_id = azurerm_key_vault.ecommerce.id
}
```

### 3. Environment Variables Security
```yaml
# Secure environment variables
apiVersion: v1
kind: ConfigMap
metadata:
  name: ecommerce-config
  namespace: ecommerce
data:
  NODE_ENV: "production"
  API_URL: "https://api.ecommerce.com"
  LOG_LEVEL: "info"
  
# Reference secrets in deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ecommerce-deployment
  namespace: ecommerce
spec:
  template:
    spec:
      containers:
        - name: ecommerce-app
          env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: ecommerce-db-secret
                  key: connection-string
```

## 🚨 Compliance and Governance

### 1. Policy as Code
```yaml
# Gatekeeper admission controller
apiVersion: templates.gatekeeper.sh/v1beta1
kind: ConstraintTemplate
metadata:
  name: k8srequiredlabels
spec:
  crd:
    spec:
      names: ["apps"]
  targets:
    - api: ["apps/v1"]
      kinds: ["Deployment"]
  rego: |
    package k8srequiredlabels
    
    violation[{"msg": "missing required label", "details": {"missing_labels": "app"}}] {
      input.review.object.metadata.labels[_]
      not input.review.object.metadata.labels[_]
    }
    
    violation[{"msg": "missing required label", "details": {"missing_labels": "environment"}}] {
      input.review.object.metadata.labels[_]
      not input.review.object.metadata.labels[_]
    }
```

### 2. Security Monitoring
```yaml
# Falco - Runtime security monitoring
apiVersion: v1
kind: ConfigMap
metadata:
  name: falco-rules
  namespace: ecommerce
data:
  rules: |
    - rule: Suspicious Network Activity
      desc: Detect suspicious network connections
      condition: >
        spawned_process and 
        proc.name in (nc, ncat, telnet) and 
        not fd.type in ("pipe", "unix")
      output: >
        alert()
      priority: High
      tags: [network, security]
```

### 3. Audit Logging
```yaml
# Audit policy
apiVersion: audit.k8s.io/v1
kind: Policy
metadata:
  name: ecommerce-audit
spec:
  rules:
    - level: Metadata
      namespaces: ["ecommerce"]
      resources: ["pods", "services", "secrets"]
      omitStages: ["ResponseStarted"]
      omitManagedFields: ["controllerImage"]
```

## 🔧 CI/CD Security Integration

### 1. Jenkins Security Pipeline
```groovy
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'nayanarasse25/ecommerce-docker'
        SECURITY_SCAN = 'true'
    }
    
    stages {
        stage('Security Scan') {
            steps {
                script {
                    echo 'Running security scans...'
                    
                    // Container security scan
                    sh """
                        docker run --rm \
                          -v /var/run/docker.sock:/var/run/docker.sock \
                          aquasec/trivy:latest \
                          image ${DOCKER_IMAGE}:latest
                    """
                    
                    // Generate security report
                    archiveArtifacts artifacts: 'security-report.json'
                }
            }
        }
        
        stage('Deploy with Security Checks') {
            steps {
                script {
                    echo 'Checking security compliance...'
                    
                    // Only deploy if security checks pass
                    sh """
                        if [ "${SECURITY_SCAN}" = "true" ]; then
                            echo 'Security checks passed, proceeding with deployment...'
                            docker push ${DOCKER_IMAGE}:latest
                        else
                            echo 'Security checks failed, aborting deployment...'
                            exit 1
                        fi
                    """
                }
            }
        }
    }
}
```

### 2. GitHub Security Actions
```yaml
# .github/workflows/security-ci.yml
name: Security CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
      
    - name: Run security scan
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        format: 'sarif'
        
    - name: Upload security results
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'
        
    - name: Check for high vulnerabilities
      run: |
        if grep -q "HIGH" trivy-results.sarif; then
          echo "::error::High severity vulnerabilities found!"
          exit 1
        fi
        
    - name: Deploy only on main branch
      if: github.ref == 'refs/heads/main'
      run: |
        echo "Deploying to production..."
        # Add deployment commands here
```

## 📊 Security Monitoring and Alerting

### 1. Prometheus Security Metrics
```yaml
# Prometheus security rules
groups:
  - name: kubernetes-security
    rules:
      - alert: HighSeverityVulnerability
        expr: increase(container_vulnerabilities_high > 0)
        for: 5m
        labels:
          severity: critical
          team: security
          
      - alert: SuspiciousNetworkActivity
        expr: rate(network_connections_total[5m]) > 100
        for: 2m
        labels:
          severity: warning
          team: security
```

### 2. Grafana Security Dashboard
```json
{
  "dashboard": {
    "title": "ECommerce Security Dashboard",
    "panels": [
      {
        "title": "Vulnerability Trend",
        "type": "graph",
        "targets": [
          {
            "expr": "container_vulnerabilities_total",
            "legendFormat": "{{legend}}"
          }
        ]
      },
      {
        "title": "Security Alerts",
        "type": "table",
        "targets": [
          {
            "expr": "ALERTS_FOR_STATE",
            "format": "table"
          }
        ]
      }
    ]
  }
}
```

## 🎯 DevSecOps Security Best Practices

### 1. Security by Design
- **Threat Modeling**: Identify security requirements early
- **Secure Defaults**: Configure secure settings by default
- **Principle of Least Privilege**: Minimum required permissions
- **Defense in Depth**: Multiple security layers
- **Fail Securely**: Default to secure configuration

### 2. Automated Security Testing
- **Static Analysis**: Scan code for vulnerabilities
- **Dynamic Analysis**: Test running applications
- **Container Scanning**: Check images for security issues
- **Dependency Scanning**: Verify third-party packages
- **Infrastructure Testing**: Validate cloud configurations

### 3. Runtime Security
- **Real-time Monitoring**: Detect threats as they occur
- **Incident Response**: Automated threat mitigation
- **Log Analysis**: Security event correlation
- **Compliance Checking**: Continuous policy validation
- **Secrets Management**: Secure credential lifecycle

### 4. Security Metrics
- **Vulnerability Count**: Track security issues over time
- **Mean Time to Remediate**: MTTR for security issues
- **Security Debt**: Technical debt from security issues
- **Compliance Score**: Measure policy adherence
- **Security Coverage**: Percentage of code scanned

## 🔄 Continuous Security Improvement

### 1. Security Sprints
- **Dedicated Security Sprints**: Focus on security improvements
- **Bug Bounty Programs**: External security testing
- **Security Champions**: Internal security advocates
- **Regular Assessments**: Quarterly security reviews

### 2. Security Training
- **Developer Security Training**: Secure coding practices
- **DevSecOps Training**: Security in CI/CD pipelines
- **Threat Modeling Workshops**: Security design thinking
- **Incident Response Drills**: Security incident practice

### 3. Security Tools Integration
- **SIEM Integration**: Security Information and Event Management
- **SOAR Integration**: Security Orchestration and Automation
- **Vulnerability Management**: Track and remediate issues
- **Compliance Automation**: Policy enforcement tools

## 🎉 Advanced DevSecOps Complete!

You now have enterprise-grade security practices:

### ✅ Security Skills Mastered
- **Container Security**: Docker and Kubernetes hardening
- **Infrastructure Security**: Network and access controls
- **Application Security**: Code scanning and dependency checks
- **Secrets Management**: Secure credential handling
- **Compliance**: Policy as code and governance
- **Monitoring**: Real-time security visibility
- **Automation**: Security in CI/CD pipelines

### 🚀 Production-Ready Security Posture
Your DevSecOps practices now provide:
- **Zero Trust Architecture**: Never trust, always verify
- **Security Left**: Early integration in development
- **Continuous Security**: Automated testing and monitoring
- **Compliance Ready**: Regulatory and policy adherence
- **Incident Response**: Automated threat detection and response

This represents a mature, enterprise-grade DevSecOps security implementation!
