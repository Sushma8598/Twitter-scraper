import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
import streamlit as st
import datetime
import os



df = pd.read_csv(r"F:\Tasks\Tweets.csv")
print(df)
df_dict = df.to_dict("records")
print(df_dict)
# py = MongoClient("mongodb://Shiva:Shivadw34@ac-hiwwfdi-shard-00-00.nzfu3wg.mongodb.net:27017,ac-hiwwfdi-shard-00-01.nzfu3wg.mongodb.net:27017,ac-hiwwfdi-shard-00-02.nzfu3wg.mongodb.net:27017/?ssl=true&replicaSet=atlas-i0xspt-shard-0&authSource=admin&retryWrites=true&w=majority")
# py1 = py["MongoClient"]
# py2 = py["tweet"]
# pycollection4 = py2["tweet details"]
# pycollection4.insert_many(df_dict)
# df=pd.DataFrame(df_dict)

# streamlit

st.title('Word Finder')
def find_word(text, word):
    """Find every occurrence of a word inside a text"""
    # Find the first occurrence of the word
    lword=len(word)
    start_index = text.find(word)
    start_index = text.index(word)
    t=text[start_index:start_index + lword]


st.markdown("## Find")
text = st.text_area("Tweets", df_dict)
word = st.text_input("Word to find", "")
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')

if st.button("Find"):
    # Find all occurrences of the word
    # result = list(find_word(text, word))
# Show the results
    st.markdown("## Results")
    st.markdown(f"Found **{word}** {len(word)} times")
    st.write(word)
    st.download_button("Download txt--csv",text,file_name="res.csv")
    st.download_button("Download txt--json", text, file_name="res.json")







