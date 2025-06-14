pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Préparation') {
            steps {
                echo 'Création de l’environnement virtuel'
		sh 'python3 -m venv $VENV_DIR'
            }
        }

        stage('Install') {
            steps {
                echo 'Activation et installation des dépendances'
                sh '''
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run') {
            steps {
                echo 'Exécution du script principal'
                sh '''
                    python3 main.py
                    if [ $? -ne 0 ]; then
                      echo "Erreur dans main.py"
                      exit 1
                    fi
                '''
            }
        }

        stage('Archive') {
            steps {
                echo 'Archivage des fichiers résultats'
                archiveArtifacts artifacts: '**/*.csv', allowEmptyArchive: false
            }
        }
    }

    post {
        always {
            echo 'Nettoyage de l’environnement virtuel'
            sh 'rm -rf $VENV_DIR || true'
        }
        failure {
            echo 'Le pipeline a échoué — consultez les logs.'
        }
    }
}
