import time 
import Post
import pandas as pd
import sys
import json
'''
data = Post.ct_search(count=20,offset=0,start_date="2020-01-01",end_date="2020-01-20",api_token=Post.token,inListIds=1484047,searchTerm='COVID-19',an=None,no=None)
df = pd.json_normalize(data['result']['posts'])
df.to_csv('output.csv',index=False,encoding='utf-8')
'''
'''
# use url link to get shared post and pages name
#platform paramter can choose facebook, ig or twitter
link='https://newtalk.tw/news/view/2020-03-25/380667?f=ntk'
data = Post.ct_link(count=100, start_Date= "2020-01-01", end_Date="2020-05-01", include_History= None, link= link, include_Summary= None,
                 sortBy="date", searchField= None, offset = None, api_token=Post.token, platforms= 'facebook')
# data format transfer json to csv
df = pd.json_normalize(data['result']['posts'])
df.to_csv('output.csv',index=False,encoding='utf-8')
'''

data = Post.ct_search(count=100,offset=0,start_date="2020-03-20",end_date="2020-06-30",api_token=Post.token,inListIds=1580661,searchTerm='肺炎',an=None,no=None)
with open("sample.json", "w") as outfile:
    json.dump(data, outfile)
df = pd.json_normalize(data['result']['posts'])
df.to_csv('output.csv',index=False,encoding='utf-8')
print("sucessful")
