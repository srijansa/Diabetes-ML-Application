# Diabetes-ML-Application

## Overview

This project is a machine learning application built using Flask for the backend API and Streamlit for the frontend. The model predicts whether a person has diabetes based on various health metrics. It supports single and batch predictions, and provides interactive data visualizations.

## Features

- **Single Prediction**: Input individual health parameters to predict diabetes.
- **Batch Prediction**: Upload a CSV file with multiple data points for batch processing and predictions.
- **Data Visualizations**: Generate insightful graphs like histograms, scatter plots, and correlation matrices based on the input data.
- **Downloadable Graphs**: Users can download generated graphs for further analysis.

## Project Structure
DiabetesMLApplication/
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   └── js/
│       └── scripts.js
├── templates/
│   ├── batch_prediction.html
│   ├── index.html
│   └── single_prediction.html
├── app.py              
├── diabetes_data.csv    
├── model.pkl          
├── streamlit_app.py      
├── train_model.py       
├── README.md          
├── LICENSE               
└── requirements.txt      

## Screenshots
### Home

![Home](https://github.com/srijansa/Diabetes-ML-Application/blob/main/static/images/home.png)

### 1. Single Prediction

![Single Prediction]((https://github.com/srijansa/Diabetes-ML-Application/blob/main/static/images/SinglePredictionOne.png)
![Single Prediction]((https://github.com/srijansa/Diabetes-ML-Application/blob/main/static/images/SinglePredictionTwo.png)

### 2. Batch Prediction

![Batch Prediction One](https://github.com/srijansa/Diabetes-ML-Application/blob/main/static/images/BatchPredictionOne.png)
![Batch Prediction Two](https://github.com/srijansa/Diabetes-ML-Application/blob/main/static/images/BatchPredictionTwo.png)
![Batch Prediction Three](https://github.com/srijansa/Diabetes-ML-Application/blob/main/static/images/BatchPredictionThree.png)

### 3. Data Visualizations

- **BMI Distribution**  
  ![BMI Distribution](images/bmi_distribution.png)

- **Age vs Prediction**  
  ![Age vs Prediction](images/age_vs_prediction.png)

- **BMI vs Physical Health**  
  ![BMI vs Physical Health](images/bmi_vs_physical_health.png)

- **Prediction Distribution**  
  ![Prediction Distribution](images/prediction_distribution.png)

  
## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make the necessary changes and commit (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request.

## Contact
If you have any questions or feedback, feel free to contact:

Author: Srijan Sareen
Email: srijansa@buffalo.edu
