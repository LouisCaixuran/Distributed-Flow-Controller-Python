import socket
import json
import sys
import os
from datetime import datetime
import hashlib
import random


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
DNS_PORT = 12345 # port number of DNS
h = hashlib.new('sha256') # instead of MD5

json_file = sys.argv[-1] # json file name
with open(json_file, "r") as infile:
    obj = json.load(infile)


# init the store node if it has not been initialized before, otherwise load it
if obj['status'] == 'uninitialized':
    obj['status'] = 'available'

    obj['key'] = os.path.abspath(json_file) + '_' + datetime.now().strftime("%H:%M:%S") # relative path -> abosolute path + creation time
    h.update(obj['key'].encode('ascii'))
    obj['id'] = h.hexdigest()

    obj['label']['owner'] = obj['id']
    if obj['configuration']['allow_access']:
        obj['label']['reader'] = ['*']
    obj['label']['writer'] = [obj['id']]

    print(obj)

    with open(json_file, "w") as outfile:
        json.dump(obj, outfile, indent=4)

elif obj['status'] == 'available':
    pass


# get an open port
result = 0
while result == 0:
    port = random.randint(1024, 65535)
    print(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port)) # 0: this port is being used
    print(result)
    sock.close()

# log that open port to DNS
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
    s2.connect((HOST, DNS_PORT))
    s2.sendall(bytes(json.dumps({"operation": 'LOG', "id": obj['id'], "port": port}), encoding="utf-8"))
    data = s2.recv(1024)
    data = data.decode("utf-8")
    data = json.loads(data)
    print(data)
    s2.close()


# run as a server and handle incoming requests
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, port))
    #port = s.getsockname()[1] # actual port number

    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                data = data.decode("utf-8")
                data = json.loads(data)
                if data["operation"] == 'GET':
                    key = data["key"]
                    h.update(key.encode('ascii'))
                    if (h.hexdigest() in obj['label']['reader']) or ('*' in obj['label']['reader']):
                        conn.sendall(bytes(json.dumps({"status": "success", "data": obj['data']}), encoding="utf-8"))
                    else:
                        conn.sendall(bytes(json.dumps({"status": "reject"}), encoding="utf-8"))
                
                