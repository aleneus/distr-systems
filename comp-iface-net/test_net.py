import unittest
from comp import Computer
from iface import Iface
from net import Net


class TestNet(unittest.TestCase):
    def test_no_ping(self):
        comp = Computer(12345)

        iface = Iface()
        comp.set_iface(iface)

        net = Net()
        net.add_comp(comp, "1.2.3.4")

        ans = comp.ping("2.3.4.5")
        self.assertEqual(ans, "no answer")
