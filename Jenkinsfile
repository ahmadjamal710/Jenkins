pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        TAG = "1.0"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker-Verify') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Git-Verify') {
            steps {
                sh 'git --version'
            }
        }

        stage('Docker-Build') {
            steps {
                sh '''
                echo Building Docker image ${IMAGE_NAME}:v${TAG}
                docker build -t ${IMAGE_NAME}:v${TAG} .
                '''
            }
        }
    }
}