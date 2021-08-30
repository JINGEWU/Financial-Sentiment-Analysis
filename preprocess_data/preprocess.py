# Author: Denis de Montigny
# Date: 2020.11
#
#   Takes all files in the source directory
#   Preprocesses them (lowercase, remove punctuation, remove stop words, lemmatize)
#   Save result to target directory
#
#  Copyright (c) 2020. FinSparc Ltd
#  Denis de Montigny in collaboration with Eric Chamoun
#  2020.11.01
#

import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from os import listdir
from os.path import isfile
from os.path import join

source="data/raw/"
target="data/preprocess/"

def run_once():
    nltk.download("stopwords")
    nltk.download('punkt')
    nltk.download('wordnet')


def preprocessing(raw_contents):
    # nlp = spacy.load("en_core_web_sm", disable=['parser', 'tagger', 'ner'])
    # These stop words are too broad: against, above, below, couldn't...
    # TODO Change the stop_words list used here. Consider Loughran's list
    stop_words = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    punctuations = string.punctuation
    text = None
    try:
        text = [word for word in word_tokenize(raw_contents) if word.isalpha()]
        text = [w.lower() for w in text]
        text = [w for w in text if w not in punctuations]
        text = [w for w in text if w not in stop_words]
        text = [w for w in text if re.search('[a-zA-Z]', w)]
        text = [lemmatizer.lemmatize(w) for w in text]
    except:
        print('Preprocessing failed')
    return text

def run_preprocess(source_dir, target_dir):
    all_files = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]
    counter = 0
    for f in all_files:
        s = join(source_dir,f)
        with open(s,"r") as file:
            raw_contents = file.read()
        processed_contents = preprocessing(raw_contents)
        t = join(target_dir,f)
        with open(t,"w+") as file:
            file.write(",".join(processed_contents))
        counter += 1
        if counter%10 == 0:
            print(counter)
    print(f"{counter} files copied.")

if __name__ == "__main__":
    # run_once()
    run_preprocess(source, target)
