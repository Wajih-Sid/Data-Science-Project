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