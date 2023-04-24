# connect는 소켓 클라이언트에서 사용
# connect -> 소켓 서버에 접속
# send -> 데이터를 보냄
# 영어, 키보드 상에 존재하는 글자는 모두 1바이트
# 한글은 euc-kr 한 글자당 2바이트. ex) 대한민국 만세->13bytes
# utf-8 한 글자당 3바이트. ex) 대한민국 만세-> 19bytes
import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 4400))
sock.send('한글'.encode('utf-8'))
resp = sock.recv(1024)
print(resp.decode('utf-8'))
