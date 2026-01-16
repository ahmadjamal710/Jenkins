pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'echo "Jenkins is working ✅"'
            }
        }
    }

    post {
        success {
            echo 'Build SUCCESS 🎉'
        }
        failure {
            echo 'Build FAILED ❌'
        }
    }
}