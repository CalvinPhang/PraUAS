import pandas as pd
import numpy as np
from sklearn import linear_model
from django.conf import settings

class BaseLinearRegression:
    def __init__(self,training_data):
        self.df = pd.read_csv(settings.ML_ROOT + training_data)
        self.model = linear_model.LinearRegression()
        self.model.fit(self.df.iloc[:, 0:3], self.df.iloc[:,-1:])
        
    def predict(self, value):
        return self.model.predict([value])
    

air_purifier_model = BaseLinearRegression('dairy.csv')
red_meat_model = BaseLinearRegression('redmeat.csv')
white_meat_model = BaseLinearRegression('whitemeat.csv')
grain_model = BaseLinearRegression('grains.csv')
veg_model = BaseLinearRegression('sayuran.csv')
fruit_model = BaseLinearRegression('fruit.csv')
weather_model = BaseLinearRegression('musim.csv')
sales_model = BaseLinearRegression('sales.csv')
customer_model = BaseLinearRegression('customer.csv')

power_model = BaseLinearRegression('power.csv')
harvest_model = BaseLinearRegression('harvest.csv')
stocks_model = BaseLinearRegression('stocks.csv')
performance_model = BaseLinearRegression('performance.csv')
