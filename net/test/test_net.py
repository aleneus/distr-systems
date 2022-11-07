import unittest
from net.host import Host
from net.iface import Iface
from net.net import Net


class TestNetAddHost(unittest.TestCase):

    def test_have_iface(self):
        host = Host(12345)

        iface = Iface()
        host.set_iface(iface)

        net = Net()
        net.add_host(host, "1.2.3.4")

        self.assertEqual(host.iface().addr(), "1.2.3.4")

    def test_no_iface(self):
        with self.assertRaises(AttributeError):
            Net().add_host(Host(1), "1.2.3.4")

    def test_addreses_are_the_same(self):
        host1 = Host(1)
        host2 = Host(2)

        host1.set_iface(Iface())
        host2.set_iface(Iface())

        net = Net()
        net.add_host(host1, "1.2.3.4")

        with self.assertRaises(ValueError):
            net.add_host(host2, "1.2.3.4")


class TestNetDelHost(unittest.TestCase):

    def test_remove_and_try_to_touch(self):
        host = Host(1)

        host.set_iface(Iface())

        net = Net()
        net.add_host(host, "1.2.3.4")
        self.assertEqual(net.ping("1.2.3.4"), "answer from 1.2.3.4 (id 1)")

    def test_add_remove_and_add_again(self):
        host = Host(1)

        host.set_iface(Iface())

        net = Net()
        net.add_host(host, "1.2.3.4")
        net.del_host("1.2.3.4")
        net.add_host(host, "1.2.3.4")


class TestNetPing(unittest.TestCase):

    def test_no_ping(self):
        host = Host(12345)
        host.set_iface(Iface())

        net = Net()
        net.add_host(host, "1.2.3.4")

        ans = host.ping("2.3.4.5")
        self.assertEqual(ans, "no answer")

    def test_ping(self):
        host1 = Host(1)
        host1.set_iface(Iface())

        host2 = Host(2)
        host2.set_iface(Iface())

        net = Net()
        net.add_host(host1, "1.2.3.4")
        net.add_host(host2, "2.3.4.5")

        self.assertEqual(host1.ping("2.3.4.5"), "answer from 2.3.4.5 (id 2)")

    def test_del_and_ping(self):
        host1 = Host(1)
        host1.set_iface(Iface())

        host2 = Host(2)
        host2.set_iface(Iface())

        net = Net()
        net.add_host(host1, "1.2.3.4")
        net.add_host(host2, "2.3.4.5")

        net.del_host("2.3.4.5")

        self.assertEqual(host1.ping("2.3.4.5"), "no answer")

    def test_disconnect_and_ping(self):
        host1 = Host(1)
        host1.set_iface(Iface())

        host2 = Host(2)
        host2.set_iface(Iface())

        net = Net()
        net.add_host(host1, "1.2.3.4")
        net.add_host(host2, "2.3.4.5")

        host2.iface().disconnect()

        self.assertEqual(host1.ping("2.3.4.5"), "no answer")
        self.assertEqual(host2.ping("1.2.3.4"), "no network")
