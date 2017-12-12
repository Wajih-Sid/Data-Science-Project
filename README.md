# Data-Science-Project
Data Sets used from Kaggle

- https://www.kaggle.com/ludobenistant/hr-analytics-1/data

- https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset/data



## API

The APIs for this project are located in the folder apiserver/HRProject.py

The API server runs on Flask with the url:
<pre><code>"http://mohsinaslam.pythonanywhere.com/predict"</code></pre>

- Run a POST request from any REST client to test.


## Angular Website

The website is built on Angular 1.5 and requires node, npm dependancies

- Goto directory website
- Run `npm start`
- Should give the following response:
    <pre><code>
        > angular-seed@0.0.0 start /home/wajih/PycharmProjects/Data-Science-Project/apiserver/website
        > http-server -a localhost -p 8080 -c-1 ./app
         Starting up http-server, serving ./app
         Available on: http://localhost:8080
         Hit CTRL-C to stop the server
    </code></pre>
    
 ## Testing the App
 
 - Goto URL `http://localhost:8080/?#!/employee_churn`
 - Fill Form Data and hit Submit
 - On submit the endpoint `get_churn` is hit.
 
 ## Demo for Using the API:
 - Install POSTMAN REST client.
 - Use URL: "http://mohsinaslam.pythonanywhere.com/predict"
 - Use payload as:
 <pre><code>
 {
  "PercentSalaryHike": [
    28
  ],
  "RelationshipSatisfaction": [
    3
  ],
  "YearsSinceLastPromotion": [
    2
  ],
  "number_project": [
    2
  ],
  "EnvironmentSatisfaction": [
    4
  ],
  "sales": [
    "Research & Development"
  ],
  "MonthlyRate": [
    23159
  ],
  "Over18": [
    "Y"
  ],
  "Department": [
    "Research & Development"
  ],
  "JobLevel": [
    1
  ],
  "TotalWorkingYears": [
    8
  ],
  "satisfaction_level": [
    0.99
  ],
  "JobInvolvement": [
    1
  ],
  "MaritalStatus": [
    "Married"
  ],
  "Work_accident": [
    1
  ],
  "StandardHours": [
    80
  ],
  "PerformanceRating": [
    3
  ],
  "StockOptionLevel": [
    0
  ],
  "DailyRate": [
    1392
  ],
  "average_montly_hours": [
    11
  ],
  "salary": [
    "high"
  ],
  "promotion_last_5years": [
    0
  ],
  "Gender": [
    "Female"
  ],
  "Age": [
    33
  ],
  "YearsWithCurrManager": [
    2
  ],
  "WorkLifeBalance": [
    3
  ],
  "last_evaluation": [
    0.99
  ],
  "BusinessTravel": [
    "Travel_Rarely"
  ],
  "JobSatisfaction": [
    4
  ],
  "HourlyRate": [
    56
  ],
  "EducationField": [
    "Life Sciences"
  ],
  "JobRole": [
    "Research Scientist"
  ],
  "NumCompaniesWorked": [
    1
  ],
  "time_spend_company": [
    2
  ],
  "YearsInCurrentRole": [
    2
  ],
  "YearsAtCompany": [
    2
  ],
  "TrainingTimesLastYear": [
    3
  ],
  "MonthlyIncome": [
    290977
  ],
  "OverTime": [
    "Yes"
  ],
  "DistanceFromHome": [
    3
  ],
  "EmployeeNumber": [
    5
  ],
  "EmployeeCount": [
    1
  ],
  "Education": [
    4
  ]
}
 </code></pre>

# The API Response will be:
<code>
{
    "prediction": "0"
}
</code>
