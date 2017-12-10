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
	    'placeholder': 'Age',
	    'type': '',
	    'name': 'Age'
	  },
	  {
	    'placeholder': 'DistanceFromHome',
	    'type': '',
	    'name': 'DistanceFromHome'
	  },
	  {
	    'placeholder': 'EnvironmentSatisfaction',
	    'type': '',
	    'name': 'EnvironmentSatisfaction'
	  },
	  {
	    'placeholder': 'JobInvolvement',
	    'type': '',
	    'name': 'JobInvolvement'
	  },
	  {
	    'placeholder': 'JobLevel',
	    'type': '',
	    'name': 'JobLevel'
	  },
	  {
	    'placeholder': 'NumCompaniesWorked',
	    'type': '',
	    'name': 'NumCompaniesWorked'
	  },
	  {
	    'placeholder': 'PercentSalaryHike',
	    'type': '',
	    'name': 'PercentSalaryHike'
	  },
	  {
	    'placeholder': 'PerformanceRating',
	    'type': '',
	    'name': 'PerformanceRating'
	  },
	  {
	    'placeholder': 'RelationshipSatisfaction',
	    'type': '',
	    'name': 'RelationshipSatisfaction'
	  },
	  {
	    'placeholder': 'StockOptionLevel',
	    'type': '',
	    'name': 'StockOptionLevel'
	  },
	  {
	    'placeholder': 'TotalWorkingYears',
	    'type': '',
	    'name': 'TotalWorkingYears'
	  },
	  {
	    'placeholder': 'TrainingTimesLastYear',
	    'type': '',
	    'name': 'TrainingTimesLastYear'
	  },
	  {
	    'placeholder': 'WorkLifeBalance',
	    'type': '',
	    'name': 'WorkLifeBalance'
	  },
	  {
	    'placeholder': 'Work_accident',
	    'type': '',
	    'name': 'Work_accident'
	  },
	  {
	    'placeholder': 'YearsInCurrentRole',
	    'type': '',
	    'name': 'YearsInCurrentRole'
	  },
	  {
	    'placeholder': 'YearsWithCurrManager',
	    'type': '',
	    'name': 'YearsWithCurrManager'
	  },
	  {
	    'placeholder': 'average_montly_hours',
	    'type': '',
	    'name': 'average_montly_hours'
	  },
	  {
	    'placeholder': 'last_evaluation',
	    'type': '',
	    'name': 'last_evaluation'
	  },
	  {
	    'placeholder': 'number_project',
	    'type': '',
	    'name': 'number_project'
	  },
	  {
	    'placeholder': 'satisfaction_level_Combined',
	    'type': '',
	    'name': 'satisfaction_level_Combined'
	  },
	  {
	    'placeholder': 'YearsAtCompanyCombied',
	    'type': '',
	    'name': 'YearsAtCompanyCombied'
	  },
	  {
	    'placeholder': 'salary_combined',
	    'type': '',
	    'name': 'salary_combined'
	  },
	  {
	    'placeholder': 'BusinessTravel_numerical',
	    'type': '',
	    'name': 'BusinessTravel_numerical'
	  },
	  {
	    'placeholder': 'Gender_numerical',
	    'type': '',
	    'name': 'Gender_numerical'
	  },
	  {
	    'placeholder': 'EducationField_numerical',
	    'type': '',
	    'name': 'EducationField_numerical'
	  },
	  {
	    'placeholder': 'MaritalStatus_numerical',
	    'type': '',
	    'name': 'MaritalStatus_numerical'
	  },
	  {
	    'placeholder': 'OverTime_numerical',
	    'type': '',
	    'name': 'OverTime_numerical'
	  },
	  {
	    'placeholder': 'JobRole_numerical',
	    'type': '',
	    'name': 'JobRole_numerical'
	  },
	  {
	    'placeholder': 'department_combined',
	    'type': '',
	    'name': 'department_combined'
	  },
	  {
	    'placeholder': 'promotion_5_year_combined',
	    'type': '',
	    'name': 'promotion_5_year_combined'
	  },
	  {
	    'placeholder': 'MonthtlyRateNormalized',
	    'type': '',
	    'name': 'MonthtlyRateNormalized'
	  }
	];

    $scope.model = {};

	function parseData(data) {

		return data;
	}

	var API_URL = 'http://localhost:8000/get_churn/';


	$scope.formSubmit = function () {
		var data = parseData($scope.model);

		$http.post(API_URL, data).then(function (response) {
			if (!!response) {
				alert(response);
			}
		}, function (error) {
			console.log(error);
		});
	};

}]);