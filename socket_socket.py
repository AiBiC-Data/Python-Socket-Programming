# socket
import socket

# 소켓 생성 / AF_INET: ipv4기반의 주소 패밀리(default) / SOCK_STREAM: 신뢰성 있게 보냄(default), SOCK_DGRAM: 순차적으로 받지 못할수도 있다.
sock = socket.socket(socket.AF_INET, socket.AF_APPLETALKSOCK_STREAM)
print(sock)
