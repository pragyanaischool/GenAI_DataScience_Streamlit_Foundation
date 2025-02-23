import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

st.title("CSV Data Cleaning & Visualization App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data")
    st.write(df.head())
    
    # Display Column Types
    st.write("### Column Data Types")
    st.write(df.dtypes)
    
    # Data Cleaning
    st.write("### Data Cleaning")
    df.dropna(inplace=True)  # Remove missing values
    df.drop_duplicates(inplace=True)  # Remove duplicates
    
    st.write("Data after cleaning:")
    st.write(df.head())
    
    # Data Summary
    st.write("### Data Summary")
    st.write(df.describe())
    
    # Visualizations
    st.write("### Visualizations")
    
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_columns:
        st.write("#### Histogram")
        selected_column = st.selectbox("Select column for histogram", numeric_columns)
        fig = px.histogram(df, x=selected_column, marginal="box", nbins=30)
        st.plotly_chart(fig)
        
        st.write("#### Correlation Heatmap")
        fig = px.imshow(df[numeric_columns].corr(), text_auto=True, color_continuous_scale='RdBu_r')
        st.plotly_chart(fig)
        
        st.write("#### Box Plot")
        selected_box_column = st.selectbox("Select column for box plot", numeric_columns, key="boxplot")
        fig = px.box(df, y=selected_box_column)
        st.plotly_chart(fig)
        
        st.write("#### Pair Plot")
        fig = px.scatter_matrix(df, dimensions=numeric_columns)
        st.plotly_chart(fig)
        
        st.write("#### Line Plot")
        selected_x = st.selectbox("Select X-axis for line plot", numeric_columns, key="lineplot_x")
        selected_y = st.selectbox("Select Y-axis for line plot", numeric_columns, key="lineplot_y")
        fig = px.line(df, x=selected_x, y=selected_y)
        st.plotly_chart(fig)
        
        st.write("#### Scatter Plot")
        selected_x_scatter = st.selectbox("Select X-axis for scatter plot", numeric_columns, key="scatter_x")
        selected_y_scatter = st.selectbox("Select Y-axis for scatter plot", numeric_columns, key="scatter_y")
        fig = px.scatter(df, x=selected_x_scatter, y=selected_y_scatter)
        st.plotly_chart(fig)
        
        if 'latitude' in df.columns and 'longitude' in df.columns:
            st.write("#### Map Plot")
            fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', hover_data=df.columns,
                                    mapbox_style="open-street-map", zoom=3)
            st.plotly_chart(fig)
    else:
        st.write("No numeric columns found for visualization.")
