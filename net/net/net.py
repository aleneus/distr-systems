"""Here the network stub is implemented."""


class Net:
    """Net is the network stub."""

    def __init__(self):
        self.__ifaces = {}

    def add(self, iface, addr):
        """Add host to network."""
        if addr in self.__ifaces:
            raise ValueError(f'have host with addr {addr} already')

        iface.set_addr(addr)
        iface.connect(self)

        self.__ifaces[addr] = iface

    def remove(self, addr):
        """Remove host from network."""
        del self.__ifaces[addr]

    def call(self, addr):
        """Call to addr."""
        try:
            return f"answer from {addr} ({self.__ifaces[addr].request_call()})"
        except KeyError:
            return "no answer"
