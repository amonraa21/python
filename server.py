import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.0.223', 5566))
clients = []

print ('start server')
while True:
    data, address = sock.recvfrom(1024)
    print(f'Message from [{address}]: {data.decode('utf-8')}')
    if address not in clients:
        clients.append(address)
    for client in clients:
        if client == address:
            continue
        sock.sendto(data, client)