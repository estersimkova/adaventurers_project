## Topics Extraction and Analysis: A Walkthrough

---------------------------------------------

### 0. Project Structure:

**Main Folder:**

​	**Folders Description**

- <u>folder data</u>: *contains file such as quotes-2015.json compressed (or any others)*

- <u>folder results</u>: *contains the results of the analysis*

  - <u>folder bertopic</u>: *each subfolders contains the quotes dataframe with two new columns topic and its probabilities  You also have 12 dataframes each containing the (topics,count,words) by month. It will be optimized later to have only one dataframe. the number of the subfolder is the number of quotes treated in bertopics*
    - <u>folder 2090:</u> contains quotes with topic number and top topics for every month
    - <u>folder 55000:</u> contains quotes with topic number and top topics for every month
  - <u>folder top_topics</u>: where we will save the top topics for each month ( probably hard coded)

  **Python Files:**

  - <u>bert.py:</u> used to analysis quotes month by month
  - <u>data_loader.py:</u> load data from a compressed json
  - <u>topic_extraction.py:</u> main file to use bertopic analysis
  - <u>topic_analysis.py:</u> main file to analyze the topic once you’ve saved the bertopic results

-----------------------------------------

### 1. Data Location: 

web: https://drive.google.com/drive/folders/1Z96B94t9BSJgCgd-OmK0R56INUWHmdy-?usp=sharing

Here you can find the data for 550k quotes analyzed the idea is to do that for more, it is currently running. Dowload it and place it in a folder “results/bertopic/550000/” so that you can use the topic_analysis.py file. 

--------------------------------

### 2. How to use each file

*Topic Extraction:*

- if you want to use this file you need to download data for the year you want,
-  in the python file you can select which file to analyze and how many quotes to load. 
- The file will save its results in the results/bertopic/ folder. Then you can create a subfolder with the year and the number of quotes, for example “results/bertopic/2015_550000” 

*Topic Analysis:*

- if you want to use this file you need the results from the bertopic analysis. 
- You need to place the results in the “results/bertopic/year_nbrQuotes/“, in this folder you’ll have 13 files, 1 for the quotes dataframe and 1 for each months topics
- inside the python file, you have several parameters with a to do list of interesting analysis we could conduct.

If you have any questions just send me a message and we can discuss I’m free during the day



