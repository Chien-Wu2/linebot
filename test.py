msg = input('請輸入')
with open('answer.txt','r',encoding='utf8')as f:
    for line in f: 
        s = line.strip().split(',')
        keyword = s[0]
        answer = s[1]
        if keyword in msg:
            r = answer
            print(r)
