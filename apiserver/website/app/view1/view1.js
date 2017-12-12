'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/employee_churn', {
    templateUrl: 'view1/employee_churn.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ['$scope', '$http', function($scope, $http) {

	$scope.formFields = [
      {
        'type': 'dropdown',
        'options': [10.0, 25.0, 50.0, 75.0, 100.0],
        'placeholder': 'Percentage Hike in Salary',
        'name': 'PercentSalaryHike'
      },
      {
        'type': 'number',
        'placeholder': 'Relationship Satisfaction',
        'name': 'RelationshipSatisfaction'
      },
      {
        'type': 'number',
        'placeholder': 'Years Since Last Promotion',
        'name': 'YearsSinceLastPromotion'
      },
      {
        'type': 'number',
        'placeholder': 'Number of Projects',
        'name': 'number_project'
      },
      {
        'type': 'number',
        'placeholder': 'Environment Satisfaction',
        'name': 'EnvironmentSatisfaction'
      },
      {
        'type': 'dropdown',
        'options': ['Research & Development'],
        'placeholder': 'Sales',
        'name': 'sales'
      },
      {
        'type': 'number',
        'placeholder': 'Monthly Rate',
        'name': 'MonthlyRate'
      },
      {
        'type': 'dropdown',
        'options': ['Y', 'N'],
        'placeholder': 'Over18',
        'name': 'Over18'
      },
      {
        'type': 'dropdown',
        'options': ['technical', 'management', 'product_mng', 'hr', 'accounting', 'support', 'marketing', 'sales', 'RandD', 'IT', 'Research & Development'],
        'placeholder': 'Department',
        'name': 'Department'
      },
      {
        'type': 'number',
        'placeholder': 'Job Level',
        'name': 'JobLevel'
      },
      {
        'type': 'number',
        'placeholder': 'Total Working Years',
        'name': 'TotalWorkingYears'
      },
      {
        'type': 'number',
        'placeholder': 'Satisfaction Level',
        'name': 'satisfaction_level'
      },
      {
        'type': 'number',
        'placeholder': 'Job Involvement',
        'name': 'JobInvolvement'
      },
      {
        'type': 'options',
        'options': ['Single', 'Married', 'Divorced'],
        'placeholder': 'Marital Status',
        'name': 'MaritalStatus'
      },
      {
        'type': 'number',
        'placeholder': 'Work Accident',
        'name': 'Work_accident'
      },
      {
        'type': 'number',
        'placeholder': 'Standard Hours',
        'name': 'StandardHours'
      },
      {
        'type': 'number',
        'placeholder': 'Performance Rating',
        'name': 'PerformanceRating'
      },
      {
        'type': 'number',
        'placeholder': 'Stock Option Level',
        'name': 'StockOptionLevel'
      },
      {
        'type': 'number',
        'placeholder': 'Daily Rate',
        'name': 'DailyRate'
      },
      {
        'type': 'number',
        'placeholder': 'Average Monthly Hours',
        'name': 'average_montly_hours'
      },
      {
        'type': 'dropdown',
        'options': ["low", "medium", "high"],
        'placeholder': 'Salary',
        'name': 'salary'
      },
      {
        'type': 'number',
        'placeholder': 'Promoted in last 5 Years',
        'name': 'promotion_last_5years'
      },
      {
        'type': 'dropdown',
        'options': ['Male', 'Female'],
        'placeholder': 'Gender',
        'name': 'Gender'
      },
      {
        'type': 'dropdown',
        'options': [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
        'placeholder': 'Age',
        'name': 'Age'
      },
      {
        'type': 'number',
        'placeholder': 'Years With Current Manager',
        'name': 'YearsWithCurrManager'
      },
      {
        'type': 'number',
        'placeholder': 'Work Life Balance',
        'name': 'WorkLifeBalance'
      },
      {
        'type': 'number',
        'placeholder': 'Last Evaluation',
        'name': 'last_evaluation'
      },
      {
        'type': 'dropdown',
        'options': ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'],
        'placeholder': 'Business Travel',
        'name': 'BusinessTravel'
      },
      {
        'type': 'number',
        'placeholder': 'Job Satisfaction',
        'name': 'JobSatisfaction'
      },
      {
        'type': 'number',
        'placeholder': 'Hourly Rate',
        'name': 'HourlyRate'
      },
      {
        'type': 'dropdown',
        'options': ['Life Sciences','Other','Medical','Marketing','Technical Degree','Human Resources'],
        'placeholder': 'Education Field',
        'name': 'EducationField'
      },
      {
        'type': 'dropdown',
        'options': ['Research Scientist'],
        'placeholder': 'Job Role',
        'name': 'JobRole'
      },
      {
        'type': 'number',
        'placeholder': 'Number of Companies Worked',
        'name': 'NumCompaniesWorked'
      },
      {
        'type': 'number',
        'placeholder': 'Time Spend in Company',
        'name': 'time_spend_company'
      },
      {
        'type': 'number',
        'placeholder': 'Years In Current Role',
        'name': 'YearsInCurrentRole'
      },
      {
        'type': 'number',
        'placeholder': 'Years At Company',
        'name': 'YearsAtCompany'
      },
      {
        'type': 'number',
        'placeholder': 'Training Times Last Year',
        'name': 'TrainingTimesLastYear'
      },
      {
        'type': 'number',
        'placeholder': 'Monthly Income',
        'name': 'MonthlyIncome'
      },
      {
        'type': 'dropdown',
        'options': ["No", "Yes"],
        'placeholder': 'Over Time',
        'name': 'OverTime'
      },
      {
        'type': 'number',
        'placeholder': 'Distance From Home',
        'name': 'DistanceFromHome'
      },
      {
        'type': 'number',
        'placeholder': 'Employee Number',
        'name': 'EmployeeNumber'
      },
      {
        'type': 'number',
        'placeholder': 'Employee Count',
        'name': 'EmployeeCount'
      },
      {
        'type': 'number',
        'placeholder': 'Education',
        'name': 'Education'
      }
    ];

    $scope.model = {};



	function parseData(data) {
        angular.forEach(data, function (val, key) {
            data[key] = [val];
        });
		return data;
	}

	var API_URL = 'http://localhost:8000/get_churn/';
	API_URL = 'http://mohsinaslam.pythonanywhere.com/predict';



	$scope.formSubmit = function () {
		var data = parseData($scope.model);

		if (Object.keys(data).length !== $scope.formFields.length) {
		    alert('Please specify all fields.');
		    return
		}

		$http.post(API_URL, data).then(function (response) {
			if (!!response) {
				alert(response);
			}
		}, function (error) {
			console.log(error);
		});
	};

}]);