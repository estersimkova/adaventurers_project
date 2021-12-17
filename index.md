# Can we create an event time-line from 2015 to 2020 using only newspaper quotes ?!

Thank you for visiting our website ! We, the ADAventurers, are happy to present the outcome of our project.

The ADAventurers: Lucas Brunschwig, John Mavrothalassitis, Axelle Piguet, Ester Simkova

### Project context and research questions

This project was done in the context of the Applied Data Analysis course at EPFL given by professor Robert West.
We were provided with the [Quotebank dataset](https://zenodo.org/record/4277311#.YbntzrvTWV4), containing newspaper quotes from January 2015 to April 2020.

### Objectives

Using this dataset, the research questions we asked ourselves were the following :

1. Are newspapers’ quotes representative of events occurring in the world ? Meaning, can we deduce a time-line of important events that happened in the world during a certain time-frame only from topics emerging from newspaper quotes ?

2. When an important event occurs, does the general sentiment from newspaper quotes regarding the topic evolve ?

### Methods

#### Finding topics from quotes

The Quotebank dataset provides more than 100 millions quotes over 12 years. We decided to focus on the years 2015-2020. For each of these years, we selected a maximum of 100’000 quotes each month. Then, we used the NLP (natural language processing) model [BERTopic](https://github.com/MaartenGr/BERTopic) to extract the topics and associate each quote to a specific topic with a given probability. Using the 20 monthly hottest topics, meaning the ones that have the most quotes associated with them, we looked into the associated words and the quotes associated with the topic with the most probability.
Using this information, we chose for each month the most meaningful topics to be kept.
Then, we created a script to visually represent the chosen topics on a time-line for every month and also for every year.

#### Analysing the sentiment change before and after an event

To answer the second question, and so to perform sentiment analysis, we used a [fine-tuning algorithm for BERT](https://skimai.com/fine-tuning-bert-for-sentiment-analysis/), training the BERT sentiment classifier with data from Twitter - using 1700 complaining (negative sentiment) and 1700 non-complaining (positive sentiment) tweets. We then passed our quotes, previously regrouped into topics by BERTopic, into the trained BERT sentiment classifier and observed the evolution in percentage of positive vs negative quotes regarding a certain topic, before and after certain events occurred.

### Results


#### Time-line creation

You can see here the time-line we obtained for a few chosen months and for each year. 

To assess the performance of our time-line, we first compare the topics we found with the most important events that happened every year according to [Usatoday](https://eu.usatoday.com/story/money/2020/09/06/the-worlds-most-important-event-every-year-since-1920/113604790/) to see if BERTopic caught them. 

These are: 
- For 2015: July 14, Nasa flies by Pluto
- For 2016: November 8, Trump is elected
- For 2017: August-September: Hurricane Triple Whammy (Harvey, Irma, and Maria) devastates the US and the Caribbean
- For 2018: November, wildfires in California
- For 2019: March, Hong-kong protests
- For 2020: March, COVID-19. However, we have to keep in mind that the Quotebank dataset from 2020 spans only the months of January-April.

These topics can be seen to be quite US-centric. However, the newspapers from which the quotes originate in the Quotebank dataset are from Western countries and often the US, so it is quite coherent.

We can see that for ….

#### Sentiment analysis

For the sentiment analysis regarding a particular topic before and after a certain event occurred, looking at the obtained time-line, we chose to focus on ...

- Hong-kong protests in March 2019: how China is mentioned in the media
- Opinion of Trump before and after his election in November 2019


### Conclusion 

To conclude, let’s go back to the two questions we asked ourselves in the beginning:

1. Are newspapers’ quotes representative of events occurring in the world ? Meaning, can we deduce a time-line of important events that happened in the world during a certain time-frame only from topics emerging from newspaper quotes ?

2. When an important event occurs, does the general sentiment from quotes regarding the topic evolve ?

With the data analysis shown above, we can now answer, at least partially, these questions.

First, we showed that it is very complicated to find events occurring in the world only from quotes in newspapers, even using one of the most performant NLP (natural language processing) models available now-a-days: BERT.
However, we can still come up with meaningful topics ..

Then, we can see with sentiment analysis that...



Thank you very much for reading !
