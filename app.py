from flask import Flask,render_template,request
import joblib
import numpy as np
from joblib import load
import pandas as pd

app = Flask(__name__)
model=joblib.load('test ridge model.joblib')

@app.route("/",methods=['Get','POST'])
def predict():
    if request.method=='POST':
        income=float(request.form['average income are']) 
        avg_age=float(request.form['average area house age'])
        room=float(request.form['average area number of rooms'])
        bedroom=float(request.form['average area of bedrooms'])
        population=float(request.form['area population'])
        prediction=model.predict([[income,avg_age,room,bedroom,population]])
        output=round(prediction[0],2)
        if output>0:
                return render_template('index.html',prediction_text='The price is ${}'.format(output))
        elif output<0:
            return render_template('index.html',prediction_text='Average income/population too small')
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)


