class Select:
    def __init__(self, table, attr=None):
        if attr is None:
            attr = tuple()
        self.attr = attr
        self.table = table

    def get_table(self):
        return self.table

    def set_table(self, f):
        self.table = f

    def get_attr(self):
        return self.attr

    def set_attr(self, s):
        self.attr = s




