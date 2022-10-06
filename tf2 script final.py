import websocket
import _thread
import time
import rel
import json
import pygsheets
import gspread
import pandas 
import requests
#gc=gspread.service_account(filename=r'C:\Users\shyam\Desktop\coder\creds.json')
#client = pygsheets.authorize(service_file=r'C:\Users\shyam\Desktop\coder\creds.json')
#sh = gc.open('tf2 sheet')

#worksheet = sh.sheet1
def on_message(ws, message):
  
    message_json=json.loads(message)
    sell = message_json["payload"]
    item_intent = sell["intent"]
    me = sell["item"]
    me1 = me["name"]    
    qualityy = me["quality"]
    quality = qualityy["id"]
    particles = me["particle"]
    particle = particles["name"]
    effects = particles["id"]
    user__id = sell["steamid"]
    price = sell["currencies"]
    key_price = price["keys"]
   # effect_list = [ 37, 38,39, 40, 43, 44, 45, 46, 47,63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 107, 108, 109, 110, 114, 115, 116, 117, 118, 119, 120 , 122, 123, 124, 125, 126, 127, 128, 129, 130, 134, 135, 136, 137, 138, 158, 159, 160, 161, 164, 165,166, 167, 168  169, 170,171, 172, 173, 198, 199, 200, 201, 219, 220 ]
    effect_list = ["37", "38","39", "40", "43", "44", "45", "46", "47","63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77",
    "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "107", "108", "109", "110", "114", "115", "116", "117", "118", "119", "120"
    , "122", "123", "124", "125", "126", "127", "128", "129", "130", "134", "135", "136", "137", "138", "158", "159", "160", "161", "164", "165","166", "167", "168"
    "169", "170","171", "172", "173", "198", "199", "200", "201", "219", "220"
    ]
    blacklist = ["76561198795826430", "76561198453530349" , "76561199072654974", "76561199106217370","76561198841279602"]
    effect = str(effects)
    user_id = str(user__id)
    payload = {
	    'content':  me1 ,
        'price': key_price
          }
    header = {
	      'authorization': "Mjk2MjUxODg0OTkyNDYyODUw.GwhBAQ.KhHsOtLmzutOdUlwD3jTspzt2DksFuxHhoHBCI"
            }
    if(quality==5)and (effect in effect_list)and (key_price>50)and(user_id not in blacklist):
            r = requests.post("https://discord.com/api/v9/channels/1026466334759997525/messages", 
                  data = payload, headers=header)
#blacklist:  76561198795826430 76561198453530349  76561199072654974 
 #AshyRag: auth = MjU4MDg2NTI1MjUyNjY1MzQ1.GJLjeV.g7DlmhuQQavEeE18FM9ZqfJCDb3tEgDBTNE2Ks
def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.backpack.tf/events",
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()