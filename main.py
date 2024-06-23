import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.colors as mcolors
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import joblib

df=pd.read_csv('Datos/PPMI_2022.csv')
modelo1=pd.read_csv('Datos/randonforestdatos.csv')
modelo2=pd.read_csv('Datos/modelo_svm.csv')
df['DISEASE_STATUS_code'] = df['DISEASE_STATUS'].astype('category').cat.codes
data_modelo1 = {
    'DISEASE_STATUS': [0, 0, 0, 1, 1, 1],
    'GENDER': ['Female', 'Male', 'Female', 'Female', 'Female', 'Male'],
    'AGE': [63, 67, 77, 72, 91, 60],
    'moca': [29.0, 27.0, 28.0, 26.0, 28.0, 29.0],
    'asyn': [1657.9, 876.5, 1915.7, 1422.2, 1656.5, 1509.5],
    'fampd_bin': [2, 2, 2, 1, 1, 1],
    'upsit': [35, 40, 34, 20, 16, 38]
}

# Crear DataFrame
datos_modelo1 = pd.DataFrame(data_modelo1)
data = {
    'P177_Plasma_APOC2': [4360000.0, 5290000.0, 1960000.0, 1910000.0, 4840000.0, 1650000.0],
    'P177_Plasma_CD5L': [64679.20, 86023.60, 203099.00, 122667.00, 0.00, 8165.77],
    'P177_Plasma_F12': [2200000.0, 1830000.0, 1310000.0, 1890000.0, 2060000.0, 30115.5],
    'P177_Plasma_IGHG3': [492595.0, 433636.0, 726774.0, 393885.0, 351621.0, 532634.0],
    'P177_Plasma_IGHM': [108486.0, 460023.0, 842129.0, 215611.0, 428045.0, 94064.3],
    'P177_Plasma_IGKC': [2040000.0, 1640000.0, 2740000.0, 3170000.0, 632809.0, 1370000.0],
    'P177_Plasma_IGLV3_25': [63979.7, 27067.1, 136975.0, 135509.0, 0.0, 44812.7],
    'P177_Plasma_LGALS3BP': [41645.2, 25656.4, 68944.7, 37144.1, 34970.3, 0.0],
    'P177_Plasma_PPBP': [1800000.0, 4600000.0, 43378.1, 291566.0, 791932.0, 460011.0],
    'P177_Plasma_TF': [3410000.00, 1730000.00, 3000000.00, 3080000.00, 3230.85, 3350000.00],
    'moca': [27.0, 27.0, 27.0, 25.0, 29.0, 28.0],
    'fampd_bin': [0, 1, 1, 1, 1, 1],
    'AGE': [79, 82, 73, 81, 74, 79],
    'GENDER': [0, 1, 0, 0, 0, 0],
    'DISEASE_STATUS': [0, 0, 0, 1, 1, 1]
}
datos_modelo2 = pd.DataFrame(data)

orange_palette = [
    '#D73B0A',  # Red-Orange
    '#E15522',  # Strong Orange
    '#EB6E3A',  # Mid Orangec
    '#F58851',  # Light Orange
    '#FFA169'   # Pale Orange
]
sns.set_palette(sns.color_palette(orange_palette))
# Título de la aplicación
st.title("NeuroBioPredict: ML-Based Biomarker Discovery in Parkinson's")


# Menú con pestañas en la barra lateral, dispuestas una debajo de otra
#menu = ["Teoría", "Visualización", "Modelo"]
#choice = st.sidebar.radio("Selecciona una pestaña", menu)
st.sidebar.title("Navigation Menu")
menu = st.sidebar.radio("Go to", ["Theory", "Charts", "Model"])



