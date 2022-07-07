from lib.packets.encode.packet_encode import build
from lib.packets.decode.packet_decode import decode
import socket


def server(host='0.0.0.0', port=67):
    data_payload = 2048

    server_address = (host, port)

    sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(
        f'Starting an DHCP server  on {server_address[0]} port {server_address[1]}')

    sock.bind(server_address)

    while True:
        print('Waiting for clients')

        data, client = sock.recvfrom(data_payload)

        if data:
            res = build(data)

            sock.sendto(res, client)

            print(f'sent {decode(res)} bytes back to {client}')
   

server()
