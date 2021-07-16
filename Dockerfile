FROM python:3.10.0b4-buster

WORKDIR C:/Users/ekrem/Projects/BDDTest

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY C:/Users/ekrem/Projects/BDDTest .

CMD ["appium --port 4723"]
CMD ["behave -f allure_behave.formatter:AllureFormatter -o reports/feature"]