pipeline {
    agent any
   
    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"
                bat '"C:\\Users\\shara\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'

                bat 'start /B python app.py'
                bat 'ping 127.0.0.1 -n 5 > nul'
                bat 'pytest -v --maxfail=1 --disable-warnings'
            }
        }


        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t rajyalaxmichevula/week12:t5 ."
            }
        }

        stage('Docker Login') {
            steps {
                bat 'docker login -u rajyalaxmichevula -p @shannu2212'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat "docker push rajyalaxmichevula/week12:t5"
            }
        }

        stage('Deploy to Kubernetes') { 
            steps { 
                bat 'kubectl apply -f deployment.yaml --validate=false' 
                bat 'kubectl apply -f service.yaml' 
            } 
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
