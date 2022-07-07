import socket
#import packets.encode.packet_encode as epkt


def server(host='0.0.0.0', port=6700):
    data_payload = 2048

    sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    server_address = (host, port)

    print(
        f'Starting an DHCP server  on {server_address[0]} port {server_address[1]}')

    sock.bind(server_address)

    while True:
        print('Waiting for clients')

        data, client = sock.recvfrom(data_payload)

        if data:
            sock.sendto(data, client)

            print(f'sent {data} bytes back to {client}')


server()
