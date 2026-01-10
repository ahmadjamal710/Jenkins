pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        TAG = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker-Verify') {
            steps {
                retry(3) {
                    sh 'docker --version'
                }

                timeout(time: 10, unit: 'SECONDS') {
                    sh 'sleep 30'
                }
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
                sh 'docker images --filter "reference=${IMAGE_NAME}:${TAG}"'
            }
        }
    }
}