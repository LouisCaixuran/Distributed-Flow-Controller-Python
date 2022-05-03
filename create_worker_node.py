import socket
import json
import hashlib
import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
DNS_PORT = 12345 # port number of DNS
#PORT = 41644  # The port used by the server # only temperary, this one should be get from dns using the id
h = hashlib.new('sha256') # instead of MD5

# json_file = sys.argv[-2] # json file name
key = sys.argv[-1] # caller key
print(key)
# with open(json_file, "r") as infile:
#     obj = json.load(infile)


def getData(id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, DNS_PORT))
        s.sendall(bytes(json.dumps({"operation": 'GET', "id": id}), encoding="utf-8"))
        data = s.recv(1024)
        data = data.decode("utf-8")
        data = json.loads(data)
        port = data['port']
        s.close()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        s.sendall(bytes(json.dumps({"operation": 'GET', "key": key}), encoding="utf-8"))
        data = s.recv(1024)
        print(data)
        data = data.decode("utf-8")
        data = json.loads(data)['data']
        s.close()

    return data


mycode = '''
result = []
for id_ in getData(id)['friends']:
    result += [getData(id_)['address']]
print(result)
'''


h.update(key.encode('ascii'))
id = h.hexdigest()
exec(mycode, {'id': id, 'getData': getData})
