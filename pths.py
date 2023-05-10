
import pandas as pd
import plotly.express as px
import streamlit as st
from dataframe.py import *
df = pd.read_csv('py4ai-score.csv')

''' df['S1'].fillna(0, inplace=True)  
df['S2'].fillna(0, inplace=True)  
df['S3'].fillna(0, inplace=True)  
df['S4'].fillna(0, inplace=True)  
df['S5'].fillna(0, inplace=True)  
df['S6'].fillna(0, inplace=True)  
df['S7'].fillna(0, inplace=True)  
df['S8'].fillna(0, inplace=True)  
df['S9'].fillna(0, inplace=True)  
df['S10'].fillna(0, inplace=True)  
df['BONUS'].fillna(0, inplace=True)  
df['REG-MC4AI'].fillna('N', inplace=True) '''

def pie(df,x,title):
    fig = px.pie(df, names = x,title=title )
    st.plotly_chart(fig)
def bieu_do():
    a_names = ('PHÂN BỐ HS NAM - NỮ','PHÂN BỐ HS LỚP SÁNG - CHIỀU','PHÂN BỐ HS CHUYÊN - THƯỜNG','PHÂN BỐ HS CÁC KHỐI')
    a = st.radio('Loại biểu đồ',a_names,horizontal=True)
    if a=='PHÂN BỐ HS NAM - NỮ':
        pie(df, df["GENDER"],"PHÂN BỐ HS NAM - NỮ")
        st.write('Nam hứng thú với AI hơn')
    if a=='PHÂN BỐ HS LỚP SÁNG - CHIỀU':
        pie(df, df["PYTHON-CLASS"],"PHÂN BỐ HS LỚP SÁNG CHIỀU")
        st.write('Học sinh thường chọn học AI vào buổi sáng')
    if a=='PHÂN BỐ HS CHUYÊN - THƯỜNG':
        pie(df, df["CLASS-GROUP"],"PHÂN BỐ HS CHUYÊN - THƯỜNG")
        st.write('Học sinh lớp chuyên có hứng thú với AI hơn')
    if a=='PHÂN BỐ HS CÁC KHỐI':
        pie(df, df["GRADE"],"PHÂN BỐ HS CÁC KHỐI")
        st.write("Học sinh lớp chuyên hứng thú với AI hơn")