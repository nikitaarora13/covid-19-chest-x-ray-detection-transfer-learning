import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly
import folium
import math
import os
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import tensorflow as tf
from pandas.io.json import json_normalize
from streamlit_folium import folium_static
from streamlit.script_request_queue import RerunData



url="https://www.mohfw.gov.in/data/datanew.json"
r=requests.get(url)
df=json_normalize(r.json())
def marquee():
    structure=""
    for i in range(36):
        struc="""<tr><td>"""+df.state_name[i]+"""</td><td>"""+ df.active[i]+"""</td><td>"""+ df.cured[i]+"""</td><td>"""+ df.positive[i]+"""</td><td>"""+ df.death[i]+"""</td></tr>"""
        structure+=struc
    return structure
tab="""<table><tr><th>State</th><th>Active</th><th>Cured</th><th>Positive</th><th>Death</th></tr>"""+marquee()+"""</table>"""
st.markdown(tab,unsafe_allow_html=True)