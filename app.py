import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

# 1. Page Configuration (Wide layout for a dashboard feel)
st.set_page_config(page_title="AI Risk Manager", page_icon="🛡️", layout="wide")

# Custom CSS for Modern Buttons and UI
st.markdown("""
<style>
div.stButton > button:first-child {
    border-radius: 8px;
    transition: 0.3s;
    border: 1px solid #ff4b4b;
}
div.stButton > button:first-child:hover {
    transform: scale(1.02);
    box-shadow: 0 4px 8px rgba(255, 75, 75, 0.2);
}
</style>
""", unsafe_allow_html=True)

# 2. Load Model
@st.cache_resource
def load_model():
    return joblib.load('risk_model.pkl')

model = load_model()

# Header
st.title("🛡️ AI Risk Manager")
st.markdown("### Enterprise Fraud & Anomaly Detection System")
st.markdown("---")

# 3. MODERN TABS LAYOUT
tab1, tab2 = st.tabs(["🔍 Real-Time Quick Check", "📁 Enterprise Batch Audit"])

# --- TAB 1: Single Transaction ---
with tab1:
    st.write("Enter transaction details below for instant AI risk evaluation.")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        txn_amount = st.number_input("Transaction Amount (₹)", min_value=0.0, value=500.0)
    with col2:
        distance = st.number_input("Distance from Home (km)", min_value=0.0, value=10.0)
    with col3:
        time_diff = st.number_input("Time since last txn (mins)", min_value=0.0, value=60.0)

    # Full width button
    if st.button("Analyze Transaction Risk", type="primary", use_container_width=True):
        input_data = pd.DataFrame({'txn_amount': [txn_amount], 'distance_from_home': [distance], 'time_since_last_txn': [time_diff]})
        probabilities = model.predict_proba(input_data)[0]
        risk_score = round(probabilities[1] * 100, 2)

        st.markdown("---")
        res_col1, res_col2 = st.columns([1, 1.2])
        
        with res_col1:
            st.subheader("Analysis Result")
            if risk_score > 70:
                st.error("🚨 HIGH RISK DETECTED: Potential Fraudulent Activity")
                st.write("**Action Taken:** Transaction Blocked. Alert sent to security team.")
            elif risk_score > 40:
                st.warning("⚠️ MEDIUM RISK: Suspicious Activity")
                st.write("**Action Taken:** Step-up authentication required (OTP Sent).")
            else:
                st.success("✅ LOW RISK: Safe Transaction")
                st.write("**Action Taken:** Transaction Approved Successfully.")
                
        with res_col2:
            # MODERN FEATURE 1: Speedometer Gauge Chart
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = risk_score,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "AI Risk Probability (%)", 'font': {'size': 20}},
                gauge = {
                    'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
                    'bar': {'color': "black"},
                    'steps': [
                        {'range': [0, 40], 'color': "#09ab3b"},  # Green
                        {'range': [40, 70], 'color': "#faca2b"}, # Yellow
                        {'range': [70, 100], 'color': "#ff2b2b"}] # Red
                }
            ))
            fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: Batch Processing ---
with tab2:
    st.subheader("📁 Enterprise Batch Processing & Analytics")
    uploaded_file = st.file_uploader("Upload CSV file (Columns: txn_amount, distance_from_home, time_since_last_txn)", type=["csv"])

    if uploaded_file is not None:
        try:
            bulk_data = pd.read_csv(uploaded_file)
            features = bulk_data[['txn_amount', 'distance_from_home', 'time_since_last_txn']]
            bulk_probs = model.predict_proba(features)[:, 1]
            
            bulk_data['Risk_Score'] = (bulk_probs * 100).round(2)
            bulk_data['Status'] = bulk_data['Risk_Score'].apply(lambda x: '🚨 High Risk' if x > 70 else ('⚠️ Medium' if x > 40 else '✅ Safe'))
            
            colA, colB, colC = st.columns(3)
            colA.metric("Total Transactions Processed", len(bulk_data))
            colB.metric("High Risk Anomalies", len(bulk_data[bulk_data['Status'] == '🚨 High Risk']), delta_color="inverse") 
            colC.metric("Safe Transactions", len(bulk_data[bulk_data['Status'] == '✅ Safe']))
            
            st.markdown("---")
            st.write("### 🌌 Fraud Clustering Analysis")
            
            # MODERN FEATURE 2: Interactive Plotly Scatter Chart
            fig_scatter = px.scatter(
                bulk_data, x="txn_amount", y="distance_from_home", color="Status",
                color_discrete_map={'🚨 High Risk': 'red', '⚠️ Medium': 'orange', '✅ Safe': 'green'},
                hover_data=['Risk_Score', 'time_since_last_txn'],
                title="Transaction Amount vs Location Distance"
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

            st.write("### 📊 Complete Audit Report")
            st.dataframe(bulk_data, use_container_width=True)
            
            csv = bulk_data.to_csv(index=False).encode('utf-8')
            st.download_button(label="📥 Download Risk Audit Report (CSV)", data=csv, file_name='risk_audit.csv', mime='text/csv', type="primary")
            
        except Exception as e:
            st.error(f"Error processing file. Please ensure column names are exact. Detail: {e}")