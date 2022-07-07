from ..constants import *


def get_options(conf, msg_type):
    return (
        dhcp_msg_type(msg_type) + server_id(conf) + lease_time() + mask(conf) + router(conf) +
        dns(conf) + renew_time() + rebind_time() + private() + end()
    )


def dhcp_msg_type(msg_type):
    name = OPT_DHCP_MESSAGE_TYPE
    length = bytes([0x01])
    dhcp = msg_type

    all = name + length + dhcp

    return all


def server_id(conf):
    name = OPT_DHCP_SERVER_IDENTIFIER
    length = bytes([0x04])
    sid = conf['server']

    all = name + length + sid

    return all


def lease_time():
    name = OPT_DHCP_LEASE_TIME
    length = bytes([0x04])
    time = bytes([0x00, 0x09, 0x3a, 0x80])  # 604800s = 7 days

    all = name + length + time

    return all


def mask(conf):
    name = OPT_SUBNET_MASK
    length = bytes([0x04])
    mask = conf['netmask']

    all = name + length + mask

    return all


def router(conf):
    name = OPT_ROUTERS
    length = bytes([0x04])
    addr = conf['gateway']

    all = name + length + addr

    return all


def dns(conf):
    name = OPT_DOMAIN_NAME_SERVERS
    length = bytes([0x08])
    dns1 = conf['dns'][0]
    dns2 = conf['dns'][1]

    all = name + length + dns1 + dns2

    return all


def renew_time():
    name = OPT_DHCP_RENEWAL_TIME
    length = bytes([0x04])
    time = bytes([0x00, 0x04, 0x9d, 0x40])  # 302400s = 3 days, 12 hours

    all = name + length + time

    return all


def rebind_time():
    name = OPT_DHCP_REBINDING_TIME
    length = bytes([0x04])
    time = bytes([0x00, 0x08, 0x13, 0x30])

    all = name + length + time

    return all


def private():
    name = OPT_PRIVATE
    length = bytes([0x11])
    value = bytes([0x46, 0x47, 0x36, 0x48, 0x31, 0x45, 0x35, 0x38,
                  0x31, 0x39, 0x39, 0x30, 0x32, 0x32, 0x34, 0x33, 0x00])

    all = name + length + value

    return all


def end():
    name = OPT_END

    all = name

    return all
