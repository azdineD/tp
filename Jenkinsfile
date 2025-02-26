pipeline {
    agent any

    stages {
        stage('de_git') {
            steps {
                git branch: 'main', url: 'https://github.com/azdineD/tp.git'
            }
        }

        stage('Installation') {
            steps {
                script {
                    echo "Installing Python and dependencies..."
		sh 'apt-get update && apt-get install -y python3 python3-pip'                }
            }
        }
        stage('pyhton Script') {
            steps {
                script {
                    echo "Executop, du script script..."
                    sh 'python3 addition.py'
                }
            }
        }
        stage('demarage du Tests') {
            steps {
                script {
                    echo "demarage des  tests..."
                    sh 'python3 -m unittest test_addition.py'
                }
            }
        }
    }
}
