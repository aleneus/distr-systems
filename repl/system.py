"""System with replication."""
from db import Database


class System:
    """System with replication."""
    def __init__(self):
        self.__main = Database()
        self.__repls = [Database(), Database()]
        self.__ind = 0

    def get_main(self):
        """Return main DB."""
        return self.__main

    def get_repl(self, ind=0):
        """Return replicated DB."""
        return self.__repls[ind]

    def sync(self):
        """Synchronize system."""
        for repl in self.__repls:
            _sync(self.__main, repl)

    def add_record(self, rec):
        """Add record to database."""
        return self.__main.add_record(rec)

    def get_record(self, record_id):
        """Get record by ID."""
        rec = self.__repls[self.__ind].get_record(record_id)
        self.__update_ind()
        if rec:
            return rec
        return self.__main.get_record(record_id)

    def get_all(self):
        """Return all records."""
        res = self.__repls[self.__ind].get_all()
        self.__update_ind()
        return res

    def __update_ind(self):
        self.__ind = (self.__ind + 1) % len(self.__repls)


def _sync(src, dst):
    records = src.get_all()
    for rec_id, rec in records.items():
        if not dst.get_record(rec_id):
            dst.add_record(rec)
