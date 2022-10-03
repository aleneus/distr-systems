import unittest
from comp import Computer


class TestComp(unittest.TestCase):
    def test_serial_number(self):
        self.assertEqual(Computer(1).serial(), 1)
        self.assertEqual(Computer(2).serial(), 2)

    def test_no_iface(self):
        self.assertIsNone(Computer(0).iface())

    def test_have_iface(self):
        comp = Computer(0)
        iface = "network interface"
        comp.set_iface(iface)

        self.assertEqual(comp.iface(), iface)
