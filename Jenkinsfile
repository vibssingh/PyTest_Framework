pipeline {
  agent any

  stages {
    stage('Test') {
      steps {
        bat "cd tests"
        bat "pytest  --html=Reports/report.html -s"
      }

      post {

        // If some of the test failed, still record the test results and archive the jar file.
        success {
          publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: false,
            keepAll: false,
            reportDir: 'Reports',
            reportFiles: 'report.html',
            reportName: 'PyTest HTML Report',
            reportTitles: '',
            useWrapperFileDirectly: true
          ])
        }
      }
    }
  }
}