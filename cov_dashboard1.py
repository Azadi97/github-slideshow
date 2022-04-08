import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

cases = df[df['location'] == 'Afghanistan']['new_cases']
dates = df[df['location'] == 'Afghanistan']['date']

plt.plot(dates, cases)
