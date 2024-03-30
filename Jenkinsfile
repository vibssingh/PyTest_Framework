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
            reportName: 'PyTest HTML Report',
            reportTitles: '',
            useWrapperFileDirectly: true
          ])
        }

        always {
          // Send email notification regardless of the build result
          emailext(
            to: 'vibhasingh2004@gmail.com',
            subject: "Test Execution Report: ${currentBuild.fullDisplayName}",
            body: 'Test execution for ${currentBuild.fullDisplayName} has completed.',
            attachLog: true // Attach build log to the email
          )
        }
      }
    }
  }
}