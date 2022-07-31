import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error

#define explore coding
def show_samples (X, y, axis=[0,15000000,0,1500000]): 
    fig = plt.figure(figsize=(8, 6))
    plt.plot(X, y, 'b.', markersize=12,label='samples')
    plt.xlabel ('$TotalEnergy(kJ)$', fontsize=18) 
    plt.ylabel('$Views$', fontsize=18)
    plt.axis(axis)
    plt.legend(loc='best')
    st.plotly_chart(fig)
    
class MyLinearRegression :

    def __init__(self, theta = None): 
        self.theta = np.array(theta)
        
    def fit(self, X, y):
        m, n = X.shape
        Xo= np.hstack((np.ones((m,1)),X))
        self.theta =np.linalg.pinv(Xo.T.dot(Xo)).dot(Xo.T.dot(y))
        
    def predict(self, X):
        m,n=X.shape
        Xo=np.hstack((np.ones((m,1)),X)) 
        h=Xo.dot(self.theta)
        return h

def RMSE(y_true, y_pred):
    rmse=np.sqrt(np.mean((y_true-y_pred)**2))
    return rmse

@st.cache #cache the data, no need execute everytime
def load_data():
    youtube=pd.read_csv("YoutubeDataset.csv")
    X = youtube[['Views']].values
    y = youtube ['Total_Energy(kJ)'].values
    return X,y

X,y = load_data()

#define page
def show_predict_page():
    st.title("Youtube Energy Estimate Page")

    st.write("""### Welcome""")
    
    # Find optimal
    mylinreg = MyLinearRegression()
    mylinreg.fit(X, y)

    # Show the learnt model
    h_pred = mylinreg.predict(X)
    st.markdown(f"""Linear Regression model trained : RMSE={RMSE(y, h_pred).2f}""")
    st.success('Model trained successfully')
	
    # Visualize the result
    Xtest = np.linspace(0, 15000000, 100).reshape(-1, 1) 
    h_pred = mylinreg.predict(Xtest)
    show_samples(X, y)
    plt.plot (Xtest, h_pred, 'r-', label = 'model (MyLinearRegression)') 
    plt.legend()
    #plt.show()
    
show_predict_page()
