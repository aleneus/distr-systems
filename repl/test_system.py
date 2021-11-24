import unittest
from record import Record
from system import System


class TestSystem(unittest.TestCase):
    def test_touch_methods(self):
        system = System()
        system.add_record(Record(1))
        system.add_record(Record(2))
        system.sync()
        self.assertEqual(len(system.get_all()), 2)
        self.assertIsNotNone(system.get_record(1))
        self.assertIsNone(system.get_record(3))

    def test_get_databases(self):
        system = System()
        self.assertIsNotNone(system.get_main())
        self.assertIsNotNone(system.get_repl())

    def test_add_record(self):
        system = System()
        system.add_record(Record(1))
        self.assertEqual(system.get_main().records_num(), 1)
        self.assertEqual(system.get_repl().records_num(), 0)

    def test_add_record_and_sync(self):
        system = System()
        system.add_record(Record(1))
        self.assertEqual(system.get_main().records_num(), 1)
        system.sync()
        self.assertEqual(system.get_repl().records_num(), 1)

    def test_sync_twice(self):
        system = System()
        system.add_record(Record(1))
        self.assertEqual(system.get_main().records_num(), 1)
        system.sync()
        system.sync()

    def test_read_data_sync(self):
        system = System()
        system.add_record(Record(1))
        system.sync()
        self.assertIsNotNone(system.get_record(1))

    def test_read_data_no_sync(self):
        system = System()
        system.add_record(Record(1))
        self.assertIsNotNone(system.get_record(1))


class TestSystem_SetNumberOfReplics(unittest.TestCase):
    def test_1(self):
        system = System(1)
        system.get_repl(0)
        with self.assertRaises(IndexError):
            system.get_repl(1)

    def test_2(self):
        system = System(2)
        system.get_repl(0)
        system.get_repl(1)
        with self.assertRaises(IndexError):
            system.get_repl(2)

    def test_wrong_number(self):
        with self.assertRaises(ValueError):
            System(0)
