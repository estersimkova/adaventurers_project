##################### IMPORTS #####################

# Useful for chronological ordering
from datetime import datetime, date ,time

# Exploratory Analysis
from wordcloud import WordCloud , STOPWORDS

#To do initial data handling
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk.corpus import stopwords

# Import sentence transformer
from sentence_transformers import SentenceTransformer

# bertopic
from bertopic import BERTopic

# Used to store results
import pandas as pd
import numpy as np


def get_slice(df_quotes,month):

    # fixed date we could add bisextiles year
    #MONTHS_DAY = [31,28,31,30,31,30,31,31,30,31,30,31]

    # Sort by date
    df_quotes.sort_values(by=['date'], inplace=True, ascending=True)

    ##### IMPORTANT: we take only a subset of quotes for a given time window
    df_quotes = df_quotes[df_quotes.date.dt.month == month] # The 2016 United States elections were held on Tuesday, November 8, 2016, let's look around this period (this month)
    #df_quotes = df_quotes[df_quotes.date.dt.day <= MONTHS_DAY[month]]
    #df_quotes = df_quotes[df_quotes.date.dt.day >= 0]

    return df_quotes

# Words extraction that are not nouns

def VerbExtractor(text):
  verb_list = []
  sentences = nltk.sent_tokenize(text)
  for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(words)
    for (word, tag) in tagged:
      if (tag[0] != 'N' and 'NP'): # If the word is a noun, we keep it (singular/plural/proper name)
        verb_list.append(word)
  return verb_list

def prep_data(df_quotes):

    df_quotes = df_quotes["quotation"].squeeze().tolist()

    return df_quotes

def get_topics_bert(docs):
    topic_model = BERTopic() # call BERTopic
    topics, probs = topic_model.fit_transform(docs)
    return topics,probs,topic_model

def topics_by_month(df_quotes,month):
    #get slice from the whole dataset,for the specified month
    df_quotes = get_slice(df_quotes,month)

    #prepare the df quotes DataFrame
    docs = prep_data(df_quotes)

    topics,probs,topic_model = get_topics_bert(docs)

    return topics, probs, topic_model

def get_year_topics(df_quotes):

    topic_assignation= []
    prob_assignation = []
    topic_list = pd.DataFrame(columns=["Topic", "Count", "Name", "Words", "Month"])
    months = range(1,13)
    n_topics = 0

    print("Year analysis:")

    for month in months:

        topic_assigned, probs, topic_model = topics_by_month(df_quotes,month)

        print(f"    month: {month}, number of quotes: {len(probs)}")

        tmp_list = []
        topics_numerotation = []

        for i in range(len(topic_model.get_topic_info())):
            tmp_list.append(topic_model.get_topic(i))
            topics_numerotation.append(i)

        topics_month = topic_model.get_topic_info().copy()
        topics_month["Words"] = tmp_list
        topics_month["Topic"] = (np.array(topics_numerotation) + n_topics).tolist()
        topics_month["Month"]=month

        topic_assigned = (np.array(topic_assigned) + n_topics).tolist()

        n_topics+=len(topics_month)

        topic_list = pd.concat([topic_list,topics_month],ignore_index=True)
        topic_assignation.append(topic_assigned)
        prob_assignation.append(probs)


    return topic_assignation, prob_assignation, topic_list
