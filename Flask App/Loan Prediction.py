# -*- coding: utf-8 -*-
"""
Created on Mon Jun 1 21:51:10 2020

@author: Sujay
"""


from flask import Flask , render_template ,request
import pickle
app  = Flask(__name__)
model = pickle.load(open('Logistic_Model.pkl','rb'))

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
      
      data=[[int(gender),int(married),int(dependents),int(education),int(employed),int(income1),int(income2),int(crhist),int(area),int(loan),int(term)]]
      p=model.predict(data)  
      if p[0]==1:
          prediction="Loan To Be Granted"
      else:
          prediction="Loan Not To Be Granted"

      return render_template('index.html',prediction="Prediction: "+prediction)

if __name__=='__main__':
    app.run(debug=True)
