import csv
import pandas as pd
import plotly.express as px
import streamlit as st

_path='file/py4ai-score.csv'
df = pd.read_csv(_path)
df = pd.DataFrame(df)
def in_df(_path):
    print(pd.read_csv(_path))
def nam_nu(df):
    nn=df["GENDER"]
    nam=[]
    nu=[]
    for i in nn:
        if i == 'F':
            nu.append(i)
        else:
            nam.append(i)
    nu1=len(nu)
    nam1=len(nam)
    if nam1>nu1:
        print("Nam hứng thú với AI hơn")
    else:
        print("Nữ hứng thú với AI hơn")
    return nn
def graph_n_n(df):
    fig = px.pie(df, names = "GENDER",title="Số hs nam nữ")
    st.plotly_chart(fig)
def sang_chieu(df):
    sc=df['PYTHON-CLASS']
    sang=[]
    chieu=[]
    for j in sc:
        if j == "114-C" or j == "115-C":
            sang.append(j)
        else:
            chieu.append(j)
    if len(sang)>len(chieu):
        print("Học sinh chọn học AI vào buổi sáng nhiều hơn")
    else:
        print("Học sinh chọn học AI vào buổi chiều nhiều hơn")
def graph_s_c(df):
    fig = px.histogram(df,x="GENDER",y="CLASS")
    st.plotly_chart(fig)
def chuyen_thuong(df):
    ct=df['CLASS']
    chuyen=[]
    thuong=[]
    for n in ct:
        if n[2]=="C":
            chuyen.append(n)
        else:
            thuong.append(n)
    if len(chuyen)>len(thuong):
        print("Học sinh lớp chuyên có hứng thú với AI hơn")
    else:
        print("Học sinh lớp thường, tích hợp, song ngữ có hứng thú với AI hơn")
def graph_c_t(df):
    fig = px.pie(df, names = "CLASS",title="Phân bố học sinh lớp chuyên - thường")
    st.plotly_chart(fig)
def lop_muoi(df):
    m_mh=df['CLASS']
    muoi=[]
    mm_mh=[]
    for n in m_mh:
        if n[1]=="0":
            muoi.append(n)
        else:
            mm_mh.append(n)
    if len(muoi)>len(mm_mh):
        print("Học sinh lớp 10 có hứng thú với AI hơn")
    else:
        print("Học sinh lớp 11, 12 có hứng thú với AI hơn")
def graph_lop_muoi(df):
    fig = px.pie(df, names = "CLASS",title="Phân bố học sinh lớp 10 - 11 - 12")
    st.plotly_chart(fig)
