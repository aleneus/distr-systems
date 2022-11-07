import unittest
from net.host import Host
from net.iface import Iface


class TestHostIface(unittest.TestCase):

    def test_no_iface(self):
        self.assertIsNone(Host(0).iface())

    def test_have_iface(self):
        host = Host(0)
        iface = "network interface"
        host.set_iface(iface)

        self.assertEqual(host.iface(), iface)


class TestHost_ping(unittest.TestCase):

    def no_iface(self):
        host = Host(0)
        ans = host.ping("1.2.3.4")
        self.assertEqual(ans, "no iface")

    def have_iface_no_network(self):
        host = Host(0)
        host.set_iface(Iface())
        ans = host.ping("1.2.3.4")
        self.assertEqual(ans, "no network")
