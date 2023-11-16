import streamlit as st
import eda
import Machine_learn


navigation = st.sidebar.selectbox('Choose page:',('EDA','Online shoppers prediction'))

if navigation == 'EDA':
    eda.run()

else:
    Machine_learn.run()