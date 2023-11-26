import streamlit as st
import pandas as pd
data = [
    {"Name": "John", "Age": 28, st.button("Download"): "Engineer"},
    {"Name": "Alice", "Age": 24, st.button("Download"): "Designer"},
    {"Name": "Bob", "Age": 32, st.button("Download"): "Developer"},
]

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(data)

# Display the table using st.table()
st.table(df)