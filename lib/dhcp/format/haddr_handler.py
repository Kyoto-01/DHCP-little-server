def format_haddr(haddr: bytes, hlen = 6):
    hextects = []

    for i in range(hlen):
        hextects.append(format(haddr[i], 'x'))

    return ':'.join(hextects)
