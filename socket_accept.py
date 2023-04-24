# bind, listen, accept는 소켓 서버에서 사용
# bind -> 소켓을 주소패밀리에 묶어 준다.
# listen -> 소켓이 들어오는 것을 기다린다.
# accpet -> 실행되려면 bind되어 있어야 하고 listen상태여야한다.
# close -> 소켓 서버나 소켓 클라이언트가 사용되지 않을 때, 만들어진 자원을 운영체제로 반환
import socket

sock = socket.socket()
sock.bind(('0.0.0.0', 4400))
sock.listen()

while True:
    conn, address = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        decode_data = data.decode('utf-8')
        print(decode_data)
        conn.send('OK'.encode('utf-8'))
# res = (conn, address)로 구성
# conn = 클라이언트와의 연결을 위한 새로운 소켓 객체
# address = (host, port)로 구성
# sock.close()
