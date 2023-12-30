import requests
import schedule
import time


def send_message():
  resp = requests.post('https://textbelt.com/text', {
    'phone': 'XXXXXXXXXX',
    'message': 'Hello world',
    'key': 'textbelt',
  })
  print(resp.json())

def printText():
  print("Hello World! ")  

#schedule.every().day.at('06:00').do(send_message)

schedule.every(2).seconds.do(printText)  

while True:
  schedule.run_pending()
  time.sleep(1)

  