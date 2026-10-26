import streamlit as st
import pandas as pd
import io

# 1. Configure page settings
st.set_page_config(
    page_title="TuitionPulse",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inject Mobile Viewport & PWA Head Tags for Chrome "Add to Home Screen"
st.markdown("""
    <head>
        <!-- Mobile Viewport Optimization -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        
        <!-- Web App Capable for Chrome & Mobile Browsers -->
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="theme-color" content="#0E1117">
        <meta name="application-name" content="TuitionPulse">
        <meta name="apple-mobile-web-app-title" content="TuitionPulse">
    </head>
""", unsafe_allow_html=True)

# Application UI Header
st.title("⚡ TuitionPulse Access")

st.write("Welcome to TuitionPulse. Access your dashboard below:")

# Example Data for Download Feature
sample_data = pd.DataFrame({
    'Student ID': [101, 102, 103],
    'Name': ['Rahul Sharma', 'Priya Patel', 'Amit Verma'],
    'Status': ['Paid', 'Pending', 'Paid']
})

st.dataframe(sample_data, use_container_width=True)

# 3. Built-in Streamlit Download Button (Works natively in Mobile Chrome)
st.subheader("📥 Download Section")

# CSV Download
csv_data = sample_data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Student Report (CSV)",
    data=csv_data,
    file_name="tuitionpulse_report.csv",
    mime="text/csv",
    use_container_width=True
)

# Text or Document Download Example
sample_text = "TuitionPulse Summary Report\nGenerated successfully."
st.download_button(
    label="Download Summary (TXT)",
    data=sample_text,
    file_name="tuitionpulse_summary.txt",
    mime="text/plain",
    use_container_width=True
)
