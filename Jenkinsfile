pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh "python3 -m venv venv"
                sh "source venv/bin/activate"
                sh "python3 -m pip install -r requirements.txt"
            }
        }
        stage('Run tests'){
            steps {
                sh "source venv/bin/activate"
                sh "pytest $THREADS_NUMBER"

            }
        }
    }
}
