class Iface:
    def __init__(self):
        self.__addr = ""
        self.__net = None

    def set_addr(self, addr):
        self.__addr = addr

    def addr(self):
        return self.__addr

    def ping(self, addr):
        if self.__net is None:
            return "no network"

        return self.__net.ping(addr)

    def connect(self, net):
        self.__net = net

    def disconnect(self):
        self.__net.del_host(self.addr())
        self.__net = None

    def connected(self):
        return self.__net is not None
