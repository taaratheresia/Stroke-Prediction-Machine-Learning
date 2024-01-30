# Stroke Prediction Analysis

Stroke is the second leading cause of death globally, responsible for approximately 11% of total deaths according to the World Health Organization (WHO). This project provides insights into the factors contributing to stroke risk, assisting in prevention and risk management strategies. 

This project aims to predict the likelihood of a patient having a stroke based on various input parameters such as gender, age, medical history, and smoking status. Machine learning techniques are used to analyze a dataset containing relevant information about patients. The main metric used is recall, with a focus on reducing false negatives over false positives.

The dataset includes information about patient demographics, medical history, and lifestyle choices. Attributes include gender, age, hypertension, heart disease, marital status, occupation, residence type, glucose level, body mass index (BMI), smoking status, and stroke occurrence.

File Descriptions
- healthcare-dataset-stroke-data.csv: Raw data used for analysis.
- P1M2_taara.ipynb: Main notebook containing the analysis and modeling process.
- P1M2_taara_inf.ipynb: Additional notebook focusing on further model insights.
- best_model.pkl: Best model saved after training process.
- url.txt: Text file containing dataset and deployment links.

There is a deployM2 folder containing scripts for deployment creation.

Strengths and Limitations

Strengths:
- The project offers a systematic approach to stroke prediction, potentially aiding in preventive healthcare.
- AdaBoost model demonstrates high recall scores, indicating its effectiveness in identifying stroke risk factors.

Limitations:
- Models are sensitive to data changes and require periodic updates as medical data evolves.
- Sensitivity to data changes can pose challenges for long-term care, especially in stroke patient management.


References
Dataset: Kaggle - Stroke Prediction Dataset
Deployment: Hugging Face - DeployM2
