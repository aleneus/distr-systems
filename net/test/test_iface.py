import unittest
from net.iface import Iface
from net.net import Net


class TestIface(unittest.TestCase):

    def test_set_get_addr(self):
        iface = Iface()
        iface.set_addr("1.2.3.4")
        self.assertEqual(iface.addr(), "1.2.3.4")
