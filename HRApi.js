var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://mohsinaslam.pythonanywhere.com/predict",
  "method": "POST",
  "headers": {
    "content-type": "application/json",
    "cache-control": "no-cache",
    "postman-token": "e8e02598-3c68-425d-2059-e1b87e203456"
  },
  "processData": false,
  "data": "{ \"Age\" : [33]  , \"BusinessTravel\" : [\"Travel_Frequently\"] , \"DailyRate\" : [1392], \"Department\" : [\"Research & Development\"] , \"DistanceFromHome\": [3], \"Education\": [4], \"EducationField\" : [\"Life Sciences\"] , \"EmployeeCount\" : [1] , \"EmployeeNumber\" : [5], \"EnvironmentSatisfaction\" : [4] , \"Gender\": [\"Female\"], \"HourlyRate\": [56] , \"JobInvolvement\" : [3] , \"JobLevel\" : [1] , \"JobRole\" : [\"Research Scientist\"], \"JobSatisfaction\" : [4] , \"MaritalStatus\": [\"Married\"], \"MonthlyIncome\": [290977], \"MonthlyRate\" : [23159] , \"NumCompaniesWorked\" : [1] , \"Over18\" : [\"Y\"], \"OverTime\" : [\"Yes\"] , \"PercentSalaryHike\": [28], \"PerformanceRating\": [3], \"RelationshipSatisfaction\" : [3] , \"StandardHours\" : [80] , \"StockOptionLevel\" : [0], \"TotalWorkingYears\" : [8] , \"TrainingTimesLastYear\": [3], \"WorkLifeBalance\": [3], \"YearsAtCompany\" : [2] , \"YearsInCurrentRole\" : [2] , \"YearsSinceLastPromotion\" : [2], \"YearsWithCurrManager\" : [2] , \"satisfaction_level\": [0.99], \"last_evaluation\": [0.99], \"number_project\" : [2] , \"average_montly_hours\" : [11], \"time_spend_company\" : [2] , \"Work_accident\": [1\n], \"promotion_last_5years\" : [0] , \"sales\" : [\"Research & Development\"], \"salary\" : [\"high\"]}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});