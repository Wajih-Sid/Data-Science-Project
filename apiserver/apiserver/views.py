from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import numpy as np

from HRProject import PersistentModel


def parse_data(result):
    satisfaction = result['satisfaction_level_Combined']

    if satisfaction > 0.0 and satisfaction <= 0.25:
        result['satisfaction_level_Combined'] = 1
    elif satisfaction >= 0.26 and satisfaction <= 0.50:
        result['satisfaction_level_Combined'] = 2
    elif satisfaction >= 0.51 and satisfaction <= 0.75:
        result['satisfaction_level_Combined'] = 3
    elif satisfaction >= 0.76 and satisfaction <= 1:
        result['satisfaction_level_Combined'] = 4


    low_salary = 2618.97
    medium_salary = 5119.7

    salary = result['salary_combined']

    if salary <= low_salary:
        result['salary_combined'] = 0
    elif salary >= low_salary and salary < medium_salary:
        result['salary_combined'] = 1
    elif salary >= medium_salary:
        result['salary_combined'] = 2


    travel = result['BusinessTravel_numerical']
    travel_map = {'Travel_Rarely': 1, 'Travel_Frequently': 2, 'Non-Travel': 0}
    result['BusinessTravel_numerical'] = travel_map[travel]


    gender = result['Gender_numerical']
    gen_map = {'Female': 0, 'Male': 1}
    result['Gender_numerical'] = gen_map[gender]


    marital_status = result['MaritalStatus_numerical']
    marital_map = {'Single': 0, 'Married': 1, 'Divorced': 2}
    result['MaritalStatus_numerical'] = marital_map[marital_status]

    overtime = result['OverTime']
    overtime_map = {'No': 0, 'Yes': 1}
    result['OverTime'] = overtime_map[overtime]


    jobrole = result['JobRole_numerical']
    role_map = {
        'Sales Executive': 0,
        'Research Scientist': 1,
        'Laboratory Technician': 2,
        'Manufacturing Director': 3,
        'Healthcare Representative': 4,
        'Manager': 5,
        'Sales Representative': 6,
        'Research Director': 7,
        'Human Resources': 8
    }
    result['JobRole_numerical'] = role_map[jobrole]


    dept = result['department_combined']
    dept_map = dept_map = {'sales':1, 'RandD':2, 'hr':3, 'accounting':4, 'technical':5, 'support':6,
       'management':7, 'IT':8, 'product_mng':9, 'marketing':10}

    result['department_combined'] = dept_map[dept]

    promition_in_five_years = result['promotion_5_year_combined']
    prom_map = {'Yes': 1, 'No': 0}
    result['promotion_5_year_combined'] = prom_map[promition_in_five_years]



    monthly_rate = result['MonthtlyRateNormalized']
    first_range = 7128.6
    second_range = 11587.4
    third_range = 16888.2
    fourth_range = 22061.0

    if monthly_rate <= first_range:
        result['MonthlyRateNormalized'] = 0
    elif monthly_rate >= first_range and monthly_rate < second_range:
        result['MonthlyRateNormalized'] = 1
    elif monthly_rate >= second_range and monthly_rate < third_range:
        result['MonthlyRateNormalized'] = 2
    elif monthly_rate >= third_range and monthly_rate < fourth_range:
        result['MonthlyRateNormalized'] = 3
    elif monthly_rate >= fourth_range:
        result['MonthlyRateNormalized'] = 4


    #############Done################
    return result



@csrf_exempt
def get_churn(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        persistent_model = PersistentModel()

        try:
            predictions = persistent_model.predict_from_persistedmodel(data)
            return JsonResponse({'status': 'OK', 'predictions': list(predictions), 'data': data})

        except Exception:
            print "Failed!"

    else:
        return JsonResponse({'status': 'OK'})