n=[1,2,3,2,3,2,3,4]
l=[]
d={}
for i in n:
    if i not in l:
        l.append(i)
for i in l:
    d[i]=l.count(i)
