class Join:
    def __init__(self, table_to_join, on1, on2):
        self.table_to_join = table_to_join
        self.on1 = on1
        self.on2 = on2

    def get_table_to_join(self):
        return self.table_to_join

    def set_table_to_join(self, t):
        self.table_to_join = t

    def get_on1(self):
        return self.on1

    def set_on1(self, o1):
        self.on1 = o1

    def get_on2(self):
        return self.on2

    def set_on2(self, o2):
        self.on2 = o2
