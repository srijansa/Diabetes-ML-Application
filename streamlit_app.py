import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import io

st.title('Diabetes Prediction')

def add_border_to_plot(fig):
    fig.patch.set_linewidth(1.5)
    fig.patch.set_edgecolor('black')

def download_fig(fig, filename):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)
    return buf

uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

    if st.button('Generate Graphs'):
        st.write("Graphs for Batch Processing")

        if 'Diabetes' in data.columns:
            fig, ax = plt.subplots()
            sns.countplot(x='Diabetes', data=data, ax=ax, palette="coolwarm")
            ax.set_title('Outcome Distribution')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download Outcome Distribution', data=download_fig(fig, 'outcome_distribution.png'), file_name='outcome_distribution.png')

            fig, ax = plt.subplots()
            sns.histplot(data, x='BMI', hue='Diabetes', multiple='stack', palette="coolwarm", kde=True, ax=ax)
            ax.set_title('BMI Distribution by Outcome')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download BMI Distribution by Outcome', data=download_fig(fig, 'bmi_distribution_by_outcome.png'), file_name='bmi_distribution_by_outcome.png')

            fig, ax = plt.subplots()
            sns.boxplot(x='Diabetes', y='Age',data=data,ax=ax, palette="coolwarm")
            ax.set_title('Age vs Outcome')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download Age vs Outcome',data=download_fig(fig, 'age_vs_outcome.png'), file_name='age_vs_outcome.png')

            fig, ax = plt.subplots()
            sns.scatterplot(x='BMI', y='PhysHlth', hue='Diabetes',  data=data, ax=ax,palette="coolwarm")
            ax.set_title('BMI vs Physical Health by Outcome')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download BMI vs Physical Health by Outcome',data=download_fig(fig, 'bmi_vs_physical_health_by_outcome.png'),file_name='bmi_vs_physical_health_by_outcome.png')

            pairplot_fig = sns.pairplot(data, hue='Diabetes',  palette="coolwarm")
            st.pyplot(pairplot_fig)
            st.download_button('Download Pairplot', data=download_fig(pairplot_fig.fig,'pairplot.png'), file_name='pairplot.png')

            fig, ax = plt.subplots()
            sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
            ax.set_title('Correlation Matrix')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download Correlation Matrix', data=download_fig(fig, 'correlation_matrix.png'), file_name='correlation_matrix.png')

            fig, ax = plt.subplots()
            sns.violinplot(x='Diabetes', y='BMI', data=data, ax=ax, palette="coolwarm")
            ax.set_title('Violin Plot of BMI by Outcome')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download Violin Plot of BMI by Outcome',data=download_fig(fig, 'violin_plot_bmi_by_outcome.png'),  file_name='violin_plot_bmi_by_outcome.png')

        else:
            st.error("The uploaded file does not contain a 'Diabetes' column.")

    if st.button('Make Predictions'):
        try:
            response =requests.post('http://localhost:5000/batch_predict',json=data.to_dict( orient='records'))
            response.raise_for_status()  
            predictions = response.json().get('predictions', [])
            data['Prediction'] = predictions
            st.write(data)

            fig, ax = plt.subplots()
            sns.countplot(x='Prediction', data=data, ax=ax, palette="coolwarm")
            ax.set_title('Prediction Distribution')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download Prediction Distribution',data=download_fig(fig, 'prediction_distribution.png' ), file_name='prediction_distribution.png' )

            fig, ax = plt.subplots()
            sns.histplot(data, x='BMI', hue='Prediction', multiple='stack',palette="coolwarm", kde=True, ax=ax)
            ax.set_title('BMI Distribution by Prediction')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download BMI Distribution by Prediction',data=download_fig(fig, 'bmi_distribution_by_prediction.png'), file_name='bmi_distribution_by_prediction.png' )

            fig, ax = plt.subplots()
            sns.boxplot(x='Prediction', y='Age',data=data,ax=ax, palette="coolwarm")
            ax.set_title('Age vs Prediction')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download Age vs Prediction',data=download_fig(fig, 'age_vs_prediction.png'), file_name='age_vs_prediction.png' )

            fig, ax = plt.subplots()
            sns.scatterplot(x='BMI', y='PhysHlth',hue='Prediction', data=data, ax=ax, palette="coolwarm")
            ax.set_title('BMI vs Physical Health by Prediction')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download BMI vs Physical Health by Prediction',data=download_fig(fig, 'bmi_vs_physical_health_by_prediction.png'),file_name='bmi_vs_physical_health_by_prediction.png')

            fig, ax = plt.subplots()
            sns.heatmap(data.corr(),annot=True,cmap='coolwarm', ax=ax )
            ax.set_title('Correlation Matrix')
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download Correlation Matrix',data=download_fig(fig,'correlation_matrix.png'),file_name='correlation_matrix.png')

            fig, ax=plt.subplots()
            sns.violinplot(x='Prediction', y='BMI', data=data, ax=ax, palette="coolwarm" )
            ax.set_title('Violin Plot of BMI by Prediction' )
            add_border_to_plot(fig)
            st.pyplot(fig)
            st.download_button('Download Violin Plot of BMI by Prediction', data=download_fig( fig, 'violin_plot_bmi_by_prediction.png'), file_name='violin_plot_bmi_by_prediction.png')

        except requests.exceptions.RequestException as e:
            st.error(f"Error during prediction: {e}")
