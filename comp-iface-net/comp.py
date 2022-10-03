class Computer:
    """Computer represents computer."""

    def __init__(self, serial):
        self.__serial = serial
        self.__iface = None

    def serial(self):
        """Return serial number."""
        return self.__serial

    def set_iface(self, iface):
        """Set network interface."""
        self.__iface = iface

    def iface(self):
        """Return network interface."""
        return self.__iface
