import streamlit as st
from googlesearch import search
import pandas as pd

# Create a Streamlit app
st.title("Dataset Finder")

# Ask for a topic to find a dataset
topic = st.text_input("Enter a topic to find a dataset: ")

# Search for datasets online
if topic:
    query = f"dataset {topic}"
    results = []

    try:
        # Search for datasets online
        for result in search(query):
            results.append(result)

        # Create a DataFrame from the search results
        df = pd.DataFrame(results, columns=["Link"])

        # Display the search results in a table with links in text format
        if not df.empty:
            st.write("Search Results:")
            st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
        else:
            st.write("No results found.")
    except Exception as e:
        st.write(f"Error fetching search results: {e}")