pipeline {
  agent any

  stages {

     stage('Install dependencies') {
      steps {
        bat '''
           python3 -m venv venv
           source venv/bin/activate
           pip install pytest
        ''' 
        
      }
     }
       
    stage('Run Test') {
      steps {
       bat ''' 
         cd tests
         pytest
        '''
      }
    }
  }

      post {

        // If some of the test failed, still record the test results and archive the jar file.
        success {
          publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: false,
            keepAll: false,
            reportDir: 'Reports',
            reportFiles: 'Report.html',
            reportName: 'PyTest HTML Report',
            reportTitles: '',
            useWrapperFileDirectly: true
          ])
        }
      }
    }

