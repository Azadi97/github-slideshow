import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

cases = df[df['location'] == 'Afghanistan']['new_cases']
dates = df[df['location'] == 'Afghanistan']['date']

# Create a figure
fig = plt.figure()
plt.plot(dates, cases)

# Plots the chart
st.plotly_chart(fig)

#----------------------------------------------
# # MultySelector goes here
# # Get the countries list
clist = df['location'].unique()

# Create the streamlit sidebar
# country = st.sidebar.selectbox("Select a country:",clist)
country = st.sidebar.multiselect("Select countries:",clist)

# The header of the figure
st.header("COVID-19 cases per country - Multy Countries")

cases = df[df['location'] == country]['new_cases']
dates = list(df[df['location'] == country]['date'])

# Create a figure
fig = plt.figure()

# plt.figure(figsize=(12,5))
plt.plot(dates, cases)

# Plots the chart
st.plotly_chart(fig)

