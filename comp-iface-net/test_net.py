import unittest
from comp import Computer
from iface import Iface
from net import Net


class TestNetAddHost(unittest.TestCase):
    def test_have_iface(self):
        comp = Computer(12345)

        iface = Iface()
        comp.set_iface(iface)

        net = Net()
        net.add_host(comp, "1.2.3.4")

        self.assertEqual(comp.iface().addr(), "1.2.3.4")

    def test_no_iface(self):
        with self.assertRaises(AttributeError):
            Net().add_host(Computer(1), "1.2.3.4")


class TestNet(unittest.TestCase):
    def test_no_ping(self):
        comp = Computer(12345)
        comp.set_iface(Iface())

        net = Net()
        net.add_host(comp, "1.2.3.4")

        ans = comp.ping("2.3.4.5")
        self.assertEqual(ans, "no answer")

    def test_ping(self):
        comp1 = Computer(1)
        comp1.set_iface(Iface())

        comp2 = Computer(2)
        comp2.set_iface(Iface())

        net = Net()
        net.add_host(comp1, "1.2.3.4")
        net.add_host(comp2, "2.3.4.5")

        self.assertEqual(comp1.ping("2.3.4.5"),
                         "answer from 2.3.4.5")

    def test_del_and_ping(self):
        comp1 = Computer(1)
        comp1.set_iface(Iface())

        comp2 = Computer(2)
        comp2.set_iface(Iface())

        net = Net()
        net.add_host(comp1, "1.2.3.4")
        net.add_host(comp2, "2.3.4.5")

        net.del_host("2.3.4.5")

        self.assertEqual(comp1.ping("2.3.4.5"),
                         "no answer")

    def test_disconnect_and_ping(self):
        comp1 = Computer(1)
        comp1.set_iface(Iface())

        comp2 = Computer(2)
        comp2.set_iface(Iface())

        net = Net()
        net.add_host(comp1, "1.2.3.4")
        net.add_host(comp2, "2.3.4.5")

        comp2.iface().disconnect()

        self.assertEqual(comp1.ping("2.3.4.5"),
                         "no answer")
        self.assertEqual(comp2.ping("1.2.3.4"),
                         "no network")
