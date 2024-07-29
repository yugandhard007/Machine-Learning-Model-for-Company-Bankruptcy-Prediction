
# importing required libraries
import pickle
import streamlit as st
# import joblib
from io import BytesIO
import requests
from io import BytesIO
import pickle
import base64
import joblib

import requests # or https

URI = 'https://github.com/Ninad2603/ML_Projects/raw/main/rf_1.pkl'
classifier = joblib.load(BytesIO(requests.get(URI).content))

# this is the main function in which we define our app
def main():
    # header of the page
    st.markdown("""
        <style>
        .yellow-box {
            border: 2px solid #ffcc00;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            background-color: #fff9e6;
        }
        h2 {
            color: #ffcc00;
            text-align: center;
        }
        </style>
        <div class="yellow-box">
            <h2>Company Bankruptcy Prediction</h2>
        </div>
        """, unsafe_allow_html=True)

    # 2. Loading the data
    # Create two columns
    col1, col2 = st.columns(2)

    # First column
    with col1:
        X9  = st.number_input("After-tax net Interest Rate")
        X11 = st.number_input("Continuous interest rate_(after tax)")
        X14 = st.number_input("Cash flow rate")
        X19 = st.number_input("Net Value Per Share (C)")
        X34 = st.number_input("Current Ratio")

    # Second column
    with col2:
        X36 = st.number_input("Interest Expense Ratio")
        X47 = st.number_input("Accounts Receivable Turnover")
        X49 = st.number_input("Inventory Turnover Rate (times)")
        X59 = st.number_input("Quick Assets/Current Liability")
        X95 = st.selectbox('Net Income Flag',("0","1"))

    result =""

    if st.button("Check"):
        result = prediction(X9, X11, X14, X19, X34, X36, X47, X49, X59, X95)
        st.success('The probability of bankruptcy is {}'.format(result))

# defining the function which will make the prediction using the data which the user inputs 
def prediction(X9, X11, X14, X19, X34, X36, X47, X49, X59, X95): 
    # Convert string inputs to the correct data type if necessary
    X95 = int(X95)  # Assuming 'Net Income Flag' should be an integer

    # Reshape the input data to match the model's expectations
    features = [[X9, X11, X14, X19, X34, X36, X47, X49, X59, X95]]
    
    # Make the prediction
    prediction_proba = classifier.predict_proba(features)
    
    # Get the probability of the positive class (Bankruptcy)
    probability_bankruptcy = prediction_proba[0, 1]

    # Convert probability to percentage
    confidence_percentage = round(probability_bankruptcy * 100, 2)

    return f"probability of the company getting bankrupt is {confidence_percentage}%"

if __name__=='__main__':
    main()
