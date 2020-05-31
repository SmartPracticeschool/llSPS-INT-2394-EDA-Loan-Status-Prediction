# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:51:10 2020

@author: Sujay
"""


from flask import Flask, render_template, redirect, url_for, request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',data="null")

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
      gender = request.form['gender']
      married= request.form['married']
      dependents= request.form['dependents']
      education= request.form['education']
      employed= request.form['employed']
      income1= request.form['income1']
      income2= request.form['income2']
      crhist= request.form['crhist']
      area= request.form['area']
      loan= request.form['amount']
      term= request.form['term']
      
      data=[gender,married,dependents,education,employed,income1,income2,crhist,area,loan,term]
      status="NULL"
      prediction='Predicted Loan Status: ' + status
      return render_template('index.html',prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)