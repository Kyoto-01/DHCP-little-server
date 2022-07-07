def get_bin_addr(addr: str) -> str:
    bin_octects = map(
        lambda octect: format(int(octect), 'b').zfill(8),
        addr.split('.')
    )

    return ''.join(bin_octects)


def get_hex_addr(addr: str):
    hex_octects = bytes(map(
        lambda octect: int(octect),
        addr.split('.')
    ))

    return hex_octects


def get_int_addr(addr: str) -> str:
    return int(addr.replace('.', ''))


def get_addr_from_bin(bin_addr: str) -> str:
    dec_octects = [str(int(bin_addr[i:i+8], 2))
                   for i in range(0, len(bin_addr), 8)]

    return '.'.join(dec_octects)


def is_addr_in_range(addr: str, addr_start: str, addr_end: str) -> bool:
    addr_start = get_int_addr(addr_start)
    addr_end = get_int_addr(addr_end)

    addr = get_int_addr(addr)

    return (
        (addr < addr_start) or
        (addr > addr_end)
    )
