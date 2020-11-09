# Exam3-JCDS10

# Heart Disease Prediction

## Overview
Heart disease describes the condittion that affects the heart's activity. Frequently, heart disease is used interchangeably with cardiovascular disease. In fact, these two terms has different meanings. Cardiovascular disease is related to blood vessels, including narrowing and blockage of vessels that can cause stroke, chest pain, and heart attack. In contrast, heart disease is abnormality of heart that can reduce the performance of the heart. Heart disease includes abnormal heartbeats, congenital heart defect, weak heart muscles, heart infections, and many more. 

## Problem Definition
According to healthline.com, heart disease is considered as one of the deadliest disease. It contibutes about 15.5% of the world mortality in 2015. It means they take around 8.8millions people in the world in a year. This disease can actually be cured by careful and consistent treatment from the heart experts. But, in most cases, heart disease does not trigger serious pain, therefore it is quite complicated to detect the disease in the early stage.

## Goal
Predicting heart disease of patients based on provided data and features, including:
- Age
- Sex 
- Chest pain
- Systolic pressure
- ECG test result
- Maximum heart rate
- Exercise induced angina
- ST segment depression
- Slope of ST segments slope
- Number of major vessel
- Thallium stress test result

## General Information
1. The dataset is updated approximately 2 years ago, which is in 2018.
2. Heart disease is the deadliest disease that kills around 8million people per year.
3. Heart disease is caused by several factors:
    - Heart defect (gained by patients since they are born)
    - Thick blood vessel (inerited)
    - Bacteria, virus, and parasytes infections
    - Heart developmnet failure (malnutrion during childhood -> adolescence development)
    - Poor hygiene
4. Heart disease can cause complications:
    - Heart failure
    - Aneurysm (bulge in major vessels, causing internal bleeding)
    - Cardiac arrest (sudden heart dysfunction)

## EDA Result:
1. Overall, people in age range 20-40 has high probability of heart disease, and the probability id decreases as the older they are. As stated before, heart disease can be caused by inherited heart abnormalities and heart development failure. By then, it is known that there are many young adult (when a kid has just being an adult) suffer heart disease. Another speculation is that people with heart disease live shorter than those who do not. Consequently, there are less elder diagnosed as heart disease patients.
2. Female is more likely to experience heart disease. As we know, women's body is more weak than men (so does their antibody), thus their hearts are more likely to be infected by parasytes. Female has slower metabolism than male, so they are more probable to have overweight. Besides, now days women carries quite many responsibility, leading to stress and depression (that can cause abnormal blood pressure).
3. Chest pain is correlated with heart disease. People with chest pain, regardless how severe is the pain, tend to suffer heart disease.
4. People with normal systolic pressure and normal blood flow can suffers heart disease too. This is why heart disease is sometimes cannot be saily detected.
5. High heart rate (more than 100bpm) indicates heart disease.
6. Blood sugar concentration and cholesterol level do not indicate heart disease.


## Conclusion
1. Heart disease risk can be easily detected by considering: high heart rate, chest pain, low exercise induced angina test result, low ST Segment depression, and low number of major vessel colored by fluoroscopy.
2. Priority scoring in this machine learning model is recall_score. Recall score is the ratio between number of heart disease diagnosed patients and the number of true prediction of heart disease. By having this recall_score, we can check the number of people with heart disease that is catched and those who does not. Higher recall score means more people with heart disease is predicted so. Increasing the number of recall_score means detecting heart disease earlier and save more people by early treatment.
3. The best machine learning model for this case id Logistic Regression with 84% accuracy and 93% recall

## Recommendation
1. This machine learning model is recommended for hosplitals, specifically heart hospital.
2. By having this model, hospitals can quickly treat the patients that are predicted to have heart disease. Just a reminder, that early heart-disease detection can save a person's life.
3. The dataset is actually too few to perform machine learning. This actually reasonable because the percentage of population with heart disease is only 6.7% and not all of them go to the hospital to have treatments. However, increasing affordability of heart-treatment allows more people with heart disease to register to a hospital to increase dataset. Along with this action, more people may be saved by affordable medical treatment for heart disease. 