if menu == "Theory":
    st.header("Project definition")
    st.write("""
        Parkinson’s disease (PD) starts at the molecular and cellular levels long before motor symptoms appear, yet there are currently no early-stage molecular biomarkers for diagnosis, prognosis prediction, or monitoring therapeutic response. This absence of biomarkers significantly impedes patient care. Here, we explore the use of machine learning approaches to predict Parkinson's disease and identify potential biochemical biomarkers in urine and plasma.

Machine learning techniques have shown great potential in addressing real-world problems by effectively learning complex patterns in high-dimensional datasets. Previous studies have demonstrated that machine learning models can integrate patient genotype data, demographic information, clinical assessments, and neuroimaging data to predict disease outcomes.

The identification of molecular biomarkers for Parkinson's disease, particularly those detectable in accessible biofluids like urine and plasma, is crucial for improving patient outcomes. This research area holds immense promise for developing accurate diagnostic tools and personalized treatment strategies.

Additionally, we aim to acquire and apply advanced knowledge in machine learning techniques and omics data analysis, strengthening the necessary skills for managing and processing complex datasets. This emerging approach is crucial and increasingly implemented in the development of more accurate and personalized diagnostic and therapeutic tools. 

        """)
    st.write("Data")
    st.write("""
        For this project, we used data from the Parkinson's Progression Markers Initiative (PPMI) study database, which contains genetic, metabolic, and clinical data for Parkinson's disease patients and healthy controls. The data utilized comes from the PPMI sub-studies, titled Project 177 and Project 190.

        Data used in the preparation of this project were obtained in May 2024 from the Parkinson's Progression Markers Initiative (PPMI) database. The Parkinson's Progression Markers Initiative (PPMI) is an ongoing observational international study conducted in the United States, Europe, Israel, and Australia. To date, the study has enrolled approximately 4,000 participants, including healthy adults (HC), de novo Parkinson's disease patients (PD), prodromal individuals (age 60 or older with a dopamine transporter (DAT) deficit and REM sleep behavior disorder (RBD) or hyposmia), and non-manifesting LRRK2 and GBA carrier participants. Participants undergo extensive clinical assessment, imaging, and molecular phenotyping. """)
    
    st.write('Data Used:')
    
    st.dataframe(df)
    
    st.write('Datos utilizados en el modelo de randon forest ')
    
    st.dataframe(modelo1)
    
    st.write('Datos utilizados en el modelo de SVM ')
    
    st.dataframe(modelo2)
    col1, col2 = st.columns(2)

    with col1:
        st.header("PPMI (Project 177)")
        st.write("""
        **Project Description:** This project assessed the proteome of cerebrospinal fluid (CSF) and blood plasma of the PPMI cohort using mass spectrometry-based untargeted proteome investigation. 
        - **CSF Samples:** 2,283 from 482 participants.
        - **Blood Plasma Samples:** 949 from 179 participants.
        - **Data Processing:** OpenSwath pipeline, mapDIA, batch corrected.
        """)
        
        with st.expander("Method Description"):
            st.write("""
            Proteins were extracted, digested, and the resulting peptides were analyzed using mass spectrometry. Analysis was conducted on a Bruker timsTOF Pro mass spectrometer with a data-independent acquisition method.
            """)

    with col2:
        st.header("PPMI (Project 190)")
        st.write("""
        **Project Description:** This project focused on the proteomic investigation of the urine proteome in Parkinson's disease patients using targeted and untargeted mass spectrometry.
        - **Urine Samples:** 1,164 from the PPMI PD cohort.
        - **Analysis:** LC-MS/MS for urinary proteome profiles. Targeted analysis of Rab10 and LRRK2.
        """)
        
        with st.expander("Method Description"):
            st.write("""
            Proteins were extracted from neat urine samples and digested into peptides using the MStern blotting sample preparation protocol. Purified peptides were loaded on Evosep Evotips, separated via an Evosep One HPLC, and analyzed on a Bruker timsTOF Pro mass spectrometer with a data-independent acquisition method and a gradient length of 44 minutes. Targeted analysis was performed using the same peptide extract but using an EASY-nLC1200 HPLC with a gradient length of 21 minutes. Analysis of raw spectra was performed with DIA-NN and Skyline.
            """)

    st.write("---")
    st.markdown("""
        <div style="background-color: #FFDDC1; padding: 15px; border-radius: 5px; border: 2px solid #FF6347;">
            <h3 style="color: #D2691E; font-weight: bold;">Disclaimer</h3>
            <p style="color: #333; font-weight: bold;">
                This project is purely academic and the results obtained have no clinical or diagnostic validity.
            </p>
        </div>
        """, unsafe_allow_html=True)

    
