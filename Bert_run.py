##################### IMPORTS #####################

# NumPy to use arrays
import numpy as np
# DataFrame
import pandas as pd
# Data Decompression
import bz2
import json

# Useful for chronological ordering
from datetime import datetime, date ,time
import string

# Exploratory Analysis
from wordcloud import WordCloud , STOPWORDS

# Plotting
import matplotlib.pyplot as plt

#To do initial data handling
import gensim
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk.corpus import stopwords

#Import sentence transformer
from sentence_transformers import SentenceTransformer

#Import umap for dimensionality reduction
import umap

#Import hdbscan
import hdbscan

import gensim.corpora as corpora

from pprint import pprint

import pyLDAvis.gensim
import pickle
import pyLDAvis
import os

from bertopic import BERTopic

def data_loader(path):
    eps=1e-1 # precision for progression

    limit = 10 # will be changed when everything is running smoothly
    maximum = 1000 #10000 # hard-coded for the moment

    df_reader = pd.read_json(path, lines=True, compression='bz2', chunksize= 10000) # here we only loaded the quotes from 2016, but we can simply change the year to have the others

    print("Beginning: Loading of Quotes...")

    for i,chunk in enumerate(df_reader):

        # Keep track of progression
        if(i/limit%0.1<eps):
            print(f"Loading... {i/limit*100} %")

            # Initialize the DataFrame columns with first chunk
        if i == 0:
          df_quotes = pd.DataFrame(chunk)
        else:
          # Concatenation of new chunk into the DataFrame
            df_quotes = pd.concat([df_quotes,chunk])

        # We don't want to read it all as long as we do not have the final code
        if i>=limit:
          break

    print("Done Loading.")
    return df_quotes

def clean_data(data):
    # code for data cleaning

    # Drop duplicated rows
    data.drop_duplicates(subset="quoteID")

    # Drop columns: phase and qids that are not of interest to us
    data.drop(columns=['phase','qids'])

    # Check if ids are unique
    return data

def get_slice(df_quotes,month,start_date=-1,end_date=32):
    df_quotes.sort_values(by=['date'], inplace=True, ascending=True)

    ##### IMPORTANT: we take only a subset of quotes for a given time window
    df_quotes = df_quotes[df_quotes.date.dt.month == month] # The 2016 United States elections were held on Tuesday, November 8, 2016, let's look around this period (this month)
    df_quotes = df_quotes[df_quotes.date.dt.day <= 30]
    df_quotes = df_quotes[df_quotes.date.dt.day >= 0]
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
    # download a list of english stop words (meaning words we don't want to consider when finding topics)
    stop_words = nltk.corpus.stopwords.words('english')
    text = " ".join( list(df_quotes['quotation'].values))
    verb_list=VerbExtractor(text)

    # extend the stop words list with the ones found in our exploratory data analyses
    stop_words.extend(["like", "im", "good", "hes", "going","first","things","thing","way","someone","anyone","everything","think","people","will","need","would","dont","ive","thats","really","little","something","cant","goal","lot","well","better"])
    stop_words.extend(verb_list)

    print("Common English Words", stop_words)

    # Function to remove stop words
    def remove_stopwords(texts):
        return [[word for word in simple_preprocess(str(doc))
                 if word not in stop_words] for doc in texts]

    df_quotes = df_quotes["quotation"].squeeze().tolist()

    # remove the stop words
    df_quotes = remove_stopwords(df_quotes)


    docs = [item for sub_list in df_quotes for item in sub_list] # flatten the list obtained by removing the stopwords
    return docs

def get_topics_bert(docs):
    topic_model = BERTopic() # call BERTopic
    topics, probs = topic_model.fit_transform(docs)
    return topics,probs,topic_model

def get_topics(path,month,start_date=-1,end_date=32):
    #Get DataFrame from csv
    df_quotes = data_loader(path)

    #clean up the DataFrame
    df_quotes = clean_data(df_quotes)

    #get slice from the whole dataset,for the specified month
    df_quotes = get_slice(df_quotes,month,start_date,end_date)

    #prepare the df quotes DataFrame
    docs = prep_data(df_quotes)

    topics,probs,topic_model = get_topics_bert(docs)

    return topics,probs,topic_model


def get_topics(path,month,start_date=-1,end_date=32):
    df_quotes = data_loader(path)

    #clean up the DataFrame
    df_quotes = clean_data(df_quotes)

    #get slice from the whole dataset,for the specified month
    df_quotes = get_slice(df_quotes,month,start_date,end_date)

    #prepare the df quotes DataFrame
    docs = prep_data(df_quotes)

    topics,probs,topic_model = get_topics_bert(docs)

    return topics,probs,topic_model

def topics_of_interval(df_quotes,month,start_date=-1,end_date=32):
    df_quotes = get_slice(df_quotes,month,start_date,end_date)

    #prepare the df quotes DataFrame
    docs = prep_data(df_quotes)

    topics,probs,topic_model = get_topics_bert(docs)

    return topics,probs,topic_model

def get_year_topics(path,interval = 32):
    df_quotes = data_loader(path)

    #clean up the DataFrame
    df_quotes = clean_data(df_quotes)
    topic_list = []
    prob_list = []
    for i in range(12):
        count = 0
        for i in range(31):
            if(count > 31):
                break
            topics,probs,_ = topics_of_interval(df_quotes,i+1,count,count+interval)
            topic_list.append(topics)
            prob_list.append(probs)
            count = count + interval
    return topic_list,prob_list
