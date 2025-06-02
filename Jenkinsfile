pipeline {
    agent any

    stages {
        stage('Clean Up Old Containers') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker rm -f log-watcher log-writer jenkins || true'
            }
        }

        stage('Build & Run Containers') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }

        stage('Check Container Status') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        always {
            echo "Pipeline run completed."
        }
    }
}

