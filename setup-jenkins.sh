#!/bin/bash

# Jenkins Setup Script for DevSecOps Level 4
# This script sets up Jenkins with Docker for CI/CD

echo "🚀 Setting up Jenkins for ECommerce CI/CD Pipeline..."

# Create Jenkins data directory
echo "Creating Jenkins data directory..."
mkdir -p jenkins-data

# Stop any existing Jenkins container
echo "Stopping existing Jenkins container..."
docker stop jenkins-master 2>/dev/null || true
docker rm jenkins-master 2>/dev/null || true

# Run Jenkins container
echo "Starting Jenkins container..."
docker run -d \
  --name jenkins-master \
  -p 9090:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$(which docker):/usr/bin/docker" \
  --restart unless-stopped \
  jenkins/jenkins:lts

echo "⏳ Waiting for Jenkins to start..."
sleep 30

# Get initial admin password
echo "Getting Jenkins initial admin password..."
ADMIN_PASSWORD=$(docker exec jenkins-master cat /var/jenkins_home/secrets/initialAdminPassword)

echo "✅ Jenkins is running!"
echo "🌐 Access Jenkins at: http://localhost:9090"
echo "🔑 Initial Admin Password: $ADMIN_PASSWORD"
echo ""
echo "📋 Next Steps:"
echo "1. Open http://localhost:9090 in your browser"
echo "2. Use 'admin' as username and the password shown above"
echo "3. Install recommended plugins"
echo "4. Create your first admin user"
echo "5. Set up GitHub integration"
echo "6. Create your first pipeline using the Jenkinsfile"
echo ""
echo "🔧 Jenkins Commands:"
echo "View logs: docker logs jenkins-master"
echo "Stop Jenkins: docker stop jenkins-master"
echo "Start Jenkins: docker start jenkins-master"
