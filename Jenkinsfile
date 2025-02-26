pipeline {
    agent any

    stages {
        stage('de git') {
            steps {
                git branch: 'main', url: 'https://github.com/azdineD/tp.git'
            }
        }

        stage('Tests') {
            steps {
                script {
                    echo "lancement du tests..."
                    sh 'python3 -m unittest test_addition.py'
                }
            }
        }

        stage('creation image Docker') {
            steps {
                script {
                    echo "creation  image Docker .."
                    sh 'docker build -t azdineD/addition:latest .'
                }
            }
        }

        stage(' Docker Container') {
            steps {
                script {
                    echo "demarragedu Docker container..."
                    sh 'docker run --rm azdineD/addition 5 10'
                }
            }
        }
    }
}
