# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:03:01 2017

@author: Mohsin Aslam
"""
import os
import numpy as np
import pandas as pd

dir_paths = {
    'mohsin': {
        'df1': 'F:\\HRProject\\HR_IBM.csv',
        'df2': 'F:\\HRProject\\HR_comma_sep.csv'
    },
    'wajih': {
        'df1': os.getcwd() + '/HR_IBM.csv',
        'df2': os.getcwd() + '/organization.csv'
    }
}

fields_to_drop = ['EmployeeCount', 'Over18', 'EmployeeNumber', 'StandardHours']


def LoadData(path):
    return pd.read_csv(path)
    
def MergeDataSets(df1,df2):
    result = df1.append(df2, ignore_index=True)
    return result

def combined_dfs(df1, df2):
    return df1.append(df2, ignore_index=True)
    
def MergeDataSetToCsv(path,df):
    df.to_csv(path,sep = ',',encoding='utf-8')
    return


def satisfaction_combine(result):
    result['satisfaction_level_Combined'] = np.where(result['satisfaction_level'].between(0.76, 1), 4,
                                                     result['satisfaction_level'])
    result['satisfaction_level_Combined'] = np.where(result['satisfaction_level_Combined'].between(0.51, 0.75), 3,
                                                     result['satisfaction_level_Combined'])
    result['satisfaction_level_Combined'] = np.where(result['satisfaction_level_Combined'].between(0.26, 0.50), 2,
                                                     result['satisfaction_level_Combined'])
    result['satisfaction_level_Combined'] = np.where(result['satisfaction_level_Combined'].between(0.0, 0.25), 1,
                                                     result['satisfaction_level_Combined'])
    result.satisfaction_level_Combined.fillna(result.JobSatisfaction, inplace=True)

    fields_to_drop.extend(['satisfaction_level', 'JobSatisfaction'])



def years_at_company_combine(result):
    result['YearsAtCompanyCombied'] = result.time_spend_company.fillna(result.YearsAtCompany)
    fields_to_drop.extend(['time_spend_company', 'YearsAtCompany'])

def combine_attritions(result):
    def mapper(val):
        if val == 'Yes':
            return 1
        elif val == 'No':
            return 0
        else:
            return val

    result['attrition_combined'] = [mapper(x) for x in result['Attrition'].values]
    result.attrition_combined.fillna(result.left, inplace=True)
    result.attrition_combined = result.attrition_combined.astype(int)
    fields_to_drop.extend(['Attrition', 'left'])

def incomes_combined(result):
    def sal_mapper(val):
        if val == 'low':
            return 0
        elif val == 'medium':
            return 1
        elif val == 'high':
            return 2
        else:
            return val

    def cat_to_sal(sal):
        if sal <= low_range:
            return 0
        elif sal >= low_range and sal < medium_range:
            return 1
        elif sal >= medium_range:
            return 2
        else:
            return sal

    # Convery salary from low,med,high to 0,1,2
    result['salary'] = [sal_mapper(x) for x in result.salary]

    a = np.array(result['MonthlyIncome'])
    low_range = np.nanpercentile(a, 33)
    medium_range = np.nanpercentile(a, 66)

    # Create new column from monthlyincome based on percentiles and categorize
    result['salary_combined'] = [cat_to_sal(x) for x in result.MonthlyIncome]

    result.salary_combined.fillna(result.salary, inplace=True)
    result.salary_combined = result.salary_combined.astype(int)

    fields_to_drop.extend(['salary', 'MonthlyIncome'])

# Person using this file goes here for path, replace name with yours
user = dir_paths['wajih']

df1 = LoadData(user['df1'])
df2 = LoadData(user['df2'])

result = combined_dfs(df1, df2)


satisfaction_combine(result)
years_at_company_combine(result)
combine_attritions(result)
incomes_combined(result)



result_Combined = result.drop(fields_to_drop,axis=1)
