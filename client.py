import socket
import threading


server = '192.168.0.223', 5566
name = input('Введите ваше имя: ')
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('', 0))
socket.sendto(
    (name + ' Connect to server').encode('utf-8'),
    server
)

def read_socket():
    while True:
        data = socket.recv(1024)
        print(data.decode('utf-8'))

thread = threading.Thread(target=read_socket)
thread.start()

while True:
    message = input()
    socket.sendto((f'[{name}]: {message}').encode('utf-8'), server)