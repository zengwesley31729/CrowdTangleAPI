import time 
import Post
import pandas as pd

'''
data = Post.ct_get_posts(count=20,offset=0,start_date="2020-04-01",end_date="2020-05-01",api_token=Post.token,inListIds=1484047,searchTerm='COVID',an=None,no=None)
df = pd.json_normalize(data['result']['posts'])
df.to_csv('output.csv',index=False)
'''
#link='https://www.rfi.fr/tw/%E4%B8%AD%E5%9C%8B/20200309-%E6%B3%95%E5%9C%8B-%E4%B8%96%E7%95%8C%E5%A0%B1-%E6%AD%A6%E6%BC%A2p4%E7%97%85%E6%AF%92%E5%AF%A6%E9%A9%97%E5%AE%A4%E6%98%AF%E5%90%A6%E7%99%BC%E7%94%9F%E9%81%8E%E6%B3%84%E9%9C%B2?fbclid=IwAR1izd7GqOZRZ1pT5nQyxHzyujMg4KieTptZC8pYvsbxLG5kQ6hGAYe1dmU&ref=fb_i'
#link='https://www.ntdtv.com.tw/b5/20200205/video/263401.html?%E6%AD%A6%E6%BC%A2%E8%82%BA%E7%82%8E%E7%97%85%E6%AF%92%E4%BA%BA%E5%B7%A5%E5%90%88%E6%88%90%EF%BC%9F%E5%9C%8B%E9%9A%9B%E8%BC%BF%E8%AB%96%E9%8E%96%E5%AE%9A%E7%9F%B3%E6%AD%A3%E9%BA%97'
link='https://tfc-taiwan.org.tw/articles/2293'
data = Post.ct_link(count=100, start_Date= "2020-01-01", end_Date="2022-04-30", include_History= None, link= link, include_Summary= None,
                 sortBy="date", searchField= None, offset = None, api_token=Post.token, platforms= 'facebook')


df = pd.json_normalize(data['result']['posts'])
df.to_csv('output.csv',index=False)
print("finish")


'''
link='https://newtalk.tw/news/view/2020-03-25/380667?f=ntk'


def ct_link(count=None, startDate= None, end_Date= None, include_History= None, link= None, include_Summary= None,
                 sortBy="date", searchField= None, offset = None, api_token=None,platforms=None):
'''
                 
