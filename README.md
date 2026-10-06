# ⚡ Combined Cycle Power Plant Power Output Prediction

## 📌 Project Overview

This project develops an **end-to-end Machine Learning system** to predict the electrical power output of a Combined Cycle Power Plant (CCPP).

The system uses operational and environmental parameters to predict the **Net Electrical Energy Output (PE)** of the power plant.

The project covers the complete Machine Learning lifecycle:

* Data quality analysis
* Exploratory Data Analysis (EDA)
* Data preprocessing
* Outlier investigation
* Feature analysis
* Model comparison
* Hyperparameter tuning
* Model evaluation
* Model serialization
* Flask-based web deployment

The final trained Machine Learning model is integrated into a simple web application where users can enter plant operating conditions and receive a predicted power output.

---

## 🎯 Problem Statement

Combined Cycle Power Plants operate under varying environmental conditions. Changes in ambient temperature, atmospheric pressure, exhaust vacuum, and relative humidity can affect the plant's electrical power output.

The objective of this project is to build a Machine Learning regression model that can predict the plant's net electrical energy output based on these operating conditions.

### Input Features

| Feature | Description         | Unit  |
| ------- | ------------------- | ----- |
| AT      | Ambient Temperature | °C    |
| V       | Exhaust Vacuum      | cm Hg |
| AP      | Ambient Pressure    | mbar  |
| RH      | Relative Humidity   | %     |

### Target Variable

| Variable | Description                  | Unit |
| -------- | ---------------------------- | ---- |
| PE       | Net Electrical Energy Output | MW   |

---

## 📊 Dataset

The project uses the **Combined Cycle Power Plant dataset**, which contains measurements collected from a power plant under different operating conditions.

The dataset contains four input variables:

```text
AT
V
AP
RH
```

and one target variable:

```text
PE
```

---

## 🔍 Data Quality Analysis

Before model development, the dataset was investigated to identify potential data quality issues.

The following checks were performed:

### Missing Values

The dataset was checked for missing/null values.

```python
df.isnull().sum()
```

No significant missing-value problem was identified.

### Duplicate Records

Duplicate rows were investigated using:

```python
df.duplicated().sum()
```

Duplicate records were handled before model development where required.

### Invalid Values

The numerical variables were examined for unrealistic or invalid values.

### Outlier Analysis

The Interquartile Range (IQR) method was used to identify potential outliers.

The analysis showed that most observations were within the expected operating range.

Outliers were primarily detected in:

* Ambient Pressure (AP)
* Relative Humidity (RH)

Because these observations represent a very small proportion of the dataset and may correspond to legitimate operating conditions, they were **retained rather than automatically removed**.

This avoids losing potentially useful information about plant behavior under different environmental conditions.

---

## 📈 Exploratory Data Analysis

Several exploratory analyses were performed to understand the relationships between the variables.

### Analyses performed

* Distribution analysis
* Boxplots
* Correlation analysis
* Feature-target relationships
* Scatter plots
* Feature importance analysis

The correlation analysis showed that the environmental and operating variables have meaningful relationships with power output.

In particular, **Ambient Temperature (AT)** has a strong relationship with the plant's electrical power output.

---

## 🧹 Data Preprocessing

The dataset contains only numerical features.

Therefore:

* Categorical encoding was **not required**.
* Missing-value checks were performed.
* Duplicate records were investigated.
* Outliers were analyzed.
* Numerical features were standardized where required by the ML pipeline.

The final feature set used for prediction is:

```python
FEATURES = ["AT", "V", "AP", "RH"]
```

---

## 🧪 Train-Test Split

The dataset was divided into training and testing sets.

```text
Training Data: 80%
Testing Data: 20%
```

A fixed random state was used to ensure reproducibility.

---

## 🤖 Machine Learning Models

Multiple regression algorithms were evaluated to identify the most suitable model.

The following models were considered:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree Regressor
5. Random Forest Regressor
6. Gradient Boosting Regressor
7. Support Vector Regression (SVR)

Each model was evaluated using appropriate regression metrics.

---

## 📏 Evaluation Metrics

The following metrics were used:

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted power output.

Lower MAE indicates better performance.

### Root Mean Squared Error (RMSE)

RMSE penalizes larger prediction errors more strongly.

Lower RMSE indicates better performance.

### R² Score

R² measures how much of the variation in the target variable is explained by the model.

A value closer to 1 indicates better predictive performance.

---

## 🌲 Final Model

After comparing the candidate models, the **Random Forest Regressor** was selected as the final model based on its predictive performance.

