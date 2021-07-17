import random
x = random.randint(0,9)
print(x)
p =[]
with open('stk.txt','r',encoding='utf8') as f:
    for line in f: 
        pac,sti = line.strip().split(',')
        p.append([pac,sti])
    print(p[x][0]) 