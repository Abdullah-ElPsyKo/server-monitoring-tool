from ping3 import ping


def ping_server(host):
    response = ping(host)

    if response is False:
        return False
    else:
        return True