Hyperparameter tuning was performed using `GridSearchCV`.

The final model was implemented as a complete Scikit-learn pipeline containing preprocessing and the trained model.

This approach ensures that the same preprocessing is automatically applied during both training and prediction.

---

## ⚙️ Hyperparameter Tuning

GridSearchCV was used to search for suitable Random Forest parameters.

Parameters investigated included:

```text
n_estimators
max_depth
min_samples_split
```

Example search space:

```python
param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [10, 15, None],
    "model__min_samples_split": [2, 5]
}
```

Cross-validation was used during hyperparameter selection to reduce the risk of choosing parameters based only on one train-test split.

---

## 💾 Model Saving

The final trained pipeline was saved using Joblib:

```python
joblib.dump(
    final_model,
    "models/power_output_prediction_model.pkl"
)
```

The complete pipeline is saved so that the web application can directly load it and perform predictions.

---

## 🌐 Web Application

A lightweight web application was developed using **Flask**.

The application allows users to enter:

* Ambient Temperature
* Exhaust Vacuum
* Ambient Pressure
* Relative Humidity

The Flask backend passes these values to the trained Machine Learning pipeline and returns the predicted power output.

### Application Flow

```text
User
  │
  ▼
HTML Web Interface
  │
  ▼
Flask Backend
  │
  ▼
Saved ML Pipeline
  │
  ▼
Power Output Prediction
  │
  ▼
Result displayed to User
```

---

## 🖥️ Running the Application

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd CCPP-ML-Project
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the Flask application

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000/
```

Open the address in a web browser.

---

## 📁 Project Structure

```text
CCPP-ML-Project/
│
├── data/
│   └── CCPP_data.csv
│
├── models/
│   └── power_output_prediction_model.pkl
│
├── outputs/
│   ├── model_comparison.csv
│   ├── final_metrics.csv
│   ├── feature_importance.csv
│   ├── correlation_heatmap.png
│   ├── actual_vs_predicted.png
│   ├── residual_plot.png
│   └── feature_importance.png
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Business Interpretation

The prediction system can help power plant operators estimate expected electrical power output based on current environmental and operating conditions.

Potential business applications include:

* Power generation forecasting
* Operational planning
* Performance monitoring
* Early identification of unusual operating conditions
* Supporting energy management decisions
* Improving understanding of environmental effects on plant output

For example, if environmental conditions indicate that the plant is likely to produce lower output, operators can use the prediction as an additional input when planning generation and maintenance activities.

---

## 💡 Key Findings

The project demonstrates that Machine Learning can effectively model the relationship between environmental operating conditions and power generation.

Important observations include:

* Ambient conditions have a significant effect on power output.
* Ambient Temperature is an important predictive feature.
* Tree-based ensemble models provide strong predictive performance.
* Random Forest was selected as the final model after model comparison and tuning.
* Keeping the complete preprocessing and prediction pipeline together makes deployment more reliable.

---

## ⚠️ Limitations

This model is intended as a predictive analytics demonstration and should not be treated as the sole decision-making system for real-world power plant operations.

The model's predictions depend on:

* Quality of input measurements
* Similarity between new operating conditions and training data
* Dataset coverage
* Model assumptions

Real-world deployment would require continuous monitoring, model validation, and retraining using updated plant data.

---

## 🚀 Future Improvements

Possible future improvements include:

* Real-time sensor integration
* Real-time power generation monitoring
* Automated model retraining
* Cloud deployment
* IoT integration
* Dashboard with historical predictions
* Prediction confidence/error analysis
* Model monitoring and drift detection
* Additional operational variables
* Advanced ensemble and boosting techniques

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Model Persistence

* Joblib

### Web Development

* Flask
* HTML
* CSS
* JavaScript

### Development Environment

* Jupyter Notebook / Google Colab
* Visual Studio Code

---

## 📌 Conclusion

This project implements an end-to-end Machine Learning solution for predicting Combined Cycle Power Plant electrical power output.

The workflow covers the complete process from **data quality investigation and exploratory analysis to model development, evaluation, serialization, and web deployment**.

The final system provides a simple interface through which users can enter operating conditions and obtain an estimated electrical power output.

The project demonstrates how Machine Learning can be integrated with a web application to transform a predictive model into a practical decision-support tool.

---

## 👨‍💻 Author

**Pravin**

Machine Learning / Data Science Project

---

## 📜 Disclaimer

This application provides **predicted power output based on a trained Machine Learning model**. The prediction should be considered an analytical estimate and not a guaranteed measurement of actual plant output.
