pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        TAG = "v${BUILD_NUMBER}"  // استخدم الـ Jenkins Build Number
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
                echo Building Docker image ${IMAGE_NAME}:${TAG}
                docker build -t ${IMAGE_NAME}:${TAG} .
                '''
            }
        }

        stage('Docker-Image-Verify') {
            steps {
                sh '''
                echo Verifying Docker image ${IMAGE_NAME}:${TAG}
                docker images --filter "reference=${IMAGE_NAME}:${TAG}"
                '''
            }
        }
    }
}