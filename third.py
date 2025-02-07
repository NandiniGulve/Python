import numpy as np
import pandas
import streamlit as st


st.title("Welcome Everyon, we are learning pyhton")
st.write("Python requires practice")
data=pandas.DataFrame({'c1':[10,20,30,40],'c2':['A','B','C','D']})
st.write("Below is the data Table")
st.write(data)

chart_data=pandas.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.altair_chart(chart_data)
#st.write(chart_data)
