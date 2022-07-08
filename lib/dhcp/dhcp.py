from audioop import add
from random import randint
import lib.dhcp.format.addr4_handler as addr4
import lib.dhcp.config as config


leases = {}


def get_config(hw_addr: str):
    conf = {
        'addr': get_addr_bytes(),
        'netmask': get_netmask_bytes(),
        'gateway': get_gateway_bytes(),
        'dns': get_dns_bytes(),
        'server': get_dhcp_server_bytes()
    }

    save_lease(hw_addr, conf)

    return conf


def save_lease(hw_addr, conf):
    leases[hw_addr] = conf


def get_lease(hw_addr):
    return leases[hw_addr]


def del_lease(hw_addr):
    del leases[hw_addr]


def is_addr_valid(addr):
    subnet_range = get_subnet_range()

    return addr4.is_addr_in_range(addr, subnet_range[0], subnet_range[1])


def get_addr() -> str:
    subnet = get_subnet()
    netmask = get_netmask()

    subnet_bin = addr4.get_bin_addr(subnet)
    netmask_bin = addr4.get_bin_addr(netmask)

    new_addr = list(subnet_bin)

    for i in range(len(netmask_bin)):
        if netmask_bin[i] == '0':
            new_addr[i] = str(randint(0, 1))

    new_addr = ''.join(new_addr)
    new_addr = addr4.get_addr_from_bin(new_addr)

    if not is_addr_valid(new_addr):
        get_addr()

    return new_addr


def get_addr_bytes():
    addr = get_addr()
    addr = addr4.get_hex_addr(addr)

    return addr


def get_subnet():
    return config.subnet


def get_subnet_range():
    return config.subnet_range


def get_netmask():
    return config.netmask


def get_netmask_bytes():
    mask = get_netmask()
    mask = addr4.get_hex_addr(mask)

    return mask


def get_gateway():
    return config.gateway


def get_gateway_bytes():
    gw = get_gateway()
    gw = addr4.get_hex_addr(gw)

    return gw


def get_dns():
    return config.dns_servers


def get_dns_bytes():
    dns1, dns2 = get_dns()
    dns1 = addr4.get_hex_addr(dns1)
    dns2 = addr4.get_hex_addr(dns2)

    return dns1, dns2


def get_dhcp_server():
    return config.dhcp_server


def get_dhcp_server_bytes():
    server = get_dhcp_server()
    server = addr4.get_hex_addr(server)

    return server


if __name__ == '__main__':
    conf = get_config('aa:bb:cc:dd:ee:ff')
    print(conf)
