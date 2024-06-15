import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.colors as mcolors
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import joblib

df=pd.read_csv('PPMI_2022.csv')
df['DISEASE_STATUS_code'] = df['DISEASE_STATUS'].astype('category').cat.codes

orange_palette = [
    '#D73B0A',  # Red-Orange
    '#E15522',  # Strong Orange
    '#EB6E3A',  # Mid Orange
    '#F58851',  # Light Orange
    '#FFA169'   # Pale Orange
]
sns.set_palette(sns.color_palette(orange_palette))
# Título de la aplicación
st.title("NeuroBioPredict: ML-Based Biomarker Discovery in Parkinson's")


# Menú con pestañas en la barra lateral, dispuestas una debajo de otra
#menu = ["Teoría", "Visualización", "Modelo"]
#choice = st.sidebar.radio("Selecciona una pestaña", menu)
st.sidebar.title("Menú de Navegación")
menu = st.sidebar.radio("Ir a", ["Teoria", "Graficos", "Modelo"])



if menu == "Teoria":
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
    
    # Comparing Models
    
elif menu == "Graficos":
    option = st.sidebar.selectbox(
    'Seleccione una categoría de gráficos',
    ('Gráficos de CSF', 'Gráficos de Plasma', 'Gráficos de Orina')
    )
    st.title("Graficos")
    if option == 'Gráficos de CSF':
        st.header('Gráficos de CSF')
        
        fig, ax = plt.subplots()
        sns.countplot(data=df, x='GENDER',hue='DISEASE_STATUS', ax=ax, palette='Oranges')

    # Configurar etiquetas y título
        ax.set_xlabel('GENDER')
        ax.set_ylabel('Participants')
        ax.set_title('Comparison of Participants')
        # Mostrar gráfico en Streamlit
        st.pyplot(fig)
    #******************
        # Gráfico de líneas con área sombreada por Disease Status
        st.subheader('Gráfico de Dispersión de Puntuación MOCA')
        fig=plt.figure()
        sns.scatterplot(data=df, x=df.index, y='moca', hue='DISEASE_STATUS', style='DISEASE_STATUS', s=100)
        plt.xlabel('Índice de Observación')
        plt.ylabel('Puntuación MOCA')
        plt.title('Gráfico de Dispersión de Puntuación MOCA por Estado del paciente')
        plt.legend(title='Estado del paciente')
        st.pyplot(fig)
    elif option == 'Gráficos de Plasma':
        st.header('Gráficos de Plasma')
        
        
    elif option == 'Gráficos de Orina':
        st.header('Gráficos de Orina')
        
    

   
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.scatterplot(data=df, x='DISEASE_STATUS', y='PATNO', ax=ax, palette=orange_palette)

    # Configurar etiquetas y título
    ax.set_xlabel('Disease Status')
    ax.set_ylabel('Participants')
    ax.set_title('Comparison of Participants by Disease Status')

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)
            
    
        
    fig, ax = plt.subplots(figsize=(16, 10))
    sns.countplot(data=df, x='DISEASE_STATUS', hue='GENDER', ax=ax, palette=orange_palette)

    # Configurar etiquetas y título
    ax.set_title('Gender Distribution by Disease Status')
    ax.set_xlabel('Disease Status')
    ax.set_ylabel('Number of Patients')

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)
    
      
elif menu == "Modelo":
    
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
    st.subheader("Modelos de Predicción de Parkinson")
    
    
with tab2:
    st.header("Modelo de Clasificacion de la Enfermedad de Parkinson")
    model_path = "svm_model.pkl"
    scaler_path = "scaler.pkl"
    imputer_path = "imputer.pkl"

    svm_model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    imputer = joblib.load(imputer_path)
    # Entradas del usuario organizadas en dos columnas
    col1, col2 = st.columns(2)
    inputs = {}

    with col1:
        inputs['P177_Plasma_APOC2'] = st.number_input("P177_Plasma_APOC2", value=0.0)
        inputs['P177_Plasma_CD5L'] = st.number_input("P177_Plasma_CD5L", value=0.0)
        inputs['P177_Plasma_F12'] = st.number_input("P177_Plasma_F12", value=0.0)
        inputs['P177_Plasma_IGHG3'] = st.number_input("P177_Plasma_IGHG3", value=0.0)
        inputs['P177_Plasma_IGHM'] = st.number_input("P177_Plasma_IGHM", value=0.0)
        inputs['P177_Plasma_IGKC'] = st.number_input("P177_Plasma_IGKC", value=0.0)
    
    with col2:
        inputs['P177_Plasma_IGLV3_25'] = st.number_input("P177_Plasma_IGLV3_25", value=0.0)
        inputs['P177_Plasma_LGALS3BP'] = st.number_input("P177_Plasma_LGALS3BP", value=0.0)
        inputs['P177_Plasma_PPBP'] = st.number_input("P177_Plasma_PPBP", value=0.0)
        inputs['P177_Plasma_TF'] = st.number_input("P177_Plasma_TF", value=0.0)
        inputs['moca'] = st.number_input("MoCA Score:", min_value=0, max_value=30, value=15)
        inputs['fampd_bin'] = st.selectbox("Historia Familiar de Parkinson:", [0, 1])
        inputs['AGE'] = st.number_input("Edad:", min_value=30, max_value=100, value=65)
        inputs['GENDER'] = st.selectbox("Género:", ["Male", "Female"])
        inputs['GENDER'] = 0 if inputs['GENDER'] == "Male" else 1

    if st.button("Predecir"):
        # Crear un DataFrame con la entrada del usuario
        user_data = pd.DataFrame([inputs])

        # Imputar y escalar las características del usuario usando el mismo imputer y scaler que se usó para entrenar el modelo
        user_data_imputed = imputer.transform(user_data)
        user_data_scaled = scaler.transform(user_data_imputed)

        # Realizar predicción
        prediction = svm_model.predict(user_data_scaled)

        # Mostrar el resultado
        if prediction == 1:
            st.success("Predicción: Posible enfermedad de Parkinson")
        else:
            st.info("Predicción: No se detecta enfermedad de Parkinson")
    
    with tab3:
        st.header("Modelo de clasificacion")        