import requests
from time import sleep

def format(text, time):
    msg = f"""
Title: {text[0]}\n
    
Posted: {int(time)} mins ago\n
    
Link:
    {text[1]}
    """
    
    return msg

def send_msg(text, time):
   text = format(text, time)
   token = "" # Your telegram token
   chat_id = "" # Your chat id (See: https://www.alphr.com/find-chat-id-telegram/#:~:text=still%20pretty%20nifty%3A-,Go%20to%20https%3A%2F%2Fweb.telegram.org.,are%20actually%20your%20chat%20ID.)
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
   results = requests.get(url_req)
#    print(results.json())