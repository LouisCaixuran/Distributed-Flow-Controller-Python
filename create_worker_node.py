import socket
import json
import hashlib
import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 41644  # The port used by the server # only temperary, this one should be get from dns using the id
h = hashlib.new('sha256') # instead of MD5

# json_file = sys.argv[-2] # json file name
# key = sys.argv[-1] # caller key
# with open(json_file, "r") as infile:
#     obj = json.load(infile)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes("GET 100", encoding="utf-8"))

    
    data = s.recv(1024)
    
    print(f"Received {data!r}")