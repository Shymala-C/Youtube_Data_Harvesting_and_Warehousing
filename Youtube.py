import streamlit as st
import googleapiclient.discovery
import mysql.connector as sql
from datetime import datetime
import pandas as pd
from PIL import Image



# setting page configurations
icon = Image.open("D:\DS_Guvi_Projects\Youtube_data\YouTube-logo.jpg")
st.set_page_config = ("page_title = YouTube Data Harvesting and Warehousing",
    page_icon = icon,
    layout = "wide",
    )