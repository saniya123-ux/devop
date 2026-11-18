pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t adrios12-app:latest .'
                echo 'Docker image built successfully!'
            }
        }
        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f adrios12-container || exit 0'
                bat 'docker run -d --name adrios12-container -p 8081:80 adrios12-app:latest'
            }
        }
    }
}

