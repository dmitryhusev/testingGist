pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "python3 -m pip install -r requirements.txt"
            }
        }
        stage('Run tests'){
            steps {
                sh ". venv/bin/activate"
                sh "ls -l"
                sh "python3 -m pytest $THREADS_NUMBER src/tests"

            }
        }
    }
}
