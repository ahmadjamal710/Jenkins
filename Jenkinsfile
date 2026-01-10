pipeline {
    agent any

    environment {
        Docker_Image_Name = "myapp"
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '1'))
    }

    stages {

        stage('Pre-Checks') {
            parallel {

                stage('Docker-Verify') {
                    steps {
                        retry(3) {
                            sh 'docker --version'
                        }
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
                    return env.GIT_BRANCH == "origin/main"
                }
            }
            steps {
                retry(3) {
                    sh "echo Building Docker image ${Docker_Image_Name}:${env.BUILD_NUMBER}"
                    sh "docker build -t ${Docker_Image_Name}:${env.BUILD_NUMBER} ."
                    sh "docker inspect ${Docker_Image_Name}:${env.BUILD_NUMBER}"
                }
            }
        }

        stage('Docker-Image-Verify') {
            steps {
                sh "echo Verifying Docker image"
                sh "docker images --filter reference=${Docker_Image_Name}:${env.BUILD_NUMBER}"
            }
        }
    }
}