# Master Thesis: Financial Sentiment Analysis

## Introduction

This thesis investigates a textual-based sentiment analysis model by adopting the newly-devised Natural Language Processing (NLP) tools and performs the stock return prediction by integrating sentiment indices from different information sources, through applying the powerful sequential neural networks. During the experiment, we try different neural networks such as Convolutional Neural Network (CNN),  Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU) with different methods of word embedding such as Word2Vec and Bidirectional Encoder Representations from Transformers (BERT). Instead of English BERT model, this thesis also considers the implementation of Chinese BERT model, which intends to investigate the co-movement of Chinese financial market and U.S. financial market. Our research shows its power on predictability of equity return by using unstructured textual data which can support financial decisions. 

 In terms of the BERT model, this thesis applies Google’s [PAPER](https://arxiv.org/abs/1810.04805) which introduce BERT, a language model based on Transformer, to tackle NLP tasks in financial domain. It has achieved the state-of-the-art on sentiment analysis. 

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

   - [Chinese dataset](https://github.com/JINGEWU/Master_Thesis/blob/main/data/CH.csv)： data/CH.csv 

   - [English dataset](https://github.com/JINGEWU/Master_Thesis/blob/main/data/EN.csv): data/EN.csv 

   We also provide the raw data and a full data before cleaning and filtering for future research, which are:

   - [Chinese dataset](https://github.com/JINGEWU/Master_Thesis/tree/main/data/raw/CH):  

     - data/raw/CH/choice_news_ustime.csv

       This is the Chinese data using US time zone. 

     - data/raw/CH/choice_news.csv 

       This is the Chinese data using China time zone. 

   - [English dataset](https://github.com/JINGEWU/Master_Thesis/tree/main/data/raw/EN):

     There are many files:

     - data/raw/EN/nytimes_title.rar 

       Headlines from the New York Times

     - Dataset from [Kaggle](https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests)

3. Figure

   This repository also contains some plots of results for your information.

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
