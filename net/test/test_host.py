import unittest
from net.host import Host
from net.iface import Iface


class TestHostIface(unittest.TestCase):

    def test_no_iface(self):
        self.assertIsNone(Host(0).iface())


class TestHostCall(unittest.TestCase):

    def test_no_iface(self):
        host = Host(0)
        ans = host.call("1.2.3.4")
        self.assertEqual(ans, "no iface")

    def test_have_iface_no_network(self):
        host = Host(0)
        host.set_iface(Iface())
        ans = host.call("1.2.3.4")
        self.assertEqual(ans, "no network")
