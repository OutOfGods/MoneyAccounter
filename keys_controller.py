import argparse
from accounter import *


class KeysController:
    acc = Accounter()
    acc.load_data()

    parser = argparse.ArgumentParser(description='Keys controller for Accounter.'
                                                 'Nice to do this, i`m really happy.')

    parser.add_argument("-add", action='store',
                        help="adding new raw into accounter '-add 123'")
    parser.add_argument("-c", action='store', default="",
                        help="comment new raw '-add 123 -c 'comment''")
    parser.add_argument("-d", action='store',
                        help="use own date on new raw '-add 123 -c 'comment' -d '20170415''")
    parser.add_argument("-print", action='store_true',
                        help="print accouter")
    parser.add_argument("-sort_date", action='store_true',
                        help="sort table by date")
    parser.add_argument("-drop_data", action='store_true',
                        help="drop all data")
    parser.add_argument("-income", action='store_true',
                        help="print incomes")
    parser.add_argument("-outcome", action='store_true',
                        help="print outcomes")
    parser.add_argument("-cs", action='store', default="",
                        help="search by comment '-cs 'comment''")
    parser.add_argument("-gis", action='store_true',
                        help="print income sum")
    parser.add_argument("-gos", action='store_true',
                        help="print outcome sum")

    def __init__(self):
        self.args = self.parser.parse_args()
        if self.args.add:
            self.add_keys()
        elif self.args.print:
            print(self.acc)
        elif self.args.sort_date:
            self.sort_date()
        elif self.args.drop_data:
            self.acc.drop_data()
        elif self.args.income:
            print(self.acc.get_income())
        elif self.args.outcome:
            print(self.acc.get_outcome())
        elif self.args.cs:
            print(self.acc.get_by_comment(self.args.cs))
        elif self.args.gis:
            print(self.acc.get_income_sum())
        elif self.args.gos:
            print(self.acc.get_outcome_sum())

    def add_keys(self):
        if self.args.d:
            self.acc.add_new_data(self.args.add, self.args.c, self.args.d)
        else:
            self.acc.add_new_data(self.args.add, self.args.c)
        self.acc.save_data()

    def sort_date(self):
        self.acc.sort_by_date()
        print(self.acc)
        self.acc.save_data()

if __name__ == "__main__":
    k = KeysController()
