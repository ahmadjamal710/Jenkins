pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-image"
    }

    stages {

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
                  echo "Building Docker Image"
                  docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                '''
            }
        }
    }
}