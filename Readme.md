# Getir Android BDD Test Automation

In this project; appium.io , python-behave library and for reporting; allure-reporting and junit reporter libraries are used.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install behave and allure-report.

```bash
pip install Appium-Python-Client
pip install behave
pip install allure-behave
```

There are behave and allure-report download links. You can use these links for setting up ;
[appium](https://pypi.org/project/Appium-Python-Client/),
[behave ](https://pypi.org/project/behave/), 
[allure-report](https://pypi.org/project/allure-behave/).

## Running Tests

```python
# start appium server with true port

# run this command on terminal;
behave feature/('this is running for all tests')
behave feature/AddBasket.feature ('this is running for a specific test')

```

## Reporting
```python
# run below command for create a report file;
# behave –f allure behave.formatter:AllureFormatter –o name of report folder you want” [Path where your features are present];
behave -f allure_behave.formatter:AllureFormatter -o reports/feature

```
```python
# run below command for generate a report;
# allure generate [path where reports are present]
allure generate C:\Users\ekrem\Projects\BDDTest\reports

```
```python
# run below command for open the created report;
# allure open [path where index file is present]
allure open C:\Users\ekrem\Projects\BDDTest\allure-report
```

```python
# run below command also creates a xml file report;
# behave --junit [path where index file]
behave --junit 
```