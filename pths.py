
import pandas as pd
import plotly.express as px
import streamlit as st
from dataframe import *
def dtf():
    df = pd.read_csv('py4ai-score.csv')
    df['S1'].fillna(0, inplace=True)  
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
    df['REG-MC4AI'].fillna('N', inplace=True)  

    class_mapping = {
            '10CT1': 'Chuyên Toán',
            '10CT2': 'Chuyên Toán',
            '11CT1': 'Chuyên Toán',
            '11CT2': 'Chuyên Toán',
            '11CT3': 'Chuyên Toán',
            '10CTIN': 'Chuyên Tin',
            '10CL1': 'Chuyên Lý',
            '10CL2': 'Chuyên Lý',
            '10CA1': 'Chuyên Anh',
            '10CA2': 'Chuyên Anh',
            '11CA3': 'Chuyên Anh',
            '10CV1': 'Chuyên Văn',
            '10CV2': 'Chuyên Văn',
            '10CSD': 'Chuyên Sử Địa',
            '11CSD': 'Chuyên Sử Địa',
            '10TH1': 'Tích Hợp',
            '10TH2': 'Tích Hợp',
            '10SN': 'Song Ngữ',
            '10CH2': 'Chuyên Hóa',
            '12CH1': 'Chuyên Hóa',
            '10CTRN': 'Chuyên Trung Nhật',
            '10A1': 'Lớp thường',
            '10A2': 'Lớp thường',
            '10A3': 'Lớp thường',
            '11A': 'Lớp thường',
            '11B': 'Lớp thường',

        }

    df['CLASS-GROUP'] = df['CLASS'].map(class_mapping)


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
        st.write("Học sinh lớp 10 hứng thú với AI hơn")
