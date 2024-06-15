# Machine Learning y Proteómica para la identificación de Biomarcadores del Parkison

## Backround

La enfermedad de Parkinson es una condición degenerativa, progresiva y crónica del sistema nervioso central. 
Es actualmente la segunda enfermedad neurodegenerativa más prevalente en el mundo, después del Alzheimer

Según la OMS, la enfermedad de Parkinson afecta a 1 de cada 100 personas mayores de 60 años y se estima que para el año 2030 habrán alrededor de 12 millones de pacientes en el mundo.

Los signos distintivos de la Enfermedad de Parkinson incluyen trastornos del movimiento, como lentitud de movimiento (bradicinesia), incapacidad para moverse (acinesia), temblores en reposo, marcha parkinsoniana y rigidez muscular. 
los síntomas no motores (por ejemplo, trastornos olfativos, estreñimiento y trastornos del sueño) ocurren con frecuencia en la etapa temprana de la enfermedad y pueden incluso preceder a la aparición de una disfunción motora. 

Identificar a las personas con enfermedad de Parkinson (EP) de alto riesgo en etapas más tempranas es una prioridad urgente para retrasar la aparición y progresión de la enfermedad.

## Objetivos

Desarrollar y validar modelos de riesgo en un conjunto de datos de referencia para diagnosticar grupos tempranos de EP con características clínicas no motoras, biomarcadores e identificar los predictores para predecir mejor el pronóstico individual y guiar la prevención.

## Data

utilizamos la base de datos del estudio PPMI (Parkinson's Progression Markers Initiative),[PPMI](http://www.ppmi-info.org) que contiene datos genéticos, metabólicos y clínicos de pacientes con enfermedad de Parkinson y controles sanos.

Es una investigación prospectiva, multicéntrica y global (Estados Unidos, Europa, Israel y Australia) cuyo objetivo de diseño es investigar y verificar biomarcadores que puedan frenar la progresión de la enfermedad.

## Subestudios de PPMI

### Proyecto 177

- **Evaluación proteómica del LCR y el plasma sanguíneo basada en espectrometría de masas.**
- El análisis se llevó a cabo en **2.283 muestras** de **482 participantes** de LCR y **949 muestras** de plasma de **179 participantes**.

### Proyecto 190

- **Investigación basada en espectrometría de masas basada en el proteoma de la orina.**
- Se analizaron **1.164 muestras** de orina.

## Modelos

Métodos de diagnóstico utilizados para distinguir entre la enfermedad de Parkinson en etapas tempranas y los controles sanos.

### RandonForest
Se utilizó un modelo de Random Forest con 314 pacientes, empleando datos clínicos y de líquido cefalorraquídeo (CSF). Las características evaluadas incluyeron:

    UPSIT (Test de Identificación del Olfato de la Universidad de Pensilvania)
    Edad
    Género
    MoCA (Evaluación Cognitiva de Montreal)
    Historial familiar
    α-sinucleína

### SVM (Máquinas de Vectores de Soporte)

Para este modelo, se incluyeron 94 pacientes usando datos clínicos y plasma. Las características consideradas fueron:

    Edad
    Género
    MoCA
    Historial familiar
    APOC
    TF
    CD14%L
    F12
    IGHG3
    IGHM
    IGKC
    IGLV3
    LGALS3BP
    PPBP
### XGBoost

El modelo XGBoost se aplicó a 318 pacientes utilizando datos clínicos y orina. Las características utilizadas fueron:

    Edad
    Género
    Historial familiar
    MoCA
    PC(200X)