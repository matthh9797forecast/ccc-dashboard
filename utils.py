import pandas as pd
import numpy as np


def costs_per_month(df, column):
  """
  Given a dataframe column create a pivoted table with the costs per month split by 
  the column input.
  """
  # Parameters
  index_cols = ['som']
  value_cols = ['amount_usd']
  index_cols.append(column)

  # This pivot funciton errors for some reason
  pivot_long = pd.pivot_table(
      data=df,
      index=index_cols,
      values=value_cols,
      aggfunc=np.sum
  ).reset_index()

  pivot_wide = pivot_long.pivot(index='som', columns=[column], values=[
                                'amount_usd']).reset_index()

  # Rename columns, streamlit doesn't currently support multi-level indexes
  new_names = []
  for i, colname in enumerate(pivot_wide.columns):
    if colname[0] == '':
      new_names.append(colname[1])
    elif colname[1] == '':
      new_names.append(colname[0])
    else:
      # new_names.append('_'.join(colname).strip())
      new_names.append(colname[1])

  pivot_wide.columns = new_names

  # Format df
  pivot_wide = (
      pivot_wide
      .pipe(lambda x: x.fillna(0))
      .pipe(lambda x: x.sort_values(by='som', ascending=False))
      .pipe(lambda x: x.assign(som=x.som.dt.strftime('%b-%Y')))
  ).set_index('som')

  # pivot_wide = pivot_wide.style.format('${0:,.2f}')

  return pivot_wide


def costs_per_week(df, column):
  """
  Given a dataframe column create a pivoted table with the costs per month split by 
  the column input.
  """
  # Parameters
  index_cols = ['sow']
  value_cols = ['amount_usd']
  index_cols.append(column)

  # This pivot funciton errors for some reason
  pivot_long = pd.pivot_table(
      data=df,
      index=index_cols,
      values=value_cols,
      aggfunc=np.sum
  ).reset_index()

  pivot_wide = pivot_long.pivot(index='sow', columns=[column], values=[
                                'amount_usd']).reset_index()

  # Rename columns, streamlit doesn't currently support multi-level indexes
  new_names = []
  for i, colname in enumerate(pivot_wide.columns):
    if colname[0] == '':
      new_names.append(colname[1])
    elif colname[1] == '':
      new_names.append(colname[0])
    else:
      # new_names.append('_'.join(colname).strip())
      new_names.append(colname[1])

  pivot_wide.columns = new_names

  # Format df
  pivot_wide = (
      pivot_wide
      .pipe(lambda x: x.fillna(0))
      .pipe(lambda x: x.sort_values(by='sow', ascending=False))
      .pipe(lambda x: x.assign(sow=x['sow'].dt.date))
  ).set_index('sow')

  # pivot_wide = pivot_wide.style.format('${0:,.2f}')

  return pivot_wide


def filter_column(df, column_name, opt):
  opt = [opt] if isinstance(opt, str) else opt
  return df.loc[df[column_name].isin(opt)]
