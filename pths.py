
import pandas as pd
import plotly.express as px
import streamlit as st
from dataframe import df

def student():
    class_mapping1 = {
            '10CT1': 'Lớp 10',
            '10CT2': 'Lớp 10',
            '11CT1': 'Lớp 11',
            '11CT2': 'Lớp 11',
            '11CT3': 'Lớp 11',
            '10CTIN': 'Lớp 10',
            '10CL1': 'Lớp 10',
            '10CL2': 'Lớp 10',
            '10CA1': 'Lớp 10',
            '10CA2': 'Lớp 10',
            '11CA3': 'Lớp 11',
            '10CV1': 'Lớp 10',
            '10CV2': 'Lớp 10',
            '10CSD': 'Lớp 10',
            '11CSD': 'Lớp 11',
            '10TH1': 'Lớp 10',
            '10TH2': 'Lớp 10',
            '10SN': 'Lớp 10',
            '10CH2': 'Lớp 10',
            '12CH1': 'Lớp 12',
            '10CTRN': 'Lớp 10',
            '10A1': 'Lớp 10',
            '10A2': 'Lớp 10',
            '10A3': 'Lớp 10',
            '11A': 'Lớp 11',
            '11B': 'Lớp 11',

        }

    df['GRADE'] = df['CLASS'].map(class_mapping1)
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
