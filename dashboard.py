import streamlit as st
import pandas as pd
import numpy as np
from utils import costs_per_month, costs_per_week, filter_column

# Read data ...
costs_df_raw = pd.read_csv('../../repository/daily_usage_by_service.csv')

# Add 'account_type's
costs_df = (
    costs_df_raw
    .pipe(lambda x: x.assign(date=pd.to_datetime(x['date'], format='%d/%m/%Y')))
)
costs_df['sow'] = costs_df['date'].dt.to_period('W').apply(lambda r: r.start_time)
costs_df['som'] = costs_df['date'].dt.to_period('M').dt.to_timestamp()
costs_df['date'] = costs_df['date'].dt.date


########################################################################################
# SIDEBAR
########################################################################################

# Select filters for sidebar
# Add a selectbox to the sidebar:
col = 'account_type'
opt = tuple(costs_df_raw[col].unique())

add_selectbox = st.sidebar.selectbox(
    'Which service(s) would you like to view?',
    opt
)

# Add radio buttons to side bar
col = 'account_name'
opt = tuple(costs_df_raw[col].unique())

chosen = st.sidebar.radio(
    'Account',
    opt)
st.sidebar.write(f"You have chosen account: {chosen}")


########################################################################################
# Layout
########################################################################################

# X = account_name
# Y = month/year
# Values = costs
account_name_per_month = costs_per_month(
    filter_column(costs_df, 'account_name', chosen),
    'account_name'
)
account_name_per_week = costs_per_week(
    # filter_column(costs_df, 'account_name', chosen),
    costs_df,
    'account_name'
)
account_type_per_month = costs_per_month(
    filter_column(costs_df, 'account_type', add_selectbox),
    'account_type'
)

st.title('Cloud Cost Control')
st.subheader('Dashboard for the cloud cost control project')

left_column, right_column = st.columns(2)

with left_column:
  st.write('Cloud costs per provider')
  st.bar_chart(account_type_per_month)

with right_column:
  if st.checkbox('Show cost data'):
    st.write('Cloud cost by project and service')
    st.write(account_name_per_month.style.format('${0:,.2f}'))

# Line chart
st.write('Cloud cost by week')
st.area_chart(account_name_per_week)
