#from cfg import fff
import webbrowser
import openai
usrl1 = 'https://www.youtube.com/'
def fff():
 while True:
  openai.api_key= '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'
  model = 'text-davinci-003'
  user = input('напиши сво вопрос ')
  complection = openai.Completion.create(model = 'text-davinci-003',
     prompt = user,
     max_tokens = 1024,
     temperature = 0.5,
     n = 1,
     stop = None)
  response = complection.choices[0].text
  print("камилла:",response)
  break

while True:
 user = input()
 if user == 'ютуб':
  webbrowser.open(usrl1)
 if user == 'музыка':
  usrl1 = 'https://music.yandex.ru/home'
  webbrowser.open(usrl1)
 if user == 'телеграмм':
  usrl1 = 'https://web.telegram.org/z/'
  webbrowser.open(usrl1)
 if user == 'вк':
  usrl1 = 'https://vk.com/feed'
  webbrowser.open(usrl1)
 if user == 'ватсап':
  usrl1 = 'https://web.whatsapp.com/'
  webbrowser.open(usrl1)
 if user == 'код':
  from wert import rgb
  rgb()
 if user == 'заметка':
  my_file = open("заметка.txt", "w+")
  s = input("что записать")
  my_file.write(s)
  my_file.close()
 if user == 'у меня есть вопрс':
  fff()
 if user == 'давай поговорим':
  fff()
 if user == 'AI':
  fff()
 if user == 'блокнот':
  from sdf import wer
  wer()
 if user == 'таблица':
  from cfg import fgh
  fgh()
 if user == 'сделай рисунок':
  from sdf import ccc
  ccc()
 if user == 'фото':
  from cfg import vcb
  vcb()
 if user == 'видео':
  from asf import kml
  kml()
 if user == 'нарсуй ресунок':
  from ijk import ggg
  ggg()
 if user == 'выключить':
  from wert import iii
  iii()