import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = input('Enter an ip address: ')
sPORT = int(input('Enter a port (start): '))
ePORT = int(input('Enter a port (end): '))

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port,'is open!')
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(sPORT,ePORT):
    q.put(worker)

q.join()