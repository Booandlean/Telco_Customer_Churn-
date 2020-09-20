import pandas as pd
import numpy as np
from scipy import stats

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler



def prep_df():
    data_path = 'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'
    df = pd.read_csv(data_path)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
    #This is a string for some ungodly reason
    encode_df = df.drop(['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges'],  axis = 1)
    le = LabelEncoder()
    encoded_df = encode_df.apply(le.fit_transform)
    encoded_df[['tenure', 'MonthlyCharges', 'TotalCharges']] = df[['tenure', 'MonthlyCharges', 'TotalCharges']]
    
    return encoded_df