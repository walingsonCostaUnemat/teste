import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv(sep=',',thousands = '.', decimal = ',')
st.write(data)