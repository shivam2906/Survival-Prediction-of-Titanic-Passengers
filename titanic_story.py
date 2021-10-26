import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache
def load_data():
    df = pd.read_csv("Titanic.csv")
    return df

df = load_data()

def titanic_story_page():
    st.title("     Story  of  Titanic - 1912 ")

    st.image('titanic_ship.jpg', width=650)

    st.markdown(""" The **RMS Titanic**, a luxury steamship, sank in the early hours of April 15, 1912, off the coast of Newfoundland in 
                the North Atlantic after sideswiping an iceberg during its maiden voyage. Of the 2,240 passengers and crew on board, 
                more than 1,500 lost their lives in the disaster. Titanic has inspired countless books, articles and films 
                (including the 1997 “Titanic” movie starring Kate Winslet and Leonardo DiCaprio), and the ships story has entered 
                the public consciousness as a cautionary tale about the perils of human hubris.""" )

    ## showing dataset
    st.subheader("Data Available")
    st.dataframe(df.head(10))
    
    st.subheader("Distribution of data into features through visualization.")
    ###
    fig, axis = plt.subplots(2,3, figsize=(12, 8))

    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

    sns.countplot(df['Pclass'], ax = axis[0,0])
    df['Pclass'].value_counts().plot(kind = "pie", autopct = "%.2f", ax = axis[0,1])
    sns.countplot(df['SibSp'], ax = axis[0,2])
    sns.countplot(df['Embarked'], ax = axis[1,0])
    df['Embarked'].value_counts().plot(kind = "pie", autopct = "%.2f", ax = axis[1,1])
    sns.countplot(df['Parch'], ax = axis[1,2])
    st.pyplot(fig)
    ###
    
    # visualizing the outliers 
    st.subheader("Outliers - through boxplot ")
    fig, axis = plt.subplots(1,2, figsize =(13,5) )

    sns.boxplot(df['Age'], ax = axis[0], color = "green")
    sns.boxplot(df["Fare"], ax = axis[1], color = "red")
    st.pyplot(fig)
    
    st.markdown(" *Fare $500 is potential outlier and some more* ")
    st.markdown(" * **Age Feature** we can observe 2 outliers in Age columns *")
    st.markdown(" *Age min value = 0.17 <br /> * Age max value = 76*" )
    
    ## target column 
    st.subheader("Distribution of target column - *Survival* ")
    fig, axis = plt.subplots(1,2, figsize=(7,4))

    sns.countplot(df["Survived"], ax = axis[0])
    df['Survived'].value_counts().plot(kind = "pie", autopct ='%.2f', ax = axis[1])
    st.pyplot(fig)
    
    
    
    
    