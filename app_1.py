import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CSV Data Cleaning & Visualization App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data")
    st.write(df.head())
    
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
    
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_columns:
        st.write("#### Histogram")
        selected_column = st.selectbox("Select column for histogram", numeric_columns)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, ax=ax)
        st.pyplot(fig)
        
        st.write("#### Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
        
        st.write("#### Box Plot")
        selected_box_column = st.selectbox("Select column for box plot", numeric_columns, key="boxplot")
        fig, ax = plt.subplots()
        sns.boxplot(y=df[selected_box_column], ax=ax)
        st.pyplot(fig)
        
        st.write("#### Pair Plot")
        st.pyplot(sns.pairplot(df[numeric_columns]))
        
        st.write("#### Line Plot")
        selected_x = st.selectbox("Select X-axis for line plot", numeric_columns, key="lineplot_x")
        selected_y = st.selectbox("Select Y-axis for line plot", numeric_columns, key="lineplot_y")
        fig, ax = plt.subplots()
        sns.lineplot(x=df[selected_x], y=df[selected_y], ax=ax)
        st.pyplot(fig)
        
        st.write("#### Scatter Plot")
        selected_x_scatter = st.selectbox("Select X-axis for scatter plot", numeric_columns, key="scatter_x")
        selected_y_scatter = st.selectbox("Select Y-axis for scatter plot", numeric_columns, key="scatter_y")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[selected_x_scatter], y=df[selected_y_scatter], ax=ax)
        st.pyplot(fig)
    else:
        st.write("No numeric columns found for visualization.")
