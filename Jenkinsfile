pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    environment {
        Docker_Image_Name = "myapp"
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

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
                sh """
                echo Building Docker image ${Docker_Image_Name}:${TAG}
                docker build -t ${Docker_Image_Name}:${TAG} .
                docker inspect ${Docker_Image_Name}:${TAG}
                """
            }
        }

        stage('Docker-Image-Verify') {
            steps {
                sh '''
                echo Verifying Docker image
                docker images --filter reference=${Docker_Image_Name}:${TAG}
                '''
            }
        }
    }
}