import streamlit as st
import streamlit.components.v1 as stc
import pickle

with open('GBM_model.pkl', 'rb') as file:
    Multi_Class_Classification_Model = pickle.load(file)

html_temp = """ <div style="background-color:#000;padding:10px;border-radius:10px">
                <h1 style="color:#fff;text-align:center">Customer Segmentation Prediction App</h1>
                <h4 style="color:#fff;text-align:center">Project Six Final Project</h4>
                """

desc_temp = """ ### Customer Segmentation Prediction App
                This app is used by credit team for deciding Customer Segmentation Application
                
                ### Data Source
                Kaggle: Link <https://www.kaggle.com/datasets/kaushiksuresh147/customer-segmentation/data>
                """

profession_mapping = {
    'Artist': 0,
    'Doctor': 1,
    'Engineer': 2,
    'Entertainment': 3,
    'Executive': 4,
    'Healthcare': 5,
    'Homemaker': 6,
    'Marketing': 7,
    'Lawyer': 8
}

spending_mapping = {
    'Low' : 0,
    'Average' : 1,
    'High' : 2
}

var_1_mapping = {
    'Cat_1' : 0,
    'Cat_2' : 1,
    'Cat_3' : 2,
    'Cat_4' : 3,
    'Cat_5' : 4,
    'Cat_6' : 5,
    'Cat_7' : 6
}

label_mapping = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D'
}


def main():
    stc.html(html_temp)
    menu = ["Home", "Machine Learning App"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning App":
        run_ml_app()

def run_ml_app():
    design = """<div style="padding:15px;">
                    <h1 style="#fff;>Loan Eligibility Prediction</h1>
                </div>
            """
    st.markdown(design, unsafe_allow_html=True)
    left, right = st.columns((2,2))
    gender = left.selectbox('Gender', ('Male', 'Female'))
    married = right.selectbox('Married', ('Yes', 'No'))
    age = left.number_input('Customer Age')
    education = right.selectbox('Education', ('Graduate', 'Non-Graduate'))
    profession = left.selectbox('Customer Profession', list(profession_mapping.keys()))
    work_experience = right.number_input('Customer Work Experience')
    spending = left.selectbox('Spending', list(spending_mapping.keys()))
    family_size = right.number_input('Family Size')
    var_1  = st.selectbox('var_1', list(var_1_mapping.keys()))
    button = st.button("Predict")

    #If button is clicked
    if button:
        result = predict(gender, married, age, education, profession, work_experience, spending, family_size, var_1)

        st.success(f'Customer classified as {result} Segmentation')

def predict(gender, married, age, education, profession, work_experience, spending, family_size, var_1):
    # Process user input
    gen = 0 if gender == 'Male' else 1
    mar = 0 if married == 'Yes' else 1
    edu = 0 if education == "Graduate" else 1
    prof = profession_mapping[profession]
    spend = spending_mapping[spending]
    var1 = var_1_mapping[var_1]

    # Making prediction
    prediction = Multi_Class_Classification_Model.predict([[gen, mar, edu, age, prof, work_experience, spend, family_size, var1]])

    # Map the prediction to class labels
    prediction_label = label_mapping[prediction[0]]
    
    return prediction_label


if __name__ == "__main__":
    main()