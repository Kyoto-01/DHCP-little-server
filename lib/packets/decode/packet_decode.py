def decode(pkt):
    op = bytes([pkt[0]])
    htype = bytes([pkt[1]])
    hlen = bytes([pkt[2]])
    hops = bytes([pkt[3]])
    xid = pkt[4:8]
    secs = pkt[8:10]
    flags = pkt[10:12]
    ciaddr = pkt[12:16]
    yiaddr = pkt[16:20]
    siaddr = pkt[20:24]
    giaddr = pkt[24:28]
    chaddr = pkt[28:44]
    sname = pkt[44:108]
    file = pkt[108:236]
    magic = pkt[236:240]
    options = decode_options(pkt[240:])

    pkt_obj = {
        'op': op,
        'htype': htype,
        'hlen': hlen,
        'hops': hops,
        'xid': xid,
        'secs': secs,
        'flags': flags,
        'ciaddr': ciaddr,
        'yiaddr': yiaddr,
        'siaddr': siaddr,
        'giaddr': giaddr,
        'chaddr': chaddr,
        'sname': sname,
        'file': file,
        'magic': magic,
        'options': options
    }

    return pkt_obj


def decode_options(options):
    opt_list = []

    i = 0
    while options[i] != 0xff:
        opt_name = options[i]
        opt_len = options[i + 1]
        opt_data = options[i + 2:i + opt_len + 2]

        i += opt_len + 2

        opt = {
            'name': opt_name,
            'length': opt_len,
            'data': opt_data
        }

        opt_list.append(opt)

    return opt_list


if __name__ == '__main__':

    from pprint import pprint

    pkt_dhcp_encoded = bytes([
        0x02, 0x01, 0x06, 0x00, 0xcd, 0x29, 0xaf, 0x6a,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x0a, 0x00, 0x04, 0xde, 0x00, 0x00, 0x00, 0x00,
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
        0x35, 0x01, 0x02, 0x36, 0x04, 0x0a, 0x00, 0x04,
        0xfe, 0x33, 0x04, 0x00, 0x09, 0x3a, 0x80, 0x01,
        0x04, 0xff, 0xff, 0xff, 0x00, 0x03, 0x04, 0x0a,
        0x00, 0x04, 0xfe, 0x06, 0x08, 0x0a, 0x00, 0x07,
        0x13, 0x0a, 0x00, 0x07, 0x14, 0x3a, 0x04, 0x00,
        0x04, 0x9d, 0x40, 0x3b, 0x04, 0x00, 0x08, 0x13,
        0x30, 0xe0, 0x11, 0x46, 0x47, 0x36, 0x48, 0x31,
        0x45, 0x35, 0x38, 0x31, 0x39, 0x39, 0x30, 0x32,
        0x32, 0x34, 0x33, 0x00, 0xff
    ])

    pkt_dhcp_decoded = decode(pkt_dhcp_encoded)

    pprint(pkt_dhcp_decoded, sort_dicts=False)