# 🐳 Docker Guide for ECommerce-SOAP-MERN

This guide will help you understand and use Docker for containerizing your ECommerce project as part of your DevSecOps Level 3 learning.

## 📋 Prerequisites

- Docker Desktop installed and running
- Basic understanding of command line
- Your ECommerce-SOAP-MERN project files

## 🏗️ Project Structure

```
ECommerce-SOAP-MERN/
├── Dockerfile              # Container build instructions
├── docker-compose.yml      # Multi-container orchestration
├── nginx.conf              # Nginx web server configuration
├── .dockerignore           # Files to exclude from build
├── soap-simple.html       # Main homepage
├── cart.html              # Shopping cart page
├── payment.html           # Payment processing page
├── login.html             # User login page
├── register.html          # User registration page
├── profile.html           # User profile page
├── product-detail.html    # Product details page
└── images/                # Product and carousel images
```

## 🚀 Quick Start

### 1. Build the Docker Image

```bash
# Navigate to project directory
cd "c:\Users\HP\OneDrive\Desktop\CNA pro\ECommerce-SOAP-MERN"

# Build the image
docker build -t lushlather-ecommerce .
```

### 2. Run the Container

```bash
# Run the container (port 8080 on host maps to port 80 in container)
docker run -d -p 8080:80 --name lushlather-test lushlather-ecommerce

# Access your application
# Open: http://localhost:8080
```

### 3. Stop and Remove Container

```bash
# Stop the container
docker stop lushlather-test

# Remove the container
docker rm lushlather-test
```

## 📚 Docker Commands Cheat Sheet

### Image Management
```bash
# Build an image
docker build -t <image-name> .

# List all images
docker images

# Remove an image
docker rmi <image-name>

# Remove all unused images
docker image prune
```

### Container Management
```bash
# Run a container
docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop <container-name>

# Start a container
docker start <container-name>

# Remove a container
docker rm <container-name>

# View container logs
docker logs <container-name>

# Execute commands inside a running container
docker exec -it <container-name> /bin/sh
```

### Using Docker Compose
```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs

# Rebuild and start
docker-compose up --build
```

## 🔧 Configuration Files Explained

### Dockerfile
- **Base Image**: Uses `nginx:alpine` (lightweight web server)
- **Working Directory**: Sets `/usr/share/nginx/html` as the web root
- **File Copy**: Copies all project files to the container
- **Port Exposure**: Exposes port 80 for web traffic
- **Command**: Starts nginx server

### nginx.conf
- **Static File Serving**: Configures nginx to serve HTML, CSS, JS, and images
- **Compression**: Enables gzip compression for better performance
- **Caching**: Sets appropriate caching headers for different file types
- **Security Headers**: Adds security headers for protection
- **Error Handling**: Configures custom error pages

### docker-compose.yml
- **Service Definition**: Defines the frontend service
- **Port Mapping**: Maps host port 8080 to container port 80
- **Networking**: Creates a custom network for services
- **Restart Policy**: Configures automatic restart on failure
- **Monitoring**: Optional monitoring service (can be enabled with profile)

## 🎯 DevSecOps Learning Objectives Met

### ✅ Level 3: Containerization (Docker)

**Topics Covered:**
- ✅ What is Docker? (Containerizing your web application)
- ✅ Containers vs VMs (Lightweight, fast startup)
- ✅ Docker images (Created `lushlather-ecommerce` image)
- ✅ Dockerfile (Comprehensive build instructions)
- ✅ Docker Compose (Multi-container orchestration)

**Commands Practiced:**
- ✅ `docker build` - Build images
- ✅ `docker run` - Run containers
- ✅ `docker ps` - List containers
- ✅ `docker logs` - View logs
- ✅ `docker-compose up` - Start services

**Mini Project Completed:**
- ✅ Containerized a web application (ECommerce site)
- ✅ Used nginx as the web server
- ✅ Configured proper file serving and caching
- ✅ Added security headers and optimizations

## 🔄 Next Steps for DevSecOps Roadmap

### Level 4: CI/CD with Jenkins
Now that you have Docker working, you can:
1. **Set up GitHub Repository**: Create repo at `https://github.com/nayanarasse25/ecommerce-docker`
2. **Set up Jenkins container**: Use Docker to run Jenkins
3. **Create a pipeline**: Automatically build your Docker image on code push
4. **Push to container registry**: Docker Hub or GitHub Container Registry
5. **Deploy automatically**: Continuous deployment pipeline

### Level 5: Microsoft Azure Overview
1. **Create Azure account**: Free tier available
2. **Deploy Docker container**: Azure Container Instances or App Service
3. **Set up Azure Container Registry**: Private container registry
4. **Learn cloud deployment**: IaaS, PaaS, SaaS concepts

### GitHub Setup Commands
```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit: Dockerized ECommerce application"

# Add remote (replace with your actual GitHub repo)
git remote add origin https://github.com/nayanarasse25/ecommerce-docker.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 🛠️ Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
# Check what's using port 8080
netstat -ano | findstr :8080

# Use a different port
docker run -d -p 8081:80 --name lushlather-test lushlather-ecommerce
```

**Build Context Too Large:**
- Check your `.dockerignore` file
- Exclude unnecessary files and directories

**Container Not Starting:**
```bash
# Check logs
docker logs lushlather-test

# Check if nginx config is valid
docker exec lushlather-test nginx -t
```

**Images Not Loading:**
- Verify image paths in HTML files
- Check if images are copied correctly to container
- Use `docker exec` to inspect container contents

### Performance Optimization

- Use `.dockerignore` to reduce build context
- Enable gzip compression (already configured)
- Set proper caching headers (already configured)
- Use multi-stage builds for production (advanced)

## 📝 Best Practices

1. **Use Specific Image Tags**: Instead of `nginx:latest`, use `nginx:alpine`
2. **Minimize Layers**: Combine RUN commands when possible
3. **Use .dockerignore**: Exclude unnecessary files
4. **Security**: Use non-root users in production (advanced)
5. **Health Checks**: Add health checks to containers
6. **Resource Limits**: Set memory and CPU limits

## 🎉 Success!

You've successfully containerized your ECommerce application! This demonstrates:
- Understanding of Docker concepts
- Ability to create Dockerfiles
- Container orchestration with Docker Compose
- Web server configuration
- Security best practices

Your application is now running in a portable, scalable container that can be deployed anywhere Docker is available!
