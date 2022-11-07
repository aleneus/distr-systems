"""Here the network stub is implemented."""


class Iface:
    """Network interface."""

    def __init__(self):
        self.__addr = ""
        self.__net = None
        self.__host = None

    def set_host(self, host):
        """Set host."""
        self.__host = host

    def connect(self, net):
        """Connect iface to network."""
        self.__net = net

    def disconnect(self):
        """Disconnect from current network."""
        self.__net.remove(self.addr())
        self.__net = None

    def set_addr(self, addr):
        """Set address."""
        self.__addr = addr

    def addr(self):
        """Return address."""
        return self.__addr

    def call(self, addr):
        """Call to given addr."""
        if self.__net is None:
            return "no network"

        return self.__net.call(addr)

    def request_call(self):
        """Process incoming request for call."""
        return self.__host.request_call()
