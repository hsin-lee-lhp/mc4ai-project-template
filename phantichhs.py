import csv
import pandas as pd
import plotly.express as px
import streamlit as st

_path='file/py4ai-score.csv'
df = pd.read_csv(_path)
df = pd.DataFrame(df)
# def in_noi_dung(_path):
#     print(df)
# def kt_null(df):
#     s= df.isnull().sum()
#     print(s)
# def xoa_null(df):
#     df['S1'].fillna(0, inplace=True)
#     df['S2'].fillna(0, inplace=True)
#     df['S3'].fillna(0, inplace=True)
#     df['S4'].fillna(0, inplace=True)
#     df['S5'].fillna(0, inplace=True)
#     df['S6'].fillna(0, inplace=True)
#     df['S7'].fillna(0, inplace=True)
#     df['S8'].fillna(0, inplace=True)
#     df['S9'].fillna(0, inplace=True)
#     df['S10'].fillna(0, inplace=True)
#     df['S1'].fillna(0, inplace=True)
#     df['BONUS'].fillna(0, inplace=True)
#     df['REG-MC4AI'].fillna("UNKNOWN", inplace=True)
# def nam_nu(df):
#     nam = df[2] == "M"
#     nu=df[2] == "F"
#     print(df[nam])
#     print(df[nu])
#     if df[nam]>df[nu]:
#         print("Nam hứng thú với AI hơn")
#     else:
#         print("Nữ hứng thú với AI hơn")
#     px.pie(df, names='GENDER')
# def n_n(df):
#     for i in df:

# def nam_nu(df):
#     df1= df[(f["GENDER"] == "M") | (df['GENDER'] == "F")]
#     fig = px.histogram(df1, color='CLASS')
#     fig.show()
def sang_chieu(df):
    fig = px.histogram(df,x="GENDER",y="CLASS",color="PYTHON-CLASS")
    st.plotly_chart(fig)