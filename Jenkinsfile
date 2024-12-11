pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone mã nguồn từ GitHub
                git branch: 'main', // Thay 'main' bằng nhánh bạn muốn clone
                    url: 'https://github.com/ducluong16/Test_KTLHPM.git' // URL repo GitHub
            }
        }
    }

}
