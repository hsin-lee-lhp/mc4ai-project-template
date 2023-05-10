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

