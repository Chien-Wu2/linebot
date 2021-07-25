import random

x = random.randint(0,9)
p=[]
with open('stk.txt','r',encoding='utf8') as f:
    for line in f: 
        pac,sti = line.strip().split(',')
        p.append([pac,sti])
print(x)
print(p[x][0])
print(p[x][1])
#if r == 'no':
#    line_bot_api.reply_message(
#    event.reply_token,
#    StickerSendMessage(
#        package_id='f[x][0]',
#        sticker_id='f[x][1]'
#    ))