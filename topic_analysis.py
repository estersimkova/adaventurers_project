"""
:TITLE: Topic Analysis based on the results of bert topics results
:AUTHORS: Axelle Piguet, Ester Simkova, John ..., Lucas Brunschwig
:LAST MODIFICATION: 14.12.2021

DESCRIPTION: this python file goal is to analyze topics we got for each month and
see which topics are hot in one month and compare which topics occurs over time.

:TO-DO LIST:
    - Find topics that are alike through months (find an index to measure that)
    - common topics that comes back each month
    - variations of frequency for common topics
    - for hot topic: extract topics that are related to an event (probably needs to be hard coded)
    - ...

"""

import pandas as pd

#--------------------------------------------------------#
# Load Data

nbr_quotes = 550000 # 2090 or 55000 yet

# Load results files
quote_year = pd.read_pickle(f"results/bertopic/{nbr_quotes}/Quotes_with_topics_{nbr_quotes}.pkl")

topics_by_month = []
for i in range(1,13):
    topics_by_month.append(pd.read_pickle(f"results/bertopic/{nbr_quotes}/topics_month_{i}_{nbr_quotes}.pkl"))

#--------------------------------------------------------#
# Topics overview by months

month = 11 # January = 0, December = 11

# Description and highest counts
print(topics_by_month[month].columns)
print()

top_topics = topics_by_month[month].sort_values(by="Count",ascending=False)

# Top topic of the month
topic_number = top_topics[0:20].Topic.values[10]
print()
print(top_topics[top_topics.Topic==topic_number].words.values)
print()

# Quotes associate to the top topic
# Will be change to target most probable quotes
print(quote_year[quote_year.topics_number == topic_number][0:10].quotation.values)



#--------------------------------------------------------#
# Next Analysis
