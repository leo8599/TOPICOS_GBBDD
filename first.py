import streamlit as st
import pandas as pd
import json

# Color palette
BACKGROUND_COLOR = "#F0F8FA"  # Light background (AliceBlue)
PRIMARY_COLOR = "#5F9EA0"  # CadetBlue
SECONDARY_COLOR = "#2F4F4F"  # DarkSlateGray
ACCENT_COLOR = "#008B8B"     # DarkCyan

# Set background color for the entire app
st.set_page_config(page_title="File Viewer", page_icon=":file_folder:", layout="wide") #wide makes it more responsive
st.markdown(f"""
    <style>
        body {{
            background-color: {BACKGROUND_COLOR};
            color: {SECONDARY_COLOR}; /* Default text color */
        }}
        .stButton>button {{
            background-color: {PRIMARY_COLOR};
            color: white;
        }}
        .stDataFrame {{ /* Style for DataFrames */
            border: 1px solid {PRIMARY_COLOR};
        }}

        h1, h2, h3 {{
            color: {ACCENT_COLOR};
        }}

    </style>
""", unsafe_allow_html=True)



st.title("CSV/JSON File Viewer")
st.subheader("Visualize your data files with ease.") # Subtitle added

# GitHub Link
github_repo_url = "https://github.com/leo8599/TOPICOS_GBBDD"
st.markdown(f"**GitHub Repository:** [{github_repo_url}]({github_repo_url})", unsafe_allow_html=True)  # Added GitHub link


uploaded_file = st.file_uploader("Choose a CSV or JSON file", type=["csv", "json"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()

    try:
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
            st.write("## CSV Data")
            st.dataframe(df)

        elif file_extension == "json":
             try:
                # Attempt to read as a list of dictionaries (common JSON format)
                data = json.load(uploaded_file)
                df = pd.DataFrame(data)  # Convert to DataFrame for easier display
                st.write("## JSON Data")
                st.dataframe(df)

             except ValueError:
                try:
                    # Attempt to read as a single dictionary
                    data = json.load(uploaded_file)
                    st.write("## JSON Data")
                    st.write(data) # Display the raw JSON data
                except json.JSONDecodeError:
                    st.error("Invalid JSON format.  Please ensure your JSON is correctly formatted.")
                    
        else:
            st.error("Unsupported file type. Please upload a CSV or JSON file.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
