import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv("US House Price .csv")



scale = MinMaxScaler()
last_month_data = df.groupby('Year').tail(1)
cols = ['Disposable income', 'population', 'Share Market',
         'construction cost', 'Unemployment Rate', 'Interest Rate', 'Mortgage Rate']

last_month_data[['Home Index','Disposable income','population', 'Share Market',
         'construction cost', 'Unemployment Rate', 'Interest Rate', 'Mortgage Rate'] ] = scale.fit_transform(last_month_data[['Home Index','Disposable income','population', 'Share Market',
         'construction cost', 'Unemployment Rate', 'Interest Rate', 'Mortgage Rate'] ])


with st.sidebar:
    st.header("Analyze Home Index with given filters")
    slct= st.selectbox("Select Columns ", cols)
    st.header("Links for data")
    st.text("1) Mortgage Price ")
    st.link_button(label="MortgageData",url="https://fred.stlouisfed.org/series/MORTGAGE30US")
    st.text("2) Population index ")
    st.link_button(label="Population Data",url="https://fred.stlouisfed.org/series/POPTHM")
    st.text("3) share price Willshare ")
    st.link_button(label="Share Data",url="https://fred.stlouisfed.org/series/WILL5000PR")
    st.text("4) House index price ")
    st.link_button(label="House Data",url="https://fred.stlouisfed.org/series/CSUSHPISA")
    st.text("5) Unemployment Rate ")
    st.link_button(label="Unemployment Data",url="https://fred.stlouisfed.org/series/UNEMPLOY")
    st.text(""" 6) Disposable Income 
    Disposable income is the price remaining in pocket of people after doing household expenses.""")
    st.link_button(label="Income Data",url="https://fred.stlouisfed.org/series/DSPIC96") 

    
st.header("Year Wise analyzation of Home price Index")
st.write("""Here, We can see that from 2002 to 2006 there is 44 % 
             but from 2006 to 2012 market is continuously 26 % down and 
             then from 2012 we can see a continuous growth of house index upto 113 % 
             and in last five years there is best ever growth of 50 % we can seẻ""")
plt.figure(figsize=(20, 8))
plt.bar(last_month_data["Year"],last_month_data["Home Index"],color="cyan")
plt.plot(last_month_data["Year"],last_month_data[slct],marker="x",color="red")
st.pyplot(plt)



if slct=='Disposable income':
    st.header(f"Correlation of Home index and Disposable Income is {df['Home Index'].corr(df[slct])}")
    st.text("""There is year on year growth in disposable income and it does not seem 
             there is no relation between Home price index and Disposable income""")

if slct == 'population':
    st.header(f""" {slct}
              Correlation of Home index and Population growth is {df['Home Index'].corr(df[slct])}""")
    st.write("""Population is growing with time and we can not seen any change in home index
              when population is increasing """)

if slct == 'Share Market':
    st.header(f""" {slct}
              Correlation of Home index and Share MArket is {df['Home Index'].corr(df[slct])}""")
    st.write("""We can see Share Market's up and down it is affecting the prices of
             Home according to plots and correlation is also high between this two """)


if slct == 'construction cost':
    st.header(f""" {slct}
              Correlation of Home index and Construction Cost is {df['Home Index'].corr(df[slct])}""")
    st.write("""There is high similarity and correlation between
              this two factors construction cost will affect home prices """)

if slct == 'Unemployment Rate':
    st.header(f""" {slct}
              Correlation of Home index and Unemployment is {df['Home Index'].corr(df[slct])}""")
    st.write(""" when unemployment rate is higher there is decrease in home prices """)
   
if slct == 'Interest Rate':
    st.header(f""" {slct}
              Correlation of Home index and Interest Rate is {df['Home Index'].corr(df[slct])}""")
    st.write("""Interest rate and home index are less correlated but have similar plot """)

if slct == 'Mortgage Rate':
    st.write("""Mortgage Rate is impacting the home prices as we can see in plot """)
    st.header(f""" {slct}
              Correlation of Home index and Mortgage Rate is {df['Home Index'].corr(df[slct])}""")

fig, ax = plt.subplots(figsize=(15, 6))
sns.heatmap(df[["Home Index",'Disposable income','population', 'Share Market',
         'construction cost', 'Unemployment Rate', 'Interest Rate', 'Mortgage Rate']].corr(),annot=True)
ax.set(ylabel='Over Years')
ax.set_title(f'{slct} Over Years')
st.pyplot(fig)





