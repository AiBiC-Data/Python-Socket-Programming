# connect는 소켓 클라이언트에서 사용
# connect -> 소켓 서버에 접속
# send -> 데이터를 보냄
# 영어, 키보드 상에 존재하는 글자는 모두 1바이트
# 한글은 euc-kr 한 글자당 2바이트. ex) 대한민국 만세->13bytes
# utf-8 한 글자당 3바이트. ex) 대한민국 만세-> 19bytes
import socket        # 소켓 패키지 임포트

sock = socket.socket()           # 소켓 생성
sock.connect(('127.0.0.1', 4400))      # 로컬 호스트에 4400포트로 연결
while True:                            # 통신을 반복
    print('Input: (exit:EXIT)', end=' ')       # 입력 문구 출력
    user_input = input()       # input 입력
    sock.send(user_input.encode('utf-8'))           # 입력한 인풋을 인코딩하여 소켓 서버로 보내줌
    if user_input == 'EXIT':        # 입력으로 EXIT이 들어오면 연결 종료
        sock.close()             # 소켓 종료
        break            # 반복문 종료
    resp = sock.recv(1024)      # 소켓 서버로부터 받은 데이터를 resp에 저장
    print(resp.decode('utf-8'))          # resp를 디코딩하여 출력
