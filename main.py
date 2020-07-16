import random
from telebot import types
from mailbox import Message
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(message.chat.id,'Пссс, парень, не хочешь немного евробита? для справки можешь написать /help')

@bot.message_handler(commands=['help'])
def helper(message: Message):
    bot.send_message(message.chat.id, 'Я бот евробита я подберу тебе евробит под настроение. Введи команду /eurobeat')

@bot.message_handler(commands=['eurobeat'])
def eurobeat(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btnSad = types.KeyboardButton('Мне грустно')
    btnFun = types.KeyboardButton('Мне весело')
    btnFight =types.KeyboardButton('Порву всех')
    markup.add(btnSad,btnFun,btnFight)
    bot.send_message(message.chat.id, "Выберите настроение", parse_mode='html', reply_markup=markup)\

@bot.message_handler(content_types=['text'])
def chooseTrack(message: Message):
    if 'Мне грустно' in message.text:
        track = random.randint(0,4)
        switcher = {
            0: "https://downloader.disk.yandex.ru/disk/a50bc5e413451763dd489cec331e590fb4491383b2114738f38a542dafb2e9df/5f106794/GM2ATZBXAusjDYQ-jwIa4spoOxD0h_KfjQHFVBY4E2qZyZPrO04IVb4gDsLzwRjVWguGG1gULsu0Go50rsj3JA%3D%3D?uid=0&filename=heartbeat-extended-mix.mp3&disposition=attachment&hash=OraGnkG8Rj6wtUyy4WeACZ0Woj/41hAp00kTcVscgiVhQP5%2B95xXqMmWtlqOwRApq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=9837429&hid=f15ce6be0eacc4cd50088e3c239feb74&media_type=audio&tknv=v2",
            1: "https://downloader.disk.yandex.ru/disk/40bda996cf5423511859ec37b0b72534ea27aa4dd43f44cb0ff67f078d353098/5f1067f6/GM2ATZBXAusjDYQ-jwIa4rqDa65l4Hyq-f_Wo-BqjHsYumFj7-2VVaXNFWxgT7uxsM3wK7Dywt_gux8mIZwrWQ%3D%3D?uid=0&filename=dave-simon-i-need-your-lovedinitial-d.mp3&disposition=attachment&hash=9nUZDKqblOC4c8qAqU8v1I2cEvQK/SGthXoh9DFcOdLBxKDvyGe7Lo9glBWWw/2Dq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=9422621&hid=012f1f53fa59016a380b5f3742256c98&media_type=audio&tknv=v2",
            2: "https://downloader.disk.yandex.ru/disk/40de10fdc310588a8e846318d9b9a3dd401e29f3ece5be3c203953f201d77a83/5f1068dc/GM2ATZBXAusjDYQ-jwIa4u27ADTDuCoBrZam0xz_eOmTdzWMks-fEA53IvlMZIKv-W5tgUAOD6DVIkjxxM7X7A%3D%3D?uid=0&filename=initiald-arcade-stage-zero-bgm-forever-sad-hely.mp3&disposition=attachment&hash=JHSJfHbILWH9jnPAUvPSUiLBC4OAjwnqQEydvYyg77SgCL1/YpdM/544VsPiYz0Cq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=10883816&hid=f2bcb0c359be4d85fa361c2dd626e88a&media_type=audio&tknv=v2",
            3: "https://downloader.disk.yandex.ru/disk/f69a331224db31a13d9c440bc6098f1fef58fc5c7568d1f38c851dd93e77decb/5f10693e/GM2ATZBXAusjDYQ-jwIa4mGcA_N69U0QA2nI2SD9KgvyijLyQIWhgpoKPj5PcOb5WevjAxBhx3wvtqxhyzCcZQ%3D%3D?uid=0&filename=heartbeat-nathalie.mp3&disposition=attachment&hash=kdaJpGJB/xrDNjCvfWv/VVPvY6tDauKwqNU4TZL5qO8D1vqdPepYHy%2BLpQxBulebq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=9542515&hid=d713550438769c27b0c19ea18ae42fcc&media_type=audio&tknv=v2",
            4: "https://downloader.disk.yandex.ru/disk/9b9345796d883156171ad004dd5389c29bb18b3f46b066cc130441844aece834/5f106995/GM2ATZBXAusjDYQ-jwIa4uHyo4ssu1DQXGa3zFEIkLewZbPd7aU-aA4uiwKKtfXX290FUu7K0vttNdY1wZIjHA%3D%3D?uid=0&filename=jilly-be-my-babedinitial-d.mp3&disposition=attachment&hash=R0aLl93KfvLfF5MyRsnGTJyMyymr4/c8OHamzWveE/xi4wLQxyakP9fAjpn80Ko3q/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=9459762&hid=d5281d8260e86fa34504db5a53b8c5db&media_type=audio&tknv=v2",
        }
        bot.send_audio(message.chat.id, audio=switcher.get(track))

    if 'Мне весело' in message.text:
        track = random.randint(0,4)
        switcher = {
            0: "https://downloader.disk.yandex.ru/disk/46fd8e47e8de157cb2689c7e0aa06177165a598f2fa24130fc476094feffe173/5f106704/GM2ATZBXAusjDYQ-jwIa4uDLnuZg9BfOnjxJDl5n0BIFVFCtPyO0TEJZwfp6yuY_2sMXpjwZf_rhWSSfE4thWg%3D%3D?uid=0&filename=lupin-black-ufo.mp3&disposition=attachment&hash=lw1kFEl92p7Fds4APZW5bEvNkUUs1I4vJkbJzkBOjbnnf3rQ/Qzhoxnr1nj0uxdfq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=8952257&hid=cf6c475b6c3308b13f7418e99f041ba6&media_type=audio&tknv=v2",
            1: "https://downloader.disk.yandex.ru/disk/7379a075d9f280bfa7afa5a22f4322f8ddff32c340b99d0053b06e86b12185f0/5f1067d7/GM2ATZBXAusjDYQ-jwIa4ssmfcdUgSlolfhpApqjCbKlWJ57xdrkG4dhWmIcgohBj2zRp7hOYleLcs_rk5U95Q%3D%3D?uid=0&filename=initial-d-dancing-c-o-o-l-v-i-b-r-a-t-i-o-n-s.mp3&disposition=attachment&hash=23zN0MWc9UCsBjVNcewqt0ICY3Qhm7athnZfe94Nvsks/RFhGnqZj86MaUsoeYrlq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=9479876&hid=590731d58149da50931a54e5a8bd8e00&media_type=audio&tknv=v2",
            2: "https://downloader.disk.yandex.ru/disk/92e5c8d07df56d879140c7af1944fcef7317573f9a9df89791aa09d2071934f9/5f106817/GM2ATZBXAusjDYQ-jwIa4rRL6-Y8CWh63gdg7feghuZUtIGI5YFmWTx1HROX_3jhIeObwD-D1UaJNOejyv2hVw%3D%3D?uid=0&filename=no-one-sleep-in-tokyo-extended-mix.mp3&disposition=attachment&hash=mfuymoMgwNnJM1n5j576Z4nvbNm8RIJ3QeeMHaLIiID7pktBlhYj22Q6es/X4hgqq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=9279168&hid=63a4f9c214d9721f0bbb5a25ec002ab4&media_type=audio&tknv=v2",
            3: "https://downloader.disk.yandex.ru/disk/5f5c426051a518fa2287e25702c309a7e0793984502bd6701c083eeb2c9fc902/5f10682f/GM2ATZBXAusjDYQ-jwIa4i3Ib7Ld3985PktlI0mCgBU7Wx307XYxL9mLR3yPCjXGpsXbw9Dr0Fd8xtW1oNYmwQ%3D%3D?uid=0&filename=chemical-love.mp3&disposition=attachment&hash=16JgskAeGlV2xIvw%2BjCfOSbx8Dsm4XMMw9bZDzddQFN27S9qxluLDldr0Yg2/glcq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=11519724&hid=8090e18ac730f6939c002fe645a01996&media_type=audio&tknv=v2",
            4: "https://downloader.disk.yandex.ru/disk/66756a07cf076213c881b5bd1deda4b44aa2115ba5d976fea91c208120a556f6/5f10687e/GM2ATZBXAusjDYQ-jwIa4gNrOSY52dRDbkTc_LqmbRUJNylfPSaY7wgeEePcFW1DkziLg8da8g8BRW6zQGSzYA%3D%3D?uid=0&filename=initial-d-dont-stop-the-music.mp3&disposition=attachment&hash=qdzbIciHcqN2eUo%2B26HEoG7ty3bJRkX%2BhGkXIUI9qeTV15mT7AB9jLEV7GUgXUdTq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=9551401&hid=5c375df95ce1397d6c728821dcbdb30c&media_type=audio&tknv=v2",
        }
        bot.send_audio(message.chat.id, audio=switcher.get(track))

    if 'Порву всех' in message.text:
        track = random.randint(0, 4)
        switcher = {
            0: "https://downloader.disk.yandex.ru/disk/5fcfdac6afa397cc8020f82cd88ae6feb44f7ea42a13f6af2edbf9350ebdd00e/5f105238/tTQYOnqZVyvzFevLXX8fo3BpPcksFW62q6AWXtyE_JhVgjp7UMpkUImoiZpVs3kwNTe7dsnd-PbT1SGEDApGmg%3D%3D?uid=0&filename=Ken%20Blast%20-%20The%20Top%20%28maximp3.ru%29.mp3&disposition=attachment&hash=g0WzPcXfAXeZT9HMDRhoc2/SOgpLGiSJPgeC2XMYDaRihOi9Fi7QSngEaHqMfSoyq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmp3&owner_uid=104550969&fsize=11063994&hid=0e0cb0819f2391ca19f7ed766d3ef8d8&media_type=audio&tknv=v2",
            1: "https://downloader.disk.yandex.ru/disk/57526b649fd15aeb180c4585483f992a7065e99f3a6349fc661b1f040ddb3c75/5f106590/GM2ATZBXAusjDYQ-jwIa4t8lKOQmq7YojchPQa6qsim6N2sXczVOzEocNOH7JJOtlrFkJ6L6gLEq9kP7wXy83A%3D%3D?uid=0&filename=a-perfect-hero-extended-mix.mp3&disposition=attachment&hash=DVccbIQ5uygAj0OxsL6wHl6zlpQvsyVwsrtjgJi9/JZgzLdPBX9eGt6js5W8cqCuq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=10371439&hid=8f58bba9946a0a567c1447db92e1d30e&media_type=audio&tknv=v2",
            2: "https://downloader.disk.yandex.ru/disk/8e7f86204f88ce4f63f83b28eb2c207c1375b6bfad0a8f3196970f8cf0f16ee3/5f1065f1/GM2ATZBXAusjDYQ-jwIa4vmhpbMOxZpblGB4jtUC3o7U2Su3eepTwDdYDvic2xE7Y6u2yYYH7ooGuJEC3I2x0A%3D%3D?uid=0&filename=adrenaline-ace.mp3&disposition=attachment&hash=G7qIvIMdF3j9UXwFLQevCfuHsI8nduYav2rIlRJOAVIMIvfdU8JWzPq3/Y73uaBRq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=7234965&hid=c39acc7bc74f4ed7bd80f4c306d8c3f9&media_type=audio&tknv=v2",
            3: "https://downloader.disk.yandex.ru/disk/ad41992de8918ca6e64ee1e5e820ffd6f0060c9ad12f3aac8d688e2efc13d9cf/5f106610/GM2ATZBXAusjDYQ-jwIa4v-YtAzuWrh-4ZJVA4bV8JgQ_rPMTdUkAe12u14g1Kuv54if6BHZKOFB-V9sor1nuA%3D%3D?uid=0&filename=dave-rodgers-beat-of-the-rising-sunofficial-lyric-videodinitial-d.mp3&disposition=attachment&hash=4UpmIF%2BPS2ZLyZ1duDN9ZhX4lcMuWKslq9Za4p312xWq3B0OuyKGUIe3zktH%2BYmJq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=6197577&hid=b5f5a71dda0429b9637416e57683e7ed&media_type=audio&tknv=v2",
            4: "https://downloader.disk.yandex.ru/disk/e74f689e9509192fd28f5d890d231e8fe48bf48dcf3621c599f255ea539a0d7f/5f10662d/GM2ATZBXAusjDYQ-jwIa4jui8DKmHDiP-6a2m0zWHilpJclV2mEW2hPA4-7vfbQXd185icBJriBmAfa1A_uWYg%3D%3D?uid=0&filename=manuel-gas-gas-gasofficial-lyric-videodinitial-d.mp3&disposition=attachment&hash=h1Ycf/Pg%2BgDkEPE6F9hpjuhlnlZMTUBo72tTJpw2ifym8PtdtHYOdkAoDrqGw3mWq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=audio%2Fmpeg&owner_uid=104550969&fsize=6340552&hid=cb93a7ecfe145378c2302b62a2a7b30e&media_type=audio&tknv=v2",
        }
        bot.send_audio(message.chat.id, audio=switcher.get(track))

bot.polling(none_stop=True)