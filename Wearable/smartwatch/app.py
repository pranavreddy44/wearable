# Import necessary libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import time
import random

# Custom CSS styles
st.markdown("""  
    <style>  
    .stMetric {font-size: 24px;}  
    .title {color: #4CAF50; font-size: 48px; font-family: 'Arial';}  
    .metric {font-size: 18px; margin-bottom: 10px;}  
    </style>  
    """, unsafe_allow_html=True)

# Title and subheader
st.markdown('<p class="title">🏋️‍♂️ Smart Wrist Band</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size:24px; font-family:Arial; color:gray;">Monitor your health parameters in real-time.</p>', unsafe_allow_html=True)

# Create columns for a better layout
col1, col2 = st.columns(2)

# Simulated data
heart_rate = 72
spo2 = 98
temperature = 37.2
steps_count = 1000

# Displaying data in columns
metric_container1 = st.container()
metric_container2 = st.container()

with metric_container1:
    st.markdown('<div class="metric">💓 Heart Rate:<span style="color:#FF4B4B;"> {} bpm</span></div>'.format(heart_rate), unsafe_allow_html=True)
    st.markdown('<div class="metric">🩸 SpO2 Level:<span style="color:#1F77B4;"> {}%</span></div>'.format(spo2), unsafe_allow_html=True)

with metric_container2:
    st.markdown('<div class="metric">🌡 Body Temperature:<span style="color:#FFA500;"> {:.1f} °C</span></div>'.format(temperature), unsafe_allow_html=True)
    st.markdown('<div class="metric">👣 Steps Count:<span style="color:#008000;"> {}</span></div>'.format(steps_count), unsafe_allow_html=True)

# Create columns for graphs
col3, col4 = st.columns(2)

# Adding a plotly line chart for heart rate and SpO2 level
data = pd.DataFrame({
    "Time": [1, 2, 3, 4, 5],
    "Heart Rate": [70, 72, 75, 74, 78],
    "SpO2": [95, 98, 99, 97, 100]
})

fig1 = px.line(data, x='Time', y='Heart Rate', title='Heart Rate Over Time', markers=True).update_layout(
    yaxis_title='BPM',
    yaxis_color='#FF4B4B',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig1.update_traces(line_color='#FF4B4B')
fig2 = px.line(data, x='Time', y='SpO2', title='SpO2 Level Over Time', markers=True).update_layout(
    yaxis_title='%',
    yaxis_color='#1F77B4',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig2.update_traces(line_color='#1F77B4')

with col3:
    st.plotly_chart(fig1, use_container_width=True)

with col4:
    st.plotly_chart(fig2, use_container_width=True)

# Create columns for steps count graph
col5, col6 = st.columns(2)

# Adding a plotly line chart for steps count
steps_data = pd.DataFrame({
    "Time": [1, 2, 3, 4, 5],
    "Steps": [800, 1000, 1200, 1100, 1300]
})
steps_data2 = pd.DataFrame({
    "Time": [1, 2, 3, 4, 5],
    "Temperature": [36.5, 37.2, 37.5, 37.2, 37.5]
})

fig3 = px.line(steps_data, x='Time', y='Steps', title='Steps Count Over Time', markers=True).update_layout(
    yaxis_title='Steps',
    yaxis_color='#008000',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig3.update_traces(line_color='#008000')
fig4 = px.line(steps_data2, x='Time', y='Temperature', title='Body Temperature Over Time', markers=True).update_layout(
    yaxis_title='°C',
    yaxis_color='#FFA500',
    plot_bgcolor='rgba(0,0,0,0)'
)
fig4.update_traces(line_color='#FFA500')

with col5:
    st.plotly_chart(fig3, use_container_width=True)

with col6:
    st.plotly_chart(fig4, use_container_width=True)

# Sidebar navigation
st.sidebar.title("📊 Smart Wrist Band")
st.sidebar.markdown("## Monitor your health parameters in real-time.")
st.sidebar.markdown("---")
st.sidebar.markdown(
    """  
    **Project By**:  
    Bhanu Chaitanya, Nihar Reddy, Pranav Reddy, Karthikeya  
    """
)

# Real-time updates
if st.sidebar.checkbox("Enable Real-time Updates"):
    update_int = st.sidebar.slider("Update Interval (sec)", 1, 10, 5)
    while True:
        heart_rate = random.randint(60, 90)
        spo2 = random.randint(90, 100)
        temperature = round(random.uniform(36.0, 38.0), 1)
        steps_count = random.randint(800, 1500)
        with metric_container1:
            st.markdown('<div class="metric">💓 <span style="color:#FF4B4B;">*Heart Rate*: {} bpm</span></div>'.format(heart_rate), unsafe_allow_html=True)
            st.markdown('<div class="metric">🩸 <span style="color:#1F77B4;">*SpO2 Level*: {}%</span></div>'.format(spo2), unsafe_allow_html=True)
        with metric_container2:
            st.markdown('<div class="metric">🌡 <span style="color:#FFA500;">*Body Temperature*: {:.1f} °C</span></div>'.format(temperature), unsafe_allow_html=True)
            st.markdown('<div class="metric">👣 <span style="color:#008000;">*Steps Count*: {}</span></div>'.format(steps_count), unsafe_allow_html=True)
        time.sleep(update_int)