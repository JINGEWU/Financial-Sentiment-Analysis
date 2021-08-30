This repository serves an code and data source of the Master Thesis.



There are mainly two parts of this:

1. Code

   This repository contains codes for data preprocessing and model training.

   The data used in model training is already preprocessed and no need to run those codes in preprocess_data. These files contain model training and evaluation:

   - CH_BERT.ipynb
   - CH_SVC_NB.ipynb
   - EN_sentiment_analysis.ipynb

   To run these files, you need to change the filepath before running. All these codes were run on Google Colab.

2. Data

   There are different version of dataset in this repository. The main two dataset used in model training are:

   - [Chinese dataset]()： data/CH.csv 

   - [English dataset](): data/EN.csv 

   We also provide the raw data and a full data before cleaning and filtering for future research, which are:

   - [Chinese dataset]():  

     - data/raw/CH/choice_news_ustime.csv

        This is the Chinese data using US time zone. 

     - data/raw/CH/choice_news.csv 

       This is the Chinese data using China time zone. 

   - [English dataset]():

     There are many files:

     - data/raw/EN/nytimes_title.rar 

       Headlines from the New York Times

     - Dataset from [Kaggle](https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests)

3. Figure

   This repository also contains some plots of results for your information.