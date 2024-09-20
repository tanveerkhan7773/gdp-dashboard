import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.title('Hello world')

st.write('*Data Science Course 2024*')
file_path='data/BastarCraton.csv'
df = pd.read_csv('data/Bastar Craton.csv')
cat_names = df.columns.tolist()[27:]
st.title('Hello world')
el1 = st.selectbox('select element', cat_names = 
  )
st.write (el1)
with col1;
st.dataframe(df)
st.write(el1)

with col2:
    el2