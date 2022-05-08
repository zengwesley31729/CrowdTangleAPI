import ast
  
# reading the data from the file
with open('sample.json') as f:
    data = f.read()
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
  
print("Data type after reconstruction : ", type(d))
#print(d['result']['posts'])
for i in d['result']['posts']:
    print(i['platformId'])
