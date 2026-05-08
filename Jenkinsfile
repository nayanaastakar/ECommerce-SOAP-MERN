pipeline {
    agent any

    tools {
        maven 'Maven 3.6.3'
    }

    environment {
        DOCKER_IMAGE = 'nayanarasse25/ecommerce-docker'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Checking out source code...'
                    git branch: 'main', url: 'https://github.com/nayanarasse25/ecommerce-docker.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    
                    echo 'Docker image built successfully!'
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    echo 'Testing Docker container...'
                    
                    // Run container in test mode
                    sh """
                        docker run -d --name test-container -p 8081:80 ${DOCKER_IMAGE}:${DOCKER_TAG}
                        sleep 10
                        curl -f http://localhost:8081 || exit 1
                        docker stop test-container
                        docker rm test-container
                    """
                    
                    echo 'Container test passed!'
                }
            }
        }

        stage('Push to Registry') {
            steps {
                script {
                    echo 'Pushing Docker image to registry...'
                    
                    // Tag for registry
                    sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                    
                    // Push to Docker Hub (you'll need to configure credentials)
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh """
                            echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin
                            docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                            docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        """
                    }
                    
                    echo 'Image pushed to registry successfully!'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to production...'
                    
                    // Example deployment step (customize based on your target)
                    sh """
                        # Pull latest image
                        docker pull ${DOCKER_IMAGE}:${DOCKER_TAG}
                        
                        # Stop old container if running
                        docker stop ecommerce-app || true
                        docker rm ecommerce-app || true
                        
                        # Run new container
                        docker run -d --name ecommerce-app -p 8080:80 ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                    
                    echo 'Deployment completed successfully!'
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'Cleaning up...'
                sh 'docker system prune -f'
            }
        }
        
        success {
            script {
                echo 'Pipeline completed successfully!'
                // Send notification (optional)
                emailext (
                    subject: "✅ ECommerce Deployment Successful",
                    body: "The ECommerce application has been successfully deployed!\nBuild: ${BUILD_NUMBER}\nCommit: ${GIT_COMMIT}",
                    to: "nayanarasse25@example.com"
                )
            }
        }
        
        failure {
            script {
                echo 'Pipeline failed!'
                emailext (
                    subject: "❌ ECommerce Deployment Failed",
                    body: "The ECommerce deployment failed!\nBuild: ${BUILD_NUMBER}\nPlease check Jenkins logs.",
                    to: "nayanarasse25@example.com"
                )
            }
        }
    }
}
