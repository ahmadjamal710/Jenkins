pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '1'))
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
                sh """
                    echo Building Docker image ${IMAGE_NAME}:${env.BUILD_NUMBER}
                    docker build -t ${IMAGE_NAME}:${env.BUILD_NUMBER} .
                    docker inspect ${IMAGE_NAME}:${env.BUILD_NUMBER}
                """
            }
        }

        stage('Docker-Image-Verify') {
            steps {
                sh """
                    echo Verifying Docker image
                    docker images --filter reference=${IMAGE_NAME}:${env.BUILD_NUMBER}
                """
            }
        }

        stage('Docker-CleanUp') {
            steps {
                sh ' docker rm -f $( docker ps -a -q) 2> /dev/null || true'
            }
        }

        stage('Docker-Deploy') {
            steps {
                sh " docker run -itd -p 80:80 ${IMAGE_NAME}:${env.BUILD_NUMBER}"
                sh " docker ps"
            }
        }
    }
}