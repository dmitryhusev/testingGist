pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip install -r requirements.txt"
            }
        }
        stage('Run tests'){
            steps {
                sh "pytest $THREADS_NUMBER"

            }
        }
    }
}
