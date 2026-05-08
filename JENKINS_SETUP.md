# 🔧 Jenkins CI/CD Setup Guide

This guide will help you set up Jenkins for automated Docker builds as part of your DevSecOps Level 4 learning.

## 📋 Prerequisites

- Docker Desktop installed and running
- Your ECommerce project with Dockerfile
- GitHub account (nayanarasse25)
- Jenkinsfile created

## 🚀 Quick Setup

### 1. Run the Setup Script
```bash
# Navigate to project directory
cd "c:\Users\HP\OneDrive\Desktop\CNA pro\ECommerce-SOAP-MERN"

# Make setup script executable (Linux/Mac)
chmod +x setup-jenkins.sh

# Run Jenkins setup
./setup-jenkins.sh
```

### 2. Access Jenkins
- Open: http://localhost:9090
- Username: `admin`
- Password: Use the password shown in setup output

## 📚 Manual Jenkins Setup

### Alternative: Manual Docker Command
```bash
docker run -d \
  --name jenkins-master \
  -p 9090:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$(which docker):/usr/bin/docker" \
  --restart unless-stopped \
  jenkins/jenkins:lts
```

## 🔌 Required Jenkins Plugins

Install these plugins through Jenkins UI:

1. **Git Plugin** - For GitHub integration
2. **Docker Pipeline Plugin** - For Docker commands
3. **GitHub Integration Plugin** - For webhook triggers
4. **Email Extension Plugin** - For notifications
5. **Pipeline Utility Steps** - For advanced pipeline steps

## 🔗 GitHub Integration Setup

### 1. Create GitHub Repository
- Repository: `ecommerce-docker`
- URL: `https://github.com/nayanarasse25/ecommerce-docker`

### 2. Set up Webhook
In GitHub repository settings:
1. Go to Settings → Webhooks
2. Add webhook: `http://localhost:9090/github-webhook/`
3. Select "Just the push event"
4. Add webhook

### 3. Configure Jenkins Credentials
In Jenkins Dashboard:
1. Manage Jenkins → Manage Credentials
2. Add Credentials → Global
3. Kind: Username with password
4. Scope: Global
5. ID: `docker-hub-credentials`
6. Add your Docker Hub credentials

## 📝 Creating Your First Pipeline

### 1. New Item
1. Click "New Item" in Jenkins
2. Name: `ecommerce-pipeline`
3. Select "Pipeline"
4. Click OK

### 2. Pipeline Configuration
1. Scroll down to "Pipeline" section
2. Select "Pipeline script from SCM"
3. SCM: Git
4. Repository URL: `https://github.com/nayanarasse25/ecommerce-docker.git`
5. Script Path: `Jenkinsfile`
6. Save

### 3. Build Now
1. Click "Build Now"
2. Watch the pipeline execute
3. Check console output

## 🔄 Pipeline Stages Explained

Your Jenkinsfile includes these stages:

### 1. Checkout
- Clones your GitHub repository
- Uses your credentials to access private repos

### 2. Build Docker Image
- Runs `docker build` command
- Tags image with version number

### 3. Test Container
- Starts container in test mode
- Runs health checks
- Stops and cleans up test container

### 4. Push to Registry
- Logs into Docker Hub
- Pushes image to registry
- Tags with build number

### 5. Deploy
- Pulls latest image
- Stops old container
- Starts new container

## 📧 Email Notifications

Configure email in Jenkins:
1. Manage Jenkins → Configure System
2. E-mail Notification section
3. Add your SMTP settings
4. Test email configuration

## 🛠️ Useful Jenkins Commands

```bash
# View Jenkins logs
docker logs jenkins-master

# Restart Jenkins
docker restart jenkins-master

# Access Jenkins shell
docker exec -it jenkins-master /bin/bash

# Backup Jenkins data
docker cp jenkins-data:/var/jenkins_home ./jenkins-backup
```

## 🎯 DevSecOps Level 4 Complete

Once Jenkins is running and your pipeline works, you've mastered:

### ✅ CI/CD Concepts
- ✅ Continuous Integration (automated builds)
- ✅ Continuous Deployment (automated deployment)
- ✅ Pipeline as Code (Jenkinsfile)
- ✅ Automated testing
- ✅ Container registry integration

### ✅ Jenkins Skills
- ✅ Jenkins setup and configuration
- ✅ Pipeline creation and management
- ✅ GitHub integration
- ✅ Docker integration
- ✅ Automated builds and deployments

## 🔄 Next Level: Azure Cloud

After completing Jenkins setup, you're ready for:
- **Level 5**: Microsoft Azure Overview
- **Cloud deployment**: Deploy containers to Azure
- **Infrastructure as Code**: Learn Terraform
- **Advanced DevSecOps**: Security in CI/CD

## 🚨 Troubleshooting

### Common Issues

**Jenkins won't start:**
```bash
# Check if port 9090 is free
netstat -ano | findstr :9090

# Check Docker logs
docker logs jenkins-master
```

**Pipeline fails on Docker build:**
- Check if Docker is accessible from Jenkins container
- Verify Jenkins has Docker socket access
- Check Jenkinsfile syntax

**GitHub webhook not working:**
- Verify Jenkins is accessible from internet
- Check webhook URL in GitHub settings
- Look at Jenkins logs for webhook attempts

**Docker push fails:**
- Verify Docker Hub credentials in Jenkins
- Check if image name is correct
- Ensure you're logged into Docker Hub

## 🎉 Success!

You now have a complete CI/CD pipeline that:
- Automatically builds on code changes
- Tests your Docker containers
- Pushes to container registry
- Deploys to production
- Sends notifications on success/failure

This is a professional-grade DevOps setup that demonstrates your CI/CD skills!
