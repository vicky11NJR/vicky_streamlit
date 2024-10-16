import streamlit as st
import pandas as pd
st.title('🖥️_streamlit_learning')
st.write('hello all ')
data=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
data
