import streamlit as st
import pandas as pd
import json

st.title("CSV/JSON File Viewer")

uploaded_file = st.file_uploader("Choose a CSV or JSON file", type=["csv", "json"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()

    try:
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
            st.write("## CSV Data")
            st.dataframe(df)  # Display as a dataframe

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