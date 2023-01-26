import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
import streamlit as st


df = pd.read_csv(r"F:\Tasks\Tweets.csv")
print(df)
df_dict = df.to_dict("records")
print(df_dict)
py = MongoClient("mongodb://Shiva:Shivadw34@ac-hiwwfdi-shard-00-00.nzfu3wg.mongodb.net:27017,ac-hiwwfdi-shard-00-01.nzfu3wg.mongodb.net:27017,ac-hiwwfdi-shard-00-02.nzfu3wg.mongodb.net:27017/?ssl=true&replicaSet=atlas-i0xspt-shard-0&authSource=admin&retryWrites=true&w=majority")
py1 = py["MongoClient"]
py2 = py["tweet"]
pycollection4 = py2["tweet details"]
pycollection4.insert_many(df_dict)

# streamlit

st.title('Word Finder')
def find_word(text, word):
    """Find every occurrence of a word inside a text"""
    # Find the first occurrence of the word
    index = text.lower().find(word)
    # Keep searching until all occurrences have been found
    while index != -1:
        yield index
        # Find the next occurrence of the word
        index = text.find(word, index + 1)
st.markdown("## Find")
text = st.text_area("Tweets", df_dict)
word = st.text_input("Word to find", "text")
Date = st.text_input("Date", " ")
# retweetCount = st.retweetcount("count limit", "   ")


if st.button("Find"):
    # Find all occurrences of the word
    result = list(find_word(text, word))
    # Show the results
    st.markdown("## Results")
    st.markdown(f"Found **{word}** {len(result)} times")
    st.write(result)
    if result:st.download_button("Download the output",("\n").join(result))