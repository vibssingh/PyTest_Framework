pipeline {
  agent any

  stages {

     stage('Install dependencies') {
      steps {
        bat '''
           pip install pytest
        ''' 
        
      }
     }
       
    stage('Run Test') {
      steps {
       bat ''' 
         cd tests
         python -m pytest
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

