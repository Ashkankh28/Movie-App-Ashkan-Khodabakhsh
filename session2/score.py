data= [
      {'id':1 , 'name':'Alice' , 'score':3 },
      {'id':2 , 'name':'Bob' , 'score':7.87 },
      {'id':3 , 'name':'Charlie' , 'score':9.001 },
      {'id':4 , 'name':'David' , 'score':11 },
      {'id':5 , 'name':'Eve' , 'score':13 },
      {'id':6 , 'name':'Frank' , 'score':8 },
      {'id':7 , 'name':'Grace' , 'score':9 },
      {'id':8 , 'name':'Hannah' , 'score':9.2 },
      {'id':9 , 'name':'Issac' , 'score':8.86 }
      ]
for i in data:
    i['score']=round(i['score'])
    if(i['score']<10):
        print(f"{i['name']} score:{i['score']} Failed")
    elif(i['score']>=10):
        print(f"{i['name']} score:{i['score']} Passed")