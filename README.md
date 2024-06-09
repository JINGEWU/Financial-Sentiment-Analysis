# Financial Sentiment Analysis

## Introduction

This work investigates a textual-based sentiment analysis model by adopting the newly-devised Natural Language Processing (NLP) tools and performs the stock return prediction by integrating sentiment indices from different information sources, through applying the powerful sequential neural networks. 


## Experiment with 12 different models: 

- Keras CNN

- Keras GRU

- Keras LSTM

- Keras BiGRU

- Keras BiLSTM

- Word2Vec CNN 

- Word2Vec GRU

- Word2Vec LSTM

- Word2Vec BiGRU

- Word2Vec BiLSTM

- BERT

- CH_BERT 

#### 

## Explanation of Files

There are three folders in this repository

1. Code

   This repository contains codes for data preprocessing and model training.

   The data used in model training is already preprocessed and no need to run those codes in preprocess_data. These files contain model training and evaluation:

   - CH_BERT.ipynb
   - CH_SVC_NB.ipynb
   - EN_sentiment_analysis.ipynb

   To run these files, you need to change the filepath before running. All these codes were run on Google Colab.

2. Data

   There are different version of dataset in this repository. The main two dataset used in model training are:

   - Chinese dataset： data/CH.csv 

   - English dataset: data/EN.csv 

   We also provide the raw data and a full data before cleaning and filtering for future research, which are:

   - Chinese dataset:  

     - data/raw/CH/choice_news_ustime.csv

       This is the Chinese data using US time zone. 

     - data/raw/CH/choice_news.csv 

       This is the Chinese data using China time zone. 

   - English dataset:

     There are many files:

     - data/raw/EN/nytimes_title.rar 

       Headlines from the New York Times

     - Dataset from [Kaggle](https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests)


## Set up

This project uses Google Colab Pro for training and testing, we highly recommend you run this on [Google Colab Pro](https://research.google.com/colaboratory/).

### Python Version

- 3.7

### Modules 

* numpy

* pandas

* json

* os

* tensorflow (2.x)

* sklearn

* seborn

* matplotlib.pyplot

* gensim.downloader

* tensorflow_hub

* tokenization

* sentencepiece 

* torch

* transformers

* tqdm.notebook
