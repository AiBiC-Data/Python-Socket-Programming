# bind, listen, accept는 소켓 서버에서 사용
# bind -> 소켓을 주소패밀리에 묶어 준다.
# listen -> 소켓이 들어오는 것을 기다린다.
# accpet -> 실행되려면 bind되어 있어야 하고 listen상태여야한다.
# close -> 소켓 서버나 소켓 클라이언트가 사용되지 않을 때, 만들어진 자원을 운영체제로 반환
import socket
import collections

storage = collections.defaultdict(str)
sock = socket.socket()
sock.bind(('0.0.0.0', 4400))
sock.listen()

# res = (conn, address)로 구성
# conn = 클라이언트와의 연결을 위한 새로운 소켓 객체
# address = (host, port)로 구성
# while True:
conn, address = sock.accept()
while True:
    data = conn.recv(1024)
    if not data or data.decode('utf-8') == 'EXIT':
        conn.close()
        break
    data_split = data.decode('utf-8').split(',')
    print(data_split)
    if data_split[0] == 'PUT':
        if len(data_split) == 3:
            storage[data_split[1]] = data_split[2]
            conn.send('Success!'.encode('utf-8'))
        else:
            conn.send("Input Error!".encode('utf-8'))
    elif data_split[0] == 'GET' or data_split[0] == 'DELETE':
        if len(data_split) != 2:
            conn.send("Input Error!".encode('utf-8'))
        elif data_split[1] not in storage:
            conn.send("Not exist!".encode('utf-8'))
        else:
            if data_split[0] == 'GET':
                conn.send(storage[data_split[1]].encode('utf-8'))
            else:
                del storage[data_split[1]]
                conn.send('Success!'.encode('utf-8'))
    elif data_split[0] == 'LIST':
        if storage:
            s = ''
            for k, v in storage.items():
                s += f'{k},{v}\n'
            conn.send(s[:-1].encode('utf-8'))
        else:
            conn.send("Not exist!".encode('utf-8'))
    else:
        conn.send('ERROR!'.encode('utf-8'))
