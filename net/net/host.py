"""Here the host stub is implemented."""


class Host:
    """Host represents computer in the network."""

    def __init__(self, host_id, is_on=True):
        self.__host_id = host_id
        self.__iface = None

    def set_iface(self, iface):
        """Set network interface."""
        self.__iface = iface
        self.__iface.set_host(self)

    def iface(self):
        """Return network interface."""
        return self.__iface

    def call(self, addr):
        """Call to addr."""
        if self.iface() is None:
            return "no iface"

        return self.iface().call(addr)

    def request_call(self):
        """Process incoming call."""
        return f'id {self.__host_id}'
