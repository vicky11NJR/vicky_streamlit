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
# "","island","bill_length_mm","bill_depth_mm","flipper_length_mm","","sex
with st.expander('data visualization'):
  st.scatter_chart(data=df,x='bill_length_mm' ,y='body_mass_g' , color='species')

with st.sidebar:
  st.header('Input feature')
  island =st.selectbox('Island',('Biscoe','Dream','Torgesen'))
  
