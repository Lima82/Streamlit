import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Streamlit App')

# Создание интерактивного слайдера
num = st.slider('Select a number:', 0, 10, 5)
st.write(f'Selected number: {num}')

# Отображение таблицы
data = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.randn(10),
})
st.write('Data Table:')
st.write(data)

# Построение графика
st.line_chart(data)
