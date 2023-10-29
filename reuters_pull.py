

import pandas as pd
import numpy as np

import itertools
import requests
import json
import time
import datetime
from datetime import datetime as dt
from io import StringIO
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from credenciales import cnbc_credentials, reuters_credentials 



headers_reuters = {
	"X-RapidAPI-Key": reuters_credentials["X-RapidAPI-Key"],
	"X-RapidAPI-Host": reuters_credentials["X-RapidAPI-Host"]
}

start_time = time.time()

date_range_ = pd.date_range(end= dt.now().date(), periods= 1375)
news_category = [7, 10, 16, 44, 90, 92, 239]


for term in itertools.product(date_range_, news_category):
    
    news_cat = term[1]
    date_ = term[0]
    #print('News date: ', date_, ' and category: ', news_cat)


    reuters_url = "https://reuters-business-and-financial-news.p.rapidapi.com/category-id/{}/article-date/{}".format(str(news_cat), str(date_ )[:10])
    #print(reuters_url)

    print('Loading: category ', str(news_cat), ' on ', str(date_ ))
    response = requests.get(reuters_url , headers=headers_reuters)
    df_temp = pd.DataFrame(json.loads(response.text))
    print('   Call  size: ', df_temp.shape)
    print('   Call  response size: ', len(response.text))
    #display(df_temp)
    time.sleep(10)

    if df_temp.shape[0] > 0:

        df_temp['news_category_id'] = news_cat
        df_temp['news_category_date'] = date_
        df_reuters = pd.concat([df_reuters, df_temp], axis = 0)

    print('   Current dataframe shape: ', df_reuters.shape)


def extract_text_from_json(json_str):

    try:
        
        news = []
        data_dict = json.loads(json_str)

        for i in range(len(data_dict)):
            content= data_dict[i].get("content")
            if content is not None:
                soup = BeautifulSoup(content, 'html.parser')
                text = soup.get_text()
                #news.join(text)
                news.append(text)
            else:
                text = ""
                news.append(text)

        results = " ".join(news)

    except json.JSONDecodeError:
        results = ""
    
    print('##### Done')
    print(results)
    return results


def clean_news_for_analysis(news):

    stop_words = stopwords.words("english")

    news = news.lower()
    news = re.sub(r'\d+', '', news)
    news = news.translate(str.maketrans('', '', string.punctuation))
    news = news.encode('ascii', 'ignore').decode()
    news = ' '.join([word for word in news.split(' ') if word not in stop_words])
    news = re.sub(r'https*\S+', ' ', news)
    news = re.sub(r'@\S+', ' ', news)
    news = re.sub(r'#\S+', ' ', news)
    news= re.sub(r'\'\w+', '', news)
    news= re.sub('[%s]' % re.escape(string.punctuation), ' ', news)
    news = re.sub(r'\w*\d+\w*', '', news)
    news= re.sub(r'\s{2,}', ' ', news)

    return news