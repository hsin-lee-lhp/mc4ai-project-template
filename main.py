import streamlit as st
import pandas as pd
from dataframe import df
from graph import box, histogram,pie
from tab0 import student_list
from tab1 import score

st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')


tabs_titles = ('Danh sách',
               'Biểu đồ',
               'Phân nhóm',
               'Phân loại')
tabs = st.tabs(tabs_titles)
def checkbox(a,b):
    if a:
        pass
    if b:
        pass
df2 = pd.DataFrame(columns = df.columns)
                
with tabs[0]:
    student_list()
    
    

    # COLS = df.columns.values.tolist().copy()
    # st.write(df[COLS[5]].value_counts())

    

    
    
with tabs[1]:
    tabs1_titles = ('Số lượng hs',
                    'Điểm')
    tabs1 = st.tabs(tabs1_titles)
    with tabs1[1]:
        score()

    
    
    


with tabs[2]:
    # temp_options = ('low','medium','high')
    # temp = st.select_slider('Temperature',options=temp_options)
    # st.write('The temperature is:',temp)

    number = st.slider('Số nhóm',min_value=1,max_value=5,step=1)









