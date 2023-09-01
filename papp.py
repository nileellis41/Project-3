# Import the libraries for Pandas and Streamlit
import streamlit as st
import pandas as pd

# Create a title for your application using markdown syntax and the Streamlit
# `write` function.
st.write("#Stock Picking")

# Create an opening sentence for your application using regular text and the
# Streamlit `write` function.
st.write("Do you think Ford is a good buy?")

# Create a Pandas dataframe
df = pd.DataFrame({'Ford': [100, .2], 'TSLA': [100, .15]})

# Write the Pandas dataframe to the page
st.write(df)

# Create a text input box using the Streamlit `text_input` function.
# Save the input as a variable.
text = st.text_input("Enter your pick here!")

# Utilize the Streamlit `button` function to display the text input variable
# created in the prior step to the page.
if st.button("Display the Text Message"):
    st.write(text)


# Bonus
library = st.sidebar.selectbox(
    "What is your favorite stock?",
    ("Ford", "TSLA", "Another in CD")
)

if st.sidebar.button("Display selection"):
    st.sidebar.write(library)
