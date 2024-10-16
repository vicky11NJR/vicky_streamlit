import streamlit as st
import pandas as pd
st.title('🖥️_streamlit_learning')
st.write('hello all ')
with st.expander('data'):
  st.write('**rathish**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('X')
  x = df.drop('species',axis=1)
  x

  st.write('Y')
  y = df.species
  y
# "","island","","bill_depth_mm","flipper_length_mm","","sex
with st.expander('data visualization'):
  st.scatter_chart(data=df,x='bill_length_mm' ,y='body_mass_g' , color='species')

with st.sidebar:
  st.header('Input feature')
  island =st.selectbox('Island',('Biscoe','Dream','Torgesen'))
  gender =st.selectbox('Gender',('Male','Female'))
  bill_length_mm= st.slider('Bill length (mm)',32.1,59.6,43,9)
  bill_depth_mm=st.slider('Bill depth (mm)', 13.1,21.5,17.2)
  flipper_length_mm =st.slider('Flipper_length (mm)'173.0,231.0,201.0)
  body_mass_g =st.slider('Body mass (g)',2700.0,6300.0,4207.0)
