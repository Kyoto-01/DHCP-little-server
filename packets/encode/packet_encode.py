from ..constants import *
from ..decode.packet_decode import decode
from ...dhcp import dhcp

import options


def build(cpkt):
    cdata = decode(cpkt)
    conf = dhcp.get_config()

    req_msg_type = cdata['options'][0]['data'][0]

    if req_msg_type == DHCP_DISCOVER:
        res_msg_type = DHCP_OFFER
    elif req_msg_type == DHCP_REQUEST:
        res_msg_type = DHCP_ACK

    op = OP_REPLY
    htype = cdata['htype']
    hlen = cdata['hlen']
    hops = cdata['hops']
    xid = cdata['xid']
    secs = bytes([0x00, 0x00])
    flags = cdata['flags']
    ciaddr = cdata['ciaddr']
    yiaddr = conf['addr']  # bytes([0x0a, 0x00, 0x04, 0xde]) ex.: 192.168.1.x
    siaddr = conf['server']  # ex.: 192.168.1.8 addr deste server
    giaddr = bytes([0x00, 0x00, 0x00, 0x00])
    chaddr = cdata['chaddr']
    chaddr_pad = bytes(padding_generator(16 - hlen))
    sname = bytes(padding_generator(64))
    file = bytes(padding_generator(128))
    opts = options.get_options(conf, res_msg_type)

    pkt = (
        op + htype + hlen + hops + xid + secs + flags + ciaddr + yiaddr +
        siaddr + giaddr + chaddr + chaddr_pad + sname + file + opts
    )

    return pkt


def padding_generator(length, value=0x00):
    return [value for _ in range(length)]


if __name__ == '__main__':

    req = bytes([
        0x01, 0x01, 0x06, 0x00, 0xcd, 0x29, 0xaf, 0x6a,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x04, 0x0e, 0x3c, 0xfc,
        0x91, 0x35, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x63, 0x82, 0x53, 0x63,
        0x35, 0x01, 0x01, 0x0c, 0x0c, 0x44, 0x53, 0x4b,
        0x32, 0x30, 0x4c, 0x42, 0x30, 0x32, 0x2d, 0x4a,
        0x50, 0x37, 0x0d, 0x01, 0x1c, 0x02, 0x03, 0x0f,
        0x06, 0x77, 0x0c, 0x2c, 0x2f, 0x1a, 0x79, 0x2a,
        0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00
    ])

    res = build(req)

    print(res)
