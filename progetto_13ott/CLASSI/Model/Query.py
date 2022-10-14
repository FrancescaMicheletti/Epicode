from progetto_13ott import CLASSI
from progetto_13ott.CLASSI.Model.Join import Join
from progetto_13ott.CLASSI.Model.Select import Select
from progetto_13ott.CLASSI.Model.Where import Where
from progetto_13ott.CLASSI.Model.GroupBy import GroupBy
from progetto_13ott.CLASSI.Model.OrderBy import OrderBy
from progetto_13ott.CLASSI.Model.Having import Having

class Query:
    def __init__(self):
        self.select = None
        self.where = None
        self.join = None  # fai una lista di ogetto join e poi iteri sulla lista
        self.orderby = None
        self.groupby = None
        self.having = None

    def get_select(self):
        return self.select

    def set_select(self, s):
        self.select = s

    def get_where(self):
        return self.where

    def set_where(self, w):
        self.where = w

    def get_join(self):
        return self.join

    def set_join(self, j):
        self.join = j

    def get_orderby(self):
        return self.orderby

    def set_orderby(self, ob):
        self.orderby = ob

    def get_groupby(self):
        return self.groupby

    def set_groupby(self, gb):
        self.groupby = gb

    def get_having(self):
        return self.having

    def set_having(self, h):
        self.having = h

    @property
    def stmt(self):
        # SELECT
        stmt = 'SELECT'

        if len(self.get_select().get_attr()) == 0:

            stmt = stmt + '*'
        elif type(self.get_select().get_attr()) == str:

            stmt = f"SELECT {self.get_select().get_attr()}"
        elif type(self.get_select().get_attr()) == tuple:

            stmt = f"SELECT {','.join(self.get_select().get_attr())}"
        #FROM
        if isinstance(self.get_select().get_table(), CLASSI.Model.Query.SubQuery):

            stmt = f"{stmt} FROM {self.get_select().get_table().stmt_sq()}"
        else:
            stmt = f"{stmt} FROM {self.get_select().get_table()}"

        # JOIN
        if isinstance(self.get_join(), CLASSI.Model.Join.Join):
            # se passo a self_get_join un oggetto Join
            if len(self.get_join().get_table_to_join()) > 0:
                stmt = f"{stmt} JOIN {self.get_join().get_table_to_join()} ON " \
                       f"{self.get_join().get_on1()} = {self.get_join().get_on2()}"

        if type(self.get_join()) == list:
            # se passo a self_get_join una lista di oggetti Join
            for join_obj in self.get_join():
                stmt = f"{stmt} JOIN {join_obj.get_table_to_join()} ON " \
                       f"{join_obj.get_on1()} = {join_obj.get_on2()}"

        # WHERE
        if isinstance(self.get_where(), CLASSI.Model.Where.Where):
            stmt = f"{stmt} WHERE {self.get_where().get_condition()}"

        # ORDER BY
        if isinstance(self.get_orderby(), CLASSI.Model.OrderBy.OrderBy):
            stmt = f"{stmt} ORDER BY {self.get_orderby().get_attr_o()}"

        # GROUP BY
        if isinstance(self.get_groupby(), CLASSI.Model.GroupBy.GroupBy):
            stmt = f"{stmt} GROUP BY {self.get_groupby().get_attr_g()}"

        # HAVING
        if isinstance(self.get_having(), CLASSI.Model.Having.Having):
            stmt = f"{stmt} HAVING {self.get_having().get_condition_h()}"

        stmt = f"{stmt};"

        return stmt

class SubQuery(Query):
    def __init__(self):
        super().__init__()
        self.alias = None

    def get_alias(self):
        return self.alias

    def set_alias(self, a):
        self.alias = a

    def stmt_sq(self):
        if self.get_alias() is not None:
            stmt1 = f"({super(SubQuery, self).stmt[:-1]}) AS {self.get_alias()}"
            return stmt1
