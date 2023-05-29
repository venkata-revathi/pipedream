# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 07:40:08 2021

@author: shiri
"""
from flask import Flask, render_template, request
from flask import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__,template_folder='templates')
model = pickle.load(open('DiabetesPrediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index2.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        age = int(request.form['Age'])
        gender=request.form['Gender']
        if(gender=='Male'):
            gender=1
        else:
            gender=0
        polyuria=request.form['Polyuria']
        if(polyuria=='Yes'):
            polyuria=1
        else:
            polyuria=0
        polydipsia=request.form['Polydipsia']
        if(polydipsia=='Yes'):
            polydipsia=1
        else:
            polydipsia=0
        sudden_weight_loss=request.form['Sudden weight loss']
        if(sudden_weight_loss=='Yes'):
            sudden_weight_loss=1
        else:
            sudden_weight_loss=0
        weakness=request.form['Weakness']
        if(weakness=='Yes'):
            weakness=1
        else:
            weakness=0
        polyphagia=request.form['Polyphagia']
        if(polyphagia=='Yes'):
            polyphagia=1
        else:
            polyphagia=0
        genital_thrush=request.form['Genital thrush']
        if(genital_thrush=='Yes'):
            genital_thrush=1
        else:
            genital_thrush=0
        visual_blurring=request.form['Visual blurring']
        if(visual_blurring=='Yes'):
            visual_blurring=1
        else:
            visual_blurring=0
        itching=request.form['Itching']
        if(itching=='Yes'):
            itching=1
        else:
            itching=0
        irritability=request.form['Irritability']
        if(irritability=='Yes'):
            irritability=1
        else:
            irritability=0
        delayed_healing=request.form['Delayed healing']
        if(delayed_healing=='Yes'):
            delayed_healing=1
        else:
            delayed_healing=0
        partial_paresis=request.form['Partial paresis']
        if(partial_paresis=='Yes'):
            partial_paresis=1
        else:
            partial_paresis=0
        muscle_stiffness=request.form['Muscle stiffness']
        if(muscle_stiffness=='Yes'):
            muscle_stiffness=1
        else:
            muscle_stiffness=0
        alopecia=request.form['Alopecia']
        if(alopecia=='Yes'):
            alopecia=1
        else:
            alopecia=0
        obesity=request.form['Obesity']
        if(obesity=='Yes'):
            obesity=1
        else:
            obesity=0
        
       
        prediction=model.predict([[gender,polyuria,polydipsia,sudden_weight_loss,weakness,visual_blurring,itching,polyphagia,genital_thrush,irritability,delayed_healing,partial_paresis,muscle_stiffness,alopecia,obesity,age]])
        output=round(prediction[0],3)
        if output==0:
            print(output)
            return render_template('diabetes.html',prediction_text="You do not have diabetes")
        else:
            print(output)
            return render_template('diabetes.html',prediction_text="Ooops!! You might have diabetes")
    else:
        return render_template('index2.html')

if __name__=="__main__":
    app.run(debug=True)

