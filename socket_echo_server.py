import socket

server = socket.socket()
# 첫번째 인자를 받아야함->튜플형태로 생성 / 127.0.0.1은 내 컴퓨터에서 들어오는 요청만 연결하겠다, 0.0.0.0은 모든 네트워크 연결허용하겠다.
server.bind(('0.0.0.0', 6543))
server.listen()

while True:
    conn, addr = server.accept()  # 데이터 받기
    data = conn.recv(1024)  # 받은 데이터 저장
    conn.send(data)  # 받은 데이터 다시 전송
