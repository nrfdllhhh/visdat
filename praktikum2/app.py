import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import graphviz

# nama kelompok dan tim anggota
st.title("Kelompok 8 - Visualisasi Data")
st.write("Anggota:")
st.write("1. Royhan Audy Akbar - NIM 0110223064")
st.write("2. Farida Rabani - NIM 0110223069")
st.write("3. Nur Fadilah - NIM 0110223075")

# 1. Visualisasi

# Bar Chart
st.title('Area - Bar Chart')
df = pd.DataFrame(np.random.randn(40, 4), columns=["C1", "C2", "C3", "C4"])
st.bar_chart(df)

# Line Chart
st.title('Area - Line Chart')
df = pd.DataFrame(np.random.randn(40, 4), columns=["C1", "C2", "C3", "C4"])
st.line_chart(df)

# Area Chart
st.title('Area - Area Chart')
df = pd.DataFrame(np.random.randn(40, 4), columns=["C1", "C2", "C3", "C4"])
st.area_chart(df)

# Map
st.title('Map')
locate_map = pd.DataFrame(np.random.randn(50, 2) / [10, 10] + [15.4589, 75.0078], columns=['latitude', 'longitude'])
st.map(locate_map)

# Graphviz - First example
st.title('Graphviz - First Example')
st.graphviz_chart('''
digraph {
  "Training Data" -> "ML Algorithm"
  "ML Algorithm" -> "Model"
  "Model" -> "Result Forecasting"
  "New Data" -> "Model"
}
''')

# Graphviz - Second example
st.title('Graphviz - Second Example')
graph = graphviz.Digraph()
graph.edge('Training Data', 'ML Algorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')
st.graphviz_chart(graph)

# 2. Columns and Navigation

# Columns with images
st.title('Columns with Images')
col1, col2 = st.columns(2)
col1.write("First Column")
col1.image("c:/gambar/Animal1.jpg")
col2.write("Second Column")
col2.image("C:/gambar/Animal2.jpeg")

# Spaced-Out Columns
st.title("Spaced-Out Columns")
img = Image.open("c:/gambar/Animal1.jpg")
for _ in range(2):
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

# Columns with Padding
st.title("Padding Columns")
img = Image.open("C:/gambar/Animal2.jpeg")
col1, padding, col2 = st.columns((10, 2, 10))
with col1:
    st.image(img)
with col2:
    st.image(img)

# Grid Layout
st.title("Grid Layout")
img = Image.open("C:/gambar/Animal2.jpeg")
for _ in range(4):
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

# Expanders/Accordions
st.title('Expanders')
with st.expander("Streamlit with Python"):
    st.write("Develop ML Applications in Minutes!")

# Containers
st.title("Container")
with st.container():
    st.write("Element Inside Container")
    st.line_chart(np.random.randn(40, 4))
st.write("Element Outside Container")

# Out of Order Container
st.title("Out of Order Container")
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))

# Empty Containers
st.title("Empty Containers")
import time
with st.empty():
    for seconds in range(5):
        st.write(f"{seconds} seconds have passed")
        time.sleep(1)
st.write("V Times up!")

# Sidebars
st.sidebar.title("Sidebar")
user_choice = st.sidebar.radio("Are you a New User", ["Yes", "No"])
number = st.sidebar.slider("Select a Number", 0, 10)
st.write(f"User selected: {user_choice}")
st.write(f"Number selected: {number}")
