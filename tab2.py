import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dataframe import *
from sklearn.cluster import KMeans
df = pd.read_csv('py4ai-score.csv')
def kmeans():
    df1 = df.iloc[:,4:16]
    n = st.slider('Số nhóm',min_value=2,max_value=5,step=1)

    kmeans = KMeans(n_clusters=n, n_init='auto')
    kmeans.fit(df1)
    df1['labels'] = kmeans.labels_
    df_clustered = df.copy()
    df_clustered['labels'] = kmeans.labels_

    fig = go.Figure(data=[go.Scatter3d(x=df1['S1'],y=df1['S2'],z=df1['GPA'],mode='markers', marker = dict(color=kmeans.labels_))])
    st.plotly_chart(fig)

    for i in range(1,n+1):
        df2 = df1[df1['labels'] == i-1]
        st.write('Nhóm',i,'GPA cao nhất:',df2['GPA'].max(),'thấp nhất:',df2['GPA'].min(),'trung bình:',round(df2['GPA'].mean(),1))
        df3 = (df_clustered[df_clustered['labels'] == i-1])
        st.dataframe(df3[['NAME','CLASS','GPA']])

