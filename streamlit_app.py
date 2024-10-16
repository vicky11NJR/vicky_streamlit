import streamlit as st
import pandas as pd
st.title('🖥️_streamlit_learning')
st.write('hello all ')
with st.expander('data'):
  st.write('**rathish**')
  data=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  data

  st.write('X')
  x = data.drop('species',axis=1)
  x

  st.write('Y')
  y = data.species
  y
