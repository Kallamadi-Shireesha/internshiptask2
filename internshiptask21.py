import pandas as pd
import os
import hashlib
'''
a=pd.read_csv("excel1.csv")
b=pd.read_csv("excel2.csv")
c=pd.read_csv("excel3.csv")
'''
l=["excel1.csv","excel2.csv","excel3.csv"]
d={}
for i in range(1,len(l)):
    t1=open(l[0], 'r')
    t2=open(l[i], 'r')
    fileone = t1.readlines()
    filetwo = t2.readlines()
    if(fileone==filetwo):
        if l[0] in d:
            d[l[0]]+=1
        else:
            d[l[0]]=1
        #print(l.index(l[0]))
       
    else:
        if l[i] in d:
            d[l[i]]+=1
        else:
            d[l[i]]=1
        #print(l.index(l[i]))
print(d)

#calculate checksum
hasher=hashlib.md5()
with open('excel1.csv','rb') as open_file:
    content=open_file.read()
    hasher.update(content)
print(hasher.hexdigest())

'''
for i in range(1,len(file_list)):
    if (os.path.isfile(file_list[0])==os.path.isfile(file_list[i])) :
        if (file_list[0] in dictionary):
            dictionary[file_list[0]] += 1
        else:
            dictionary[file_list[0]] = 1
        
    else:
        if (file_list[i] in dictionary):
            dictionary[file_list[i]] += 1
        else:
            dictionary[file_list[i]] = 1
       
        
print(dictionary)      


'''