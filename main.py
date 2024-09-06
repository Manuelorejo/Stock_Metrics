# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:00:51 2024

@author: Oreoluwa
"""

#IMPORT STATEMENTS
import yfinance as yf
import streamlit as st
import datetime

st.header("STOCK METRICS VISUALIZATION")
st.write("This is a simple app that shows certain metrics of stocks over a period of time")




#Define the ticker symbol based on user input 
company = st.selectbox('Which stocks do you want to see',("Google","Apple","The Walt Disney Company","NVIDIA","Intel Corporation","META","Microsoft","Vanguard S&P 500 ETF","S&P 500"))

if company == 'Google':
    ticker = 'GOOGL'

elif company == 'Apple':
    ticker = 'AAPL'
    
elif company == 'The Walt Disney Company':
    ticker = 'DIS'
    
elif company == 'NVIDIA':
    ticker = 'NVDA'

elif company == 'Intel Corporation':
    ticker = 'INTC'

elif company == 'Vanguard S&P 500 ETF':
    ticker = 'VOO'

elif company == 'META':
    ticker = 'META'

elif company == 'S&P 500':
    ticker = '^GSPC'
    
elif company == 'Microsoft':
    ticker = 'MSFT'
    
    
    
    

#Get data on the ticker
tickerData = yf.Ticker(ticker)

#Select the range of dates based on user input
start = st.date_input("Select the start date of the plot", datetime.date(2014,9,6))
end = st.date_input("Select the end date of the plot",datetime.date(2024,9,6))

#Get the historical prices for this ticker based on the metrics selected by the user
tickerDf = tickerData.history(period ='1d',start = start, end = end)


st.write("Below are the close and volume metrics for ",company)
metrics = st.multiselect("What metrics do you want to visualize?", ['Close','Volume','Open','High','Low'])

if st.button("Check"):
    for metric in metrics:
        if metric == 'Close':
            st.title("Close")
            st.line_chart(tickerDf.Close)
            
        elif metric == 'Volume':
            st.title("Volume")
            st.line_chart(tickerDf.Volume)
            
        elif metric == 'Open':
            st.title("Open")
            st.line_chart(tickerDf.Open)
            
        elif metric == 'High':
            st.title("High")
            st.line_chart(tickerDf.High)
            
        elif metric == 'Low':
            st.title("Low")
            st.line_chart(tickerDf.Low)
        




