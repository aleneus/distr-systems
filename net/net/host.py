"""Here the Host stub is implemented."""


class Host:
    """Host represents computer in the network."""

    def __init__(self, host_id, is_on=True):
        self.__host_id = host_id
        self.__iface = None

    def set_iface(self, iface):
        """Set network interface."""
        self.__iface = iface

    def iface(self):
        """Return network interface."""
        return self.__iface

    def ping(self, addr):
        """Send ping to addr."""
        if self.iface() is None:
            return "no iface"

        return self.iface().ping(addr)

    def request_ping(self):
        """Process incoming ping."""
        return f'id {self.__host_id}'
