msg = input('請輸入：')
r = 'no'

with open('answer.txt','r',encoding='utf8')as f:
    for line in f: 
        keyword,answer = line.strip().split(',')
        print(keyword,answer)
        if keyword in msg:
            r = answer
            print(r)    

if r == 'no':
    print('sticker')
else:
    print(r)