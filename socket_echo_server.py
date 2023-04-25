# bind, listen, accept는 소켓 서버에서 사용
# bind -> 소켓을 주소패밀리에 묶어 준다.
# listen -> 소켓이 들어오는 것을 기다린다.
# accpet -> 실행되려면 bind되어 있어야 하고 listen상태여야한다.
# close -> 소켓 서버나 소켓 클라이언트가 사용되지 않을 때, 만들어진 자원을 운영체제로 반환
import socket        # 소켓 패키지 임포트
import collections      # defaultdict를 이용하기 위한 collections 패키지 임포트

# storage 딕셔너리 생성, 모든 키에 대해서 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정
storage = collections.defaultdict(str)
sock = socket.socket()          # 소켓 생성
# 서버가 로컬 호스트의 모든 ip로의 연결에 대해 소켓을 네트워크 자원인 4400 포트에 매핑
sock.bind(('0.0.0.0', 4400))
sock.listen()  # 클라이언트가 bind된 포트로 연결을 할 때까지 기다리는 블럭킹 함수

# conn = 클라이언트와의 연결을 위한 새로운 소켓 객체로 데이터를 주고 받을 수 있는 창구, address = (host, port)로 구성
conn, address = sock.accept()
while True:              # 통신을 지속
    data = conn.recv(1024)                       # 클라이언트에서 보낸 데이터 받아 data에 저장
    # 받은 데이터가 없거나 EXIT이면 연결을 종료
    if not data or data.decode('utf-8') == 'EXIT':
        conn.close()                # 연결 종료
        break             # 반복문 종료
    # 받은 데이터를 콤마(,)를 기준으로 split하여 data_split에 리스트로 저장
    data_split = data.decode('utf-8').split(',')
    if data_split[0] == 'PUT':            # 사용자가 PUT을 입력했을 때
        if len(data_split) == 3:                 # PUT을 입력할 때 PUT,textA,textB로 입력하였는지 체크
            # storage 딕셔너리에 textA:textB 형태로 저장
            storage[data_split[1]] = data_split[2]
            # 클라이언트에게 잘 저장되었다고 알려줌
            conn.send('Success!'.encode('utf-8'))
        else:                                       # PUT구문의 입력이 이상할 때
            conn.send("Input Error!".encode('utf-8'))            # input에러 송신
    # 사용자가 GET이나 DELETE 입력했을 때
    elif data_split[0] == 'GET' or data_split[0] == 'DELETE':
        if len(data_split) != 2:                    # 구문 입력이 이상할 때
            conn.send("Input Error!".encode('utf-8'))           # input에러 송신
        elif data_split[1] not in storage:              # 찾거나 삭제하려는 키가 딕셔너리에 없을 때
            conn.send("Not exist!".encode('utf-8'))          # Not exist 송신
        else:                        # GET과 DELETE 구분
            if data_split[0] == 'GET':                          # GET이 입력일 때
                # textA에 해당하는 value 값 송신
                conn.sendall(storage[data_split[1]].encode('utf-8'))
            else:                        # DELETE가 입력일 때
                # textA에 해당하는 ket:value쌍을 딕셔너리에서 제거
                del storage[data_split[1]]
                conn.send('Success!'.encode('utf-8'))      # 클라이언트에게 제거 알림
    elif data_split[0] == 'LIST':            # LIST가 인풋일 때
        if storage:                 # 빈 딕셔너리가 아니라면
            s = ''                    # key,value 쌍을 저장할 빈 문자열 생성
            for k, v in storage.items():       # 딕셔너리의 key:value쌍 반복
                s += f'{k},{v}\n'            # 문자열 s에 해당값
            # 값이 많을 수 있으므롤 sendall 이용
            conn.sendall(s[:-1].encode('utf-8'))
        else:                                     # 빈 딕셔너리일 경우
            conn.send("Not exist!".encode('utf-8'))        # not exist 송신
    else:                                 # 입력 구문이 잘 못 되었을 경우
        conn.send('ERROR!'.encode('utf-8'))            # ERROR 송신
