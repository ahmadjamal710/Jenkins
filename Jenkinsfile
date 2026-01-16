pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '3'))
        timestamps()
    }

    stages {

        stage('Verify Tools') {
            steps {
                sh 'git --version || true'
                sh 'docker --version'
            }
        }

        stage('Docker Build') {
            steps {
                sh """
                  echo "Building image ${IMAGE_NAME}:${BUILD_NUMBER}"
                  docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                """
            }
        }

        stage('Docker Image Verify') {
            steps {
                sh """
                  docker images | grep ${IMAGE_NAME}
                """
            }
        }

        stage('Docker Deploy') {
            steps {
                sh """
                  docker run -d \
                    --name ${IMAGE_NAME}_${BUILD_NUMBER} \
                    -p 8081:80 \
                    ${IMAGE_NAME}:${BUILD_NUMBER}
                """
                sh 'docker ps'
            }
        }
    }

    post {
        failure {
            echo "❌ Build Failed"
        }
        success {
            echo "✅ Build Succeeded"
        }
    }
}