elif menu == "Charts":
    option = st.sidebar.selectbox(
    'Select a chart category',
    ('CSF Charts', 'Plasma Charts', 'Urine Charts')
    )
    st.title("Charts")
    if option == 'CSF Charts':
        st.header('CSF Charts')
        
        st.header('Gender Distribution by Disease Status')
        def grafico_genero(df):
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(data=df, x='GENDER', hue='DISEASE_STATUS', ax=ax)
            ax.set_title('Gender Distribution by Disease Status')
            
            # Mostrar números en las barras
            for p in ax.patches:
                height = p.get_height()
                ax.text(p.get_x() + p.get_width() / 2., height + 0.1, height, ha='center')
            
            # Ajustar la leyenda
            ax.legend(title='Disease Status', loc='lower right')
            
            return fig

        fig_genero = grafico_genero(modelo1)
        st.pyplot(fig_genero)
        
        st.header('MOCA Distribution by Disease Status')
        def grafico_moca(df):
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.violinplot(data=df, x='DISEASE_STATUS', y='moca', ax=ax)
            ax.set_title('MOCA Distribution by Disease Status')
            ax.legend(labels=df['DISEASE_STATUS'].unique())
            return fig
        

        fig_moca = grafico_moca(modelo1)
        st.pyplot(fig_moca)

        st.header('Relationship between ASYN and UPSIT by Disease Status and Family History')
        def grafico_asyn_upsit(df):
            fig, ax = plt.subplots(figsize=(10,6))
            sns.scatterplot(data=df, x='asyn', y='upsit', hue='DISEASE_STATUS', style='fampd_bin', ax=ax)
            ax.set_title('Relationship between ASYN and UPSIT by Disease Status and Family History')
            ax.set_xlabel('ASYN')
            ax.set_ylabel('UPSIT')
            ax.legend(title='Disease Status / Family History',  loc='lower right')
            return fig

        fig_asyn_upsit = grafico_asyn_upsit(modelo1)
        st.pyplot(fig_asyn_upsit)
    
    elif option == 'Plasma Charts':
        st.header('Plasma Charts')
        biomarcadores = [col for col in modelo2.columns if col.startswith('P177_Plasma')]

        st.title('Visualization of Biomarkers in Patients')
        biomarcador = st.selectbox('Select a biomarker:', biomarcadores)


        def crear_histograma(df, biomarcador):
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(data=df, x=biomarcador, hue='DISEASE_STATUS', kde=True, element='step', ax=ax)
            ax.set_title(f'Distribution of {biomarcador} by Disease Status')
            ax.set_xlabel(biomarcador)
            ax.set_ylabel('Density')
            
            # Ajustar la leyenda para que no se solape
            legend_labels = {'PD': 'Parkinson\'s Disease', 'HC': 'Healthy Control'}
            ax.legend(title='Legend', labels=legend_labels, loc='upper right')
            
            # Personalizar el estilo (opcional)
            sns.set_style('whitegrid')
            
            return fig

        if biomarcador:
            fig = crear_histograma(modelo2, biomarcador)
            st.pyplot(fig)
                
    elif option == 'Urine Charts':
        st.header('Urine Charts')
        
      
