from random import randint
import format.addr4_handler as addr4
import config


leases = []


def get_config(hw_addr: str):
    conf = {
        'addr': get_addr(),
        'netmask': get_netmask(),
        'gateway': get_gateway(),
        'dns': get_dns(),
        'server': get_dhcp_server()
    }

    save_lease(conf['addr'], hw_addr)

    return conf


def save_lease(net_addr, hw_addr):
    lease = {
        'net_addr': net_addr,
        'hw_addr': hw_addr
    }

    leases.append(lease)


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


def get_subnet():
    return config.subnet


def get_subnet_range():
    return config.subnet_range


def get_netmask():
    return config.netmask


def get_gateway():
    return config.gateway


def get_dns():
    return config.dns_servers


def get_dhcp_server():
    return config.dhcp_server


if __name__ == '__main__':
    conf = get_config('aa:bb:cc:dd:ee:ff')
    print(conf)
