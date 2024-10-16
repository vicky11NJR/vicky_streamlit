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
