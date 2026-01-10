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
            when {
                expression {
                    return env.GIT_BRANCH == "origin/test"
                }
            }
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
    }
}