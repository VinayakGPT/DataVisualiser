import os


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Data Visualiser",
                          layout="centered",
                          page_icon="📊")

# Title
st.title("📊 Data Visualiser")

# File Uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:

    # reading the csv file as a pandas dataframe
    df = pd.read_csv(uploaded_file)

    col1, col2 = st.columns(2)
    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head(5))

    with col2:
        # user selection of df columns
        x_axis = st.selectbox("Select the X-Axis", options=columns + ["None"], index=None)
        y_axis = st.selectbox("Select the Y-Axis", options=columns + ["None"], index=None)

        plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot", "Count Plot"]

        selected_plot = st.selectbox("Select the plot type", options=plot_list, index=None)

    # Button to generate plot
    if st.button("Generate Plot"):
        fig, ax = plt.subplots(figsize=(6,4))

        if selected_plot == "Line Plot":
            sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == "Bar Chart":
            sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == "Scatter Plot":
            sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == "Distribution Plot":
            sns.histplot(x=df[x_axis], kde=True, ax=ax)

        elif selected_plot == "Count Plot":
            sns.countplot(x=df[x_axis], ax=ax)

        # adjust label sizes
        ax.tick_params(axis="x", labelsize=10)
        ax.tick_params(axis="y", labelsize=10)

        # title and axes labels
        plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)

        st.pyplot(fig)
