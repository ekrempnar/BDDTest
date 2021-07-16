pipeline {
  agent any

  stages {

    stage('Checkout') {
      steps{
         checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ekrempnar/BDDTest.git']]])
      }
    }

    stage('Build') {
      steps{
         git branch: 'main', url: 'https://github.com/ekrempnar/BDDTest.git'
         bat ' behave feature/'
      }
    }

    stage('Test') {
      steps{
         echo 'The BDD test succeeded'
      }
    }

  }

}
