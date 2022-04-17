import socket
import json


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 12345 # port number of DNS

port = {}

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

                data = data.decode("utf-8") # e.g. LOG port id  /  GET id
                data = json.loads(data)
                print(data)
                if data['operation'] == 'LOG':
                    port_, id_ = data['port'], data['id']
                    port[id_] = port_
                    conn.sendall(bytes(json.dumps({"status": 'success'}), encoding="utf-8"))
                elif data['operation'] == 'GET':
                    id_ = data['id']
                    conn.sendall(bytes(json.dumps({"status": 'success', "port": port[id_]}), encoding="utf-8"))

