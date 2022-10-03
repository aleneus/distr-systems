class Iface:
    def __init__(self):
        self.__addr = ""
        self.__net = None

    def set_addr(self, addr):
        self.__addr = addr

    def addr(self):
        return self.__addr

    def ping(self):
        if self.__net is None:
            return "no network"

        return "no answer"

    def connect(self, net):
        self.__net = net

    # TODO feat: + disconnet
