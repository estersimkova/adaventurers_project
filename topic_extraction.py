from data_loader import data_loader, clean_data
from bert import get_year_topics

import pandas as pd
#--------------------------------------------------------#
# Initialize

files_to_load = "quotes-2015.json.bz2"
data_year = pd.DataFrame()

#--------------------------------------------------------#
# Load data

print("\nBeginning: Loading File\n")

data_year = data_loader("data/"+files_to_load, limit = 10, chunksize_ = 190)

print("Done: Loading File\n")

#--------------------------------------------------------#
# Bert Topic Analysis

print("\nBeginning: Bert Topic Analysis\n")

topic_assignation, prob_assignation, topic_list= get_year_topics(data_year)

topics_assignation = [element  for month in topic_assignation  for element in month ]
prob_assignation = [element  for month in prob_assignation  for element in month ]

data_year.sort_values(by=['date'], inplace=True, ascending=True)

data_year["topic_number"]=topics_assignation
data_year["topic_prob"]=prob_assignation

print("\nExample of the format")
print(data_year.columns)
print(data_year.head())

print("\nDone: Bert Topic Analysis\n")

#--------------------------------------------------------#
# Saving Topics

print("Saving Data:")
data_year.to_pickle(f"results/bertopic/Quotes_with_topics_{len(data_year)}.pkl")
for i,list_ in enumerate(topic_list):
    list_.to_pickle(f"results/bertopic/topics_month_{i+1}_{len(data_year)}.pkl")
print("Done savings Data")

#--------------------------------------------------------#
# End of topic extractions
print("\nYou can find the results in results/bertopic/ folder")
