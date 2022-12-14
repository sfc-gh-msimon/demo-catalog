import pandas as pd
import numpy as np
from datetime import datetime
import statsmodels as stats
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from pandas.tseries.offsets import DateOffset
import streamlit as st
import altair as alt
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import avg, sum, col, to_date
import string


#set the page icon and title - use wide mode so the chart can strech out over the page 
st.set_page_config(page_title="Predictive Sales Forecast", page_icon="⚛️", layout="wide")

st.header("Predictive Sales Model")

st.markdown("""##### This application uses Snowpark to natively run a Python Machine Learning Model to predict forward looking sales. \
It uses the SARIMAX algorithm from statsmodel.""")
st.markdown("###### You can use the slidebar to select the number of days to predict.")

#allows tooltips in the expanded view
st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>', unsafe_allow_html=True)

## Create a Snowpark session
@st.cache
def create_session_object():
    connection_parameters = {
      "account":    string.sf_account,
      "user":       string.sf_user,
      "password":   string.sf_password,
      "role":       string.sf_role,
      "warehouse":  string.sf_warehouse,
      "database":   string.sf_database,
      "schema":     string.sf_schema
    }

    session = Session.builder.configs(connection_parameters).create()
   
    ## use snowpark to get sum of all invoices by date to get total sales by date 
    #invoice table - select invoice_id and invoice_date 
    df_invoice = session.table('INVOICES').select(col("INVOICE_ID"), to_date(col("INVOICE_DATE")).alias("INVOICE_DATE")).filter(col("INVOICE_DATE") <= '2022-07-18')
    #invoice lines table - select invoice_id and item_price
    df_inv_lines = session.table('INVOICE_LINES').select(col("INVOICE_ID"), col("ITEM_PRICE"))
    #join invoices and invoice lines on invoice_id 
    df_inv_and_lines = df_invoice.join(df_inv_lines, df_inv_lines.col("INVOICE_ID") == df_invoice.col("INVOICE_ID"))
    #sum item prices by date
    df_inv_and_lines = df_inv_and_lines.group_by('INVOICE_DATE').agg(sum('ITEM_PRICE').cast("float").alias("ITEM_PRICE")).sort("INVOICE_DATE")
    
    #convert Snowflake Dataframe to pandas Dataframe so we can use generic Pandas operations. This gets executed in Snowflake! 
    return_df= df_inv_and_lines.to_pandas()

    #set the index of the Dataframe to be the date column of invoice date
    return_df.set_index('INVOICE_DATE', inplace=True)

    return return_df

def model_data(df):

    #use a streamlit slider to predict the next 1-90 days of sales. Default = 45 days 
    predict_days = st.slider('Select Number of Days to Forecast. ', 1, 90, 45)
    
    
    # Model the data using the SARIMAX (Seasonal Auto-Regressive Integrated Moving Average) method for time series data 
    model=sm.tsa.statespace.SARIMAX(df['ITEM_PRICE'],order=(1, 0, 1),seasonal_order=(1,1,1,24))
    results=model.fit()

    #get the last date of our current dataframe and set it as forecast start date
    predict_start = df.index.max()
    #get the slider input and set it as forecast end date 
    predict_end = predict_start + pd.DateOffset(days=predict_days)

    #add some empty rows to our data frame for 90 days out
    future_dates=[df.index[-1]+ DateOffset(days=x)for x in range(0,90)]
    future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
    future_df=pd.concat([df,future_datest_df])
    
    #Predict the new data from the last day in our base dataset to the last date based upon our slider
    # Note: in a prod environment the predidiction should be pulled out of this function and stored seprately, so you dont re-model every time you want to predict new values
    future_df['Forecast'] = results.predict(start = predict_start, end = predict_end, dynamic= True)  
    future_df['Current Sales'] = future_df['ITEM_PRICE']

    ## Plot the Results using StreamLit AltAir         
    chart_data = pd.DataFrame(future_df,  columns=['Current Sales', 'Forecast'])

    #add a new column for date from the index 
    chart_data['invoice_date'] = chart_data.index

    base = alt.Chart(chart_data).mark_line().transform_fold(
    ['Current Sales:Q', 'Forecast:Q'],
    as_=['Measure', 'Value']
    ).encode(
        alt.Color('Measure:N'),
        alt.X('invoice_date:T')
    )

    #define the X and Y axis for Invoice date and Price
    line_current = base.transform_filter(
        alt.datum.Measure == 'Current Sales:Q'
    ).encode(
        alt.Y('Current Sales:Q',  scale=alt.Scale(domain=[500000, 3500000]), axis=alt.Axis(title='Total Sales by Day')),
        alt.X('invoice_date:T',  axis=alt.Axis(title='Invoice Date')),
        tooltip= [alt.Tooltip("invoice_date:T", title="Invoice Date"), 
                    alt.Tooltip("Current Sales:Q", title="Current Sales by Day")]
    )

    #define the second Y axis for forecasted data
    line_forecast = base.transform_filter(
        alt.datum.Measure == 'Forecast:Q'
    ).encode(
        alt.Y('Forecast:Q', scale=alt.Scale(domain=[500000, 3500000]), axis=alt.Axis(title='Forecast')),
         tooltip= [alt.Tooltip("invoice_date:T", title="Invoice Date"),  
                   alt.Tooltip("Forecast:Q", title="Forecast")]
    )

    #add some points to the graph so it is easier to mouse over for tooltips
    points_current = line_current.mark_point(filled=True, size=40, color='#16537e')
    points_forecast = line_forecast.mark_point(filled=True, size=40, color='#ff8c00')
    
    #build the chart layers 
    chart2= alt.layer(line_current + points_current, line_forecast + points_forecast).interactive()
    
    #plot the chart 
    st.altair_chart(chart2.properties(height = 600), use_container_width=True)
     
    #expand out to see model resutls 
    expander = st.expander("Expand to view Model Results Summary")
    expander.write(results.summary())
     
 
if __name__ == "__main__":
    df_model = create_session_object()
    with st.spinner('Running Model'):
        model_data(df_model)
    st.success('Model Generated')