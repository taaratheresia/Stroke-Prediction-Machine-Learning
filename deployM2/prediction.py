import streamlit as st
import pandas as pd
import pickle

#Load All files

with open('best_model.pkl', 'rb') as file_1:
  model_ada_best = pickle.load(file_1)

def run():
    # Membuat Form
    with st.form(key='Stroke'):
        age = st.number_input(label='Input your age here', min_value=0.08, max_value=82.0, value=0.08)
        avg_glucose_level = st.number_input(label='Input your average glucose level here', min_value=55.22, max_value=169.365, value=55.22)
        bmi = st.number_input(label='Input your BMI here', min_value=10.3, max_value=47.5, value=10.3)
        hypertension = st.selectbox(label='Choose your hypertension here, 0 = No, 1 = Yes', options= ['0', '1'])
        heart_disease = st.selectbox(label='Choose your heart disease here, 0 = No, 1 = Yes', options= ['0', '1'])
        ever_married = st.selectbox(label='Choose your married status here, 0 = No, 1 = Yes', options= ['No', 'Yes'])

        submitted = st.form_submit_button('Predict')

    data_inf = {
        'age': age,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'ever_married': ever_married
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # Membuat kolom predict 
        inf_predict = model_ada_best.predict(data_inf)
        inf_predict

        st.write('# Predict : ', str(int(inf_predict)))
        if inf_predict[0] == 0:
            st.write('PASIEN TIDAK TERKENA STROKE')
            st.markdown("[CARA MENCEGAH TERKENA STROKE](https://www.siloamhospitals.com/informasi-siloam/artikel/cara-mencegah-stroke-sejak-dini)")

        else:
            st.write('PASIEN KEMUNGKINAN TERKENA STROKE')
            st.markdown("[BAGAIMANA CARA MENGOBATI PENYAKIT STROKE?](https://ciputrahospital.com/bagaimana-cara-mengobati-penyakit-stroke/)")

if __name__ == '__main__':
    run()
