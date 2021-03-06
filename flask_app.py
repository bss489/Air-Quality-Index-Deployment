# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:16:52 2020

@author: bhave
"""

from flask import Flask,render_template,url_for,request
import pandas as pd 

import pickle

# load the model from disk
loaded_model=pickle.load(open('random_forest_regression_model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv('real_2015.csv')
    my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('results.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)