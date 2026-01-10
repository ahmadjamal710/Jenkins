pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '1'))
    }

    environment {
        IMAGE_NAME = "myapp"
    }

    stages {

        stage('Pre-Checks') {
            parallel {
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
            }
        }

        stage('Docker-Build') {
            steps {
                sh '''
                echo Building Docker image ${IMAGE_NAME}:${BUILD_NUMBER}
                docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                docker inspect ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }

        stage('Docker-Image-Verify') {
            steps {
                sh '''
                echo Verifying Docker image
                docker images --filter reference=${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }
    }
}