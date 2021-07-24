x = random.randint(0,9)
    p = []
    with open('stk.txt','r',encoding='utf8') as f:
        for line in f: 
            pac,sti = line.strip().split(',')
            p.append([pac,sti])

            sticker_message = StickerSendMessage(
            package_id='f[x][0]',
            sticker_id='f[x][1]'
            )
            line_bot_api.reply_message(
            event.reply_token,
            sticker_message)


            p = []
    with open('answer.txt','r',encoding='utf8')as f:
        for line in f: 
            s = keyword, answer = line.strip().split(',')
            p.append([keyword, answer])
            

            if keyword in msg:
                r = answer
                
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text = r))
                
            else:
                sticker_message = StickerSendMessage(
                package_id='11539',
                sticker_id='52114117'
                )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
                