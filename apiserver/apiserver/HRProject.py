# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:03:01 2017

@author: Mohsin Aslam
"""
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.externals import joblib
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
try:
    from sklearn.model_selection import train_test_split
except:
    from sklearn.cross_validation import train_test_split

dir_paths = {
    'mohsin': {
        'df1': 'F:\\HRProject\\HR_IBM.csv',
        'df2': 'F:\\HRProject\\HR_comma_sep.csv'
    },
    'pwd': {
        'df1': os.getcwd() + '/HR_IBM.csv',
        'df2': os.getcwd() + '/organization.csv'
    }
}

fields_to_drop = ['EmployeeCount', 'Over18', 'EmployeeNumber', 'StandardHours','DailyRate','HourlyRate','Education']

cols_to_use = ['Age', 'DistanceFromHome', 'EnvironmentSatisfaction',
       'JobInvolvement', 'JobLevel', 'NumCompaniesWorked',
       'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction',
       'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
       'WorkLifeBalance', 'Work_accident', 'YearsInCurrentRole',
       'YearsWithCurrManager', 'average_montly_hours', 'last_evaluation',
       'number_project', 'satisfaction_level_Combined',
       'YearsAtCompanyCombied', 'salary_combined',
       'BusinessTravel_numerical', 'Gender_numerical',
       'EducationField_numerical', 'MaritalStatus_numerical',
       'OverTime_numerical', 'JobRole_numerical', 'department_combined',
       'promotion_5_year_combined', 'MonthtlyRateNormalized']

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

    fields_to_drop.extend(['satisfaction_level','JobSatisfaction'])


def ConvertCategoricalFeaturesToNumerical(result_Combined):
    result_Combined['BusinessTravel_numerical'] = result_Combined.loc[result_Combined.BusinessTravel == 'Travel_Rarely', 'BusinessTravel'] = 1
    result_Combined['BusinessTravel_numerical'] = result_Combined.loc[result_Combined.BusinessTravel == 'Travel_Frequently', 'BusinessTravel'] = 2
    result_Combined['BusinessTravel_numerical'] = result_Combined.loc[result_Combined.BusinessTravel == 'Non-Travel', 'BusinessTravel'] = 0
    result_Combined['BusinessTravel_numerical'] = result_Combined['BusinessTravel'].convert_objects(convert_numeric=True)
    
    
    result_Combined['Gender_numerical'] = result_Combined.loc[result_Combined.Gender == 'Female', 'Gender'] = 0
    result_Combined['Gender_numerical'] = result_Combined.loc[result_Combined.Gender == 'Male', 'Gender'] = 1
    result_Combined['Gender_numerical'] = result_Combined['Gender'].convert_objects(convert_numeric=True)
    
    
    result_Combined['EducationField_numerical'] = result_Combined.loc[result_Combined.EducationField == 'Life Sciences', 'EducationField'] = 0
    result_Combined['EducationField_numerical'] = result_Combined.loc[result_Combined.EducationField == 'Other', 'EducationField'] = 1
    result_Combined['EducationField_numerical'] = result_Combined.loc[result_Combined.EducationField == 'Medical', 'EducationField'] = 2
    result_Combined['EducationField_numerical'] = result_Combined.loc[result_Combined.EducationField == 'Marketing', 'EducationField'] = 3
    result_Combined['EducationField_numerical'] = result_Combined.loc[result_Combined.EducationField == 'Technical Degree', 'EducationField'] = 4
    result_Combined['EducationField_numerical'] = result_Combined.loc[result_Combined.EducationField == 'Human Resources', 'EducationField'] = 5
    result_Combined['EducationField_numerical'] = result_Combined['EducationField'].convert_objects(convert_numeric=True)
    
    result_Combined['MaritalStatus_numerical'] = result_Combined.loc[result_Combined.MaritalStatus == 'Single', 'MaritalStatus'] = 0
    result_Combined['MaritalStatus_numerical'] = result_Combined.loc[result_Combined.MaritalStatus == 'Married', 'MaritalStatus'] = 1
    result_Combined['MaritalStatus_numerical'] = result_Combined.loc[result_Combined.MaritalStatus == 'Divorced', 'MaritalStatus'] = 2
    result_Combined['MaritalStatus_numerical'] = result_Combined['MaritalStatus'].convert_objects(convert_numeric=True)
    
    
    result_Combined['OverTime_numerical'] = result_Combined.loc[result_Combined.OverTime == 'No', 'OverTime'] = 0
    result_Combined['OverTime_numerical'] = result_Combined.loc[result_Combined.OverTime == 'Yes', 'OverTime'] = 1
    result_Combined['OverTime_numerical'] = result_Combined['OverTime'].convert_objects(convert_numeric=True)
    
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Sales Executive', 'JobRole'] = 0
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Research Scientist', 'JobRole'] = 1
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Laboratory Technician', 'JobRole'] = 2
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Manufacturing Director', 'JobRole'] = 3
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Healthcare Representative', 'JobRole'] = 4
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Manager', 'JobRole'] = 5
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Sales Representative', 'JobRole'] = 6
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Research Director', 'JobRole'] = 7
    result_Combined['JobRole_numerical'] = result_Combined.loc[result_Combined.JobRole == 'Human Resources', 'JobRole'] = 8
    result_Combined['JobRole_numerical'] = result_Combined['JobRole'].convert_objects(convert_numeric=True)
    fields_to_drop.extend(['BusinessTravel','Gender','EducationField','MaritalStatus','OverTime','JobRole'])

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

def BinMonthlyRate(result):
    
    def BinMapper(x):
        if x <= first_range:
            return 0
        elif x >= first_range and x < second_range:
            return 1
        elif x >= second_range and x < third_range:
            return 2
        elif x >= third_range and x < fourth_range:
            return 3
        elif x >= fourth_range:
            return 4
        else:
            return x
    
    a = np.array(result['MonthlyRate'])
    first_range = np.nanpercentile(a, 20)
    second_range = np.nanpercentile(a, 40)
    third_range = np.nanpercentile(a, 60)
    fourth_range = np.nanpercentile(a, 80)
    
    result['MonthtlyRateNormalized'] = [BinMapper(x) for x in result.MonthlyRate]
    fields_to_drop.extend(['MonthlyRate'])
    
    
def combine_departments(result):
    def mapper(val):
        if val == 'Sales':
            return val.lower()
        elif val == 'Research & Development':
            return 'RandD'
        elif val == 'Human Resources':
            return 'hr'
        else:
            return val

    result['department_combined'] = [mapper(x) for x in result['Department'].values]
    result.department_combined.fillna(result.sales, inplace=True)
    dept_map = {'sales':1, 'RandD':2, 'hr':3, 'accounting':4, 'technical':5, 'support':6,
       'management':7, 'IT':8, 'product_mng':9, 'marketing':10}
    result['department_combined'] = [dept_map[x] for x in result['department_combined'].values]
    
    result.department_combined = result.department_combined.astype(int)
    fields_to_drop.extend(['Department', 'sales'])


def combine_promotion_last_5_years(result):
    def mapper(val):
        if val <= 5:
            return 1
        else:
            return 0

    result['promotion_5_year_combined'] = [mapper(x) for x in result['YearsSinceLastPromotion'].values]
    result.promotion_5_year_combined.fillna(result.promotion_last_5years, inplace=True)
    result.promotion_5_year_combined = result.promotion_5_year_combined.astype(int)
    fields_to_drop.extend(['YearsSinceLastPromotion', 'promotion_last_5years'])

def MissingDataTreatment(result):
    for i in result.columns:
        med = np.nanmedian(result[i])
        result[i].fillna(med,inplace=True)
    return result

def splitdata(result_Combined):
    input_x = list(result_Combined.columns)
    input_x.remove('attrition_combined')
    X_train, X_test, y_train, y_test = train_test_split( result_Combined[input_x], result_Combined['attrition_combined'], test_size=0.33, random_state=42)
    return X_train, X_test, y_train, y_test

def TrainLogisticRegression(X_train, y_train):
    logmodel = LogisticRegression()
    logmodel.fit(X_train,y_train)
    return logmodel
    
def ScoreLogisticRegression(X_test, y_test,logmodel):
    predictions = logmodel.predict(X_test)
    report = classification_report(y_test,predictions)
    confuionMatrix = confusion_matrix(y_test,predictions)
    return predictions,report,confuionMatrix

def TrainDecissionTree(X_train, y_train):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    return clf

def ScoreDecissionTree(X_test, y_test,clf):
    predictions = clf.predict(X_test)
    report = classification_report(y_test,predictions)
    confuionMatrix = confusion_matrix(y_test,predictions)
    return predictions,report,confuionMatrix

def TrainRandomForest(X_train, y_train):
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf = clf.fit(X_train, y_train)
    return clf

def ScoreRandomForest(X_test, y_test,clf):
    predictions = clf.predict(X_test)
    report = classification_report(y_test,predictions)
    confuionMatrix = confusion_matrix(y_test,predictions)
    return predictions,report,confuionMatrix


class PersistentModel(object):
    def create_persisted_model(self, clf, filename):
        joblib.dump(clf, filename)

    def load_persisted_model(self, model_name):
        return joblib.load(model_name)

    def map_all(self, result):
        satisfaction_combine(result)
        years_at_company_combine(result)
        combine_attritions(result)
        incomes_combined(result)
        ConvertCategoricalFeaturesToNumerical(result)
        combine_departments(result)
        combine_promotion_last_5_years(result)
        BinMonthlyRate(result)


    def predict_from_persistedmodel(self, val):

        if not isinstance(val, dict):
            return "Invalid data."
        try:
            val = pd.DataFrame([val], columns=val.keys())
            self.map_all(val)
        except:
            print "Failed to parse data."

        clf = self.load_persisted_model('../logistic.pkl')
        churn = clf.predict(val)
        return churn


# Person using this file goes here for path, replace name with yours
user = dir_paths['pwd']

df1 = LoadData(user['df1'])
df2 = LoadData(user['df2'])

result = combined_dfs(df1, df2)


satisfaction_combine(result)
years_at_company_combine(result)
combine_attritions(result)
incomes_combined(result)
ConvertCategoricalFeaturesToNumerical(result)
combine_departments(result)
combine_promotion_last_5_years(result)
BinMonthlyRate(result)

result_Combined = result.drop(fields_to_drop,axis=1)
result_Combined = MissingDataTreatment(result_Combined)
X_train, X_test, y_train, y_test = splitdata(result_Combined)
logmodel = TrainLogisticRegression(X_train, y_train)
predictions,report,confuionMatrix = ScoreLogisticRegression(X_test, y_test,logmodel)
decission_tree_model = TrainDecissionTree(X_train, y_train)
predictions_dt,report_dt,confuionMatrix_dt = ScoreDecissionTree(X_test, y_test, decission_tree_model)
random_forest_model = TrainRandomForest(X_train, y_train)
predictions_rf,report_rf,confuionMatrix_rf = ScoreRandomForest(X_test, y_test, random_forest_model)

    


# Persist model in file
pers_model = PersistentModel()

pers_model.create_persisted_model(logmodel, 'logistic.pkl')

# Predict churn of employees of age > 40 from persisted model
# predict_from_persistedmodel(result_Combined[result_Combined.Age > 40.0][cols_to_use])

y_complete = X_test
y_complete['actual'] = y_test
y_complete['predicted'] = predictions

MergeDataSetToCsv(os.getcwd() + '/PredictedDF.csv',y_complete)

MergeDataSetToCsv(os.getcwd() + '/MergedDF.csv', result_Combined)