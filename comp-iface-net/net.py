class Net:
    def __init__(self):
        pass

    def add_comp(self, comp, addr=None):
        # TODO test: no iface
        comp.iface().connect(self)
