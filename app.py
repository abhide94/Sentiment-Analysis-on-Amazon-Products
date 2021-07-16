import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import CountVectorizer
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
count_vector = pickle.load(open('count_vector.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['text']
    review = str(review)
    text = count_vector.transform([review])
    
    output = model.predict(text)
    
    if output == 1:
        res_val = "Positive"
    else:
        res_val = "Negative"
        

    return render_template('index.html', prediction_text='Customer has given a {} review'.format(res_val))

if __name__ == "__main__":
    app.run()