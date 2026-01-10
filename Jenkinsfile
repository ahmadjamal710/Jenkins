pipeline {
    agent any
    environment {
        Docker_Image_Name = "myapp"
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '1'))
    }
    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Check Branch') {
            steps {
                echo "Current branch: ${env.GIT_BRANCH}"
            }
        }

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
                    return env.GIT_BRANCH == "main" || env.GIT_BRANCH == "origin/main"
                }
            }
            steps {
                sh "echo Building Docker image ${Docker_Image_Name}:${env.BUILD_NUMBER}"
                sh "docker build -t ${Docker_Image_Name}:${env.BUILD_NUMBER} ."
                sh "docker inspect ${Docker_Image_Name}:${env.BUILD_NUMBER}"
            }
        }

        stage('Docker-Image-Verify') {
            steps {
                sh "echo Verifying Docker image"
                sh "docker images --filter reference=${Docker_Image_Name}:${env.BUILD_NUMBER}"
            }
        }

        stage('Docker-CleanUp') {
            steps {
                sh 'sudo docker rm -f $(sudo docker ps -a -q) 2> /dev/null || true'
            }
        }

        stage('Docker-Deploy') {
            steps {
                sh "sudo docker run -itd -p 80:80 ${Docker_Image_Name}:${env.BUILD_NUMBER}"
                sh "sudo docker ps"
            }
        }
    }
}
   