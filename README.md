# Creation of a time-line of events from 2015 to 2020 using the QuoteBank dataset and subsequent sentiment analysis of quotes before and after a certain event occurred


## Authors

The ADAventurers - Lucas Brunschwig, Ioannis Mavrothalassitis, Axelle Piguet, Ester Simkova, in the framework on the EPFL Applied Data Analysis course (CS-401)

## Table of contents

0. [Abstract](#1)
1. [Research Questions](#2)
2. [Proposed additional datasets](#3)
3. [Methods](#4)
4. [Proposed project timeline](#5)
4. [Questions for the TAs](#6)

## 0. Abstract: <a name="1"></a>

Our project goals are two-fold:

- First, we would like to use the quotes from 2015 to 2020 in the QuoteBank dataset to create a time-line of major events that occurred in the world during this period. We plan on doing this by finding some “hot topics” emerging from the quotes. Once we have created the time-line, we will compare it to an external time-line and see if it corresponds.
- Then, once we have created this time-line of events, we would like to do a sentiment analysis on the quotes regarding a certain topic before and after an event occurred, to see if the general sentiment changes, in general and in the country where the event occured. We are not fixed on a topic nor event for now, since we have to see which events emerge from the time-line.

The motivation behind the project is to be able to see if quotes in newspapers are really representative of the events happening in the world and how an event highly covered in the news can shift the sentiment regarding its domain.

## 1. Research Questions: <a name="2"></a>

As said above, our research questions are the following:

1. Are newspapers’ quotes representative of events occurring in the world ? Meaning, can we deduce a time-line of important events that happened in the world during a certain time-frame only from topics emerging from newspaper quotes ?
2. When an important event occurs, does the general sentiment from quotes regarding the topic evolve ? We will take a more concrete example of an event when we have our re-created time-line.

## 2. Proposed additional datasets: <a name="3"></a>

- To do the first part of the project (create the time-line of events), we only need the quotes and so no external data-set is needed, apart from the external time-line of events that happened in the world during this years, as mentioned below in the methods section.
- Regarding the second part of the project, we could take the Wikidata dataset and extract the speakers’ nationalities for quotes on a certain topic, to see how the sentiment change varies according to the country. However, we did not focus on this part yet since the first part is expected to be time-consuming and this would only be a refinement of the results.

## 3. Methods: <a name="4"></a>


The methods to do our project will be the following:

- Regarding the first part, so the time-line creation, we are going to follow the following pipe-line:

1. Identification of events
	1. To identify events, we have to first regroup quotes into topics. To do that, we will follow the Latent Dirichlet Allocation method using [the following tutorial](https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0), suggested by our TA.
We do this by selecting an appropriate time window, for example one month, to see the topics that emerge during this timeframe during the years 2015-2020.
	2. Once we have a list of topics for each time-period, we choose a frequency threshold and only consider topics that appear in the newspaper at a frequency above this frequency threshold as a significant event. 
Our hypothesis would be that if a topic becomes hot beyond a certain frequency threshold (i.e. very often mentioned in a time window), it is probably related to an event having occurred. However, if a certain topic is present in almost all of the time windows, it is probably a general society preoccupation and is probably not related to a particular event, so we would have to take note of that and only look at the monthly frequency variation.
	3. Manual research: We then check if no major events were forgotten and, to do so, find a database that relates major events of each year and see if we accurately found the majority. This step will help us to validate our timeline (and by doing so, our research hypothesis) and be sure that it does not have too much bias.
External time-line: for instance, the [CNBC website](https://www.cnbc.com/2015/12/31/major-global-events-that-shook-2015.html) (here for 2015) relates the major events that happened during each calendar year.

2. Creation of the time-line

	1. To create the time-line, we suggest the following format:
		- name of the event
		- time when it happened - if there is no definite time, we approximate
		- time it was mentioned for the first time in a newspaper (in 2015-2020)
		- last time it was mentioned (in 2015-2020)
		- number of times it was mentioned
		- list of newspapers and quotes on the topic chronologically


	2. Create a graphical representation of the timeline:
    
	This remains to be defined according to the topic/event we decide to focus on depending on the obtained time-line.


- Regarding the second part, so the sentiment analysis, if time allows it, we are going to follow the following pipe-line:

3. Sentiment analysis 

	1. First we will have to select a topic on which to focus and an event that occurred somewhere during the time period 2015-2020. 
	2. Then, we can take all the quotes related to this topic before and after the event occurred, using for example a time-frame of one month and analyse the sentiment of each quote using a sentiment analysis [API from Google](https://cloud.google.com/natural-language/docs/analyzing-sentiment#language-sentiment-string-python)
	3. We would then analyse the general sentiment regarding the topic at different time points (ex: every 3 days) for example in the periods one month before and one month after the event and see if it changes over time. To find the general sentiment, we can simply take the % of positively-labeled quotes over the defined time frame (ex: 3 days).
	4. The last step would be to do a visualisation of this sentiment analysis, to be clarified depending on the chosen topic.
	
## 4. Proposed project timeline: <a name="5"></a>


We have from November 26th until December 17th to work on Milestone 3 of the project. 
During these 3 weeks, we will:

- Allocate the first 2 weeks to the first part: the quotes classification into topics and the time-line creation, since it is the task that takes the most time. 
- During the last week, we will do sentiment analysis on quotes about one topic before and after one particular event occurring using the Google API. 

During this whole time, we will also progressively create the required website to show our results.
	
## 5. Questions for the TAs: <a name="6"></a>

We were wondering if you had any advice about how to improve our method of finding topics from quotes ? It is quite hard to infere events occuring from our LDA analysis for now.



