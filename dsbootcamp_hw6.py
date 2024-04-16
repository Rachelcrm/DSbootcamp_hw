import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", 101)

data = pd.read_csv("employee.csv")

data_train = data.copy()
data_train.head()
cat_cols = [c for c in data_train.columns if data_train[c].dtype == 'object'
            and c not in ['is_manager', 'certifications']]
final_data = pd.get_dummies(data_train, columns=cat_cols, drop_first= True,dtype=int)
y = final_data['salary']
X = final_data.drop(columns=['salary'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
num_cols = ['job_years','hours_per_week','telecommute_days_per_week']
scaler.fit(X_train[num_cols])
X_train[num_cols] = scaler.transform(X_train[num_cols])
reg=LinearRegression()
reg.fit(X_train, y_train)
print(mean_squared_error(y_train,reg.predict(X_train))/np.mean(y_train))
print(mean_absolute_error(y_train,reg.predict(X_train))/np.mean(y_train))