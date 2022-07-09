import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('rf.pkl', 'rb')
classifier= pickle.load(pickle_in)


def welcome():
    return 'welcome all'


# defining the function which will make the prediction using
# the data which the user inputs
# 'AGE','CUS_Month_Income','YEARS_WITH_US','total debit amount', 'total credit amount','total transactions','TAR_Desc'



    # Pre-processing user input
def prediction(AGE, CUS_Month_Income, Gender, CUS_Marital_Status, YEARS_WITH_US, total_debit_amount,
                   total_credit_amount,
                   total_transactions, TAR_Desc, CUS_Target):
    if Gender == "MALE":
        Gender = 1
    else:
        Gender = 0

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
        [[AGE, CUS_Month_Income,Gender, CUS_Marital_Status, YEARS_WITH_US, total_debit_amount, total_credit_amount,
          total_transactions, TAR_Desc, CUS_Target]])
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Churn Customer Prediction")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Predicting Churn Customer with ML App </h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction

    AGE = st.number_input("Age",  min_value=14, max_value=150)
    CUS_Marital_Status = st.selectbox("Marital Status", ('MARRIED', 'SINGLE', 'WIDOWED', 'DIVORCE', 'OTHER', 'PARTNER'))
    Gender= st.selectbox("Gender", ('FEMALE', 'MALE'))
    CUS_Month_Income = st.number_input("Monthly income",min_value=0.0)
    YEARS_WITH_US = st.number_input("Years with us", min_value=0)
    total_debit_amount = st.number_input("total debit amount",min_value=0.0)
    total_credit_amount = st.number_input("total credit amount", min_value=0.0)
    total_transactions = st.number_input("Total Transcations", min_value=0)
    TAR_Desc = st.selectbox("TAR Descrption", ('EXECUTIVE', 'LOW', 'MIDDLE', 'PLATINUM'))
    CUS_Target = st.text_input("CUS Target", "Type Here")
    result = ""


    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(AGE, CUS_Month_Income,Gender, CUS_Marital_Status, YEARS_WITH_US, total_debit_amount,
                            total_credit_amount, total_transactions, TAR_Desc, CUS_Target)
        if result==1:
            result='ACTIVE'
        else:
            result='Churn'
    st.success('Customer is {}'.format(result))


if __name__ == '__main__':
    main()