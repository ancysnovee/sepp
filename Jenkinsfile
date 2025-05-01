pipeline{
    agent any
    stages{
        stage("cloning"){
            steps{
                git url:"https://github.com/ancysnovee/sepp.git", branch:"main"
            }
        }
        stage("install dependency"){
            steps{
                bat '''
                    C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m venv venv
                    call venv\\Scripts\\Activate
                    pip install --upgrade pip
                    pip install pytest
                '''
            }
        }
        stage("testing"){
            steps{
                bat '''
                    call venv\\Scripts\\Activate
                    pytest test.py
                '''

            }

        }
        stage("deploy"){
            steps{
                bat '''
                call venv\\Scripts\\Activate
                C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe school.py
            '''

            }
            
        }
    }
}
