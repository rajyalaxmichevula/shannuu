pipeline {
    agent any

    environment {
        IMAGE_NAME = "app"
        IMAGE_TAG = "v2"
        DOCKER_REPO = "rajyalaxmichevula/shannu12"
    }

    stages {
        stage("Docker Login") {
            steps {
                echo "Logging into Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                }
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "Building Docker Image..."
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage("Push Docker Image to Docker Hub") {
            steps {
                echo "Tagging and pushing image..."
                bat '''
                    docker tag %IMAGE_NAME%:%IMAGE_TAG% %DOCKER_REPO%:latest
                    docker push %DOCKER_REPO%:latest
                '''
            }
        }

        stage("Deploy to Kubernetes") {
            steps {
                echo "Deploying to Kubernetes..."
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
        stage('Restart Deployment'){
              steps{
                  echo "Restarting Deployment to pick up new image.."
                  bat "Kubectl rollout restart deployment/app-deployment"
              }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}
