"""Here the network stub is implemented."""


class Net:
    """Net is the network stub."""

    def __init__(self):
        self.__hosts = {}

    def add_host(self, host, addr):
        """Add host to network."""
        if addr in self.__hosts:
            raise ValueError(f'have host with addr {addr} already')

        host.iface().set_addr(addr)
        host.iface().connect(self)

        self.__hosts[addr] = host

    def del_host(self, addr):
        """Remove host from network."""
        del self.__hosts[addr]

    def ping(self, addr):
        """Send ping to addr."""
        try:
            return f"answer from {addr} ({self.__hosts[addr].request_ping()})"
        except KeyError:
            return "no answer"
