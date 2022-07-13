#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import pickle
import streamlit as st


# loading in the model to predict on the data
classifier= pickle.load(open('rf.pkl', 'rb'))


def welcome():
    return 'welcome all'


# defining the function which will make the prediction using
# the data which the user inputs
# 'AGE','CUS_Month_Income','YEARS_WITH_US','total debit amount', 'total credit amount','total transactions','TAR_Desc'



# Pre-processing user input
def prediction(AGE, CUS_Month_Income, CUS_Gender, CUS_Marital_Status, YEARS_WITH_US, total_debit_amount,
                   total_credit_amount,
                   total_transactions, CUS_Target, TAR_Desc):
    
    if CUS_Gender == "MALE":
        CUS_Gender = 1
    else:
        CUS_Gender = 0

    if CUS_Marital_Status == "MARRIED":
        CUS_Marital_Status = 0
    elif CUS_Marital_Status == "SINGLE":
        CUS_Marital_Status = 1
    elif CUS_Marital_Status == "WIDOWED":
        CUS_Marital_Status = 2
    elif CUS_Marital_Status == "DIVORCE":
        CUS_Marital_Status = 3
    elif CUS_Marital_Status == "OTHER":
        CUS_Marital_Status = 4
    else:
        CUS_Marital_Status = 5

    if TAR_Desc == "EXECUTIVE":
        TAR_Desc = 0
    elif TAR_Desc == "LOW":
        TAR_Desc = 1
    elif TAR_Desc == "MIDDLE":
        TAR_Desc = 2
    else:
        TAR_Desc = 3

    prediction = classifier.predict(
        [[AGE, CUS_Month_Income,CUS_Gender, CUS_Marital_Status, YEARS_WITH_US, total_debit_amount, total_credit_amount,
          total_transactions, CUS_Target, TAR_Desc]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Standard Bank-ML APP")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """    
    <h3 style ="color:white;"> Churn Customer Prediction and Recommendations </h3>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction

    AGE = st.number_input("Age",  min_value=14, max_value=150)
    CUS_Marital_Status = st.selectbox("Marital Status", ('MARRIED', 'SINGLE', 'WIDOWED', 'DIVORCE', 'OTHER', 'PARTNER'))
    CUS_Gender= st.selectbox("Gender", ('FEMALE', 'MALE'))
    CUS_Month_Income = st.number_input("Monthly income",min_value=0.0)
    YEARS_WITH_US = st.number_input("Years with us", min_value=0)
    total_debit_amount = st.number_input("total debit amount",min_value=0.0)
    total_credit_amount = st.number_input("total credit amount", min_value=0.0)
    total_transactions = st.number_input("Total Transcations", min_value=0)
    TAR_Desc = st.selectbox("TAR Descrption", ('EXECUTIVE', 'LOW', 'MIDDLE', 'PLATINUM'))
    CUS_Target = st.selectbox("CUS Target", ([2231, 2223, 2222, 2235, 2212, 2232, 2230, 2211, 2234, 2224, 2233,
       2236]))
    result = ""


    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(AGE, CUS_Month_Income,CUS_Gender, CUS_Marital_Status, YEARS_WITH_US, total_debit_amount,
                            total_credit_amount, total_transactions,CUS_Target, TAR_Desc)
      
        if result==0: #0 is active and 1 churn
            result='ACTIVE'
        else:
            result='Churn'
    st.success('Customer is {}'.format(result))


if __name__ == '__main__':
    main()


# In[ ]:




