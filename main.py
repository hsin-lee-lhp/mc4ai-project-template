import streamlit as st
import pandas as pd
from dataframe import *
from graph import *
from tab0 import *
from tab1 import *
from tab2 import *
# from tab3 import *

st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')

tabs_titles = ('Danh sách',
               'Biểu đồ',
               'Phân nhóm',
               'Phân loại')
tabs = st.tabs(tabs_titles)

with tabs[0]:
    student_list()
      
with tabs[1]:
    tabs1_titles = ('Số lượng hs',
                    'Điểm')
    tabs1 = st.tabs(tabs1_titles)
    with tabs1[0]:
        bieu_do()
    with tabs1[1]:
        score()

with tabs[2]:
    kmeans()
'''
    with tabs[3]:
    regression()
    classify()
    data()
    '''








