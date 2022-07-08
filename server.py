from lib.packets.encode.packet_encode import build
from lib.packets.decode.packet_decode import (decode, get_requested_addr)
import lib.dhcp.dhcp as dhcp
from lib.packets.constants import *
import lib.dhcp.format.haddr_handler as haddr

import socket


def server(host='0.0.0.0', port=67):
    data_payload = 2048

    server_address = (host, port)

    sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(f'Starting an DHCP server  on {host} port {port}')

    sock.bind(server_address)

    while True:
        print('Waiting for clients')

        try:
            data, _ = sock.recvfrom(data_payload)

            if data:
                data = decode(data)

                ciaddr = get_requested_addr(data['options'])
                chaddr = data['chaddr']

                if data['options'][OPT_DHCP_MESSAGE_TYPE[0]]['data'] == DHCP_DISCOVER:
                    conf = dhcp.get_config(chaddr)
                    lease_action = 'RESERVED'

                elif data['options'][OPT_DHCP_MESSAGE_TYPE[0]]['data'] == DHCP_REQUEST:
                    conf = dhcp.get_lease(chaddr)
                    lease_action = 'STORED'

                else:
                    dhcp.del_lease(chaddr)
                    continue

                res = build(data, conf)

                sock.sendto(res, (ciaddr, 68))

                lease = dhcp.get_lease(chaddr)
                formated_haddr = haddr.format_haddr(chaddr)
                formated_iaddr = socket.inet_ntoa(lease["addr"])

                print(f'{lease_action} CONFIG: ({formated_haddr}, {formated_iaddr})\n')

        except KeyboardInterrupt as ki:
            sock.close()
            break

        except Exception as e:
            print(e)
            sock.close()
            break


server()
