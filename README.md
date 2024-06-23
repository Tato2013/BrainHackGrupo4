# Machine Learning y Proteómica para la identificación de Biomarcadores del Parkison

## ⚠️ **Advertencia: Naturaleza Académica del Proyecto**

Este proyecto es de naturaleza académica y no tiene ninguna validez médica. Los modelos y resultados presentados son puramente experimentales y deben ser tratados como tal. Se recomienda no utilizar estos resultados para diagnóstico o tratamiento médico.


## 📋 **Índice**

- 📖 *[Background](#background)*
- 👥 *[Integrantes del Equipo](#integrantes-del-equipo)*
- 🎯 *[Objetivos](#objetivos)*
- 📊 *[Data](#data)*
- 🔬 *[Subestudios de PPMI](#subestudios-de-ppmi)*
- 🧩 *[Modelos](#modelos)*
- 💡 *[Conclusiones](#conclusión-general)*
- 🛠️ *[Desafíos](#desafíos)*
- 🔮 *[Desafíos Futuros](#desafíos-futuros)*
- 📚 *[Referencias](#referencias)*

## Integrantes del Equipo

| Nombre          | Rol                | Contacto                   |
|-----------------|---------------------|----------------------------|
| Ivana Primost   |                    | 1   |
| Leonardo Rivadeneira| Científico de Datos| 2    |
| Naiara Zilinski |                     |                            |
| Marcelo Peralta | Cientifico de Datos   | cheloperalta22@gmail.com |



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

#### Conclusiones 

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

#### Conclusiones  

### XGBoost

El modelo XGBoost se aplicó a 318 pacientes utilizando datos clínicos y orina. Las características utilizadas fueron:

    Edad
    Género
    Historial familiar
    MoCA
    PC(200X)

#### Conclusiones 

## Conclusión General

Basados en los resultados obtenidos, se pueden derivar las siguientes conclusiones y recomendaciones:

- **Eficacia de los Modelos**
  - Los modelos propuestos han demostrado ser eficaces en la identificación y detección de biomarcadores en diversas muestras biológicas.

- **Necesidad de Investigación Adicional**
  - Es esencial continuar investigando para fortalecer estos modelos en la búsqueda de biomarcadores a partir de muestras biológicas más accesibles.

- **Exploración de Nuevas Combinaciones**
  - Probar nuevas combinaciones de proteínas puede ofrecer insights adicionales y mejorar la precisión de los modelos.

- **Selección de Métodos Estadísticos**
  - Elegir métodos estadísticos adecuados para los datos específicos es crucial para obtener resultados válidos y robustos.

- **Revalidación en Bases de Datos Más Amplias**
  - Revalidar los modelos en bases de datos con un tamaño muestral mayor (n) para asegurar su generalizabilidad y robustez.

## Desafíos

En el análisis y desarrollo de modelos para la enfermedad de Parkinson, enfrentamos varios desafíos significativos:

- **Gran Tamaño de la Base de Datos**
  - **Descripción**: La base de datos contiene una gran cantidad de registros y atributos, lo que hace que el procesamiento y análisis sean complejos y requieran una alta capacidad computacional.
  - **Impacto**: Manejar este volumen de datos puede ser costoso en términos de tiempo y recursos, y requiere estrategias eficientes para el almacenamiento y procesamiento.

- **Exclusión de Participantes por Falta de Datos de Biomarcadores**
  - **Descripción**: Algunos participantes deben ser excluidos del análisis debido a la falta de datos completos de biomarcadores.
  - **Impacto**: Esta exclusión reduce el tamaño de la muestra y puede introducir sesgos, afectando la representatividad y validez de los resultados.

- **Trabajo con Datos Precurados**
  - **Descripción**: Utilizar datos que ya han sido precurados limita la flexibilidad del análisis, ya que se han tomado decisiones previas sobre la calidad y el procesamiento de estos datos.
  - **Impacto**: Restringe la capacidad de explorar nuevas hipótesis y enfoques analíticos, ya que no se puede acceder a los datos en su forma original.

## Desafíos Futuros

Para avanzar en la investigación y mejora del diagnóstico de la enfermedad de Parkinson, se identifican las siguientes áreas de desarrollo:

- **Incorporar Variaciones Genéticas**
  - **Descripción**: Integrar datos genéticos en el análisis para personalizar el enfoque y entender mejor los factores de riesgo individuales.
  - **Objetivo**: Aumentar la precisión de los modelos predictivos y mejorar la identificación de subtipos de la enfermedad.

- **Generar y Trabajar con Datos Propios**
  - **Descripción**: Obtener y analizar datos generados internamente, en lugar de depender únicamente de bases de datos externas.
  - **Objetivo**: Controlar mejor la calidad y relevancia de los datos para estudios específicos.

- **Incluir Estadios Avanzados de Parkinson**
  - **Descripción**: Incluir datos de pacientes en etapas avanzadas de la enfermedad para entender mejor su progresión.
  - **Objetivo**: Desarrollar estrategias de tratamiento y manejo para todas las fases de la enfermedad.

- **Reducir la Dependencia de Datos Clínicos como Indicadores Tempranos**
  - **Descripción**: Investigar nuevos biomarcadores que permitan identificar la enfermedad en sus primeras etapas sin depender exclusivamente de datos clínicos.
  - **Objetivo**: Facilitar la detección temprana y precisa, mejorando las oportunidades de intervención y tratamiento.

## Referencias

- **Kaiser, S., Zhang, L., Mollenhauer, B. et al.** (2023). "Una visión proteogenómica de la causalidad y heterogeneidad de la enfermedad de Parkinson". *npj Parkinsons Dis*, 9, 24. [https://doi.org/10.1038/s41531-023-00461-9](https://doi.org/10.1038/s41531-023-00461-9)

- **Rutledge, J., Lehallier, B., Zarifkar, P. et al.** (2024). "La proteómica integral del LCR, el plasma y la orina identifica la DDC y otros biomarcadores de la enfermedad de Parkinson temprana". *Acta Neuropathol*, 147, 52. [https://doi.org/10.1007/s00401-024-02706-0](https://doi.org/10.1007/s00401-024-02706-0)

- **Dou, K., Ma, J., Zhang, X., Shi, W., Tao, M., Xie, A.** (2022). "Modelado de predictores múltiples para predecir la progresión temprana de la enfermedad de Parkinson y los síntomas no motores". *Revista*, Volumen, Páginas. [https://doi.org/10.xxxxx/yyyyyy](https://doi.org/10.xxxxx/yyyyyy)

- **The Parkinson Progression Marker Initiative (PPMI)**. [Enlace al recurso](https://www.ppmi-info.org/)

## Vea el Trabajo Realizado

Para explorar y interactuar con el trabajo realizado, visita el siguiente enlace:

🔗 [Deploy del Trabajo](https://neurobiopredict.streamlit.app/)

Este enlace te llevará a la aplicación desplegada donde podrás explorar los modelos y resultados del proyecto relacionado con la enfermedad de Parkinson.

## Probar el Deployment Local con Streamlit

1. **Clonar el Repositorio**: Clona este repositorio a tu máquina local.
1. **Clonar el Repositorio**: Clona este repositorio a tu máquina local para obtener el código fuente.

    ```bash
    git clone https://github.com/Tato2013/BrainHackGrupo4.git
    
    ```

2. **Crear un Entorno Virtual (Recomendado)**: Crea y activa un entorno virtual para mantener las dependencias del proyecto aisladas.

    ```bash
    python -m venv env       # Crea un entorno virtual
    source env/bin/activate  # Activa el entorno virtual (Linux/Mac)
    env\Scripts\activate     # Activa el entorno virtual (Windows)
    ```

3. **Instalar Dependencias**: Instala las bibliotecas y dependencias necesarias utilizando el archivo `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar la Aplicación**: Ejecuta el siguiente comando para iniciar la aplicación Streamlit desde la carpeta donde se encuentra el archivo principal (por ejemplo, `main.py`).

    ```bash
    streamlit run main.py
    ```

5. **Interactuar con la Aplicación**: Una vez que la aplicación esté en funcionamiento, abre tu navegador web y visita `http://localhost:8501` para interactuar con la aplicación Streamlit.

   Asegúrate de tener el entorno virtual activado y todas las dependencias instaladas antes de ejecutar la aplicación.