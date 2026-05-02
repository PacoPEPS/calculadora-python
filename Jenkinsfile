pipeline {
    agent any

    triggers {
        githubPush()
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Program') {
            steps {
                sh 'python3 calculadora.py 3 4'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest'
            }
        }
    }
}
