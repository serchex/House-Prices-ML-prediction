# House Price Prediction using CatBoost & Streamlit

**My name**: Sergio Daniel Gonzalez Lopez  
**Project**: Predicting house prices from Ames/Kaggle dataset

---

##  Project Overview

This is a machine learning model trained on the Kaggle Ames Housing dataset to **predict house prices**. The model uses **CatBoost**, 
which provided the best performance after comparing with LightGBM, XGBoost, and Random Forest. It's deployed as a web app using **Streamlit**, 
allowing users to input home features and get instant price predictions.

**Live demo**: https://house-prices-ml-prediction-sergio-gonzalez.streamlit.app

---

##  Key Features

- Data cleaning & preprocessing: handled missing values, categorical encoding and scaling was omitted by using Catboost
- Feature engineering: created new features to improve model accuracy (0.12402)
- Model evaluation: used MAE, RMSE, R² metrics
- Hyperparameter tuning: optimized CatBoost parameters for best results
- Deployment: Streamlit app with real-time interactive interface for no tecnical users

---

##  Performance (public score in kaggle)
<img width="1257" height="86" alt="Image" src="https://github.com/user-attachments/assets/bc09e202-106c-4f67-af87-71d60145ec7d" />
---
##  Setup Instructions

Make sure you have Python 3.9+ installed:

```bash
git clone https://github.com/serchex/House-Prices-ML-prediction.git
cd House-Prices-ML-prediction
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py



CatBoost outperformed other tested models by [brief statement of improvement].

 Why This Project Matters
Demonstrates full ML pipeline: from data preprocessing to deployment

Highlights proficiency with CatBoost, a high-performance model

Includes interactive deployment via Streamlit Cloud

Ideal for showcasing skills to recruiters and tech teams

 Video Guides


 Technologies Used
Python (pandas, numpy, scikit-learn, CatBoost, joblib)

Streamlit for web deployment

GitHub for version control

 License
This project is licensed under the MIT License (see LICENSE).

 Acknowledgments
Kaggle for the Ames Housing dataset

Streamlit for making deployment easy and free

 Contact
Feel free to reach out at gonzalezsergio2234@gmail.com.










