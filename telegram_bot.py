import telegram

# bot 선언, token 넣기
bot = telegram.Bot(token = '1124663503:AAFrRRYjFpQM1rzG1SwJMDzlXWQr2lTfc7o')

## bot에 대한 업데이트 내용 가져오기
#for i in bot.getUpdates():
#    print(i.message)

bot.sendMessage(chat_id = '1015736406', text = "테스트입니다.")
