pipeline {
    agent any

    stages {

        stage('Build Program A') {
            steps {
                script {
                    sh '''
                        docker build -t program_a ./program_a
                    '''
                }
            }
        }

        stage('Run Program A') {
            steps {
                script {
                    sh '''
                        docker run --rm \
                            -v ./tests:/tests \
                            -v ./program_a/results:/results \
                            program_a
                    '''
                }
            }
        }

        stage('Build Program B') {
            steps {
                script {
                    sh '''
                        docker build -t program_b ./program_b
                    '''
                }
            }
        }

        stage('Run Program B') {
            steps {
                script {
                    sh '''
                        docker run --rm \
                            -v ./tests:/tests \
                            -v ./program_b/results:/results \
                            program_b
                    '''
                }
            }
        }

        stage('Compare Results') {
            steps {
                script {
                    sh '''
                        python3 compare.py 
                    '''
                }
            }
        }
    }
}