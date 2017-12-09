# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:03:01 2017

@author: Mohsin Aslam
"""

def LoadData(abc):
    import pandas as pd
    path = abc
    df = pd.read_csv(path)
    return df
    
    
def MergeDataSets(df1,df2):
    import pandas as pd
    result = df1.append(df2, ignore_index=True)
    return result
    
def MergeDataSetToCsv(path,df):
    import pandas as pd
    df.to_csv(path,sep = ',',encoding='utf-8')
    return 
df1 = LoadData('F:\\HRProject\\HR_IBM.csv')
df2 = LoadData('F:\\HRProject\\HR_comma_sep.csv')
result = df1.append(df2, ignore_index=True)

import numpy as np
result['satisfaction_level_Combined'] = np.where(result['satisfaction_level'].between(0.76,1), 4, result['satisfaction_level'])
result['satisfaction_level_Combined'] = np.where(result['satisfaction_level_Combined'].between(0.51,0.75), 3, result['satisfaction_level_Combined'])
result['satisfaction_level_Combined'] = np.where(result['satisfaction_level_Combined'].between(0.26,0.50), 2, result['satisfaction_level_Combined'])
result['satisfaction_level_Combined'] = np.where(result['satisfaction_level_Combined'].between(0.0,0.25), 1, result['satisfaction_level_Combined'])   

result.satisfaction_level_Combined.fillna(result.JobSatisfaction, inplace=True)

result['YearsAtCompanyCombied'] = result.time_spend_company.fillna(result.YearsAtCompany)
result_Combined = result.drop(['Over18','EmployeeCount','satisfaction_level','JobSatisfaction','time_spend_company','YearsAtCompany'],axis=1)
    
#result = result.drop('satisfaction_level_Combined',axis=1)
