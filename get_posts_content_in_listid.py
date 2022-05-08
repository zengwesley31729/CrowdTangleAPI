import time 
import Post
import sys
import json
import pandas as pd
"""
i = 0
page = {'Init'}
while True:
	data = Post.ct_get_posts(count=100,include_history='true',offset=i,start_date='2020-01-01',end_date='2020-12-31',api_token=Post.token,listIds=1528808)
	try:
		page = data['result']['pagination']['nextPage']
		f=open("ABC/"+str(i)+'.json','w')
		f.write("%s" %data)
		print(i)
		i += 100
		time.sleep(13)
	except:
		break
"""
'''
#non_bmp_map = dict.fromkeys(range(0x10000,sys.maxunicode + 1),0xfffd)
data = Post.ct_search(count=20,offset=0,start_date="2020-04-01",end_date="2020-05-01",api_token=Post.token,inListIds=1484047,searchTerm='COVID-19',an=None,no=None)
#f=open("ABC/"+str(i)+'.json','w')
#f.write("%s" %data)
#f.close()
#print(i)
#time.sleep(15)
#for i in data:
 #           i = i.translate(non_bmp_map)
  #          print(i)
            

#data=data.translate(non_bmp_map)
#print(data)

with open("sample.json", "w") as outfile:
    json.dump(data, outfile)

'''
data=Post.ct_get_posts(count=100, start_date='2020-03-20', end_date= '2020-06-30', include_history= None,listIds = 1580661,language = None,
                 sort_by="date", types=None, search_term='肺炎',searchTerm = None, 
                 min_interactions = 0, offset = None, api_token=Post.token)
df = pd.json_normalize(data['result']['posts'])
df.to_csv('output.csv',index=False,encoding='utf-8')
print("finish")
