class Net:
    def __init__(self):
        self.__hosts = set()

    def add_host(self, comp, addr):
        comp.iface().set_addr(addr)
        comp.iface().connect(self)
        self.__hosts.add(addr)

    def del_host(self, addr):
        self.__hosts.remove(addr)

    def ping(self, addr):
        if addr in self.__hosts:
            return f"answer from {addr}"

        return "no answer"
