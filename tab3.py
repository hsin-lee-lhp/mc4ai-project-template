import pandas as pd
import numpy as np
import plotly.graph_objects as go
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Input
from tensorflow.random import set_seed
from tensorflow.keras.backend import clear_session
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from dataframe import *
import streamlit as st
dtf()
def regression():
    z = df["S10"].values
    y=df['S6'].values
    x=df['GPA'].values
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    X = x.reshape(-1,1)
    y=y.reshape(-1,1)
    model.fit(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
    model = LinearRegression() 
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    plt.scatter(X_test, y_test, color ='r')
    plt.plot(X_test, y_pred, color ='b')
    plt.xlabel('S10')
    plt.ylabel('S6')
    plt.show()


    fig = go.Figure(data=[go.Scatter3d(x=df['GPA'], y=df['S6'], z=df['S10'], mode='markers')])
    st.plotly_chart(fig)


X = df[['S1','S6','S10']].values
from sklearn.model_selection import train_test_split

def create_data():
    means = [[2, 2], [8, 3], [3, 6]]
    cov = [[1, 0], [0, 1]]
    N = 300
    X0 = np.random.multivariate_normal(means[0], cov, N)
    X1 = np.random.multivariate_normal(means[1], cov, N)
    X2 = np.random.multivariate_normal(means[2], cov, N)
    y0 = np.zeros(N)
    y1 = np.ones(N)
    y2 = np.ones(N)*2

    X = np.concatenate((X0, X1, X2), axis = 0)
    y = np.concatenate((y0, y1, y2), axis = 0)

    return X, y
def data():
    X, y = create_data()
    X.shape, y.shape
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    from tensorflow.keras.utils import to_categorical

    y_train_ohe = to_categorical(y_train, num_classes=3)
    y_test_ohe = to_categorical(y_test, num_classes=3)

    y_train.shape, y_train_ohe.shape

    clear_session()
    set_seed(42)

    model = Sequential()
    model.add(Input(shape=X_train.shape[1:]))
    model.add(Flatten())
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics='accuracy')
    model.summary()
    history = model.fit(X_train, y_train_ohe, epochs = 10, verbose=1)

    margin = 0.1
    x_min, x_max = X_train[:, 0].min() - margin, X_train[:, 0].max() + margin
    y_min, y_max = X_train[:, 1].min() - margin, X_train[:, 1].max() + margin
    xrange = np.linspace(x_min, x_max, 500)
    yrange = np.linspace(y_min, y_max, 500)
    xx, yy = np.meshgrid(xrange, yrange)

    y_pred = model.predict(np.c_[xx.ravel(), yy.ravel()])

    scatter = go.Scatter(x=X_train[:,0], y=X_train[:, 1], mode='markers',
                      marker=dict(size=7,color=y_train,# colorscale=colorscale,
                      ))

    surface = go.Contour(x=xrange,
                      y=yrange,
                      z=np.argmax(y_pred, axis=1).reshape(500, 500),
                      #  colorscale=colorscale,
                      showscale=False,
                      opacity=0.5
    )

    fig = go.Figure(data=[scatter, surface])
    fig.update_layout(title="Decision Boundary")
    st.plotly_chart(fig)
