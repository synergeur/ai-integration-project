# Phishing URL Detection - AI Integration Project

## Overview

This project aims to develop a **supervised machine learning model** to detect phishing URLs based on key characteristics of the URL structure and content. With the increasing sophistication of phishing attacks, this system leverages **Google BigQuery**, **FastAPI**, **Flask**, and **machine learning models** to classify URLs as **legitimate** or **malicious**.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

## Features

- **Automated Phishing Detection**: Uses AI models to classify URLs as phishing or legitimate.
- **FastAPI API Integration**: Provides real-time URL classification.
- **Web-Based User Interface**: Users can submit URLs for scanning.
- **BigQuery Machine Learning**: Efficient model storage and inference using Google Cloud.
- **Multiple Model Support**: Uses Decision Trees, Logistic Regression, Random Forest, and XGBoost.
- **Flask Backend for Web App**: Serves the front-end UI with URL input capabilities.

---

## :one: Main Branch: Data Processing and Model Training

### Dataset

The dataset consists of **235,795 URLs** with **54 features**. Key characteristics include:

- **URL Structure**: Length, presence of special characters, subdomains.
- **Domain Information**: Whether the domain uses an IP address, SSL certificate validity.
- **Obfuscation Indicators**: The presence of encoded characters or misleading text.
- **Page Content Features**: Number of popups, JavaScript usage, external references.
- **Financial & Sensitive Data Indicators**: Whether the page is associated with **banking, payment systems, or cryptocurrencies**.

### Data Processing Pipeline

1. **Data Extraction**
   - Data fetched using `ucimlrepo`.
   - Imported into **BigQuery** using Python scripts.

2. **Data Cleaning**
   - Removing duplicates and inconsistent entries.
   - Handling missing values and standardizing column names.

3. **Feature Engineering**
   - Selecting key variables through correlation analysis.
   - Encoding categorical variables and normalizing numerical ones.

4. **Model Development**
   - **Logistic Regression**: Baseline model.
   - **Random Forest**: Better feature interactions.
   - **XGBoost**: High-performance gradient boosting.
   - **DNN**: Captures complex patterns.

### **Best Performing Model**
The **XGBoost classifier** achieved the highest accuracy and F1-score, making it the final choice for deployment.

---

## :two: API Branch: Phishing Detection API

The **API** is built using **FastAPI** and integrates with **Google BigQuery ML** to provide real-time URL classification.

### API Features

- **Automatic AI Scan**: Takes a URL, extracts key features, and predicts whether it's phishing.
- **Manual AI Scan**: Accepts precomputed URL features and runs model predictions.
- **Multiple Model Support**: Predictions generated using Decision Trees, Logistic Regression, Random Forest, and XGBoost.
- **Authentication Support**: Uses Google Cloud authentication for security.

### API Endpoints

| Method | Endpoint                | Description |
|--------|-------------------------|-------------|
| POST   | `/automatic_ai_scan`    | Takes a URL, extracts features, and runs AI models. |
| POST   | `/manual_ai_scan`       | Accepts URL features manually and runs AI models. |

### How It Works

1. The API extracts **key URL features** using the `utils.py` script:
   - Checks for **IP addresses in the domain**.
   - Detects **redirects, banking keywords, hidden fields, popups, and form submissions**.
   
2. The extracted features are passed to **Google BigQuery ML**, where different machine learning models make predictions.

3. The API returns the model predictions, indicating whether the URL is likely **phishing or legitimate**.

### Key Files

```
📁 api-branch/
📝 main.py  (FastAPI application entry point)
📝 utils.py  (Feature extraction for URLs)
📝 url_scan_router.py  (API router handling URL scans)
📝 url_scan_models.py  (Pydantic models for request validation)
📝 google_auth.py  (Google Cloud authentication setup)
```

---

## :three: Web-App Branch: Front-End & Flask Backend

The web application allows users to enter a URL and get phishing detection results from the API.

### **Technologies Used**
- **Flask** for backend processing.
- **HTML, CSS, JavaScript** for the front-end.
- **Fetch API** for communicating with the FastAPI backend.

### **How It Works**
1. **User enters a URL** in the front-end input field.
2. **JavaScript sends an API request** to the FastAPI service (`automatic_ai_scan`).
3. **API processes the URL and returns results**.
4. **Results are displayed** in the web interface.

### **Web Application UI**
- **User-friendly interface** with real-time response handling.
- **Simple and clean design** with a modern look.
- **CSS Styling** for responsiveness.

### **Key Files**
```
📁 web-app/
📝 app.py         (Flask backend)
📝 views.py       (Flask routing and rendering)
📝 index.html     (Front-end UI)
📝 index.js       (Fetch API and event handling)
📝 style.css      (Styling for the web page)
```
---

## Future Enhancements

- **Enhanced Model Training**: Adding reinforcement learning and additional phishing indicators.
- **Browser Extension**: Allow users to check URLs directly in their browser.
- **Dashboard & Reporting**: View statistics on phishing trends.
- **Live Threat Detection**: Monitor and flag newly registered phishing domains.

---

## Contributors

- **Synergeur** (Project Owner)

---

## License

This project is licensed under the **MIT License**.

