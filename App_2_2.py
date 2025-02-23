import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Plotly Data Cleaning & Visualization App")

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
    
    # Sidebar for Chart Selection
    st.sidebar.header("Choose a Chart Type")
    chart_type = st.sidebar.selectbox("Select Chart", ["Histogram", "Correlation Heatmap", "Box Plot", "Pair Plot", "Line Plot", "Scatter Plot"])
    
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    
    if chart_type and numeric_columns:
        if chart_type == "Histogram":
            selected_column = st.sidebar.selectbox("Select column for histogram", numeric_columns)
            fig = px.histogram(df, x=selected_column, marginal="box", nbins=30)
            st.plotly_chart(fig)
        
        elif chart_type == "Correlation Heatmap":
            fig = px.imshow(df[numeric_columns].corr(), text_auto=True, color_continuous_scale='RdBu_r')
            st.plotly_chart(fig)
        
        elif chart_type == "Box Plot":
            selected_y = st.sidebar.selectbox("Select Y-axis for box plot", numeric_columns)
            selected_hue = st.sidebar.selectbox("Select category (optional)", categorical_columns, index=0) if categorical_columns else None
            fig = px.box(df, y=selected_y, color=selected_hue)
            st.plotly_chart(fig)
        
        elif chart_type == "Pair Plot":
            fig = px.scatter_matrix(df, dimensions=numeric_columns)
            st.plotly_chart(fig)
        
        elif chart_type == "Line Plot":
            selected_x = st.sidebar.selectbox("Select X-axis", numeric_columns)
            selected_y = st.sidebar.selectbox("Select Y-axis", numeric_columns)
            fig = px.line(df, x=selected_x, y=selected_y)
            st.plotly_chart(fig)
        
        elif chart_type == "Scatter Plot":
            selected_x = st.sidebar.selectbox("Select X-axis", numeric_columns)
            selected_y = st.sidebar.selectbox("Select Y-axis", numeric_columns)
            selected_hue = st.sidebar.selectbox("Select category (optional)", categorical_columns, index=0) if categorical_columns else None
            fig = px.scatter(df, x=selected_x, y=selected_y, color=selected_hue)
            st.plotly_chart(fig)
        
        elif chart_type == "Map Plot" and 'latitude' in df.columns and 'longitude' in df.columns:
            fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', hover_data=df.columns,
                                    mapbox_style="open-street-map", zoom=3)
            st.plotly_chart(fig)
        
    else:
        st.write("No numeric columns found for visualization.")
