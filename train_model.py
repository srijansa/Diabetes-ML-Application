import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

df=pd.read_csv(r'C:\Users\srija\Downloads\project_dataset\diabetes_data.csv')
X =df.drop('Diabetes', axis=1)
y =df['Diabetes']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
joblib.dump(model,  'model.pkl' )
