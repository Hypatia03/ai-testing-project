pipeline {

    agent any

    tools {
        allure 'allure'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Thêm --clean-alluredir để tự động dọn sạch kết quả cũ của lượt build trước
                bat '"C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v --alluredir=allure-results --clean-alluredir'
            }
        }

    }

    post {
        always {
            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            )
        }
    }
}