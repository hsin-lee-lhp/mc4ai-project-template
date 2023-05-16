import streamlit as st
from graph import box,histogram,pie
from dataframe import *
def score():                                
    s_names = ('S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','GPA')
    s = st.radio('Điểm từng session',s_names,horizontal=True)
    if s == 'S1':
        box(df,'CLASS-GROUP','S1','GENDER')
        histogram(df,'S1',None,'PYTHON-CLASS')
    
    if s == 'S2':
        box(df,'CLASS-GROUP','S2','GENDER')
        histogram(df,'S2',None,'PYTHON-CLASS')

    if s == 'S3':
        box(df,'CLASS-GROUP','S3','GENDER')
        histogram(df,'S3',None,'PYTHON-CLASS')    
    if s == 'S4':
        box(df,'CLASS-GROUP','S4','GENDER')
        histogram(df,'S4',None,'PYTHON-CLASS')

    if s == 'S5':
        box(df,'CLASS-GROUP','S5','GENDER')
        histogram(df,'S5',None,'PYTHON-CLASS')

    if s == 'S6':
        box(df,'CLASS-GROUP','S6','GENDER')
        histogram(df,'S6',None,'PYTHON-CLASS')

    if s == 'S7':
        box(df,'CLASS-GROUP','S7','GENDER')
        histogram(df,'S7',None,'PYTHON-CLASS')    

    if s == 'S8':
        box(df,'CLASS-GROUP','S8','GENDER')
        histogram(df,'S8',None,'PYTHON-CLASS')   

    if s == 'S9':
        box(df,'CLASS-GROUP','S9','GENDER')
        histogram(df,'S9',None,'PYTHON-CLASS')    

    if s == 'S10':
        box(df,'CLASS-GROUP','S10','GENDER')
        histogram(df,'S10',None,'PYTHON-CLASS')  

    if s == 'GPA':
        box(df,'CLASS-GROUP','GPA',None)
        histogram(df,'GPA',None,'PYTHON-CLASS')
        histogram(df,'GPA',None,'GENDER')
        pie(df[df['GPA'] >= 6],'CLASS-GROUP','Tỉ lệ đậu lớp MC')
      
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
