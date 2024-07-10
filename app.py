from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)
model=joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/single_prediction', methods=['GET', 'POST'])
def single_prediction():
    if request.method=='POST':
        data=request.form.to_dict()
        df=pd.DataFrame([data])
        df=df.apply(pd.to_numeric)
        prediction=model.predict(df)
        return render_template('single_prediction.html', prediction=int(prediction[0]), data=data)
    return render_template('single_prediction.html', data={})

@app.route('/batch_prediction', methods=['GET', 'POST'])
def batch_prediction():
    if request.method=='POST':
        file=request.files['file']
        df=pd.read_csv(file)
        predictions=model.predict(df)
        df['Prediction'] = predictions
        generate_charts(df)
        return render_template('batch_prediction.html', tables=[df.to_html(classes='data')], titles=df.columns.values, charts=True)
    return render_template('batch_prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    data=request.json
    df=pd.DataFrame([data])
    df=df.apply(pd.to_numeric)
    prediction=model.predict(df)
    return jsonify({'prediction': int(prediction[0])})

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    data=request.json
    df=pd.DataFrame(data)
    df=df.apply(pd.to_numeric)
    predictions=model.predict(df)
    return jsonify({'predictions': predictions.tolist()})

def generate_charts(df):
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Prediction',data=df )
    plt.title('Prediction Distribution') 
    plt.savefig('static/images/prediction_distribution.png' )
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.histplot(df['BMI'],kde=True)
    plt.title('BMI Distribution')
    plt.savefig('static/images/bmi_distribution.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Prediction',y='Age', data=df)
    plt.title('Age vs Prediction')
    plt.savefig('static/images/age_vs_prediction.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='BMI', y='PhysHlth', hue='Prediction', data=df)
    plt.title('BMI vs Physical Health colored by Prediction')
    plt.savefig('static/images/bmi_vs_physical_health.png')
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)
