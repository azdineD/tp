pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/azdineD/tp.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing Python and dependencies..."
                    sh 'sudo apt-get update && sudo apt-get install -y python3 python3-pip'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running unit tests..."
                    sh 'python3 -m unittest test_addition.py'
                }
            }
        }
    }
}
