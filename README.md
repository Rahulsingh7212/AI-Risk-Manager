# 🛡️ AI Risk Manager

### Enterprise Fraud & Anomaly Detection System

---

## 📌 The Problem
Financial institutions lose billions of dollars globally due to fraudulent transactions. Traditional rule-based systems are slow, rigid, and often fail to adapt to new, sophisticated patterns of fraud, leading to massive financial and reputational damage.

## 💡 The Solution
**AI Risk Manager** is an intelligent, Machine Learning-powered web application designed to detect suspicious transactions instantly. By analyzing key data points (transaction amount, geographical distance, transaction frequency), the AI assigns a real-time **Risk Probability Score** to prevent fraud before it happens.

---

## ✨ Premium Features
*   **🔍 Real-Time Quick Check:** Instantly evaluate single transactions. Features a modern UI with a **Speedometer Gauge Chart** to visualize risk probability dynamically.
*   **📁 Enterprise Batch Audit:** Upload bulk transaction data via CSV for large-scale analysis. 
*   **🌌 Interactive Anomaly Clustering:** Utilizes `Plotly` to generate advanced scatter plots, visually isolating Safe (Green) vs. Fraudulent (Red) clusters based on amount and distance.
*   **📥 Downloadable Audit Reports:** Generates AI-evaluated risk reports that can be exported as CSV files for compliance and legal audits.
*   **⚡ Automated Action Triggers:** Categorizes risk into Safe, Medium, and High Risk, suggesting immediate actions like 'OTP Verification' or 'Transaction Block'.

---

## ⚙️ Tech Stack
*   **Core AI/ML:** Python, Scikit-Learn (Random Forest Classifier)
*   **Data Processing:** Pandas, NumPy
*   **Frontend / UI:** Streamlit
*   **Data Visualization:** Plotly (Graph Objects & Express)
*   **Model Deployment:** Joblib

---

## 🚀 How to Run the Project Locally

Follow these steps to test the project on your local machine:

**1. Clone the repository**
```bash
git clone [https://github.com/Rahulsingh7212/AI-Risk-Manager.git](https://github.com/Rahulsingh7212/AI-Risk-Manager.git)
cd AI-Risk-Manager

2. Install the required dependencies

pip install pandas scikit-learn numpy joblib streamlit plotly

3. Train the AI Model & Generate the .pkl file

python model_builder.py

4. Launch the Enterprise Dashboard

python -m streamlit run app.py

📊 Sample Data format for Batch Upload
If you want to test the Enterprise Batch Audit feature, upload a .csv file with the following exact column headers:

txn_amount (float/int)

distance_from_home (float/int)

time_since_last_txn (float/int)

Built for the Hackathon 2026 - Ready for the Industry.
