import streamlit as st
import pandas as pd

st.title('Fong Clinical Risk Score for Colorectal Cancer Recurrence')

st.write('''
This application calculates the Fong Clinical Risk Score for predicting the risk of colorectal cancer recurrence after hepatic resection for metastatic colorectal cancer.
''')

# Input fields
node_positive_primary = st.selectbox("Is the primary node-positive?", ["No", "Yes"])
disease_free_interval = st.selectbox("Is the disease-free interval from the primary to liver metastases less than 12 months?", ["No", "Yes"])
more_than_one_liver_metastasis = st.selectbox("Are there more than one liver metastasis?", ["No", "Yes"])
largest_liver_metastasis = st.selectbox("Is the largest liver metastasis greater than 5 cm?", ["No", "Yes"])
cea_level = st.selectbox("Is the carcinoembryonic antigen level greater than 200 ng/mL?", ["No", "Yes"])

# Calculate Fong Score
fong_score = 0

if node_positive_primary == "Yes":
    fong_score += 1

if disease_free_interval == "Yes":
    fong_score += 1

if more_than_one_liver_metastasis == "Yes":
    fong_score += 1

if largest_liver_metastasis == "Yes":
    fong_score += 1

if cea_level == "Yes":
    fong_score += 1

st.write(f'Fong Clinical Risk Score: {fong_score}')
