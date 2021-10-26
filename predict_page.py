import streamlit as st
import pickle 
import numpy as np 


def load_model():
    with open("rf_titanic_model.pkl", 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
rf_model = data["model"]


def prediction_page():
    ## in this function we will built our streamlit application 
    
    ## streamlit work as widgets
    st.write("")
    st.title("Survival  Prediction  of  Titanic- 1912 ")
    
    
    Embarked_tu = ('Southampton', 'Cherbourg', 'Queenstown')
    Class = ('First', 'Second', 'Third')
    Sex = ('Male', 'Female')
    
    p_class = st.selectbox('Passenger Class', Class)
    embarked = st.selectbox("Embarked", Embarked_tu)   ## hear whatever the value comes form ui that will be stored into Embarked_variable 
                                                       ## and in "Embarked" will print on GUI
    sex = st.radio("Sex", ("Male", "Female"))
    age = float(st.slider("Age", 0, 75, 5))  ## 0 to 75 and start value is 5
    sib_sp = st.number_input("Number of Siblings/Spouses OnBoard",value = 0, min_value = 0)
    parch = st.number_input("Number of Parents/Children OnBoard",value = 0, min_value = 0)
    fare = st.number_input("Fare", min_value = 0.00)
    
    user_data = st.button("Submit")
    
    if user_data:
        if sex == "Male":
            sex_val = 1
        else:
            sex_val = 0
        
        if p_class == "First":
            p_class_val = 1
        elif p_class == "Second":
            p_class_val = 2
        elif p_class == "Third":
            p_class_val = 3
        
        dic = {
            'Southampton':0, 
            'Cherbourg'  :1, 
            'Queenstown' :2 }
        
        embarked_val = dic[embarked]
        
        # order of our model's features is [Pclass	Sex	Age	SibSp	Parch	Fare	Embarked]
        X = np.array([ [p_class_val, sex_val, age, sib_sp, parch, fare, embarked_val] ])
        
        result = rf_model.predict(X)
        if result == 1:
            st.subheader("Survived")
            if sex == "Male":
                st.success("He did make it on to a lifeboat!")
            else:
                st.success("She did make it on to a lifeboat!")
            st.balloons()
        else:
            st.subheader("Not Survived")
            if sex == "Male":
                st.error("He did not make it on to a lifeboat!")
            else:
                st.error("She did make it on to a lifeboat!")
            
# prediction_page()

