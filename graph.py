import plotly.express as px
import pandas as pd
import streamlit as st
from dataframe import df

def box(df,x,y,color):
    fig = px.box(df, x= x, y = y,color=color)
    st.plotly_chart(fig)

def histogram(df,x,y,color):
    fig = px.histogram(df, x=x, y = y,color=color)
    st.plotly_chart(fig)

def pie(df,x,title):
    fig = px.pie(df, names = x,title=title )
    st.plotly_chart(fig)
