pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                bat "cd tests"
                bat "pytest  --html=Reports/report.html -s"
            }

            post {

                // If Maven was able to run the tests, even if some of the test
                // failed, record the test results and archive the jar file.
                success {
                  publishHTML([
                              allowMissing: false,
                              alwaysLinkToLastBuild: false,
                              keepAll: false,
                              reportDir: 'Reports',
                              reportFiles: 'report.html',
                              reportName: 'report',
                              reportTitles: '',
                              useWrapperFileDirectly: true])
                }
            }
        }
    }
}