elif menu == "Model":
    
    st.title("Results: Parkinson’s Disease Classification Models")

    # Overview
    st.header("Progress Overview")
    st.write("""
    We developed three versions of a classification model capable of predicting Parkinson’s disease:
    1. **Model 1:** Used clinical data.
    2. **Model 2:** Incorporated plasma proteomics data, allowing us to analyze protein profiles.
    3. **Model 3:** Explored urinary proteomics, examining the protein composition of urine for disease signatures.

    The workflow consisted of data preparation, feature selection, model training, and evaluation.
    """)

    # Comparing Models
    
    st.header("Comparison of Models")

    tab1, tab2,tab3  = st.tabs(["Model 1: Clinical Data", "Model 2: Plasma Proteomics SVM","Model 3: Urinary Proteomics"])

    with tab1:
        min_age, max_age = 40, 93
        min_moca, max_moca = 17, 30
        min_asyn, max_asyn = 606.1, 5256.9
        min_upsit, max_upsit = 1, 40
        st.subheader("Parkinson's Prediction Models")
        st.write("Example Data for Model Testing:")
        st.write('Disease_status: HC: 0, PD: 1')
        st.write(datos_modelo1)
        model_path1 = "modelos/random_forest_model.pkl"
        scaler_path1 = "modelos/scaler_randomforest.pkl"
        imputer_path1 = "modelos/imputerrandom_forest.pkl"

        rf_model = joblib.load(model_path1)
        scaler1 = joblib.load(scaler_path1)
        imputer1 = joblib.load(imputer_path1)
        with st.form("Data Prediction"):
            gender = st.selectbox("Gender", options=["Male", "Female"], help="Select the patient's gender.")
            age = st.number_input(f"Age (Range: {min_age}-{max_age})", min_value=min_age, max_value=max_age, step=1, help="Enter the patient's age.")
            moca = st.number_input(f"MOCA Score (Range: {min_moca}-{max_moca})", min_value=min_moca, max_value=max_moca, step=1, help="Enter the MOCA score.")
            fampd_bin = st.selectbox("FAMPD_BIN (Family History)", options=[0, 1], help="Indicate if there is a family history of Parkinson's (0: No, 1: Yes).")
            upsit = st.number_input(f"UPSIT Score (Range: {min_upsit}-{max_upsit})", min_value=min_upsit, max_value=max_upsit, step=1, help="Enter the UPSIT score.")
            asyn = st.number_input(f"ASYN (Range: {min_asyn}-{max_asyn})", min_value=min_asyn, max_value=max_asyn, step=0.1, help="Enter the ASYN value.")

            # Convertir el género a numérico si es necesario
            gender_numeric = 1 if gender == "Male" else 0

            # Crear botón para hacer predicción
            submitted = st.form_submit_button("Prediction")

            if submitted:
                try:
                    # Validación de entrada
                    if not (min_age <= age <= max_age):
                        st.warning(f"Please enter a valid age within the range {min_age}-{max_age}.")
                    elif not (min_moca <= moca <= max_moca):
                        st.warning(f"Please enter a valid MOCA score within the range {min_moca}-{max_moca}.")
                    elif not (min_upsit <= upsit <= max_upsit):
                        st.warning(f"Please enter a valid UPSIT score within the range {min_upsit}-{max_upsit}.")
                    elif not (min_asyn <= asyn <= max_asyn):
                        st.warning(f"Please enter a valid ASYN value within the range {min_asyn}-{max_asyn}.")
                    else:
                        # Crear DataFrame con los nuevos datos
                        new_data = pd.DataFrame({
                            'GENDER': [gender_numeric],
                            'AGE': [age],
                            'moca': [moca],
                            'fampd_bin': [fampd_bin],
                            'upsit': [upsit],
                            'asyn': [asyn]
                        })

                        # Placeholder para la predicción
                        st.success("Prediction processed successfully!")
                        new_data_imputed = imputer1.transform(new_data)
                        new_data_scaled = scaler1.transform(new_data_imputed)
                        prediction = rf_model.predict(new_data_scaled)

                        prediction_message = "Unlikely to have Parkinson's" if prediction[0] == 0 else "Possible Parkinson's"
                        st.write("Prediction:", prediction_message)

                except ValueError as e:
                    st.error("Invalid input: Please enter valid numerical values.")
                        # Imputar, escalar y predecir
                        
    with tab2:
        st.header("Parkinson's Disease Classification Model")
        st.write("Example Data for Model Testing:")
        st.write('Disease_status: HC: 0, PD: 1')
        st.write(datos_modelo2)
        model_path = "modelos/svm_model.pkl"
        scaler_path = "modelos/scaler.pkl"
        imputer_path = "modelos/imputer.pkl"

        svm_model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        imputer = joblib.load(imputer_path)
        # Entradas del usuario organizadas en dos columnas
        # Definir los rangos mínimos y máximos para validación
        min_values = {
            'P177_Plasma_APOC2': 24886.1,
            'P177_Plasma_CD5L': 0.0,
            'P177_Plasma_F12': 12714.9,
            'P177_Plasma_IGHG3': 0.0,
            'P177_Plasma_IGHM': 0.0,
            'P177_Plasma_IGKC': 141342.0,
            'P177_Plasma_IGLV3_25': 0.0,
            'P177_Plasma_LGALS3BP': 0.0,
            'P177_Plasma_PPBP': 0.0,
            'P177_Plasma_TF': 0.0,
            'moca': 21,
            'fampd_bin': 1,
            'AGE': 40,
            'GENDER': 0
        }

        max_values = {
            'P177_Plasma_APOC2': 12400000.0,
            'P177_Plasma_CD5L': 470615.0,
            'P177_Plasma_F12': 3780000.0,
            'P177_Plasma_IGHG3': 1360000.0,
            'P177_Plasma_IGHM': 2870000.0,
            'P177_Plasma_IGKC': 5130000.0,
            'P177_Plasma_IGLV3_25': 240776.0,
            'P177_Plasma_LGALS3BP': 220156.0,
            'P177_Plasma_PPBP': 4600000.0,
            'P177_Plasma_TF': 3550000.0,
            'moca': 30,
            'fampd_bin': 2,
            'AGE': 93,
            'GENDER': 1
        }

        # Crear el formulario en Streamlit
        with st.form(key='prediction_form'):
            col1, col2 = st.columns(2)

            inputs = {}

            with col1:
                inputs['P177_Plasma_APOC2'] = st.number_input(f"P177_Plasma_APOC2 (Range: {min_values['P177_Plasma_APOC2']} - {max_values['P177_Plasma_APOC2']})", value=0.0)
                inputs['P177_Plasma_CD5L'] = st.number_input(f"P177_Plasma_CD5L (Range: {min_values['P177_Plasma_CD5L']} - {max_values['P177_Plasma_CD5L']})", value=0.0)
                inputs['P177_Plasma_F12'] = st.number_input(f"P177_Plasma_F12 (Range: {min_values['P177_Plasma_F12']} - {max_values['P177_Plasma_F12']})", value=0.0)
                inputs['P177_Plasma_IGHG3'] = st.number_input(f"P177_Plasma_IGHG3 (Range: {min_values['P177_Plasma_IGHG3']} - {max_values['P177_Plasma_IGHG3']})", value=0.0)
                inputs['P177_Plasma_IGHM'] = st.number_input(f"P177_Plasma_IGHM (Range: {min_values['P177_Plasma_IGHM']} - {max_values['P177_Plasma_IGHM']})", value=0.0)
                inputs['P177_Plasma_IGKC'] = st.number_input(f"P177_Plasma_IGKC (Range: {min_values['P177_Plasma_IGKC']} - {max_values['P177_Plasma_IGKC']})", value=0.0)

            with col2:
                inputs['P177_Plasma_IGLV3_25'] = st.number_input(f"P177_Plasma_IGLV3_25 (Range: {min_values['P177_Plasma_IGLV3_25']} - {max_values['P177_Plasma_IGLV3_25']})", value=0.0)
                inputs['P177_Plasma_LGALS3BP'] = st.number_input(f"P177_Plasma_LGALS3BP (Range: {min_values['P177_Plasma_LGALS3BP']} - {max_values['P177_Plasma_LGALS3BP']})", value=0.0)
                inputs['P177_Plasma_PPBP'] = st.number_input(f"P177_Plasma_PPBP (Range: {min_values['P177_Plasma_PPBP']} - {max_values['P177_Plasma_PPBP']})", value=0.0)
                inputs['P177_Plasma_TF'] = st.number_input(f"P177_Plasma_TF (Range: {min_values['P177_Plasma_TF']} - {max_values['P177_Plasma_TF']})", value=0.0)
                inputs['moca'] = st.number_input(f"MoCA Score (Range: {min_values['moca']} - {max_values['moca']})", min_value=min_values['moca'], max_value=max_values['moca'], value=27)
                inputs['fampd_bin'] = st.selectbox("Family History of Parkinson's (1: No, 2: Yes):", [1, 2])
                inputs['AGE'] = st.number_input(f"Age (Range: {min_values['AGE']} - {max_values['AGE']})", min_value=min_values['AGE'], max_value=max_values['AGE'], value=70)
                inputs['GENDER'] = st.selectbox("Gender:", ["Male", "Female"])
                inputs['GENDER'] = 0 if inputs['GENDER'] == "Male" else 1


            # Botón de envío para el formulario
            submit_button = st.form_submit_button(label='Prediction')

            # Solo realiza la predicción si se presiona el botón
            if submit_button:
                # Validar los inputs
                valid = True
                for key, value in inputs.items():
                    if not (min_values[key] <= value <= max_values[key]):
                        st.warning(f"Please enter a valid value for {key} within the range {min_values[key]}-{max_values[key]}.")
                        valid = False

                if valid:
                    try:
                        # Convertir a DataFrame
                        input_data = pd.DataFrame([inputs])

                        # Imputar y escalar
                        input_data_imputed = imputer.transform(input_data)
                        input_data_scaled = scaler.transform(input_data_imputed)

                        # Predicción
                        prediction = svm_model.predict(input_data_scaled)

                        # Mostrar la predicción
                        prediction_message = "Unlikely to have Parkinson's" if prediction[0] == 0 else "Possible Parkinson's"
                        st.write("Prediction:", prediction_message)
                    except Exception as e:
                        st.error(f"An error occurred during prediction: {e}")
                
    with tab3:
        st.header("Modelo de clasificacion")        