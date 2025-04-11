pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
            }
        }
        stage('Notify') {
            steps {
                echo 'Notifying...'
            }
        }
        stage('Archive') {
            steps {
                echo 'Archiving...'
            }
        }
        stage('Report') {
            steps {
                echo 'Reporting...'
            }
        }
        stage('Approval') {
            steps {
                input message: 'Do you want to proceed with the deployment?', ok: 'Yes'
            }
        }
        stage('Post-Deployment') {
            steps {
                echo 'Post-deployment tasks...'
            }
        }
        stage('Finalization') {
            steps {
                echo 'Finalizing...'
            }
        }
    }
}