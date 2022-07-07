from lib.packets.constants import *
from lib.packets.decode.packet_decode import decode
import lib.dhcp.dhcp as dhcp

import lib.packets.encode.options as options


def build(cpkt):
    cdata = decode(cpkt)
    conf = dhcp.get_config(cdata['chaddr'])

    req_msg_type = bytes([cdata['options'][0]['data'][0]])

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
    sname = bytes(padding_generator(64))
    file = bytes(padding_generator(128))
    magic = bytes([0x63, 0x82, 0x53, 0x63])
    opts = options.get_options(conf, res_msg_type)

    pkt = (
        op + htype + hlen + hops + xid + secs + flags + ciaddr + yiaddr +
        siaddr + giaddr + chaddr + sname + file + magic + opts
    )

    return pkt


def padding_generator(length, value=0x00):
    return [value for _ in range(length)]
