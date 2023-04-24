import socket

client = socket.socket()
client.connect(('127.0.0.1', 6543))  # 서버와 접속
# 데이터 전송, 바이트 형식으로 전송해야됨-> encode('utf-8')사용
client.send('Hello Pyhton Network'.encode('utf-8'))
print(client.recv(1024))
