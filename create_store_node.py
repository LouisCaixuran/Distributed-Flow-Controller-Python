import socket
import json
import sys
import os
from datetime import datetime
import hashlib

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


json_file = sys.argv[-1] # json file name
with open(json_file, "r") as infile:
    obj = json.load(infile)

# init the store node if it has not been initialized before, otherwise load it
if obj['status'] == 'uninitialized':
    obj['status'] = 'available'
    obj['key'] = os.path.abspath(json_file) + '_' + datetime.now().strftime("%H:%M:%S") # relative path -> abosolute path + creation time
    h = hashlib.new('sha256') # instead of MD5
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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)