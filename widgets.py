from turtle import right
import pandas as pd
import numpy as np
import streamlit as st

# Sliders
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Text input
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

# Checkboxes

if st.checkbox('Show dataframe'):
  chart_data = pd.DataFrame(
      np.random.randn(20, 3),
      columns=['a', 'b', 'c'])

  chart_data

# Select boxes
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected: ', option

# Layout
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
left_column.button('Press me!')

with right_column:
  chosen = st.radio(
      'Sorting hat',
      ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
  st.write(f"You are in {chosen} house!")
