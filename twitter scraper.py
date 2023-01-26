import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
import streamlit as st
import datetime
st.title('Word Finder')

# Creating list to append tweet data
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:IPL').get_items()):  # declare a username
    if i > 1000:  # number of tweets you want to scrape
        break
    tweets_list1.append(
        [tweet.date, tweet.id,tweet.url,tweet.replyCount,tweet.renderedContent, tweet.source, tweet.content, tweet.retweetCount,tweet.lang,tweet.likeCount])  # declare the attributes to be returned

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'url', 'replyCount', 'renderedContent', 'source','text','retweetCount','language','likes'])
print(tweets_df1)
tweets_df1.to_csv('Tweets.csv')
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
def find_word(tweet, word):
    """Find every occurrence of a word inside a text"""
    # Find the first occurrence of the word
    index = text.lower().find(word)
    # Keep searching until all occurrences have been found
    while index != -1:
        yield index
        # Find the next occurrence of the word
        index = text.find(word, index + 1)
st.markdown("## Find")
text = st.text_area("Tweets", tweet)
word = st.text_input("Word to find", "text")
# min_date=datetime.datetime(2022,12,23)
# max_date=datetime.datetime(2023,1,16)
# Date = st.date_input("Range", min_value=min_date,max_value=max_date)

if st.button("Find"):
    # Find all occurrences of the word
    result = list(find_word(tweet, word))
    # Show the results
    st.markdown("## Results")
    st.markdown(f"Found **{word}** {len(result)} times")
    st.write(result)
    st.download_button("Download txt", word, file_name="res.csv")